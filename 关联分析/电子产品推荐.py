# 导入pandas模块简称为pd
import pandas as pd

# 读取文件
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\electronic.csv", encoding='utf-8')

# 一、计算{电视}的支持度
# TODO 1.用列索引，获取电视这一列数据
TVData = df['电视']

# TODO 2.用value_counts()函数，对这一列数据中每个值进行计数和排序
TVData = TVData.value_counts()

# TODO 3.访问位置索引，获取购买电视的订单数量
TVData = TVData[1]

# TODO 4.订单数量除以13，得到支持度
TVSupport = TVData / 13

# 二、计算{游戏机}的支持度
# TODO 1.用列索引，获取游戏机这一列数据
gameData = df['游戏机']

# TODO 2.用value_counts()函数，对这一列数据中每个值进行计数和排序
gameData = gameData.value_counts()

# TODO 3.访问位置索引，获取购买游戏机的订单数量
gameData = gameData[1]

# TODO 4.订单数量除以13，得到支持度
gameSupport = gameData / 13

# 三、计算{电视,游戏机}的支持度
# TODO 1.使用布尔索引，找出既购买了电视又购买了游戏机的数据
order = df[(df['游戏机'] == 1) & (df['电视'] == 1)]

# TODO 2.用列索引，获取"游戏机"这一列
order = order['游戏机']

# TODO 3.使用count()函数，统计这列订单数量
order = order.count()

# TODO 4.订单数量除以13，得到支持度
totalSupport = order / 13

# TODO 四、计算{电视}→{游戏机}的置信度

conf = totalSupport / TVSupport

# 五、计算{电视}→{游戏机}的提升度
# TODO 1.计算出提升度后，使用round()函数将其保留1位小数
lift = (conf / gameSupport).round(1)

# 六、输出结果
# 1.用if-else语句根据提升度是否大于1来格式化输出结果
# TODO 如果大于1

if lift > 1:
    # TODO 则能推荐
    # 输出示例为：电视对游戏机的提升度为{xx}，能推荐
    print(f"电视对游戏机的提升度为{lift}，能推荐")

# TODO 否则
else:

    # TODO 就不能推荐
    # 输出示例为：电视对游戏机的提升度为{xx}，不能推荐
    print(f"电视对游戏机的提升度为{lift}，不能推荐")