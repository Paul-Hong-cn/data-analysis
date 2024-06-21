# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 读取路径为/Users/hairloss/2019年国内脱发人群抽样信息.csv的文件，赋值给变量df
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\2019年国内脱发人群抽样信息.csv")

# TODO 计算df["性别"]中男女人数的Series对象，并赋值给变量sexCount
sexCount = df['性别'].value_counts()
# TODO 通过索引获取sexCount中的男性人数，并赋值给变量maleNo
maleNo = sexCount['男']
# TODO 通过索引获取sexCount中的女性人数，并赋值给变量femaleNo
femaleNo = sexCount['女']

# TODO 计算df["脱发类型"]中各脱发类型人数的Series对象，并赋值给变量typeCount
typeCount = df['脱发类型'].value_counts()
# TODO 使用idxmax()函数获取typeCount中人数最多的脱发类型，并赋值给变量typeMax
typeMax = typeCount.idxmax()

# TODO 格式化输出
# 本次抽样调查中男性脱发人数为{maleNo}，女性脱发人数为{femaleNo}，脱发类型人数最多的为{typeMax}
print(f"本次抽样调查中男性脱发人数为{maleNo}，女性脱发人数为{femaleNo}，脱发类型人数最多的为{typeMax}")

# 数据可视化
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Simsun']

# TODO 计算df["年龄"]中不同年龄人数的Series对象，并赋值给变量ageCount
ageCount = df['年龄'].value_counts()
# 绘制年龄——人数柱状图
plt.subplot(2,2,1)
ageCount.plot.bar()
plt.xlabel("年龄")
plt.ylabel("人数")

# TODO 计算df["职业"]中各职业人数的Series对象，并赋值给变量careerCount
careerCount = df['职业'].value_counts()
# 绘制职业——人数柱状图
plt.subplot(2,2,2)
careerCount.plot.bar()
plt.xlabel("职业")
plt.ylabel("人数")
plt.xticks(rotation=45)

# TODO 计算df["所在城市"]中各城市人数的Series对象，并赋值给变量cityCount
cityCount = df['所在城市'].value_counts()
# 绘制所在城市——人数柱状图
plt.subplot(2,1,2)
cityCount.plot.bar()
plt.xlabel("所在城市")
plt.ylabel("人数")

# 调整子图布局
plt.tight_layout()
# 展示图片
plt.show()