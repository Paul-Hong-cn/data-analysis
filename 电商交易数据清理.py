import pandas as pd

df = pd.read_csv(r"D:\Python-3.12\VSCode\夜曲编程\数据分析\user_data\180101-190630交易数据.csv")
df = df.set_index('id')
df.fillna(0,inplace=True)

dfOrder_id = df[df['order_id']<=0]
df.drop(index=dfOrder_id.index,inplace=True)
dfOrder_id = df[df['order_id'].duplicated()]
df.drop(index=dfOrder_id.index,inplace=True)

dfUser_id = df[df['user_id']<=0]
df.drop(index=dfUser_id.index,inplace=True)

df['payment'] = df['payment']/100
dfPayment = df[df['payment']<0]
df.drop(index=dfPayment.index,inplace=True)

df['price'] = df['price']/100
dfPrice = df[df['price']<0]
df.drop(index=dfPrice.index,inplace=True)

dfItems_count = df[df['items_count']<0]
df.drop(index=dfItems_count.index,inplace=True)

df['cutdown_price'] = df['cutdown_price']/100
dfCutdown_price = df[df['cutdown_price']<0]
df.drop(index=dfCutdown_price.index,inplace=True)

df['post_fee'] = df['post_fee']/100
dfPost_fee = df[df['post_fee']<0]
df.drop(index=dfPost_fee.index,inplace=True)

df['create_time'] = pd.to_datetime(df['create_time'])
df['pay_time'] = pd.to_datetime(df['pay_time'])
dfTime = df[df['create_time']>df['pay_time']]
df.drop(index=dfTime.index,inplace=True)

df.info()