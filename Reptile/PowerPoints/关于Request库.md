### 睡前小故事

#### （1），原理讲解：
  
* 在requests获取网页的编码格式时，有两种方式，而结果也不同，通常用apparent_encoding更合适
![](https://github.com/BinGYiZhanG/Python_/blob/master/Reptile/Images/py1911281119.jpg)
* [代码分析Python requests库中文编码问题](http://xiaorui.cc/2016/02/19/%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90python-requests%E5%BA%93%E4%B8%AD%E6%96%87%E7%BC%96%E7%A0%81%E9%97%AE%E9%A2%98/)
  * 暂时做以下理解
```
In [9]: r = requests.get('http://cn.python-requests.org/en/latest/')
 
In [10]: r.encoding
Out[10]: 'ISO-8859-1'
 
In [11]: type(r.text)
Out[11]: unicode
 
In [12]: type(r.content)
Out[12]: str
 
In [13]: r.apparent_encoding
Out[13]: 'utf-8'
 
In [14]: chardet.detect(r.content)
Out[14]: {'confidence': 0.99, 'encoding': 'utf-8'}

```
