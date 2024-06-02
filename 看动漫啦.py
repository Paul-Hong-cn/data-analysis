# 导入pandas模块，并简称pd
import pandas as pd

# 读取数据，并存储在变量df中
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\anime.csv", encoding="utf-8")

'''寻找相似的动漫'''
# TODO 用布尔索引筛选出"av_rating"这一列中大于7的数据，并赋值给df
df = df[df['av_rating']>7]

# TODO 用pivot_table()构建数据透视表
# 设置index为"user_id", columns为"name"，values为"rating"
# 将结果赋值给ratings

ratings = df.pivot_table(index='user_id',columns='name',values='rating')
# TODO 用corr()计算不同动漫间的皮尔逊相关系数，并赋值给corrMatrix
corrMatrix = ratings.corr(method='pearson')

'''寻找铃可感兴趣的动漫'''
# TODO 获取铃可评分过的动漫数据，并赋值到targetRatings
targetRatings = ratings.loc[1].dropna()

# 根据每一部铃可评分过的动漫，预测她对未评分动漫的感兴趣程度
# TODO 1. 依次获取铃可评分过的动漫的名称及评分，并赋值给变量name和score
name = targetRatings.index
score = targetRatings.values

# TODO 2. 获取铃可评分过的动漫与未评分过的动漫之间的皮尔逊相关系数，并赋值给变量sims
sims = corrMatrix[name].drop(index=name)


# TODO 3. 计算评分与皮尔逊相关系数之间的乘积，赋值给变量prod
prod = score * sims

# TODO 4. 使用sum()函数对prod变量进行横向求和，并赋值给变量animeList
animeList = prod.sum(axis=1)

'''获取可推荐动漫列表'''
# TODO 用sort_values()将推荐列表降序排序
animeList = animeList.sort_values(ascending=False)

# TODO 获取感兴趣程度最高的前3部动漫
animeList = animeList.index[0:3]

# TODO 获取可推荐的动漫的名称
animeList = animeList.values

# TODO 输出推荐列表
print(animeList)