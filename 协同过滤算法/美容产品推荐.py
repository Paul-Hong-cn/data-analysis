#引入pandas库
import pandas as pd

#读取文件
data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\Beauty_products.csv")

#建立用户数据透视表，把产品ID作为列索引
ratings = data.pivot_table(index='UserId',columns='ProductId',values='Rating')

#以列表的方式存储所有用户的信息
UserId = ratings.index.values

#计算皮尔逊相关系数，实现基于物品的协同过滤算法
corrMatrix = ratings.corr(method='pearson')

#建立一个空的列表
data = []

#对每一个用户执行一次循环
for i in UserId:
    #得到每个用户打分的产品
    targetRatings = ratings.loc[i].dropna()

    #获取产品的名称和分数
    name = targetRatings.index
    score = targetRatings.values

    #皮尔逊相关系数矩阵，行索引是用户未打分的产品，列索引是用户已打分的产品
    sims = corrMatrix[name].drop(index=name)
    prod = sims * score

    #得到该用户每个产品的推荐度
    animeList = prod.sum(axis=1)

    #选择推荐度最高的五个产品
    animeList = animeList.sort_values(ascending=False)
    animeList = animeList.index[0:5]
    animeList = animeList.values

    #添加进入列表
    data.append((i, animeList))

#形成一个dataframe对象，并输出
df = pd.DataFrame(data, columns=['用户ID', '推荐列表'])
print(df)