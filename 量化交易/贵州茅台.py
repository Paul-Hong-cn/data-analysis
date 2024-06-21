'''一、获取股票数据'''
# TODO 导入tushare模块简写为ts
import tushare as ts

# TODO 使用set_token()函数设置token码b1ea3de4b1d3f20610c72588312da6d6e1acd4475b6e92f6fc296572
ts.set_token("5c9f587776e7ecf43dbb3e2c8ef4233b92c591bf54134a9cc58da917")

# TODO 使用pro_api()函数调取pro_api接口，赋值给变量api
api = ts.pro_api()

# TODO 使用daily()函数
# 获取股票代码为"600519.SH"，时间为"20180101"到"20220101"时间段的股票信息
# 并赋值给变量df
df = api.daily(ts_code='600519.SH',start_date='20180101',end_date='20220101')

'''二、计算每个月的月平均交易量、月平均交易额和月平均收盘价'''
# TODO 自定义一个函数year_month，返回x的前6个字符
def year_month(x):
    return x[0:6]

# TODO 对df的trade_date列使用apply函数()
# 将year_month作为参数传入，提取年月信息
# 把结果重新赋值给df的trade_date列
df['trade_date'] = df['trade_date'].apply(year_month)

# TODO 使用groupby()函数和mean()函数
# 将df变量按照trade_date聚合后求均值，并把结果赋值给变量groupby
groupby = df.groupby(df['trade_date']).mean(numeric_only=True)

# TODO 获取每个月的月平均交易量，也就是groupby中vol的值，赋值给变量vol
vol = groupby['vol']

# TODO 获取每个月的月平均交易额，也就是groupby中amount的值，赋值给变量amount
amount = groupby['amount']

# TODO 获取每个月的月平均收盘价，也就是groupby中close的值，赋值给变量close
close = groupby['close']

'''可视化结果'''
# 导入matplotlib模块
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = "Simsun"

# TODO 使用plt.figure()函数创建画布
# 设置参数figsize设置画布大小为(10,6)
plt.figure(figsize=(10,6))

# TODO 使用plt.subplot()函数添加3个子图
# 子图有三行一列
# 选择序号为1子图
plt.subplot(3,1,1)

# TODO 使用plt.plot()函数绘制展现月平均交易量的折线图
plt.plot(vol.index,vol.values)

# TODO 使用plt.title()设置标题为月平均交易量
plt.title('月平均交易量')

# TODO 使用plt.xticks()函数旋转x轴的刻度至90度
plt.xticks(rotation=90)

# TODO 选择序号为2子图
plt.subplot(3,1,2)

# TODO 使用plt.plot()函数绘制展现月平均交易额的折线图
plt.plot(amount.index,amount.values)

# TODO 使用plt.title()设置标题为月平均交易额

plt.title('月平均交易额')
# TODO 使用plt.xticks()函数旋转x轴的刻度至90度
plt.xticks(rotation=90)

# TODO 选择序号为3子图
plt.subplot(3,1,3)

# TODO 使用plt.plot()函数绘制展现月平均收盘价的折线图
plt.plot(close.index,close.values)

# TODO 使用plt.title()设置标题为月平均收盘价
plt.title('月平均收盘价')

# TODO 使用plt.xticks()函数旋转x轴的刻度至90度
plt.xticks(rotation=90)

# TODO 使用plt.tight_layout()函数来调整子图布局

plt.tight_layout()
# TODO 展示图像
plt.show()