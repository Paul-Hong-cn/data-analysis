# 导入matplotlib.pyplot，并使用"plt"作为该模块的简写
import matplotlib.pyplot as plt

# 导入pandas，并使用"pd"作为该模块的简写
import pandas as pd

# 使用pd.read_csv()函数
data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\可视化基础\书店每月销量数据.csv")
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\可视化基础\书店图书销量和广告费用.csv")
percentData = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\可视化基础\书店每月销量数据百分比.csv")

# 通过给 plt.rcParams["font.sans-serif"] 赋值
# 将字体设置为 Simsun
plt.rcParams["font.sans-serif"] = "SimSun"

# 使用plt.subplot()函数添加4个子图
# 子图有两行两列
# 选择序号为1子图
plt.subplot(2,2,1)
# 使用plt.plot()函数绘制折线图
plt.plot(data["month"],data["sum"])
# 使用plt.xticks()函数旋转x轴的刻度至90度
plt.xticks(rotation=90)
# 使用plt.xlabel()函数，将x轴标题设置为"月份"
plt.xlabel("月份")
# 使用plt.ylabel()函数，将y轴标题设置为"销量"
plt.ylabel("销量")

# 选择序号为2子图
plt.subplot(2,2,2)
# 使用plt.scatter()函数
# 以df["ads_fee"]为x轴的值和df["sales"]为y轴的值，绘制散点图
plt.scatter(df["ads_fee"],df["sales"])
# 使用plt.xlabel()函数，将x轴标题设置为"广告费用"
plt.xlabel("广告费用")
# 使用plt.ylabel()函数，将y轴标题设置为"销量"
plt.ylabel("销量")

# 选择序号为3的子图
plt.subplot(2,2,3)
# 使用plot.bar()函数和ax=plt.gca()
# 根据data中的数据
# 以"month"为x轴，["first_floor","second_floor","third_floor"]为y轴
# 绘制簇形柱状图
data.plot.bar("month",["first_floor","second_floor","third_floor"],ax=plt.gca())
# 使用plt.xlabel()函数，将x轴标题设置为"月份"
plt.xlabel("月份")
# 使用plt.ylabel()函数，将y轴标题设置为"销量"
plt.ylabel("销量")

# 选择序号为4子图
plt.subplot(2,2,4)
# 使用plot.bar()函数，stacked=True和ax=plt.gca()
# 根据percentData中的数据
# 以"month"为x轴，绘制对比["一楼","二楼","三楼"]的百分比堆积柱状图
percentData.plot.bar("month",["一楼","二楼","三楼"],stacked=True,ax=plt.gca())
# 使用plt.xlabel()函数，将x轴标题设置为"月份"
plt.xlabel("月份")
# 使用plt.ylabel()函数，将y轴标题设置为"占比"
plt.ylabel("占比")

# 使用plt.tight_layout()函数来调整子图布局
plt.tight_layout()
# 使用plt.show()函数显示图像
plt.show()