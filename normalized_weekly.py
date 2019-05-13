import pandas as pd
import numpy as np

#데이터 정규화 하기
oilForeign_mean = pd.read_csv("weekly/oilForeign_weekly_mean.csv",encoding='utf-8', index_col='datetime')
oilForeign_mean.head()
normalized_df=(oilForeign_mean['Foreign mean']-oilForeign_mean['Foreign mean'].min())/(oilForeign_mean['Foreign mean'].max()-oilForeign_mean['Foreign mean'].min())
oilForeign_mean['Foreign mean'] = normalized_df

korea_weekly_df = pd.read_csv("weekly/korea_weekly_df.csv",encoding='utf-8', index_col='datetime')
korea_weekly_df.head()
normalized_df=(korea_weekly_df['korea']-korea_weekly_df['korea'].min())/(korea_weekly_df['korea'].max()-korea_weekly_df['korea'].min())
korea_weekly_df['korea'] = normalized_df


oilForeign_mean
korea_weekly_df

#병합하기
oil_normalized = pd.merge(oilForeign_mean,korea_weekly_df, how='right', on ='datetime')
local_oil_df.to_csv("weekly/oil_normalized.csv", mode='w')
