#### 8.1.2 当前工作目录
```py
In [2]: import os

In [3]: os.getcwd()#取得当前工作路径的字符串
Out[3]: 'C:\\Users\\Administrator'

In [4]: os.chdir('C:\\Windows\System32')#改变当前工作路径

In [5]: os.getcwd()
Out[5]: 'C:\\Windows\\System32'

```

#### 8.1.4 用os.makedirs()创建新文件夹

```py

In [6]: os.makedirs('D:\\Python\\pyScript\\delicious\\walnut\\waffles')
```

#### 8.1.5 os.path 模块

os.path 模块的完整文档在Python网站上：http://docs.python.org/3/library/os.path.html。

#### 8.1.6 处理绝对路径和相对路径

#### 8.1.7 查看文件大小和文件夹内容

#### 8.1.8 检查路径有效性

### 8.2 文件读写过程

#### 8.2.1 用open()函数打开文件
调用open()将返回一个File 对象。
File 对象代表计算机中的一个文件，它只是Python 中另一种类型的值，就像你已熟悉的列表和字典。

#### 8.2.2 读取文件内容

#### 8.2.3 写入文件

### 8.3 用shelve 模块保存变量
### 8.4 用pprint.pformat()函数保存变量











