### 2,intersection.py

$x_n2=x_n1-function(x_n1)*\frac{x_n1-x_n}{function(x_n1)-function(x_n)}$<br>
if abs(x_n2-x_n1)<$10^{-5}$<br>
  return x_n2<br>
x_n=x_n1<br>
x_n1=x_n2<br>

### 3,lu_decomposition.py
首先，i，j打印就非常奇怪，j竟然出现了-1，对于矩阵U如何遍历负数下标？
```py
In [12]: for i in range(3):
    ...:     print("第"+str(i)+"次")
    ...:     for j in range(i-1):
    ...:         print(str(i)+" "+str(j))
    ...:     print("********************")
    ...:     for j in range(i-1,3):
    ...:         print(str(i)+" "+str(j))
    ...:
第0次
********************
0 -1
0 0
0 1
0 2
第1次
********************
1 0
1 1
1 2
第2次
2 0
********************
2 1
2 2

```
### 4，newton_method.py

#### [牛顿法wiki:](https://zh.wikipedia.org/wiki/%E7%89%9B%E9%A1%BF%E6%B3%95)

选择一个接近$f(x)$零点的$x_{0}$,计算相应的$f(x_{0})和切线斜率f^{'}(x_{0})$($f^{'}$代表函数$f$的导数)<br>
即，求如下方程的解：
$0=(x-x_{0})·f^{'}(x_{0})+f(x_{0})$
我们将解命名为$x_{1}$，通常$x_{1}$比$x{0}$更接近方程$f(x)=0$的解,因此我们采用$x_{1}$开始下一轮迭代。<br>
公式可简化为:
$x_{n+1}=x_{n}-\frac{f(x_{n})}{f^{'}(x_{n})}$
前置条件:<br>
$f^{'}(x)\neq 0$（一共有4个条件，这里我只列出了一个，）




### 5，newton_raphson_method.py
* eval() 函数用来执行一个字符串表达式，并返回表达式的值：
```py

>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> n=81
>>> eval("n + 4")
85

```


