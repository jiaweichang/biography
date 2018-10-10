# coding: utf-8

import  requests
from bs4 import BeautifulSoup

def get_articles_content(this_page_article_href):
    data = ""
    for url in this_page_article_href:
        r = requests.get("https://www.ptt.cc" + url )
        soup = BeautifulSoup(r.text,"html.parser")
        # print(soup)
        try:
            author = soup.select('span.article-meta-value')[0].text #作者
            board = soup.select('span.article-meta-value')[1].text  #看板
            title = soup.select('span.article-meta-value')[2].text  #標題
            time = soup.select('span.article-meta-value')[3].text   #時間
            
            push_tag = soup.select('span.push-tag')                 #推文
            push_userid = soup.select('span.push-userid')           #推文id
            push_content = soup.select('span.push-content')         #推文內容
            push_ipdatetime = soup.select('span.push-ipdatetime')   #推文時間
            
            content = soup.find(id="main-content").text             #content 文章內文
            target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'       
            content = content.split(target_content)                 #去除掉 target_content
            content = content[0].split(time)
            main_content = content[1].replace('--','  ')            #去除掉文末 --
            
            print('作者:', author)
            print(board,' 版')
            print('標題:', title)
            print('時間:', time)
            print('內文:', main_content)
            
            data += '作者:' + author + '\n'
            data += board + ' 版' + '\n'
            data += '標題:' + title + '\n'
            data += '時間:' + time + '\n'
            data += '內文:' + main_content + '\n'
            
            push_list_len = len(push_tag)                           #計算推文筆數
            count = 0
            
            while (count < push_list_len):                          #利用迴圈印出所有推文
                print (push_tag[count].text + push_userid[count].text + push_content[count].text + push_ipdatetime[count].text)
                data += push_tag[count].text + push_userid[count].text + push_content[count].text + push_ipdatetime[count].text + '\n'
                count = count+1
            
            print("=======================分隔線========================")
            data += "=======================分隔線========================\n"
        except:
            pass
    return data
    
    
        
def get_all_articles_href(page_url):
    article_href =[]
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text,"html.parser")
    results = soup.findAll("div",{"class":"title"})
    for item in results:
        try:
            item_href = item.find("a").attrs["href"]
            article_href.append(item_href)
        except:
            pass
    return article_href

def main_function(url="https://www.ptt.cc/bbs/LoL/index.html"):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    this_page_article_href = get_all_articles_href(page_url=url)
    data = get_articles_content(this_page_article_href=this_page_article_href)
    
    fo = open("data.txt", "w", encoding='utf-8')
    fo.writelines(data)
    fo.close()

main_function()

