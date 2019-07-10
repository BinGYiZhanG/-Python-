```py
In [3]: import pandas as pd

In [4]: from pandas import Series,DataFrame
```
## 1,建立DataFrame变量，通过**等长列表**或**Numpy数组组成的字典**
###　DataFrame会自动加上索引（跟Series一样），且全部列会被有序排列
```py
In [5]: data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4
   ...: ,2.9]}

In [6]: frame=DataFrame(data)

In [7]: frame
Out[7]:
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002

```

## 2,指定列序列，DataFrame的列就会按照指定顺序进行排列
```py
In [8]: DataFrame(data,columns=['year','state','pop'])
Out[8]:
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
```
## 3,如果传入的列的数据找不到，会产生NA值

```py
In [9]: frame2=DataFrame(data,columns={'year','state','pop','debt'},index=['one','two','three','four','five'])

In [10]: frame2
Out[10]:
        state  year debt  pop
one      Ohio  2000  NaN  1.5
two      Ohio  2001  NaN  1.7
three    Ohio  2002  NaN  3.6
four   Nevada  2001  NaN  2.4
five   Nevada  2002  NaN  2.9

In [11]: frame2.columns
Out[11]: Index(['state', 'year', 'debt', 'pop'], dtype='object')
```

## 4,类似字典标记的方式或属性的方式，可以将DataFrame的列或缺为一个Series

```py
In [13]: frame2['state']
Out[13]:
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
Name: state, dtype: object

In [14]: frame2.year
Out[14]:
one      2000
two      2001
three    2002
four     2001
five     2002
Name: year, dtype: int64

```
*注：*返回的Series有用原DataFrame形同的索引，且其```name```属性也已经被相应地设置

## 5,取 行,不能用```frame2.ix['three']```，被deprivation

```py
In [15]: frame2.loc['three']
Out[15]:
state    Ohio
year     2002
debt      NaN
pop       3.6
Name: three, dtype: object
```

## 6,列赋值，修改列
```py
In [16]: frame2['debt']=16.5

In [17]: frame2
Out[17]:
        state  year  debt  pop
one      Ohio  2000  16.5  1.5
two      Ohio  2001  16.5  1.7
three    Ohio  2002  16.5  3.6
four   Nevada  2001  16.5  2.4
five   Nevada  2002  16.5  2.9
```
### range()改变列
```py
In [19]: frame2['debt']=np.arange(5.)

In [20]: frame2
Out[20]:
        state  year  debt  pop
one      Ohio  2000   0.0  1.5
two      Ohio  2001   1.0  1.7
three    Ohio  2002   2.0  3.6
four   Nevada  2001   3.0  2.4
five   Nevada  2002   4.0  2.9
```
## 7,给指定行，指定列赋值，其余的将被赋值为NaN

```py
In [21]: val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])

In [22]: frame2['debt']=val

In [23]: frame2
Out[23]:
        state  year  debt  pop
one      Ohio  2000   NaN  1.5
two      Ohio  2001  -1.2  1.7
three    Ohio  2002   NaN  3.6
four   Nevada  2001  -1.5  2.4
five   Nevada  2002  -1.7  2.9
```

## 8,增加新列,删除列
```py
In [24]: frame2['eastern']=frame2.state=='Ohio'

In [25]: frame2
Out[25]:
        state  year  debt  pop  eastern
one      Ohio  2000   NaN  1.5     True
two      Ohio  2001  -1.2  1.7     True
three    Ohio  2002   NaN  3.6     True
four   Nevada  2001  -1.5  2.4    False
five   Nevada  2002  -1.7  2.9    False

In [26]: del frame2['eastern']

In [27]: frame2
Out[27]:
        state  year  debt  pop
one      Ohio  2000   NaN  1.5
two      Ohio  2001  -1.2  1.7
three    Ohio  2002   NaN  3.6
four   Nevada  2001  -1.5  2.4
five   Nevada  2002  -1.7  2.9
```

## 9,嵌套字典创建DataFrame
```py
In [28]: pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,'2002':3.6}}

In [29]: frame3=DataFrame(pop)

In [30]: frame3
Out[30]:
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   NaN
2002     NaN   3.6
```
### 1,结果转置
```py
In [31]: frame3.T
Out[31]:
        2000  2001  2002  2002
Nevada   NaN   2.4   2.9   NaN
Ohio     1.5   1.7   NaN   3.6
```
### 2,显式指定索引
```py
In [32]: DataFrame(pop,index=[2001,2002.,2003])
Out[32]:
        Nevada  Ohio
2001.0     2.4   1.7
2002.0     2.9   NaN
2003.0     NaN   NaN
```
### 3,切片
```py
In [33]: pdata={'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}

In [34]: DataFrame(pdata)
Out[34]:
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     NaN   NaN
```
## 10,DataFrame构造函数可以接受的所有得数据类型

![](https://github.com/BinGYiZhanG/Python_/blob/master/%E3%80%8A%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E3%80%8B/Images/07101427.png)

## 11,关于设置行和列的```name```值
```py
In [35]: frame3.index.name='year';frame3.columns.name='state'

In [36]: frame3
Out[36]:
state  Nevada  Ohio
year
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   NaN
2002      NaN   3.6
```
### 跟Series一样，values数字那个也会以二维ndarray的形式返回DataFrame中的数据
```py
In [37]: frame3.values
Out[37]:
array([[nan, 1.5],
       [2.4, 1.7],
       [2.9, nan],
       [nan, 3.6]])
```
### 所有列存在数据类型兼容的现象
```py
In [38]: frame2.values
Out[38]:
array([['Ohio', 2000, nan, 1.5],
       ['Ohio', 2001, -1.2, 1.7],
       ['Ohio', 2002, nan, 3.6],
       ['Nevada', 2001, -1.5, 2.4],
       ['Nevada', 2002, -1.7, 2.9]], dtype=object)
```
## 12,索引对象
```py
In [40]: obj=Series(range(3),index=['a','b','c'])

In [41]: index=obj.index

In [42]: index
Out[42]: Index(['a', 'b', 'c'], dtype='object')

In [43]: index[1:]
Out[43]: Index(['b', 'c'], dtype='object')

In [44]: index[1]='d'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-44-8be6e68dba2d> in <module>()
----> 1 index[1]='d'

D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\indexes\base.py in __setitem__(self, key, value)
   1722
   1723     def __setitem__(self, key, value):
-> 1724         raise TypeError("Index does not support mutable operations")
   1725
   1726     def __getitem__(self, key):

TypeError: Index does not support mutable operations
```
### 索引对象不可改变
### 不可修改性非常重要，因为重要才能使Index对象在多个数据结构中安全共享

```py
In [46]: index=pd.Index(np.arange(3))

In [47]: obj2=Series([1.5,-2.5,0],index=index)

In [49]: obj2.index is index
Out[49]: True

```
### Index对象是pandas数据模型的重要组成部分
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E3%80%8A%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E3%80%8B/Images/07101441.png)

### Index功能也类似一个固定大小的集合
```py
In [50]: frame3
Out[50]:
state  Nevada  Ohio
year
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   NaN
2002      NaN   3.6

NameError: name 'frames' is not defined

In [52]: 'Ohio' in frame3.columns
Out[52]: True

In [53]: 2003 in frame3.index
Out[53]: False
```
### Index的属性和方法

![](https://github.com/BinGYiZhanG/Python_/blob/master/%E3%80%8A%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E3%80%8B/Images/07101444.png)




