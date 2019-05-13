import pandas as pd
import numpy as np


#st_data_oilKorea 데이터를 꺼내온 후 가공.
df=pd.read_csv("data/st_data_oilKorea.tsv",delimiter='\t',encoding='utf-8')
df['datetime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
df.set_index(df['datetime'], inplace=True) # datatime 을 인덱스로 설정
df = df.drop('datetime', 1)
df = df.drop('date', 1)
df = df.drop('itemname',1)
df.head()

# 'W-Mon' 월요일 시작하는 주별 close_val 을 가공함.
weekly_df = df.resample('W-Mon', how={'close_val':np.mean}).fillna(method='ffill')
weekly_df.head()

#컬럼 이름 바꾸기
weekly_df = weekly_df.rename(columns={"close_val": 'korea'})
weekly_df
#st_data_oilForeign 데이터를 꺼내온 후 가공.
df = pd.read_csv("data/st_data_oilForeign.tsv",delimiter='\t',encoding='utf-8')
df.head()
df['datetime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
df.set_index(df['datetime'], inplace=True)
df = df.drop(columns=['date','datetime','itemcode'], axis=1)
df = df.drop(columns=['open_val','high_val','low_val'], axis=1)
df.head()

#각 해외 유 종류별로 나눈뒤 일주일 단위로 쪼갬
dubai = df[df['itemname'] =='두바이유'].drop('itemname',1)
brent = df[df['itemname'] =='브렌트유'].drop('itemname',1)
wti = df[df['itemname'] =='WTI(서부텍사스유) '].drop('itemname',1)
brent_weekly = brent.resample('W-Mon', how={'close_val':np.mean}).fillna(method='ffill')
dubai_weekly = dubai.resample('W-Mon', how={'close_val':np.mean}).fillna(method='ffill')
wti_weekly = wti.resample('W-Mon', how={'close_val':np.mean}).fillna(method='ffill')

#컬럼 이름 바꾸기
brent_weekly = brent_weekly.rename(index=str, columns={"close_val": 'brent'})
dubai_weekly = dubai_weekly.rename(index=str, columns={"close_val": 'dubai'})
wti_weekly = wti_weekly.rename(index=str, columns={"close_val": 'wti'})
dubai_weekly.head()

#해외 유 병합
a = pd.merge(brent_weekly, dubai_weekly,how='right', on ='datetime')
oilForeign_weekly = pd.merge(a, wti_weekly,how='right', on ='datetime')

#주단위로 된 파일 저장.
oilForeign_weekly.to_csv('weekly/oilForeign_weekly.csv', mode='w')
weekly_df.to_csv("weekly/korea_weekly_df.csv", mode='w')
