# 导入pandas模块
import pandas as pd

# 读取数据
df = pd.read_csv(r'D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\PersonalLoan.csv')

# 使用drop()函数删除"是否接受贷款"和"用户编号"列，剩余的数据作为自变量x
x = df.drop(columns=["是否接受贷款","用户编号"])

# 以二维结构读取"是否接受贷款"列，作为因变量y
y = df[["是否接受贷款"]]

# TODO 导入sklearn.model_selection模块中的train_test_split函数
from sklearn.model_selection import train_test_split

# TODO 使用train_test_split()函数划分训练集和测试集
# 传入x和y，设置test_size为0.2,random_state为123
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=123)

# TODO 导入sklearn.tree模块中的分类决策树模型DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# TODO 使用DecisionTreeClassifier()初始化模型
# 并设置参数max_depth=4,random_state=123，赋值给model
model = DecisionTreeClassifier(max_depth=4,random_state=123)

# TODO 使用fit()函数用训练集的x和y训练模型
model.fit(x_train,y_train)

# TODO 将x_test传入使用predict_proba()函数预测，将结果赋值给y_pred_proba
y_pred_proba = model.predict_proba(x_test)

# TODO 导入sklearn.metrics模块中的roc_curve函数

from sklearn.metrics import roc_curve
# TODO 将y_test和预测的概率传入roc_curve()，将结果依次赋值给fpr, tpr, thres
fpr,tpr,thres = roc_curve(y_test,y_pred_proba[:,1])

# TODO 导入matplotlib.pyplot，并使用"plt"作为该模块的简写
import matplotlib.pyplot as plt

# TODO 使用plt.plot()函数，传入fpr为x轴的值，tpr为y轴的值，绘制折线图
plt.plot(fpr,tpr)

# TODO 设置标题为ROC
plt.title('ROC')

# TODO 设置x轴名称FPR
plt.xlabel('FPR')

# TODO 设置y轴名称TPR
plt.ylabel('TPR')

# TODO 显示图像
plt.show()

# TODO 导入sklearn.metrics模块中的roc_auc_score函数
from sklearn.metrics import roc_auc_score

# TODO 将y_test和y_pred_proba的第2列传入roc_auc_score()，将结果赋值给auc_score
auc_score = roc_auc_score(y_test,y_pred_proba[:,1])

# TODO 输出auc_score
print(auc_score)