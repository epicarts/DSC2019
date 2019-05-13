#heatmap 만들기
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ccf10 = pd.read_csv("ccf10_normal_korea.csv",encoding='utf-8')
ccf10 = ccf10.set_index(ccf10['datetime']) # datatime 을 인덱스로 설정
ccf10 = ccf10.drop('datetime',1)

colormap = plt.cm.RdBu
plt.figure(figsize=(15,10))
plt.title(u'10 weeks', y=1.05, size=16)

mask = np.zeros_like(ccf10.corr())
mask[np.triu_indices_from(mask)] = True
svm = sns.heatmap(ccf10.corr(),mask=mask, linewidths=0.1,vmax=1.0,
            square=True, cmap=colormap, linecolor='white', annot=True)
plt.savefig("output.png")
