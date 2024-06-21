#导入模块，pandas、matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
#读取路径为 /Users/forecast/jetrail.csv 的数据集，并赋值给变量df
df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\量化交易\数据\jetrail.csv")
#对df的Datetime列作时间格式转换，并将Datetime列设为行索引
df['Datetime'] = pd.to_datetime(df['Datetime'])
df.set_index(['Datetime'],inplace=True)
#将数据集分为训练集train（df中的10000-17552行）和测试集test（df中的17553-最后）
train = df.iloc[10000:17553]
test = df.iloc[17553:]
#使用resample()和mean()函数，分别对df、train、test按天进行重采样，并求取均值
df = df.resample('D').mean()
train = train.resample('D').mean()
test = test.resample('D').mean()
y_hat_avg = test.copy()
#通过mean()函数，直接计算训练集中通勤人数的平均值，将数据存储在y_hat_avg的avg_forecast列中
y_hat_avg['avg_forecast'] = train['Count'].mean()
#将train["Count"].copy()赋值给新变量train_series
train_series = train['Count'].copy()
#定义一个空列表result，用于存储预测结果
result = []
for i in y_hat_avg.index:
    #通过rolling()函数和mean()函数，计算train_series的移动平均值，使用[-1]取得最后一个均值，并赋值给变量predict
    predict = train_series.rolling(window=10).mean().iloc[-1]
    #将predict赋值给train_series[i]
    train_series[i] = predict
    #使用append()函数，将predict添加到result中
    result.append(predict)
#训练集（train）：折线颜色为blue，图例为train
plt.plot(train.index,train['Count'],color='blue',label='train')
#测试集（test）：折线颜色为gray，图例为test
plt.plot(test.index,test['Count'],color='gray',label='test')
#普通均值预测数据（y_hat_avg中的avg_forecast列）：折线颜色为red，图例为Average Forecast
plt.plot(y_hat_avg.index,y_hat_avg['avg_forecast'],color='red',label='Average Forecast')
#移动均值预测数据（result）：折线颜色为green，图例为Moving Average Forecast
plt.plot(y_hat_avg.index,result,color='green',label='Moving Average Forecast')
plt.legend()
plt.show()