#导入pandas模块，读取文件，设置encoding="utf-8"
import pandas as pd
data = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\TCM.csv",encoding="utf-8")
#将"病人症状"列的字符串数据转化为列表，并添加到一个空列表中，形成双重列表结构的数据；
Patients = []
for i in data['病人症状']:
    Patient = i.split(',')
    Patients.append(Patient)

#导入apriori函数进行关联分析
from apyori import apriori
#设置最小支持度为0.1，最小置信度为0.7，提取出强关联规则
rules = apriori(Patients,min_support=0.1,min_confidence=0.7)
relationship_list = []

for rule in rules:
    support = round(rule.support,3)
    for i in rule.ordered_statistics:
        #提取关联规则的前件和后件，并用"→"拼接
        head_set = list(i.items_base)
        tail_set = list(i.items_add)
        if head_set == []:
            continue
        related_category = str(head_set) + '→' + str(tail_set)
        #将支持度、置信度、提升度都保留三位小数，添加到提前创建的空列表中
        confidence = round(i.confidence,3)
        lift = round(i.lift,3)
        relationship_list.append([related_category,support,confidence,lift])
#将列表数据，转化为DataFrame形式，设置列名为"关联规则"， "支持度"， "置信度"， "提升度"
rule_data = pd.DataFrame(relationship_list,columns=['关联规则','支持度','置信度','提升度'])
#用布尔索引，提取出提升度>1的关联规则，并输出查看
pos_data = rule_data[rule_data['提升度']>1]
print(pos_data)