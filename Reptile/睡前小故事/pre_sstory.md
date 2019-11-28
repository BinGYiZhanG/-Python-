
### 1，```BeautifulSoup```获取小故事的链接和题目
```
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText




def getHTMLText(url,headers):
    try:
        r=requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        #print(r.text)
        return r.text
       
    except:
        return "爬取失败"

def parsehtml(namelist,urllist,html):
    url='http://www.tom61.com/'
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find('dl',attrs={'class':'txt_box'})# 找到小故事的连接
    #print(t)
    i=t.find_all('a') #  
    #print(i)
    for link in i:
        urllist.append(url+link.get('href')) # 获取链接
        namelist.append(link.get('title')) # 获取标题
    
    print("获取小故事的连接")
    for url_list in urllist:
        print(url_list)
        
    print("获取小故事的名称")
    for name_list in namelist:
        print(name_list)


def main():


    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
               }

    urllist=[]
    namelist=[]
    i=1
    # for i in range(1,11):
        # if i==1:
    url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index.html'
        #else:
         #   url='http://www.tom61.com/ertongwenxue/shuiqiangushi/index_'+str(i)+'.html'
    print ("正在爬取第%s页的故事链接：" % (i))
    print (url+'\n')
    html=getHTMLText(url,headers)
    parsehtml(namelist,urllist,html)
    
    
if __name__=='__main__':
    main()    

```

#### （1），原理讲解：
  
* 在requests获取网页的编码格式时，有两种方式，而结果也不同，通常用apparent_encoding更合适
![]()



















