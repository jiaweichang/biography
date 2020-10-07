var language = 'cmn-Hant-TW';
showInfo('info_start');

var final_transcript = '';
var recognizing = false;
var ignore_onend;
var start_timestamp;

var recognition;

/** 語音識別結果顯示 */
const messagesDiv = document.getElementById('cube');

const apiUrl = (
  // 'https://cors-anywhere.herokuapp.com/' + 
  'https://itri.dasgo.com.tw:5002/webhooks/rest/webhook'
);

function setUp() {
    if (!('webkitSpeechRecognition' in window)) {
        upgrade();
    } else {
        start_button.style.display = 'inline-block';
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onstart = function () {
            recognizing = true;
            showInfo('info_speak_now');
            start_img.src = '//google.com/intl/en/chrome/assets/common/images/content/mic-animate.gif';
        };

        recognition.onerror = function (event) {
            if (event.error == 'no-speech') {
                start_img.src = '//google.com/intl/en/chrome/assets/common/images/content/mic.gif';
                showInfo('info_no_speech');
                ignore_onend = true;
            }
            if (event.error == 'audio-capture') {
                start_img.src = '//google.com/intl/en/chrome/assets/common/images/content/mic.gif';
                showInfo('info_no_microphone');
                ignore_onend = true;
            }
            if (event.error == 'not-allowed') {
                if (event.timeStamp - start_timestamp < 100) {
                    showInfo('info_blocked');
                } else {
                    showInfo('info_denied');
                }
                ignore_onend = true;
            }
        };

        recognition.onend = function () {
            recognizing = false;
            if (ignore_onend) {
                return;
            }
            start_img.src = '//google.com/intl/en/chrome/assets/common/images/content/mic.gif';
            if (!final_transcript) {
                showInfo('info_start');
                return;
            }
            showInfo('');
            //if (window.getSelection) {
            //    window.getSelection().removeAllRanges();
            //    var range = document.createRange();
            //    range.selectNode(document.getElementById('textarea'));
            //    window.getSelection().addRange(range);
            //}
            //等於按按鈕
            textinput()

        };

        recognition.onresult = function (event) {
            var interim_transcript = '';
            if (typeof (event.results) == 'undefined') {
                recognition.onend = null;
                recognition.stop();
                upgrade();
                return;
            }
            var transcriptIsFinish = false;
            for (var i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                    transcriptIsFinish = true;
                    final_transcript += event.results[i][0].transcript;
                } else {
                    transcriptIsFinish = false;
                    interim_transcript += event.results[i][0].transcript;
                }
            }
            // final_transcript = capitalize(final_transcript);
            // final_span.innerHTML = linebreak(final_transcript);
            // interim_span.innerHTML = linebreak(interim_transcript);
            if (!transcriptIsFinish)
            {
                $('#textarea').val(interim_transcript)
            }
            else
            {
                $('#textarea').val(final_transcript)
            }                        
            //$('#textarea').val(final_transcript)
            //final_span.innerHTML = final_transcript;
            //interim_span.innerHTML = interim_transcript;
        };
    }
}

function startButton(event) {
    if (recognizing) {
        recognition.stop();
        return;
    }
    final_transcript = '';
    recognition.lang = language;
    recognition.start();
    ignore_onend = false;
    //textarea.innerHTML = '';
    //textarea.innerHTML = '';
    start_img.src = '//google.com/intl/en/chrome/assets/common/images/content/mic-slash.gif';
    showInfo('info_allow');
    start_timestamp = event.timeStamp;
}

function showInfo(info_id) {

    // try: comment out the contents of this function

    if (info_id) {
        var info = document.getElementById("info");
        for (var child = info.firstChild; child; child = child.nextSibling) {
            if (child.style) {
                child.style.display = child.id == info_id ? 'inline' : 'none';
            }
        }
        info.style.visibility = 'visible';
    } else {
        info.style.visibility = 'hidden';
    }
}

/** 建立訊息顯示 */
function insertMessageDivInMessagesDiv(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'cube';

    messageDiv.innerText = message;
    messagesDiv.appendChild(messageDiv);
    $('#talk').scrollTop($('#talk').height());
}

function insertMessageDivInMessagesDivReply(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'cubereply';

    messageDiv.innerText = message;
    messagesDiv.appendChild(messageDiv);
    $('#talk').scrollTop($('#talk').height());
}

/** 當API請求得到回應 */
function whenApiRequestGotResponse(message) {
    console.log(message);
    return fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            sender: 'user',
            message,
            }),
    });
}

async function textinput() {
    const textdata = document.getElementById('textarea');
    const message = textdata.value
    insertMessageDivInMessagesDiv(message.replace(/\s*/g,""));
    $('#textarea').val('')
    try {
        response = await whenApiRequestGotResponse(message.replace(/\s*/g,""));
        //response = whenApiRequestGotResponse(textdata.value);
        //[{ text: apiMessage }] = response.json();
  
        //insertMessageDivInMessagesDiv(apiMessage);
        const apiMessages  = await response.json();

        for (const apiMessage of apiMessages){
            insertMessageDivInMessagesDivReply(apiMessage.text);
        }
    } catch(error) {
        console.log(error);
    }   
}

