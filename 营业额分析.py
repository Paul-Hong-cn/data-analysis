import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = "SimSun"
data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\商场营业额数据.csv")

data["date"] = pd.to_datetime(data["date"])
data = data.set_index("date")
groupByCategory = data.groupby(data['category']).resample('ME').sum()

enter = groupByCategory.loc["娱乐"]
service = groupByCategory.loc["服务"]
retail = groupByCategory.loc["零售"]
catering = groupByCategory.loc['餐饮']

enter.index = enter.index.strftime("%Y/%m")
service.index = service.index.strftime("%Y/%m")
retail.index = retail.index.strftime("%Y/%m")
catering.index = catering.index.strftime("%Y/%m")

plt.subplot(2,2,1)
plt.bar(enter.index,enter["turnover"])
plt.xticks(rotation = 90)
plt.title("娱乐")

plt.subplot(2,2,2)
plt.bar(service.index,service["turnover"])
plt.xticks(rotation = 90)
plt.title("服务")

plt.subplot(2,2,3)
plt.bar(retail.index, retail["turnover"])
plt.xticks(rotation = 90)
plt.title("零售")

plt.subplot(2,2,4)
plt.bar(catering.index, catering["turnover"])
plt.xticks(rotation = 90)
plt.title("餐饮")

plt.tight_layout()
plt.show()