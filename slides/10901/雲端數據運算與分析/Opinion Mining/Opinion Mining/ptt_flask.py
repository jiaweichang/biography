from flask import Flask, render_template
from flask import request

import json  #用來讀取/產生 json 格式的套件
import jieba #用來處理中文斷詞的套件
import numpy as np #用來處理數值矩陣的套件

'''sklearn 又名 scikit-learn，為機器學習方法的套件'''
from sklearn.feature_extraction import DictVectorizer #用於轉換 dict 為 sklearn estimators 可用的向量
from sklearn.feature_extraction.text import TfidfTransformer #將矩陣轉換為 TF 或 TF-IDF 表示
from sklearn.svm import LinearSVC #以 LinearSVC 分類演算法為例

from collections import defaultdict #使用 dict 儲存資料

# load ptt posts

path = 'gossip.json' # 欲載入文檔之路徑

with open(path, encoding='utf8') as f:
    posts = json.load(f)

# grap comments

c_words = []
c_scores = []

for post in posts:
    for comment in post['comments']: #取得八卦文文章之鄉民留言
        l = comment['content'].strip() #去頭去尾換行之類的字符
        if l and comment['score'] != 0:
            d = defaultdict(int)
            for w in jieba.cut(l): # w 是針對 l 中的文字斷詞後所得之詞語
                d[w] += 1
            if len(d) > 0:
                c_scores.append(1 if comment['score'] > 0 else 0) #每一則留言之標記(推/噓)
                c_words.append(d)


# convert to vectors
c_dvec = DictVectorizer()
c_tfidf = TfidfTransformer()
c_vector = c_dvec.fit_transform(c_words)
c_X = c_tfidf.fit_transform(c_vector) #將一千篇所有鄉民留言的斷詞文字矩陣轉成向量並計算tf-idf


# build and train the classifier
c_svc = LinearSVC()
c_svc.fit(c_X, c_scores)

#分類留言的情緒
def comment_sentiment_classifier(model, dvec, tfidf, text):
    l = text.strip() #去頭去尾換行之類的字符
    d = defaultdict(int)

    for w in jieba.cut(l): # w 是針對 l 中的文字斷詞後所得之詞語
        d[w] += 1

    comment_vec = dvec.transform(d)
    comment_X = tfidf.transform(comment_vec)
    result = model.predict(comment_X)
    
    if result == 1:
        return '感覺還不錯哦！'
    else:
        return '你很不開心喔？'

# 網路服務
app = Flask(__name__)
app.config["DEBUG"] = True # True 表示開啟除錯模式，正式對外運行時需註解掉
app.config["JSON_AS_ASCII"] = False # False 表示不編譯為 ASCII

@app.route('/', methods=['GET', 'POST'])
def sessions():
    if request.method == 'POST': 
        sentence = request.values['sentence']
        print(sentence)
        reply = comment_sentiment_classifier(c_svc, c_dvec, c_tfidf, sentence)
        print(reply)
        return reply
    else:
        reply = "Please enter a sentence."
        return render_template('view.html', reply = reply)

app.run()