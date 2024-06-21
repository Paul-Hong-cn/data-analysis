# 导入pandas模块，并简称pd
import pandas as pd

# 读取数据，并存储在变量df中
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\music_ratings.csv")

'''寻找相似的用户'''
# TODO 用pivot_table()构建数据透视表
# 设置index为"songId", columns为"userId"，values为"rating"
# 将结果赋值给ratings
ratings = df.pivot_table(index='songId', columns='userId', values='rating')
# TODO 用corr()计算不同用户间的皮尔逊相关系数，并赋值给corrMatrix
corrMatrix = ratings.corr(method='pearson')

'''找到与每个用户最相似用户，并根据推荐规则，获取可推荐歌曲编号'''
# TODO 定义一个空列表RecommendList，用于存放推荐歌曲数据

RecommendList = []
# TODO 使用for循环，依次遍历每个用户的userId
for user in ratings.columns:
    # 寻找最相似用户
    # TODO 1.获取user与其他用户之间的皮尔逊相关系数
    userCorr = corrMatrix[user].drop(index=user)

    # TODO 2.获取最大值对应的索引，并赋值给变量mostCorrUser
    mostCorrUser = userCorr.idxmax()

    # 筛选可推荐歌曲
    # TODO 1.获取相似用户的歌曲评分数据，赋值给targetSong
    targetSong = ratings[mostCorrUser]

    # TODO 2.获取相似用户评分大于4的音乐，重新赋值给targetSong
    targetSong = targetSong[targetSong.values > 4]

    # TODO 3.获取目标用户评分过的音乐数据，赋值给valued_ratings
    valued_ratings = ratings[user].dropna()

    # 4.删除目标用户评分过的歌曲
    # TODO 获取相似用户评分大于4的歌曲编号，即targetSong的索引，并赋值给targetName
    targetName = targetSong.index

    # TODO 获取目标用户评分过的音乐的歌曲编号，即valued_ratings的索引，并赋值给user1Name
    user1Name = valued_ratings.index

    # TODO 筛选当前用户未评分过的歌曲编号，并赋值给变量SongList
    SongList = targetName[~targetName.isin(user1Name)]

    # TODO 获取可推荐歌曲的编号
    SongList = SongList.values

    # TODO 使用append()函数，将当前用户的可推荐歌曲编号添加到列表RecommendList中
    RecommendList.append(SongList)

'''输出结果'''
# TODO 创建一个字典
# 将"用户ID"和"推荐列表"依次作为该字典的键(keys)
# 将数据透视表的列索引(columns)和推荐列表依次作为该字典的值(values)
# 将结果赋值给resultDict
resultDict = {'用户ID': ratings.columns, '推荐列表': RecommendList}

# TODO 使用pd.DataFrame()函数，传入字典作为必选参数，构建一个DataFrame
result = pd.DataFrame(resultDict)

# TODO 将result输出
print(result)