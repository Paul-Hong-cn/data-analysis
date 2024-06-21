# 导入pandas模块
import pandas as pd
# 导入matplotlib模块中的日期转换函数
from matplotlib.dates import date2num
# 导入我们常用的plt模块
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams["font.sans-serif"] = "Simsun"

'''一、读取数据集并转化数据格式'''
# TODO 读取路径为"/Users/Jack/stock.csv"的CSV文件
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\量化交易\数据\stock.csv")

# TODO 使用pd.to_datetime()将trade_date列转化为时间格式
df['trade_date'] = pd.to_datetime(df['trade_date'])

# TODO 使用date2num()函数将trade_date列转换为时间戳格式
df['time'] = date2num(df['trade_date'])

# TODO 使用plt.plot()函数，绘制展示原数据股价变化的折线图
# 设置x轴为df["time"]，y轴为df["close"]，图例为"原股价变化"
plt.plot(df['time'],df['close'],label='原股价变化')

'''二、建立一元线性回归方程并做图'''
# TODO 导入sklearn.linear_model模块中的LinearRegression函数

from sklearn.linear_model import LinearRegression
# TODO 初始化一个线性回归对象赋值给变量lr
lr = LinearRegression()

# TODO 以二维结构读取"time"这一列，作为自变量x
x = df[['time']]

# TODO 以二维结构读取"close"这一列，作为因变量y
y = df[['close']]

# TODO 使用自变量x和因变量y，训练线性回归模型lr
lr.fit(x,y)

# TODO 将x传入模型的predict()函数，利用模型和自变量x来预测股价
y_pre = lr.predict(x)

# TODO 使用plt.plot()函数，绘制利用回归模型预测的股价变化的折线图
# 设置x轴为自变量x，y轴为预测结果，折线颜色为orange，图例为"回归直线"

plt.plot(x,y_pre,color='orange',label='回归直线')
'''三、建立一元对数回归模型并做图'''
# TODO 导入numpy模块命名为np
import numpy as np

# TODO 使用np.log()函数将df的close列数据对数化

y_log = np.log(df['close'])
# TODO 将自变量x和因变量依次传入fit()函数训练模型
lr.fit(x,y_log)

# TODO 将x传入模型的predict()函数，利用模型和自变量x来预测股价，并赋值给y_pred_log
y_pred_log = lr.predict(x)

# TODO 使用np.exp()函数将y_pred_log指数化，并赋值给y_pred_log
y_pred_log = np.exp(y_pred_log)

# TODO 使用plt.plot()函数，绘制利用一元对数模型预测的股价变化的折线图
# 设置x轴为自变量x，y轴为指数化后的预测结果，折线颜色为red，图例为"对数回归曲线"

plt.plot(x,y_pred_log,color='red',label='对数回归曲线')
# TODO 使用plt.legend()函数显示图例
plt.legend()

# 展示图像
plt.show()