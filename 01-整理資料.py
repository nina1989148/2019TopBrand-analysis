# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:08:53 2018

@author: nina
"""

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd

dataframe = pd.read_csv('001.csv')
item = pd.read_csv('item.csv')

df1 = dataframe[['性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷']]
df2 = dataframe.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df2 = df2.iloc[:, list(range(0,202,2))]  
print(df2.shape)
print('-'*8)
print(df1.shape)

df1.head()
df2.head()

df1 = df1.replace({'性別':{0:'未填答', 1:'男', 2:'女'},
             '年齡':{0:'未填答', 1:'26-30歲', 2:'31-35歲', 3:'36-40歲', 4:'41-45歲', 5:'46-50歲', 6:'51-55歲', 7:'56-60歲', 8:'61歲及以上'},
             '月收入':{0:'未填答', 1:'30,000元以下', 2: '30,001-50,000元', 3:'50,001-70,000元', 4:'70,001-90,000元', 5:'90,001-110,000元', 6: '110,001-130,000元', 7:'130,000元以上'},
             '居住地':{0:'未填答', 1:'基隆、宜蘭、台北、新北', 2:'桃園、新竹、苗栗', 3:'台中地區', 4:'彰化、雲林、南投', 5:'嘉義、台南', 6:'高雄、屏東', 7:'花蓮、台東'},
             '職業':{0:'未填答', 1:'製造業', 2:'軍公教', 3:'工商貿易', 4:'服務業', 5:'金融業', 6:'資訊業', 7:'自由業', 8:'學生', 9:'其他'},
             '學歷':{0:'未填答', 1:'國中（含）以下', 2:'高中職', 3:'專科及大學', 4:'研究所以上'}})
df1.head()
df1.shape

#除錯
print(df1.性別.unique())
print(df1.年齡.unique())
print(df1.月收入.unique())
print(df1.居住地.unique())
print(df1.職業.unique())
print(df1.學歷.unique())

df1['居住地'] = df1['居住地'].astype(str)
df1['職業'] = df1['職業'].astype(str)
df1.info()

#問卷資料
#df2.rename(columns={'q01 ':'q01'}, inplace=True)
df2.rename(columns={'q35 ':'q35'}, inplace=True)
df2.rename(columns={'q66 ':'q66'}, inplace=True)

q = list(item.對應題目.unique())[0]
count = item[item['對應題目']== q].子題名稱.count()

df3 = pd.DataFrame()
for i in range(0,101):
    q = list(item.對應題目.unique())[i]
    count = item[item['對應題目']== q].子題名稱.count()
    o = list(item[item['對應題目']== q].index)
    da = df2[[q]].replace(list(range(1,count-1))+[ 0, 99], list(item.iloc[o,3]))
    df3 = pd.concat([df3, da], ignore_index= True, axis= 1)
colname = list(item.調查品項.unique())
df3.columns = colname

df3.行動電話系統業者.unique()
df_final = pd.concat([df3, df1], ignore_index= False, axis= 1 ) 
df_final.shape
df_final.行動電話系統業者.unique()

#拆解步驟
df_final.head()
crosstab1 = pd.crosstab(df_final[df_final.columns[0]], df_final['性別'], margins=True).sort_values(by='All',ascending=0)
crosstab1.head()
crosstab1.rename(columns={'All': '總和'}, inplace=True)
crosstab1['{}_調查品項'.format('性別')] = df_final.columns[0]
crosstab1['對應題目'] = df2.columns[0]
crosstab1.head()

crosstab1 = crosstab1[crosstab1.index != '其他']
crosstab1 = crosstab1[crosstab1.index != '未填答']
crosstab1 = crosstab1[crosstab1.index != 'All']
crosstab1['廠商排名']=crosstab1['總和'].rank(ascending=0,method='min')
crosstab1.head()

df_crosstab = pd.DataFrame()
df_crosstab = pd.concat([df_crosstab,crosstab1], ignore_index= False, axis = 0)      
df_crosstab = df_crosstab.rename_axis(None, axis="columns")
df_crosstab['廠商名稱'] = df_crosstab.index 
df_crosstab = df_crosstab[['對應題目','{}_調查品項'.format('性別'), '廠商名稱']+list(df_final['性別'].unique())+['總和', '廠商排名']]
df_crosstab.head()

# x 放性別、年齡、月收入、居住地、職業、學歷

def crosstab_by(x):    
    df_crosstab = pd.DataFrame()
    for i in range(0,101):
        crosstab1 = pd.crosstab(df_final[df_final.columns[i]], df_final[x], margins=True).sort_values(by='All',ascending=0)
        crosstab1.rename(columns={'All': '總和'}, inplace=True)
        crosstab1['{}_調查品項'.format(x)] = df_final.columns[i]
        crosstab1['對應題目'] = df2.columns[i]
        crosstab1 = crosstab1[crosstab1.index != '其他']
        crosstab1 = crosstab1[crosstab1.index != '未填答']
        crosstab1 = crosstab1[crosstab1.index != 'All']
        crosstab1['廠商排名']=crosstab1['總和'].rank(ascending=0,method='min')
        df_crosstab = pd.concat([df_crosstab,crosstab1], ignore_index= False, axis = 0)      
        df_crosstab = df_crosstab.rename_axis(None, axis="columns")
        df_crosstab['廠商名稱'] = df_crosstab.index 
        df_crosstab = df_crosstab[['對應題目','{}_調查品項'.format(x), '廠商名稱']+list(df_final[x].unique())+['總和', '廠商排名']]
        df_crosstab
    return df_crosstab

def square(x):
    x = x**2
    return x
#Sex
print(df1.性別.unique())
sex = crosstab_by('性別')
sex.iloc[:,-4:-1] = sex.iloc[:,-4:-1]*100/df_final.shape[0]
sex = sex.round(1)
sex[list(sex.columns[3:6])] = sex[list(sex.columns[3:6])].astype(str) + '%'
sex.head(5)

#Age
print(df1.年齡.unique())
age = crosstab_by('年齡')
age.iloc[:,-11:-1] = age.iloc[:,-11:-1]*100/df_final.shape[0]
age = age.round(1)
age[list(age.columns[3:13])] = age[list(age.columns[3:13])].astype(str) + '%'
age.head(7)

#income
print(df1.月收入.unique())
income = crosstab_by('月收入')
income.iloc[:,-10:-1] = income.iloc[:,-10:-1]*100/df_final.shape[0]
income = income.round(1)
income[list(income.columns[3:12])] = income[list(income.columns[3:12])].astype(str) + '%'
income.head(7)

#Residence
print(df1.居住地.unique())
residence = crosstab_by('居住地')
#residence = residence.drop(['14'], axis = 1)
residence.iloc[:,-6:-1] = residence.iloc[:,-6:-1]*100/df_final.shape[0]
residence = residence.round(1)
residence[list(residence.columns[3:8])] = residence[list(residence.columns[3:8])].astype(str) + '%'
residence.head(7)

#job
print(df1.職業.unique())
job = crosstab_by('職業')
#job = job.drop(['nan'], axis = 1)
job.iloc[:,-12:-1] = job.iloc[:,-12:-1]*100/df_final.shape[0]
job = job.round(1)
job[list(job.columns[3:14])] = job[list(job.columns[3:14])].astype(str) + '%'
job.head(7)

#education
print(df1.學歷.unique())
education = crosstab_by('學歷')
education.iloc[:,-7:-1] = education.iloc[:,-7:-1]*100/df_final.shape[0]
education = education.round(1)
education[list(education.columns[3:9])] = education[list(education.columns[3:9])].astype(str) + '%'
education.head(7)

#Xlsx
writer = pd.ExcelWriter('交叉分析(北區).xlsx', engine='xlsxwriter') 

sex.to_excel(writer, sheet_name='北區_性別', startrow= 0, index=False)  
age.to_excel(writer, sheet_name='北區_年齡', startrow= 0, index=False)
income.to_excel(writer, sheet_name='北區_月收入', startrow= 0, index=False)
residence.to_excel(writer, sheet_name='北區_居住地', startrow= 0, index=False)
job.to_excel(writer, sheet_name='北區_職業', startrow= 0, index=False)
education.to_excel(writer, sheet_name='北區_學歷', startrow= 0, index=False)

writer.save()
