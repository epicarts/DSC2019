import pandas as pd
import numpy as np

#cross correlation 교차 분산 검증
def df_derived_by_shift(df,lag=0,NON_DER=[]):
    '''
    데이터 프레임, 움직일 횟수
    '''
    df = df.copy()
    if not lag:#예외처리
        return df
    cols ={}
    for i in range(1,lag+1):# 시프트 횟수
        for x in list(df.columns):#컬럼
            if x not in NON_DER:
                if not x in cols:
                    cols[x] = ['{}_{}'.format(x, i)]
                else:
                    cols[x].append('{}_{}'.format(x, i))
    for k,v in cols.items():
        columns = v
        dfn = pd.DataFrame(data=None, columns=columns, index=df.index)
        i = 1
        for c in columns:
            dfn[c] = df[k].shift(periods=i)
            i+=1
        df = pd.concat([df, dfn], axis=1, join_axes=[df.index])
    return df

oil_normalized = pd.read_csv("weekly/oil_normalized.csv",encoding='utf-8')
oil_normalized.set_index(oil_normalized['datetime'], inplace=True) # datatime 을 인덱스로 설정
oil_normalized = oil_normalized.drop('datetime', 1)
oil_normalized
df_new = df_derived_by_shift(oil_normalized, 50)#마지막에 datetime 있는게 한칸씩 사라짐\
df_new = df_new.dropna()
df_new.to_csv("weekly/ccf10_normal.csv", mode='w')
df_new.corr().to_csv("weekly/ccf10_corr.csv", mode='w')
