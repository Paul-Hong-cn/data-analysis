#导入Pandas模块，并读取数据
import pandas as pd
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\diabetes.csv")
#导入可视化模块matplotlib.pyplot和seaborn
import matplotlib.pyplot as plt
import seaborn as sns
#计算数据相关矩阵
corr = df.corr()
#绘制热力图，设置颜色为"RdBu"，形状为方形，显示数字标记
sns.heatmap(corr,cmap='RdBu',square=True, annot = True)
plt.show()
#用列索引获取相关矩阵中target所在列
temp1 = corr['target']
#使用布尔索引获取相关矩阵中绝对值大于0.1小于1的数据
temp2 = temp1[(abs(temp1)>0.1)&(abs(temp1)<1)]
#用index属性获得行索引的变量名
X_col = temp2.index
#再次使用布尔索引获得数据中的这些变量名所在列，作为成自变量X
X = df[X_col]
#以二维结构读取"target"，作为因变量y
Y = df[['target']]
#从statsmodels模块中导入variance_inflation_factor()函数
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = []
#通过for循环遍历X.columns
for i in X.columns:
    #依次求得每个自变量的方程膨胀系数VIF
    VIF = variance_inflation_factor(X.values,X.columns.get_loc(i))
    #用if判断该变量的VIF大于10
    if VIF > 10:
        #若VIF大于10，则删除X中该变量所在列
        X = X.drop(columns=i)
#导入sklearn.model_selection模块中的train_test_split函数
from sklearn.model_selection import train_test_split
#使用train_test_split()函数划分训练集和测试集，测试集比例为0.1，随机状态参数random_state=1
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.1,random_state=1)
#导入sklearn.linear_model模块中的LinearRegression函数
from sklearn.linear_model import LinearRegression
#初始化线性回归模型
lr_model = LinearRegression()
#使用fit()函数训练模型,传入训练集数据
lr_model.fit(x_train,y_train)
#记录输出模型的coef_属性和intercept_属性，使用round函数保留两位小数
coef = lr_model.coef_.round(2)
intercept = lr_model.intercept_.round(2)
#格式化输出回归方程，输出结果为：线性回归方程：Y=151.28-41.53X1+610.34X2+253.11X3-119.46X4-164.6X5+26.88X6+498.56X7+31.16X8
print(f"线性回归方程：Y={intercept[0]}{coef[0][0]}X1+{coef[0][1]}X2+{coef[0][2]}X3{coef[0][3]}X4{coef[0][4]}X5+{coef[0][5]}X6+{coef[0][6]}X7+{coef[0][7]}X8")