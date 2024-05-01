import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("书店每月销量数据.csv")
plt.rcParams["font.sans-serif"] = "SimSun"

plt.plot(data["month"],data["sum"],color="orange",marker="o",label="每月总销量")

plt.xlabel('月份')
plt.ylabel('销量')
plt.title('2019年8月至2020年7月书店每月销量走势')

plt.legend()
plt.show()

plt.bar(data["month"],data["sum"],width=0.5,color="skyblue",label="每月总销量")
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月销量走势")

plt.legend()
plt.show()
