import pandas as pd
import numpy as np


oilForeign=pd.read_csv("local_oil/oilForeign_mean.csv",encoding='utf-8',index_col='datetime')
#index dataframe 으로 변경
oilForeign.index =  pd.to_datetime(oilForeign.index)

#정규화
for x in list(oilForeign.columns):
    oilForeign[x] = (oilForeign[x]-oilForeign[x].min())/(oilForeign[x].max()-oilForeign[x].min())


oilForeign = oilForeign.resample('3D', how={'Foreign oil':np.mean})
oilForeign = oilForeign.interpolate()#선형으로 결측값 보강
oilForeign.to_csv("local_oil/oilForeign_3days.csv", mode='w',encoding='utf-8')
oilForeign.max()
