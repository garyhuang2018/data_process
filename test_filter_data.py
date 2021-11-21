# -*- encoding utf-8 -*-
# 导入数据分析包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['font.sans-serif'] = ['SimHei']  # 制定plt用的中文字体
data = pd.read_excel('issues.xlsx')
bar_data = pd.pivot_table(data, index='项目管理人员', aggfunc='count', values=['项目名称']).sort_values('项目名称',
                                                                                              ascending=False)
print(bar_data)
y = bar_data['项目名称'].tolist()
x = bar_data.index
plt.xlabel(u'项目管理人员')
plt.ylabel(u'问题反馈数量')
plt.bar(x, y)
plt.show()
