#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 23:57:29 2018

@author: Nina
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

#總排名-理想

#匯入資料
df001 = pd.read_csv("2019_allrank_dream.csv")
df002 = pd.read_csv("2019_allrank_dream_north.csv")
df003 = pd.read_csv("2019_allrank_dream_mid.csv")
df004 = pd.read_csv("2019_allrank_dream_south.csv")
item = pd.read_csv("item.csv")


def result(x): # x=1 --> q01, x=14 --> q14 以此類推
    
    #取出q0n那些行！！
    q = list(item.對應題目.unique())[x-1]
    data1 = df001[df001['題項'] == q ].reset_index(drop = True)
    data2 = df002[df002['題項'] == q ].reset_index(drop = True)
    data3 = df003[df003['題項'] == q ].reset_index(drop = True)
    data4 = df004[df004['題項'] == q ].reset_index(drop = True)
     
    #用函數算出各區的前五名
    def func(datan,n):  #n是區域
        list1 = []
        percent = datan.廠商百分比.values.tolist() #dataframe一列轉list
        row = -1
        for rank in datan.iloc[:,3]:
            row = row + 1
            if rank < 6 and percent[row] > 0.01:
                list1.append(datan.iloc[row,0])
                list1.append(datan.iloc[row,3])
                list1.append('%.2f'%(float(datan.iloc[row,2])*100))
            rank = np.array(list1)
            rank = rank.reshape(int(rank.shape[0]/3),3)
            rank = pd.DataFrame(rank, columns=['品項_{}'.format(n),'名次_{}'.format(n),
                                               '{}'.format(n)]) 
            rank.set_index('品項_{}'.format(n),inplace=True)                       
        return rank
    
    data001 = func(data1,'全區')
    data002 = func(data2,'北區')
    data003 = func(data3,'中區')
    data004 = func(data4,'南區')
    
    #轉dataframe 然後concat
    rank= pd.concat([data001,data002,data003,data004],axis = 1,ignore_index = False )
    rank.replace(np.NaN,'—', inplace = True)
    #新建一個dataframe，根據rank中的'名次_全區'來排序其他欄位
    rank_test = pd.DataFrame()
    rank_test = rank.sort_index(by='名次_全區')        
    rank_test.reset_index(drop=False, inplace=True)
    rank_test.columns = ['品牌名稱','名次','全區','名次','北區','名次','中區','名次','南區']
    
    ###總排名完成了鴨    
    return rank_test   #最後再把大家包進一個函數裡

#輸出想要的總排名，更換對應品項的數字
ideal_Totalrank = result(90)


##############接下來要寫交叉分析了鴨###############


def result(itemxx,x): #item是性別，年齡那些, x是對應的題項數字（如人壽保險是q14，這裡x=14）
    #匯入交叉分析的檔案
    cross001 = pd.read_excel("01_2019交叉分析(全區)_理想_格式正確.xlsx",sheet_name = '全區_{}'.format(itemxx))
    cross002 = pd.read_excel("02_2019交叉分析(北區)_理想_格式正確.xlsx",sheet_name = '北區_{}'.format(itemxx))
    cross003 = pd.read_excel("03_2019交叉分析(中區)_理想_格式正確.xlsx",sheet_name = '中區_{}'.format(itemxx))
    cross004 = pd.read_excel("04_2019交叉分析(南區)_理想_格式正確.xlsx",sheet_name = '南區_{}'.format(itemxx))

    #用函數抓出各區的交叉分析結果
    def func(cross001):        
        a = list(item.調查品項.unique())[15]  #實際的檔案不能用q，因為裡面不是q01，是q01v01
        c1 = cross001[cross001['{}_調查品項'.format(itemxx)] == a ].reset_index(drop = True)
        c1 = c1.iloc[:,2:-3]
        c1.set_index('廠商名稱',inplace=True)   
        #把百分號%去掉
        for i in range(c1.iloc[:,0].size):
            for j in range(c1.iloc[0,:].size):
                c1.iloc[i,j] = c1.iloc[i,j].rstrip('%')
                if eval(c1.iloc[i,j]) < 1:   #捨棄數值小於1的數字
                    c1.iloc[i,j] = '—'                          
        return c1
    
    c001 = func(cross001)
    c002 = func(cross002)
    c003 = func(cross003)
    c004 = func(cross004)
 
    ### 補齊沒有的項目（比如南區的月收入沒有‘90-110’，‘110-130，‘130以上’）      
    def func(c00n):       
        option = list(c001.columns.values)
        c_empty = pd.DataFrame(columns=option) ##建立了一個空的Dataframe，columns名字是全區的全部選項
        c_empty.columns = option               ##這樣就可以讓每個區的選項相等
        c_empty = c_empty.append(c00n)  ##！！裝進對應的column裡面！！其他是nan！！
                                        ##如南區月收入會有‘110-130‘...這些欄位，但是內容是nan，下面再取代
        return c_empty

    c002_intact = func(c002)  #不用001，這裡只要檢查北中南區，因為全區最完整
    c003_intact = func(c003)
    c004_intact = func(c004)    
    
    #concat,axis=0
    cross= pd.concat([c001,c002_intact,c003_intact,c004_intact],
                     axis = 1,ignore_index = False )
    cross.replace(np.NaN,'—', inplace = True)           
    cross = cross.T  ##先concat再轉置，可以避免因為長度不一樣欄位會跑掉的困擾（雖然這時候已經修正到欄位相同了）
    cross.reset_index(drop=False, inplace=True) 
    cross.rename(columns={'index':'{}'.format(itemxx)},inplace=True)     
    
    #加上最前面“全區，北區，中區，南區”那一欄
    num = int(cross.iloc[:,0].size)+1
    n = int(num/4) ##n是計算一個區有行，一個區域的名字要重複幾次
    area = ['全區','北區','中區','南區']
    area1 = []
    for i in area:
        for j in range(n):
            area1.append(i)
    cross.insert(0,'地區',area1)    
    
    return(cross)

#輸出的結果為可交付成果中的一個sheet，更換對應品項的數字即可
    
ideal_cross_gender = result('性別',90)
ideal_cross_age = result('年齡',90)
ideal_cross_income = result('月收入',90)
ideal_cross_residence = result('居住地',90)
ideal_cross_job = result('職業',90)
ideal_cross_edu = result('學歷',90)

#交叉分析結束

################################ 理想結束 ######################################
############################## 接下來是實際 #####################################

###----總排名-實際----  
#步驟一：先匯入實際的檔案
df001 = pd.read_csv("2019_allrank_act.csv")
df002 = pd.read_csv("2019_allrank_act_north.csv")
df003 = pd.read_csv("2019_allrank_act_mid.csv")
df004 = pd.read_csv("2019_allrank_act_south.csv")

#步驟二：執行24-66行

#步驟三：更改所需品項對應題項數字，執行下面這行
actual_Totalrank = result(14)

###----總排名-實際結束----

###----交叉分析-實際----
#步驟一：先去修改格式檔案

#步驟二：將77-80行中的“理想”改為“實際”，然後執行75-132行

#步驟三：更改所需品項對應題項數字，執行下面這幾行

actual_cross_gender = result('性別',14)
actual_cross_age = result('年齡',14)
actual_cross_income = result('月收入',14)
actual_cross_residence = result('居住地',14)
actual_cross_job = result('職業',14)
actual_cross_edu = result('學歷',14)

###----交叉分析-實際結束----


#輸出excel（理想和實際一起）
writer = pd.ExcelWriter('2019-14_人壽保險類_廠商授權書.xlsx', engine='xlsxwriter') 
#理想
ideal_Totalrank.to_excel(writer, sheet_name='表一、理想品牌排名統計表', startrow= 0, index=False)  
ideal_cross_gender.to_excel(writer, sheet_name='性別（理想）', startrow= 0, index=False)  
ideal_cross_age.to_excel(writer, sheet_name='年齡（理想）', startrow= 0, index=False)
ideal_cross_income.to_excel(writer, sheet_name='月收入（理想）', startrow= 0, index=False)
ideal_cross_residence.to_excel(writer, sheet_name='居住地（理想）', startrow= 0, index=False)
ideal_cross_job.to_excel(writer, sheet_name='職業（理想）', startrow= 0, index=False)
ideal_cross_edu.to_excel(writer, sheet_name='學歷（理想）', startrow= 0, index=False)
#實際
actual_Totalrank.to_excel(writer, sheet_name='表二、實際品牌排名統計表', startrow= 0, index=False)  
actual_cross_gender.to_excel(writer, sheet_name='性別（實際）', startrow= 0, index=False)  
actual_cross_age.to_excel(writer, sheet_name='年齡（實際）', startrow= 0, index=False)
actual_cross_income.to_excel(writer, sheet_name='月收入（實際）', startrow= 0, index=False)
actual_cross_residence.to_excel(writer, sheet_name='居住地（實際）', startrow= 0, index=False)
actual_cross_job.to_excel(writer, sheet_name='職業（實際）', startrow= 0, index=False)
actual_cross_edu.to_excel(writer, sheet_name='學歷（實際）', startrow= 0, index=False)

writer.save()




























