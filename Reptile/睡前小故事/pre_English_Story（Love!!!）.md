
* ```find_all():```
```
常用通过find_all()方法来查找标签元素：<>.find_all(name, attrs, recursive, string, **kwargs) ，返回一个列表类型（用len()查看列表中元素个数），存储查找的结果 
• name：对标签名称的检索字符串
• attrs：对标签属性值的检索字符串，可标注属性检索
• recursive：是否对子孙全部检索，默认True
• string：<>…</>中字符串区域的检索字符串 
```

* 解释```for link in i[1:59:2]:```
```

def parsehtml(namelist,urllist,html):
    url='http://www.en8848.com.cn/'
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find(attrs={'class':'ch_content'})
    #print(t)
    i=t.find_all('a')
    # print(i)
    # print(len(i))
    """可以先进行如此搜索，再根据显示所得，进行筛选，
    for link in i:
        print(link.get('href'))
        print(link.get('title'))
    """
    for link in i[1:59:2]:
       urllist.append(url+link.get('href'))
       namelist.append(link.get('title'))
```
![](https://github.com/BinGYiZhanG/Python_/blob/master/Reptile/Images/py19123623.jpg)

* 
![](https://github.com/BinGYiZhanG/Python_/blob/master/Reptile/Images/py19123625.jpg)
* 解释```t=soup.find(attrs={'class':'jxa_content','id':'articlebody'})```
```
# 生成短文内容
def parsehtml2(html):
    text=[]
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find(attrs={'class':'jxa_content','id':'articlebody'})
    for i in t.findAll('p'):
        text.append(i.text)
    #print(text)
    return "\n".join(text)
```
![](https://github.com/BinGYiZhanG/Python_/blob/master/Reptile/Images/py19123626.jpg)



* 代码

```
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import datetime
import time


# 记录你俩好了多少天
def getDays():
    
    inlove_date=datetime.datetime(2019,9,12)
    today_date=datetime.datetime.today()
    inlove_days=(today_date-inlove_date).days
    return str(inlove_days)

# 获取短文的网页信息
def getHTMLText(url,headers):
    try:
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return "爬取失败"

# 生成短文内容
def parsehtml2(html):
    text=[]
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find(attrs={'class':'jxa_content','id':'articlebody'})
    for i in t.findAll('p'):
        text.append(i.text)
    #print(text)
    return "\n".join(text)

def parsehtml(namelist,urllist,html):
    url='http://www.en8848.com.cn/'
    soup=BeautifulSoup(html,'html.parser')
    t=soup.find(attrs={'class':'ch_content'})
    #print(t)
    i=t.find_all('a')
    # print(i)
    # print(len(i))
    """可以先进行如此搜索，再根据显示所得，进行筛选，
    for link in i:
        print(link.get('href'))
        print(link.get('title'))
    """
    for link in i[1:59:2]:
       urllist.append(url+link.get('href'))
       namelist.append(link.get('title'))

def sendemail(url,headers,title):
    date_today=time.strftime("%Y-%m-%d", time.localtime())
    msg_from='1152768760@qq.com'                                 #发送方邮箱
    passwd='yfrplkgncgtkidga'                                   #填入发送方邮箱的授权码
    receivers=['1511180952@qq.com']             #收件人邮箱
                            
    subject="Today's story from Laofei " +str(date_today)       #主题     
    html=getHTMLText(url,headers)
    content='Dear Jiangjiang:\n    We have been in love for '+getDays()+' Days !\n\n⭐⭐⭐⭐⭐❤❤💗❤❤⭐⭐⭐⭐⭐'+parsehtml2(html)                                        #正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = ','.join(receivers)
    try:
        s=smtplib.SMTP_SSL("smtp.qq.com",465)                   #邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg['To'].split(','), msg.as_string())
        print("发送成功")
    except:
        print("发送失败")
    finally:
        s.quit()




def main():


    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
               }

    urllist=[]
    namelist=[]
    for i in range(1,21):
        if i==1:
            url='http://www.en8848.com.cn/article/love/dating/index.html'
        else:
            url='http://www.en8848.com.cn/article/love/dating/index_'+str(i)+'.html'
        print ("正在爬取第%s页的英语短文链接：" % (i))
        print (url+'\n')
        html=getHTMLText(url,headers)
        # print(html)
        parsehtml(namelist,urllist,html)
    
    #print("爬取链接完成")
    date=int(getDays()) - 82
    #print(date)
    sendemail(urllist[date],headers,namelist[date])
    #print(len(namelist))
    #print(namelist[0])
    
    
    
if __name__=='__main__':
    main()

```
