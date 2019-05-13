import pandas as pd
import numpy as np


local_oil_df = pd.read_csv("local_oil/local_oil.csv",encoding='utf-8')
local_oil_df.head()
#datetime 인덱스 생성
local_oil_df['datetime'] = local_oil_df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
local_oil_df.set_index(local_oil_df['datetime'], inplace=True) # datatime 을 인덱스로 설정
local_oil_df = local_oil_df.drop(['date','datetime'], 1)

#3일 단위로 쪼개기
local_oil_df.index =  pd.to_datetime(local_oil_df.index)
local_oil_df = local_oil_df.resample('3D', how={'kore local':np.mean})

#정규화
for x in list(local_oil_df.columns):
    local_oil_df[x] = (local_oil_df[x]-local_oil_df[x].min())/(local_oil_df[x].max()-local_oil_df[x].min())

#데이터 저장
local_oil_df.to_csv("local_oil/local_oil_normalized_3days.csv", mode='w',encoding='ms949')
local_oil_df.head()
local_oil_df.max()
