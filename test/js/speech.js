!async function () {
    /** 麥克風按鈕 */
    const microphoneButton = document.getElementById('mic_button');

    /** 麥克風按鈕圖片 */
    const microphoneButtonImage = document.getElementById('mic');

    /** 訊息顯示容器外層容器 */
    const messagesDivContainer = document.getElementById('talk');

    /** 訊息顯示容器 */
    const messagesDiv = document.getElementById('cube');

    /** 訊息文字輸入框 */
    const messageTextInput = document.getElementById('textarea');

    /** 訊息文字發送按鈕 */
    const messageTextSendButton = document.getElementById('send');

    /** 語音識別 */
    const speechRecognition = new webkitSpeechRecognition();

    /** API網址 */
    const apiUrl = ('http://itri.dasgo.com.tw:5002/webhooks/rest/webhook');

    speechRecognition.continuous = false;
    speechRecognition.lang = 'cmn-Hant-TW';
    microphoneButtonImage.style.pointerEvents = 'none';

    for await (const messageText of iterateWhenGotMessageText()) {
        appendMessageDivInMessagesDiv(messageText);
        messagesDivContainer.scrollTop = messagesDivContainer.scrollHeight;

        try {
            const response = await whenApiRequestGotResponse(messageText);
            const apiMessages = await response.json();

            for (const apiMessage of apiMessages) {
                appendMessageDivInReplyAPI(apiMessage.text);
            }

            messagesDivContainer.scrollTop = messagesDivContainer.scrollHeight;
        } catch (error) {
            console.log(error);
        }
    }

    /** 疊代當得到訊息文字 */
    function* iterateWhenGotMessageText() {
        while (true) {
            yield whenGotMessageText();
        }
    }

    /** 新增訊息顯示至訊息顯示容器 */
    function appendMessageDivInMessagesDiv(messageText) {
        messagesDiv.appendChild(createMessageDiv(messageText));
    }

    /** 建立訊息顯示 */
    function createMessageDiv(messageText) {
        return Object.assign(document.createElement('div'), {
            className: 'cube',
            innerText: messageText,
        });
    }

    /** 新增API回復顯示至訊息顯示容器 */
    function appendMessageDivInReplyAPI(messageText) {
        messagesDiv.appendChild(createMessageDivforAPI(messageText));
    }

    /** 建立API回復顯示 */
    function createMessageDivforAPI(messageText) {
        return Object.assign(document.createElement('div'), {
            className: 'cubereply',
            innerText: messageText,
        });
    }

    /** 當API請求得到回應 */
    function whenApiRequestGotResponse(messageText) {
        return fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                sender: 'user',
                message: messageText,
            }),
        });
    }

    /** 當事件標的發生事件 */
    function whenEventTargetOnEvent(eventTarget, eventName) {
        return new Promise((callback) => {
            eventTarget.addEventListener(eventName, listener);

            function listener() {
                callback();
                eventTarget.removeEventListener(eventName, listener);
            }
        });
    }

    /** 當得到訊息文字 */
    function whenGotMessageText() {
        return new Promise((callback) => {
            microphoneButton.ontouchstart = async () => {
                /** 訊息文字 */
                let messageText = '';

                const speechRecognitionOnResult = ({ resultIndex, results }) =>
                    (messageText = results[resultIndex][results.length - 1].transcript, alert(messageText));

                microphoneButtonImage.src = 'images/mic_use.png';
                speechRecognition.onresult = speechRecognitionOnResult;
                speechRecognition.start();
                await whenEventTargetOnEvent(microphoneButton, 'touchend');
                speechRecognition.stop();
                await whenEventTargetOnEvent(speechRecognition, 'end');
                microphoneButtonImage.src = 'images/mic.png';
                callback(messageText.replace(/\s*/g, ''));
            };

            microphoneButton.onmousedown = async () => {
                /** 訊息文字 */
                let messageText = '';

                const speechRecognitionOnResult = ({ resultIndex, results }) =>
                    (messageText = results[resultIndex][results.length - 1].transcript, alert(messageText));

                microphoneButtonImage.src = 'images/mic_use.png';
                speechRecognition.onresult = speechRecognitionOnResult;
                speechRecognition.start();
                await whenEventTargetOnEvent(microphoneButton, 'mouseup');
                speechRecognition.stop();
                await whenEventTargetOnEvent(speechRecognition, 'end');
                microphoneButtonImage.src = 'images/mic.png';
                callback(messageText.replace(/\s*/g, ''));
            };

            messageTextSendButton.onclick = () => {
                const messageText = messageTextInput.value;
                messageTextInput.value = '';
                callback(messageText);
            };

            window.onkeyup = (event) => event.keyCode === 13 && messageTextSendButton.click();
        });
    }
}();

