
```
import numpy as np
import pandas as pd
from pyecharts import Overlap,Page,Bar,Line,Page
from pylab import mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决中文字体显示问题
plt.rc('figure', figsize=(10, 10))            #把plt默认的图片size调大一点

data = pd.DataFrame(pd.read_excel('软微2019成绩.xlsx'))

page=Page()

data=data.drop(['政治','外语','报名号','考试方式'],axis=1)


# 去掉每门课的缺考成绩,

data=data[~data['政治分'].isin(['缺考'])]
data=data[~data['外语分'].isin(['缺考'])]
data=data[~data['科目1分'].isin(['缺考'])]
data=data[~data['科目2分'].isin(['缺考'])]

# 分类一下
technology=data[(data['专业名称']=='计算机技术')]
computer=data[(data['专业名称']=='计算机技术')&(data['科目2']=='计算机基础综合')]
#print(technology.shape)
economic=data[(data['专业名称']=='计算机技术')&(data['科目2']=='经济学综合')]
embedded_system=data[(data['专业名称']=='计算机技术')&(data['科目2']=='嵌入式技术基础')]
apply=data[(data['专业名称']=='计算机技术')&(data['科目2']=='计算机应用基础')]
soft=data[(data['专业名称']=='软件工程')]


# 重置了index序号，也就是把序号置为1,2,3,4,5,6（一开始序号不是如此，而是1,3，4这种）
s1=soft.sort_values('总分',ascending=False)
s1=s1.reset_index(drop=True)

t1=technology.sort_values('总分',ascending=False)
t1=t1.reset_index(drop=True)


c1=computer.sort_values('总分',ascending=False)
c1=c1.reset_index(drop=True)

e1=economic.sort_values('总分',ascending=False)
e1=e1.reset_index(drop=True)

a1=apply.sort_values('总分',ascending=False)
a1=a1.reset_index(drop=True)

e2=embedded_system.sort_values('总分',ascending=False)
e2=e2.reset_index(drop=True)


# 技术类总的前十名，金融的前十名，以及计算机的前十名等
technology_top_ten=t1.iloc[:10,]
computer_top_ten=c1.iloc[:10,]
economic_top_ten=e1.iloc[:10,]
embedded_system_top_ten=e2.iloc[:10,]
apply_top_ten=a1.iloc[:10,]
soft_top_ten=s1.iloc[:10,]


#构造新的dataframe
computer1=pd.DataFrame(computer,columns=['政治分','外语分','科目1分','科目2分','总分'])
#print(computer1)
"""
print("分数均值")
print(computer1.mean())
print("标准差:")
print(computer1.std())
print("数据描述")
print(computer1.describe())
print("最高分")
print(computer1.max())
print("最低分")
print(computer1.min())
"""



'''
数学成绩与专业课成绩的相关性
'''
computer2=pd.DataFrame(computer,columns=['科目1分','科目2分'])
#computer2=computer2.drop_duplicates(subset=['科目2分'])

#print(computer2.shape)

x=computer2['科目1分']
y=computer2['科目2分'].values
#print(computer1)
'''
regr=linear_model.LinearRegression()
regr.fit(x,y)
print('Intercept:{}'.format(regr.intercept_))
print('Coeffecien:{}'.format(regr.coef_))
plt.plot(x,regr.predict(x),linewidth=10,color='blue')
'''
#散点图绘制
plt.scatter(x,y,color='black')
plt.xlabel('专业课成绩')
plt.ylabel('数学成绩')

'''
单科可能未过线
'''
computer_fail=computer.loc[(computer['政治分']<50)|(computer['外语分']<50)|(computer['科目1分']<90)|(computer['科目2分']<90)]
computer_fail1=computer_fail.loc[computer['总分']>350]
print(computer_fail1)


'''
计算机大概率进复试 差额比1：1.2，150*1.2=180
软工约为57
'''
print("计算机能进复试的分数")
computer_reexamin=c1.iloc[:180,]
print(computer_reexamin)

print("软工能进复试的分数")
soft_reexamin=s1.iloc[:57],
print(soft_reexamin)




#考生编号转换列为索引
computer_top_ten.set_index('考生编号')
#print(computer_top_ten)
line1=Line("计算机前十名")
i=computer_top_ten['考生编号']
j=computer_top_ten['总分']
# Python map()函数将一个全部为int的列表，转化为全部为str的列表
attr1=list(map(str,i))  # 考生编号
v=list(j)   # 总分
# 曲线平滑
line1.add("",attr1,v,is_smooth=True,mark_line=["max","average"])
page.add(line1)


'''
绘制成绩分布直方图
'''
computer.set_index('考生编号')


computer['成绩分段']=pd.cut(computer['总分'],[1,100,200,250,290,310,330,350,370,390,410,430,450],
        labels=['0-99分','100-199分','200-249分','250-289分','290-309分','310-329分','330-349分','350-369分','370-389分','390-409分','410-429分','430-449分'],right=False)


bar1=Bar('计算机总体成绩分布')
score_total = computer['成绩分段'].value_counts().sort_index()

line2 = Line("", width=700)
bar1.add("", score_total.index, score_total.values, bar_category_gap='40%', label_color = ['#130f40'],mark_line=["max","average"])
line2.add("", score_total.index, score_total.values+5, is_smooth=True)

overlap = Overlap(width=700)
overlap.add(bar1)
overlap.add(line2)
page.add(overlap)



'''
绘制成绩分布直方图，这部分没认真看
'''
computer.set_index('考生编号')


computer['成绩分段']=pd.cut(computer['总分'],[1,100,200,250,290,310,330,350,370,390,410,430,450],
        labels=['0-99分','100-199分','200-249分','250-289分','290-309分','310-329分','330-349分','350-369分','370-389分','390-409分','410-429分','430-449分'],right=False)


bar1=Bar('计算机总体成绩分布')
score_total = computer['成绩分段'].value_counts().sort_index()

line2 = Line("", width=700)
bar1.add("", score_total.index, score_total.values, bar_category_gap='40%', label_color = ['#130f40'],mark_line=["max","average"])
line2.add("", score_total.index, score_total.values+5, is_smooth=True)

overlap = Overlap(width=700)
overlap.add(bar1)
overlap.add(line2)
page.add(overlap)



page.render("./total.html")

```

### 具体分析

#### 1，获取文件具体信息
```
data.shape
```
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/py11280328.jpg)
```
data.head
```
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/py1911280330.jpg)

##### 读取行列数及索引
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/1911280333.jpg)
##### 读取指定数据
* （1），读取指定单行和多行数据
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/1911280334.jpg)
* （2），读取指定单列和多列数据
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/py911280335.jpg)
* （3），读入单元格数据或部分数据
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/py911280336.jpg)


#### 2，输出数据到xlsx文件（举一个列出869成绩高于140分的学生信息）
```

import pandas as pd

data = pd.DataFrame(pd.read_excel('软微2019成绩.xlsx'))

tmp = []
for i in range(1,len(data.index.values)):
    if data.iloc[i,8] == '缺考':
        continue
    elif data.iloc[i,8] == '违纪':# 存在违纪同学
        continue
    if int(data.iloc[i,8]) >= 140:
        tmp.append(data.iloc[i].values)

writer = pd.ExcelWriter('869成绩高于140分的学生信息.xlsx')
data2 = pd.DataFrame(data=tmp,columns=data.columns.values)
data2.to_excel(writer,'Sheet_one',index=False)
writer.save()


```
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/py911280337.jpg)
* 863仅有两人140分，第二个也太夸张了，数学85，英语45，专业课强，但是没用，连国家线都不达
* [Pyecharts官方文档：](https://pyecharts.org/#/zh-cn/intro)


#### 3，用Python处理pdf文件中的数据：
* （1），导入库
![](https://github.com/BinGYiZhanG/Python_/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E6%88%98/Images/py911280341.jpg)
```
生成的df的类型是：
Out[4]: pandas.core.frame.DataFrame

```















