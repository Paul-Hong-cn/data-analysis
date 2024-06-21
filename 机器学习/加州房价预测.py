from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
x, y = housing.data, housing.target

# 导入sklearn.model_selection模块中的train_test_split函数
from sklearn.model_selection import train_test_split

# 使用train_test_split()函数划分训练集和测试集
# 设置测试集比例为0.2，随机参数为1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# TODO 从sklearn.tree中导入回归决策树模型DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor

# 创建空列表depth和score
depth = []
score = []

# TODO for循环遍历最大树深度1-9
for i in range(1, 10):
    # TODO 使用DecisionTreeRegressor函数，设置最大深度为i，随机参数为1,赋值给对象clf
    clf = DecisionTreeRegressor(max_depth=i, random_state=1)

    # TODO 使用append函数将i添加到列表depth
    depth.append(i)

    # TODO 调用fit函数对训练数据集及其目标变量进行训练
    clf.fit(x_train, y_train)

    # TODO 将x_test,y_test传入score函数计算出精确度，赋值到temp
    temp = clf.score(x_test, y_test)

    # TODO 使用append函数将temp添加到列表score
    score.append(temp)

# 导入matplotlib.pyplot模块进行可视化
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = "Simsun"

# TODO 调用plt.plot函数，以depth为x轴数据，score为y轴数据，绘制折线图
plt.plot(depth, score)

# TODO 使用plt.title设置图标题为"树的深度与预测精度"
plt.title('树的深度与预测精度')

# TODO 使用plt.xlabel设置x轴标签为"回归决策树深度"
plt.xlabel('回归决策树深度')

# TODO 使用plt.ylabel设置y轴标签为"预测精确度"
plt.ylabel('预测精确度')

# 展示图片
plt.show()