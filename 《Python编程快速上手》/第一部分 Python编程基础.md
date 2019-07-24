
### P45
#### 3.3 None值

### P46
#### 3.4 关键字参数和print()
但是你可以传sep关键字参数，替换掉默认的分隔字符串
```py
In [2]: print('cats','dogs','mice',sep=',')
cats,dogs,mice
```
### P49
#### 3.6 global语句
如果需要在一个函数内修改全局变量，就使用global语句

### P53
#### 3.7 异常处理
```py
In [3]: def spam(divideBy):
   ...:     return 42/divideBy
   ...:

In [4]: try:
   ...:     print(spam(2))
   ...:     print(spam(12))
   ...:     print(spam(0))
   ...:     print(spam(1))
   ...: except ZeroDivisionError:
   ...:     print('Error: Invalid argument.')
   ...:
21.0
3.5
Error: Invalid argument.
```
```print(spam(1))```从未被执行是因为，一旦执行跳到except子句的代码，就不会回到try子句，它会继续照常向下执。


### P62
#### list concatenation（连接）

### P64
#### 4.2.3 多重赋值技巧

让你在一行代码中，用列表的值为多个变量赋值。

### P65
#### 4.4.1 用index()方法在列表中查找值

```py
In [5]: spam=['hello','hi','howdy','heyas']

In [6]: spam.index('hello')
Out[6]: 0

In [7]: spam.index('howdy')
Out[7]: 2
```
### P66
#### 4.4.2 用append()和insert()方法在列表中添加值
append()和insert()都不会将spam的新值作为其返回值。

### P67
#### 4.4.3 用remove()方法从列表中删除值

### P68
sort()方法对字符串排序，使用“ASCII字符排序”

### P69
#### Python中缩进规则的例外

### P70
可变和不可变数据类型
str不可变，列表可变

### P73
#### 4.7 引用

### P75
#### 4.7.2 copy模块的copy()和deepcopy()模块




### P82
#### 5.1.4 get()方法
#### 5.1.5 setdefault()方法
### P83
#### 漂亮打印
导入pprint模块
```py
In [8]: import pprint

In [9]: message='It was a bright cold day in April.'

In [10]: count={}

In [11]: for character in message:
    ...:     count.setdefault(character,0)
    ...:     count[character]=count[character]+1
    ...:

In [12]: pprint.pprint(count)
{' ': 7,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 3,
 'b': 1,
 'c': 1,
 'd': 2,
 'g': 1,
 'h': 1,
 'i': 3,
 'l': 2,
 'n': 1,
 'o': 1,
 'p': 1,
 'r': 2,
 's': 1,
 't': 2,
 'w': 1,
 'y': 1}
```

## 第6章 字符串操作

### P96
#### 6.2.1 字符串方法upper()、lower()、isupper()和islower()
#### 6.2.2 isX字符串方法

```py
isalpha()
isalnum()
isdecimal()
isspace()
istitle()
```
### P99
#### 6.2.3 字符串方法startwith()和endwith()
#### 6.2.4 字符串方法join()和split()
#### 6.2.5 用rjust(),ljust()和center()方法对齐文本
#### 6.2.6 用strip()，rstrip()和lstrip()删除空白字符
#### 6.2.7 用pyperclip模块拷贝粘贴字符串
```py
In [14]: import pyperclip

In [15]: pyperclip.copy('Hello world')#改变剪切板内容

In [16]: pyperclip.paste()#打印剪切板内容
Out[16]: 'Hello world'

```







