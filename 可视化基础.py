import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\可视化基础\书店每月销量数据.csv")
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\可视化基础\书店图书销量和广告费用.csv")
percentData = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\可视化基础\书店每月销量数据百分比.csv")

plt.rcParams["font.sans-serif"] = "SimSun"

plt.subplot(2,2,1)
plt.plot(data["month"],data["sum"])
plt.xticks(rotation=90)
plt.xlabel("月份")
plt.ylabel("销量")

plt.subplot(2,2,2)
plt.scatter(df["ads_fee"],df["sales"])
plt.xlabel("广告费用")
plt.ylabel("销量")

plt.subplot(2,2,3)
data.plot.bar("month",["first_floor","second_floor","third_floor"],ax=plt.gca())
plt.xlabel("月份")
plt.ylabel("销量")

plt.subplot(2,2,4)
percentData.plot.bar("month",["一楼","二楼","三楼"],stacked=True,ax=plt.gca())
plt.xlabel("月份")
plt.ylabel("占比")

plt.tight_layout()
plt.show()