# 导入pandas模块
import pandas as pd
# 导入datetime模块中的datetime
from datetime import datetime

# 读取数据
data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\data.csv")

# 使用pd.to_datetime()函数将"购买日期"列转化为时间类型数据
data["购买日期"] = pd.to_datetime(data["购买日期"])

# 提取R
# TODO 使用groupby()函数和max()函数
# 将数据按"用户编号"分组，选出"购买日期"的最大值，并赋值给变量max_date
max_date = data.groupby('用户编号')['购买日期'].max()

# TODO 使用datetime()函数，构建2021年10月01日的时间，赋值给endTime
endTime = datetime(2021,10,1)

# TODO 计算endTime和max_date的差，用.dt.days将天数提取出来，赋值给R
R = (endTime - max_date).dt.days

# 提取F
# TODO 使用groupby()函数和count()函数
# 将数据按"用户编号"分组，按照"购买日期"计数，得到F
F = data.groupby('用户编号')['购买日期'].count()

# 提取M
# TODO 将"购买数量"与"购买单价"相乘，将结果添加为data的新列"金额"
data['金额'] = data['购买数量'] * data['购买单价']

# TODO 使用groupby()函数和sum()函数
# 按"用户编号"分组，按照"金额"求和
# 计算每个用户的金额总数，并赋值给变量M
M = data.groupby('用户编号')['金额'].sum()

# TODO 使用concat()函数
# 连接R,F,M三个序列为一个新的DataFrame，设置axis为1，横向连接
# 并将结果赋值给变量rfm
rfm = pd.concat([R,F,M],axis = 1)

# TODO 使用.columns函数将列名修改为["R","F","M"]
rfm.columns = ['R','F','M']

# TODO 对rfm["R"]用pd.cut()函数分箱
# 边界设置为[0,rfm["R"].mean(),rfm['R'].max()]，labels设置为[1,0]
rfm['R'] = pd.cut(rfm['R'],[0,rfm["R"].mean(),rfm['R'].max()],labels=[1,0])

# TODO 对rfm["F"]列用pd.cut()函数分箱
# 边界设置为[0,rfm["F"].mean(),rfm["F"].max()]，labels设置为[0,1]
rfm['F'] = pd.cut(rfm['F'],[0,rfm["F"].mean(),rfm["F"].max()],labels=[0,1])

# TODO 对rfm["M"]列用pd.cut()函数分箱
# 边界设置为[0,rfm["M"].mean(),rfm["M"].max()]，labels设置为[0,1]
rfm['M'] = pd.cut(rfm['M'],[0,rfm["M"].mean(),rfm["M"].max()],labels=[0,1])

# TODO 对rfm使用sum()函数横向求和，传入参数axis=1 做为rfm的新列"sum"
rfm['sum'] = rfm.sum(axis=1)

# TODO 用布尔索引将"sum"列大于等于2的数据筛选出，赋值给变量rfm_2
rfm_2 = rfm[rfm['sum']>=2]

# TODO 输出用户编号
print(rfm_2.index.values)