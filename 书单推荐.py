import pandas as pd

BookRates = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\BookRates.csv")
UserRates = BookRates.pivot_table(index='ISBN',columns='user_id',values='rating')
#建立用户数据透视表
corrMatrix = UserRates.corr(method='pearson',min_periods=5)
#建立皮尔逊相关系数矩阵
userCorr = corrMatrix[638].drop(index=638)
mostCorrUser = userCorr.idxmax()
#找到最相似的那个人
targetBook = UserRates[mostCorrUser]
targetBook = targetBook[targetBook.values > 8]
#相似用户打分8分以上的书籍
userBook = UserRates[638].dropna()
targetName = targetBook.index
userName = userBook.index
BookList = targetName[~targetName.isin(userName)]
#在相似用户里查找目标用户没看过的书
BookList = BookList.values
print(BookList)