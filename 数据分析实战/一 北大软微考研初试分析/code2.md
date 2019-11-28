
```
import tabula
import numpy as np
import pandas as pd
from pyecharts import Bar, Line, Overlap,Page
from pylab import mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']  #解决中文字体显示问题
plt.rc('figure', figsize=(10, 10))            #把plt默认的图片size调大一点
page=Page()
Data = tabula.read_pdf("F:\\正在学\\Python\\数据分析实战\\一 2019北大软微考研初试分析\\2018北大软微拟录取名单.pdf", encoding='gbk', pages='all')
# print(data)
"""
删除数据没有成功，

"""

# 
df = pd.DataFrame(columns=Data.iloc[1].values)
for index in Data.index.values[2:]:
    # print(Data.iloc[index].values)
    row={
        '序号':Data.iloc[index].values[0],
        '考生编号':Data.iloc[index].values[1],
        '考生姓名':Data.iloc[index].values[2],
        '拟录取专业':Data.iloc[index].values[3],    
        '初试成绩':Data.iloc[index].values[4],   
        '复试成绩':Data.iloc[index].values[5],
        '总成绩':Data.iloc[index].values[6],
        '备注':Data.iloc[index].values[7]
            }
    df = df.append(row,ignore_index=True) # 一定要重新复制，才能保存结果



data = df.drop('序号',axis=1,inplace=False)
# data.set_index('考生编号')

"""
#print(computer_top_ten)
line1=Line("计算机前十名")
i=data_2['考生编号']
j=data_2['总成绩']

attr1=list(map(str,i))
v=list(j)
line1.add("",attr1,v,is_smooth=True,mark_line=["max","average"])
page.add(line1)
page.render("./total1.html")
"""
computer=data[(data['拟录取专业']=='计算机技术')]

c1=computer.sort_values('总成绩',ascending=False)
c1=c1.reset_index(drop=True)  #必加，相当于改变编号，缩短


line1=Line("计算机初试成绩")
i=c1['考生编号']
j1=c1['初试成绩']

attr1=list(map(str,i))
v1=list(j1)
line1.add("",attr1,v1,is_smooth=True,mark_line=["max","average"])
page.add(line1)


line2=Line("计算机总成绩")
i=c1['考生编号']
j2=c1['总成绩']

attr1=list(map(str,i))
v2=list(j2)
line2.add("",attr1,v2,is_smooth=True,mark_line=["max","average"])
page.add(line2)

page.render("./total1.html")



```
