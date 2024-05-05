import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\2019年国内脱发人群抽样信息.csv")

sexCount = df['性别'].value_counts()
maleNo = sexCount['男']
femaleNo = sexCount['女']
typeCount = df['脱发类型'].value_counts()
typeMax = typeCount.idxmax()
print(f"本次抽样调查中男性脱发人数为{maleNo}，女性脱发人数为{femaleNo}，脱发类型人数最多的为{typeMax}")

plt.rcParams['font.sans-serif'] = ['SimSun']
ageCount = df['年龄'].value_counts()
plt.subplot(2,2,1)
ageCount.plot.bar()
plt.xlabel("年龄")
plt.ylabel("人数")

careerCount = df['职业'].value_counts()
plt.subplot(2,2,2)
careerCount.plot.bar()
plt.xlabel("职业")
plt.ylabel("人数")
plt.xticks(rotation=45)

cityCount = df['所在城市'].value_counts()
plt.subplot(2,1,2)
cityCount.plot.bar()
plt.xlabel("所在城市")
plt.ylabel("人数")

plt.tight_layout()
plt.show()