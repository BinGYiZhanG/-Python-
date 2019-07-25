#### 7.2 用正则表达式查找文本模式
基本查找
```py
In [1]: import re

In [2]: phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

In [3]: mo = phoneNumRegex.search('My number is 415-555-4242.')

In [5]: print('Phone number found:'+mo.group())
Phone number found:415-555-4242
```


