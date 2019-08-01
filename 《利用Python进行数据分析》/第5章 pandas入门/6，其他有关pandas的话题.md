
```py
In [9]: ser=np.Series(np.arange(3.))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-9-f795477a110c> in <module>()
----> 1 ser=np.Series(np.arange(3.))

AttributeError: module 'numpy' has no attribute 'Series'

In [10]: ser=pd.Series(np.arange(3.))

In [11]: ser[-1]#我们有含有0，1，2的索引，很难推断用户想要什么
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-11-44969a759c20> in <module>()
----> 1 ser[-1]

D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\series.py in __getitem__(self, key)
    621         key = com._apply_if_callable(key, self)
    622         try:
--> 623             result = self.index.get_value(self, key)
    624
    625             if not is_scalar(result):

D:\Python\Anaconda3 5.1.0\lib\site-packages\pandas\core\indexes\base.py in get_value(self, series, key)
   2558         try:
   2559             return self._engine.get_value(s, k,
-> 2560                                           tz=getattr(series.dtype, 'tz', None))
   2561         except KeyError as e1:
   2562             if len(self) > 0 and self.inferred_type in ['integer', 'boolean']:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

KeyError: -1

In [12]: ser]
  File "<ipython-input-12-89945125027e>", line 1
    ser]
       ^
SyntaxError: invalid syntax


In [13]: ser
Out[13]:
0    0.0
1    1.0
2    2.0
dtype: float64

In [14]: ser2=pd.Series(np.arange(3.),index=['a','b','c'])

In [15]: ser2
Out[15]:
a    0.0
b    1.0
c    2.0
dtype: float64

In [16]: ser2[-1]#对于一个非整数索引，没有这样的歧义
Out[16]: 2.0

In [17]: ser.ix[:1]
D:\Python\Anaconda3 5.1.0\Scripts\ipython:1: DeprecationWarning:
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
Out[17]:
0    0.0
1    1.0
dtype: float64

In [18]: ser.loc[:1]
Out[18]:
0    0.0
1    1.0
dtype: float64

In [19]: ser3=pd.Series(range(3),index=[-5,1,3])

In [20]: ser3
Out[20]:
-5    0
 1    1
 3    2
dtype: int64
```
