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

normalized_3days = pd.read_csv("local_oil/oil_normalized_3days.csv",encoding='utf-8',index_col='datetime')
normalized_3days
df_new = df_derived_by_shift(normalized_3days, 20)#마지막에 datetime 있는게 한칸씩 사라짐
df_new.info()
df_new = df_new.dropna()
df_new.to_csv("ccf10_normal.csv", mode='w',encoding='ms949')
df_new.corr().to_csv("ccf10_corr.csv", mode='w',encoding='ms949')






import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm
import matplotlib as mpl


#폰트바꾸기
font_name= font_manager.FontProperties(fname='C:\\Windows\\Fonts\\NanumGothicCoding-Bold.ttf').get_name()
plt.rc('font', family=font_name)


# 분류된 파일 읽기
oil_corr=pd.read_csv("local_oil/oil_corr_3days_arragne36912.csv",index_col='days')
oil_corr = oil_corr.sort_index(ascending=False)

#정규화 최고 (값을 찾기 위해)
for x in list(oil_corr.columns):
    oil_corr[x] = (oil_corr[x]-oil_corr[x].min())/(oil_corr[x].max()-oil_corr[x].min())

#소수 둘째 자리에서 반올림
oil_corr.round(2)



plt.figure(figsize=(15,10))
plt.title(u'days', y=1.05, size=16)
colormap = plt.cm.Blues
colormap
svm = sns.heatmap(oil_corr, cmap=colormap, linecolor='white', annot=True)
plt.savefig("oil_corr_3days_arragne_369.jpg")



oil_corr.round(2).to_csv("oil_corr_3days_arragne_round2.csv", mode='w',encoding='ms949')
