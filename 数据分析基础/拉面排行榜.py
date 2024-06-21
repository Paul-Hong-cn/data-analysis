import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\ramenRatings.csv")
plt.rcParams["font.sans-serif"] = "SimSun"

df['sum'] = df['Bowl'] + df['Cup'] + df['Pack']
df_1 = df.sort_values(by = 'sum',ascending=False)
df_1 = df_1.head(5)

df_1.plot.bar('Area',['Bowl','Cup','Pack'],stacked=True,ax=plt.gca())
plt.xlabel('国家/地区')
plt.ylabel('品牌总量')

plt.twinx()

plt.plot(df_1['Area'],df_1['rating'],marker='*',color='crimson')
plt.ylabel('评分')

plt.show()
