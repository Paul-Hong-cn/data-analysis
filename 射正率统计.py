import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Euro2012.csv')
plt.rcParams["font.sans-serif"] = "SimSun"

plt.bar(df['Team'],df['Shooting Accuracy'],label='射正率')
plt.xlabel('队名')
plt.ylabel('射正率')
plt.title('2012年欧洲杯各球队射正率柱状图')

plt.legend()
plt.show()