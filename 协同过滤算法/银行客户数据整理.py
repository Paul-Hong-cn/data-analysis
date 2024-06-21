# 导入pandas模块
import pandas as pd

# 读取数据
records = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\records.csv")
userInformation = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\user_information.csv")

# TODO 使用merge()函数
# 按照"id"这一列，合并records和userInformation
newData = pd.merge(records,userInformation)

# TODO 使用groupby()函数和mean()函数
# 将newData按照"id"这一列进行分组与聚合
# 计算每个用户的平均记录次数，并赋值给变量groupByRecord
groupByRecord = newData.groupby(newData['id']).mean()

# TODO 使用max()函数
# 获取groupByRecord["记录次数"]这一列的最大值，并赋值给timesMax
timesMax = groupByRecord['记录次数'].max()

# TODO 用布尔索引筛选出groupByRecord中
# 记录次数等于timesMax的数据，赋值给变量maxData
maxData = groupByRecord[groupByRecord['记录次数']==timesMax]

# TODO 将maxData中"近6个月有交易月份数"列的值用value_counts()进行计数排序
# 并赋值给变量monthCount
monthCount = maxData["近6个月有交易月份数"].value_counts()

# TODO 输出monthCount
print(monthCount)

# 导入matplotlib.pyplot
import matplotlib.pyplot as plt

# 通过给 plt.rcParams["font.sans-serif"] 赋值
# 将字体设置为 Simsun
plt.rcParams["font.sans-serif"] = "SimSun"

# TODO 使用plt.bar()函数绘制柱状图
# 将x轴数据设置为monthCount.index，y轴数据设置为monthCount.values
plt.bar(monthCount.index,monthCount.values)

# 使用plt.show()函数显示图像
plt.show()