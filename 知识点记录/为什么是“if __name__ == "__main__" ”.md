# What does if __name__ == “__main__”: do?

[解答链接 Overflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

我只不过是翻译成中文。。

无论什么Python的解释器都会读一个源文件，它会做两件事：
  * 它会设置很少的几个变量，像__name__,然后
  * 它会执行在该文件下发现的所有代码<br>
让我们看看这是如何工作的，以及它如何与您关于我们在Python脚本中经常看到的关于_name__检查的问题相关联。(这句话可真难翻,“Let's see how this works and how it relates to your question about the __name__ checks we always see in Python scripts.”)
#### 代码样例
让我们使用一个略微不同的代码来探索如何引用，脚本是如何工作的。假设接下来的这个文件是foo.py
```py
# Suppose this is foo.py.

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
```

### 特殊变量
当Python解释器读一个源文件，它会首先定义几个特殊的变量。在这种情况下，我们关心__name__变量。
#### 当你的模块是主程序时
如果你正在运行你的模块作为主程序，例如
```py
python foo.py
```

解释器会把硬编码的字符串“__main__”转换成“__name__”变量，例如：
```py
# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
__name__ = "__main__"
```
### 当你的模块被另一个引用时
在另一方面，假定一些其他模块是主程序并且它会引用你的模块。这意味着在主程序中会有一个陈述句，或者在主程序引用的一些其他模块中。
```py
# Suppose this is in some other main program.
import foo
```
在这种情况下，解释器将看到你的模块的文件名，foo.py.去掉（strip off）.py部分，并且指配那个字符串给你的模块的“__name__”变量,例如:
```py
# It's as if the interpreter inserts this at the top
# of your module when it's imported from another module.
__name__ == "foo"
```
### 执行模块中的代码
在特殊变量建立之后，解释器会执行模块中的所有代码，每次执行一条语句(one statement at a time)。您可能想在代码示例旁边打开另一个窗口，这样您就可以按照这个解释来操作了。（You may want to open another window on the side with the code sample so you can follow along with this explanation.）

#### 总是
  1，它会打印字符串``` before import ```（没有引用）
  2，它加载math模块并将其分配给一个名为math的变量。这相当于用以下代码替换导入数学(注意，在Python中，``` __import__ ```是一个低级函数，它接受一个字符串并触发实际的导入):（It loads the math module and assigns it to a variable called math. This is equivalent to replacing import math with the following (note that __import__ is a low-level function in Python that takes a string and triggers the actual import):）
```py
# Find and load a module given its string name,"math"
# then assign it to a local variable called math.
math = __import__("math")
```
  3，它会打印字符串``` before functionA ```.
  4，它会执行``` def ```语句块,创建一个函数对象，然后把这个函数对象赋值给一个叫``` functionA ```的变量。
  5，它会打印字符串“before functionB”。
  6，它会执行``` def ```语句块,创建一个函数对象，然后把这个函数对象赋值给一个叫``` functionB ```的变量。
  7，它会打印字符串``` before __name__ guard ```。
#### 只有当你的模块是主程序时
  8，如果你的模块是主程序，然后，确实是将``` __name__ ```实际上设置成``` __main__ ```并且它会引用两个函数，打印字符串``` FunctionA ```和``` FunctionB10.0 ```。
#### 只有当你的模块被另一个引用时
  9，（）如果你的模块不是主程序，但是它被另一个引用，然后``` __name__ ```将会是``` "__fo" ```，而不是``` "__main__" ```，并且它会跳过``` if ```语句的主体。
#### 总是
  10，它会在所有情况下打印字符串``` "after __name__ guard" ```
  
#### 总结
总之，以下是两种情况下的打印结果:
```py
# What gets printed if foo is the main program
before import
before functionA
before functionB
before __name__ guard
Function A
Function B 10.0
after __name__ guard
```

```py
# What gets printed if foo is imported as a regular module
before import
before functionA
before functionB
before __name__ guard
after __name__ guard
```






