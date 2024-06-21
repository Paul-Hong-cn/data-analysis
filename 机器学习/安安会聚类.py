# 导入pandas模块命名为pd
import pandas as pd

# 读取数据
data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\customer_data.csv")

# TODO 提取特征变量
x = data[['Income', 'Spending']]

'''数据归一化'''
# TODO 导入sklearn.preprocessing模块中的StandardScaler类
from sklearn.preprocessing import StandardScaler

# TODO 创建一个StandardScaler对象，并赋值给变量scaler
scaler = StandardScaler()

# TODO 对x进行归一化
x_scale = scaler.fit_transform(x)

'''搭建K-Means模型'''
# TODO 导入sklearn.cluster模块中的KMeans模型
from sklearn.cluster import KMeans

# TODO 使用KMeans()初始化模型
# 设置参数n_clusters=5, random_state=1
# 将结果赋值给model
model = KMeans(n_clusters=5, random_state=1)

# TODO 使用fit()函数训练模型
model.fit(x_scale)

# TODO 获取聚类后的质心，并赋值给变量centers

centers = model.cluster_centers_
# TODO 输出centers

print(centers)
# TODO 获取聚类后的类别标签，并赋值给labels
labels = model.labels_

# TODO 输出labels
print(labels)

# 导入matplotlib.pyplot命名为plt
import matplotlib.pyplot as plt

# 自定义一个颜色列表colValue
colValue = ["dodgerblue", "c", "lightgreen", "lightcoral", "lightpink"]

# 4个类分别考虑
for i in [0, 1, 2, 3, 4]:
    # 定义一个初始化的x坐标列表
    coo_X = []
    # 定义一个初始化的y坐标列表
    coo_Y = []

    # 依次遍历所有类别标签
    for j in range(len(labels)):

        # 如果第j个类被等于现在的类别i
        # 就将Income的第j个值添加到coo_X, Spending的第j个值添加到coo_Y
        if labels[j] == i:
            coo_X.append(data["Income"][j])
            coo_Y.append(data["Spending"][j])

    # 根据类别i绘制散点图
    # 横轴为coo_X，纵轴为coo_Y，设置marker为"."，颜色设置为colValue[i]
    plt.scatter(coo_X, coo_Y, marker=".", color=colValue[i])

# 展示图像
plt.show()