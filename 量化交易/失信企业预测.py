#导入pandas模块，并读取数据："/Users/data5_1/train_data.csv"
import pandas as pd
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\量化交易\数据\train_data.csv")

#使用replace()函数将grade列的数据的A、B、C、D、E、F、G替换为7、6、5、4、3、2、1
df['grade'] = df['grade'].replace({'A':7,'B':6,'C':5,'D':4,'E':3,'F':2,'G':1})

#用fillna()将debt列和loan列的缺失值用0填充
df['debt'].fillna(0,inplace=True)
df['loan'].fillna(0,inplace=True)
"""
从sklearn.linear_model模块导入LinearRegression函数，将不含有缺失值的"code","investment","stock","income","expenditure_1","expenditure_2","debt","loan","grade","Label"列数据单独取出为lr_data
"""
from sklearn.linear_model import LinearRegression
lr_data = df[["code","investment","stock","income","expenditure_1","expenditure_2","debt","loan","grade","Label"]]
for i in ["capital","assets_1","assets_2","expenditure_3","tax"]:
    #将当前列的数据单独用copy()拷贝出来，用isnull()得出缺失情况的布尔序列
    copy_i = df[i].copy()
    copy_i_null = copy_i.isnull()
    #用~布尔序列的方式索引出lr_data中不含有i列缺失值的行，做为回归的训练集的自变量x
    lr_train = lr_data[~copy_i_null]
    #用2.1的布尔序列索引出lr_data中含有i列缺失值的行，做为回归的测试集的自变量x
    lr_test = lr_data[copy_i_null]
    #用~2.1的布尔序列索引出原数据中i列已有的值，做为回归的训练集的因变量y
    lr_y_train = df[~copy_i_null][i]
    #使用LinearRegression()初始化模型，使用fit()函数，输入此时训练集的x和y训练模型
    lr_model = LinearRegression()
    lr_model.fit(lr_train,lr_y_train)
    #用predict()对测试集的自变量x做预测，也就是预测缺失值的值
    y_predict = lr_model.predict(lr_test)
    #循环遍历测试集的长度，依次将测试集索引的值index取出，把i列中index处的值替换为对应的预测值
    for j in range(0,len(lr_test)):
        x_test_index = lr_test.index[j]
        copy_i[x_test_index] = y_predict[j]
    #最后将处理完的i列重新赋值给原数据中的i列
    df[i] = copy_i
#将ID列和Label列用drop()删去做为决策树分类的x
x = df.drop(columns=['ID','Label'])
#将Label列做为决策树分类的y
y = df['Label']
#导入sklearn.model_selection模块中的train_test_split函数将数据划分为训练集和测试集，test_size设置为0.2，random_state设置为51
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=51)
#导入sklearn.tree模块中的分类决策树模型DecisionTreeClassifier并初始化模型，设置max_depth为3，random_state为598
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth = 3,random_state = 598)
#导入sklearn.model_selection模块中的交叉验证的cross_val_score()函数进行交叉验证，scoring设置为'roc_auc'，cv设置为10，输出交叉验证后auc的均值
from sklearn.model_selection import cross_val_score
auc_score = cross_val_score(model,x_train,y_train,scoring='roc_auc',cv=10)
print(auc_score.mean())
#用训练集fit()拟合决策树，并对测试集的x做概率预测
model.fit(x_train,y_train)
y_pred_proba = model.predict_proba(x_test)
#导入sklearn.metrics模块中的roc_auc_score函数，将测试集的y和模型预测的概率传入roc_auc_score()得出AUC，并将AUC输出
from sklearn.metrics import roc_auc_score
auc_score = roc_auc_score(y_test,y_pred_proba[:,1])
print(auc_score)