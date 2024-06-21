# 导入模块，读取文件 "/Users/huanhuan/bilibili.csv"
import pandas as pd
ifl = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\bilibili.csv")
#使用groupby()，count()函数按照up主进行分组计数，通过列索引任选一列用count()函数统计up主上传的视频数量
count = ifl.groupby(ifl['author']).count()
#使用reset_index()函数重置索引，用.columns属性重命名列，利用merge()函数合并统计数据与原数据
count = count['分区'].reset_index()
count.columns = ['author','times']
com = pd.merge(count,ifl,on='author',how='inner')
#使用pd.to_datetime()函数将"date"列转换为时间格式
com['date'] = pd.to_datetime(com['date'])
#利用布尔索引选取上传视频数大于等于5的up主
result = com[com['times']>=5]
#计算I值 I = (总弹幕数+总回复数)/总观看量/视频总数*100
groupByAuthor = result.groupby(result['author']).sum(numeric_only=True)
danmu = groupByAuthor['danmu']
reply = groupByAuthor['reply']
view = groupByAuthor['view']
count = result.groupby(result['author'])['times'].count()
I = ((danmu + reply)/view/count * 100)
#计算F值 F = (up主最后发布视频与最早发布视频的天数间隔)/视频总数
latest = result.groupby(result['author'])['date'].max()
earliest = result.groupby(result['author'])['date'].min()
F = ((latest - earliest).dt.days/count)
#计算L值 L = (总点赞数+总投币数+总收藏数)/总观看量*100
likes = groupByAuthor['likes']
coins = groupByAuthor['coins']
favorite = groupByAuthor['favorite']
L = ((likes + coins + favorite)/view*100)
#用pd.concat()横向合I、F、L，并使用.columns属性将合并后的数据的列名命名为"I"，"F"，"L"
IFL = pd.concat([I,F,L],axis=1)
IFL.columns = ['I','F','L']
#使用qcut()函数对I/F/L的数据进行5等分，并根据实际情况把区间标记成1-5分
IFL['I_score']= pd.qcut(IFL['I'],q=5,labels = [1,2,3,4,5])
IFL['F_score'] = pd.qcut(IFL['F'],q=5,labels = [5,4,3,2,1])
IFL['L_score'] = pd.qcut(IFL['L'],q=5,labels = [1,2,3,4,5])
#当I/F/L的标记值大于3时，转换成1，否则转换成0
def iflTrans(x):
    if x > 3:
        return 1
    else:
        return 0
IFL['I_score'] = IFL['I_score'].apply(iflTrans)
IFL['F_score'] = IFL['F_score'].apply(iflTrans)
IFL['L_score'] = IFL['L_score'].apply(iflTrans)
IFL['mark'] = IFL['I_score'].astype(str) + IFL['F_score'].astype(str) + IFL['L_score'].astype(str)
def iflType(x):
    if x == '111':
        return "高质量UP主"
    elif x == '101':
        return "高质量拖更UP主"
    elif x == '011':
        return "高质量内容高深UP主"
    elif x == '001':
        return "高质量内容高深拖更UP主"
    elif x == '110':
        return "接地气活跃UP主"
    elif x == '100':
        return "接地气UP主"
    elif x == '010':
        return "活跃UP主"
    elif x == '000':
        return "还在成长的UP主"
IFL['up_type'] = IFL['mark'].apply(iflType)
#统计每个类型的up主的占比（每类up主人数/数据筛选后的up主总人数）
up_type = IFL['up_type'].groupby(IFL['up_type']).count()
up_type = up_type/up_type.sum(numeric_only=True)
#用柱状图展示结果，如下所示（请按顺序将数据传入图表，x轴刻度旋转45度）
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = "SimSun"
plt.bar(up_type.index,up_type.values)
plt.xticks(rotation=45)
plt.show()