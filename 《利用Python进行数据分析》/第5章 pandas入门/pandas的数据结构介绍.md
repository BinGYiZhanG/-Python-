pandas是基于Numpy构建的，
```py
In [1]: import pandas as pd

In [2]: from pandas import Series,DataFrame
```
开头必加的两句，第一句不用解释，第二句是因为Series和DataFrame更为常用

## Series

#### 1,Series的```.index```与```.values```值
```py
In [3]: obj=Series([4,7,-5,3])

In [4]: obj
Out[4]:
0    4
1    7
2   -5
3    3
dtype: int64

In [5]: obj.index
Out[5]: RangeIndex(start=0, stop=4, step=1)

In [6]: print(obj.index)
RangeIndex(start=0, stop=4, step=1)

In [7]: obj.values
Out[7]: array([ 4,  7, -5,  3], dtype=int64)

In [8]: obj2=Series([4,7,-5,3],index=['d','b','a','c'])

In [9]: obj2
Out[9]:
d    4
b    7
a   -5
c    3
dtype: int64

In [10]: obj2.index
Out[10]: Index(['d', 'b', 'a', 'c'], dtype='object')

#### 2,选取单个元素
```py
In [11]: obj2['a']
Out[11]: -5

In [12]: obj2['c','a','d']
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\indexes\base.py in get_value(self, series, key)
   2565             try:
-> 2566                 return libts.get_value_box(s, key)
   2567             except IndexError:

pandas/_libs/tslib.pyx in pandas._libs.tslib.get_value_box()

pandas/_libs/tslib.pyx in pandas._libs.tslib.get_value_box()

TypeError: 'tuple' object cannot be interpreted as an integer

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-12-67f905a5ddf9> in <module>()
----> 1 obj2['c','a','d']

D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\series.py in __getitem__(self, key)
    621         key = com._apply_if_callable(key, self)
    622         try:
--> 623             result = self.index.get_value(self, key)
    624
    625             if not is_scalar(result):

D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\indexes\base.py in get_value(self, series, key)
   2572                     raise InvalidIndexError(key)
   2573                 else:
-> 2574                     raise e1
   2575             except Exception:  # pragma: no cover
   2576                 raise e1

D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\indexes\base.py in get_value(self, series, key)
   2558         try:
   2559             return self._engine.get_value(s, k,
-> 2560                                           tz=getattr(series.dtype, 'tz', None))
   2561         except KeyError as e1:
   2562             if len(self) > 0 and self.inferred_type in ['integer', 'boolean']:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: ('c', 'a', 'd')

In [13]: obj2[['c','a','d']]
Out[13]:
c    3
a   -5
d    4
dtype: int64

In [14]:

In [14]: obj2[obj2>0]
Out[14]:
d    4
b    7
c    3
dtype: int64

```
#### 3,对Series进行操作
```py
In [15]: obj2*2
Out[15]:
d     8
b    14
a   -10
c     6
dtype: int64

In [16]: np.exp(obj2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-16-6ae9d3c15d3f> in <module>()
----> 1 np.exp(obj2)

NameError: name 'np' is not defined

In [17]: import numpy as np

In [18]: np.exp(obj2)
Out[18]:
d      54.598150
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
```

#### 4,检测Series中的元素
```py
In [19]: 'b' in obj2
Out[19]: True
```

#### 5,Seires与字典
* 可以将Series看成一个定长的有序字典
* 可以通过字典来创建Series
* 可以只传入一个字典

```py
In [20]: sdata={'ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}

In [21]: obj3=Series(sdata)

In [22]: obj3
Out[22]:
Oregon    16000
Texas     71000
Utah       5000
ohio      35000
dtype: int64

In [23]: states=['California','Ohio','Oregon','Texas']

In [24]: obj4=Series(sdata,index=states)

In [25]: obj4
Out[25]:
California        NaN
Ohio              NaN
Oregon        16000.0
Texas         71000.0
dtype: float64
```

#### 6,检测Series的确实值
```py
In [26]: pd.isnull(obj4)
Out[26]:
California     True
Ohio           True
Oregon        False
Texas         False
dtype: bool

In [27]: pd.notnull(obj4)
Out[27]:
California    False
Ohio          False
Oregon         True
Texas          True
dtype: bool

In [28]: obj4.isnull()
Out[28]:
California     True
Ohio           True
Oregon        False
Texas         False
dtype: bool
```

#### 7,在算数运算中自动对齐不同索引的数据
```py
In [29]: obj3
Out[29]:
Oregon    16000
Texas     71000
Utah       5000
ohio      35000
dtype: int64

In [30]: obj4
Out[30]:
California        NaN
Ohio              NaN
Oregon        16000.0
Texas         71000.0
dtype: float64

In [31]: obj3+obj4
Out[31]:
California         NaN
Ohio               NaN
Oregon         32000.0
Texas         142000.0
Utah               NaN
ohio               NaN
dtype: float64
```

#### 8,Series对象本身机器索引都有一个name属性
```py
In [32]: obj
Out[32]:
0    4
1    7
2   -5
3    3
dtype: int64

In [33]: obj.index=['Bob','Steve','Jeff','Ryan']

In [34]: obj
Out[34]:
Bob      4
Steve    7
Jeff    -5
Ryan     3
dtype: int64


In [35]: obj4.name='population'

In [36]: obj4.index.name='state'

In [37]: obj4
Out[37]:
state
California        NaN
Ohio              NaN
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64

```

