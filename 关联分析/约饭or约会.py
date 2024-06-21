# 导入pandas模块
import pandas as pd

# 读取数据
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\campus.csv", encoding="utf-8")

# TODO 创建空列表all_list
all_list = []

# TODO 使用unique函数去重取出所有不同的消费时间段
time = df['消费时间'].unique()

# TODO for循环遍历每个消费时间段
for i in time:
    # TODO 使用布尔索引获取df中消费时间为i的数据，赋值到temp1
    temp1 = df[df['消费时间'] == i]

    # TODO 使用列索引获取数据中的个人信息，赋值到temp2
    temp2 = temp1['个人信息']

    # TODO 使用tolist()函数转化为列表，赋值到temp3
    temp3 = temp2.tolist()

    # TODO 使用append函数将temp3添加到列表all_list
    all_list.append(temp3)

# TODO 导入apyori库中的apriori()函数
from apyori import apriori

# TODO 用apriori()函数进行关联分析，将获取的关联规则赋值给rules
rules = apriori(all_list, min_support=0.0006, min_confidence=0.8)

# TODO 创建空列表set_2，set_4
set_2 = []
set_4 = []

# TODO for循环遍历rules
for rule in rules:

    # TODO for循环遍历ordered_statistics对象
    for i in rule.ordered_statistics:

        # TODO 获取前件和后件，转为列表后，分别赋值给head_set和tail_set

        head_set = list(i.items_base)
        tail_set = list(i.items_add)
        # TODO 将前件、后件用"+"拼接成一个列表，并赋值给related_category
        related_catogory = head_set + tail_set

        # 判断related_category列表长度，归类到不同列表
        # TODO 若长度为2
        if len(related_catogory) == 2:
            # TODO 使用append函数添加到列表set_2

            set_2.append(related_catogory)
        # TODO 若长度为4
        if len(related_catogory) == 4:
            # TODO 使用append函数添加到列表set_4
            set_4.append(related_catogory)

# 格式化输出
# TODO f"双人约：{set_2}"
print(f"双人约：{set_2}")

# TODO f"四人约：{set_4}"
print(f"四人约：{set_4}")