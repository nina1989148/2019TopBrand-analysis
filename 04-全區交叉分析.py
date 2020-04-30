# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:21:03 2018

@author: nina
"""

import numpy as np
import pandas as pd
#抓出性別
dataframe1 = pd.read_csv('001_win.csv')
dataframe2 = pd.read_csv('002_win.csv')
dataframe3 = pd.read_csv('003_win.csv')
dataframe = pd.concat([dataframe1], ignore_index= True , axis= 0 ) 
item = pd.read_csv('item.csv')

dataframe = pd.read_csv('001_win.csv')
item = pd.read_csv('item.csv')

df1 = dataframe.drop(['NO','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df_q = df1.iloc[:, list(range(0,203,2))]  
df_q.shape

df_q.rename(columns={'q35 ':'q35'}, inplace=True)
df_q.rename(columns={'q66 ':'q66'}, inplace=True)

q = list(item.對應題目.unique())[0]
count = item[item['對應題目']== q].子題名稱.count()

df2 = pd.DataFrame()
for i in range(0,101):
    q = list(item.對應題目.unique())[i]
    count = item[item['對應題目']== q].子題名稱.count()
    o = list(item[item['對應題目']== q].index)
    df = df_q[[q]].replace(list(range(1,count-1))+[ 0, 99], list(item.iloc[o,3]))
    df2 = pd.concat([df2, df], ignore_index= True, axis= 1)    
colname = list(item.調查品項.unique())
df2.columns = colname
#用文字代替1.2
#sex = df_q.loc[:,'性別']      #loc跟iloc差別在於loc直接輸入列首名稱；若"1:2"意思1和2行
#sexframe =pd.DataFrame(sex)
#for j in range(1,660):
#    if sex==1:
#        temp1 = sexframe.replace(1,'男')
#    elif sex==2:
#        temp1 = sexframe.replace(2,'女')
#print(sexframe)

sex = df_q.loc[:,'性別']
sex1 = sex.replace([1],'男')
sex2 = sex1.replace([2],'女')
sexframe = pd.DataFrame(sex2)
df_sex = pd.concat([df2, sexframe], ignore_index= False, axis=1)

'''
df_sex.pivot_table(index=['行動電話系統業者','性別'], values=['性別'], aggfunc=[np.sum])
pd.crosstab(df_sex.行動電話系統業者, df_sex.性別, margins= True)
for i in range(0,101):
    b= pd.crosstab(df_sex.iloc[:,i], df_sex.性別, margins=True)
    c= pd.concat()
print(b)
'''
df_S1= pd.DataFrame()
for i in range(0,100):
    S1= pd.crosstab(df_sex.iloc[:,i], df_sex.性別, margins=True).sort_values(by='All', ascending=0)
    S1.drop(['All'], inplace=True)
    S1= S1.reset_index(drop=False)
    
    all= S1.iloc[:,0].size
    Rank= pd.DataFrame(list(range(1, all+1)), columns=['廠商排名'])
    
    S1= pd.concat([S1, Rank], axis=1, ignore_index= False)
    S1.columns= ['廠商名稱', '女', '男', '綜合', '廠商排名']
    
    df_S1= pd.concat([df_S1, S1],axis= 0)
    df_S1= df_S1.reset_index(drop=True)
print(df_S1)