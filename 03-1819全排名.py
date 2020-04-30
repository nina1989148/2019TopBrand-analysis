
# coding: utf-8

# In[1]:

import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np



# # 2018檔案載入

# In[2]:


df18001 = pd.read_csv('0012018.csv')
df18002 = pd.read_csv('0022018.csv')
df18003 = pd.read_csv('0032018.csv')
df18004 = pd.read_csv('0042018.csv')


# In[3]:


print(df18001.shape,'\n',df18002.shape,'\n', df18003.shape,'\n',df18004.shape)


# In[4]:


item18 = pd.read_csv('18item.csv')
#item18[item18['調查品項']=='建設公司']item18.info()
# In[5]:


df1801 = df18001.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df1802 = df18002.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df1803 = df18003.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df1804 = df18004.drop(['NO'], axis = 1)
df181 = df1801.iloc[:, list(range(0,194,2))]
df182 = df1802.iloc[:, list(range(0,194,2))]
df183 = df1803.iloc[:, list(range(0,194,2))]
df184 = df1804.iloc[:, list(range(0,194,2))]

df181.q11
# In[6]:


print(df181.shape,'\n',df182.shape,'\n', df183.shape,'\n',df184.shape)


# In[11]:


df181.rename(columns={'q35 ':'q35'}, inplace=True)
df181.rename(columns={'q66 ':'q66'}, inplace=True)


# In[12]:


df182.rename(columns={'q35 ':'q35'}, inplace=True)
df182.rename(columns={'q66 ':'q66'}, inplace=True)


# In[13]:


df183.rename(columns={'q35 ':'q35'}, inplace=True)
df183.rename(columns={'q66 ':'q66'}, inplace=True)


# In[14]:


#df184.columns


# In[15]:


#df184.rename(columns={'q01 ':'q01'}, inplace=True)
df184.rename(columns={'q35 ':'q35'}, inplace=True)
df184.rename(columns={'q66 ':'q66'}, inplace=True)


# # test

# In[16]:


q = list(item18.對應題目.unique())[5]


# In[17]:


q


# In[18]:


count = item18[item18['對應題目']== q].子題名稱.count()


# In[19]:


o = list(item18[item18['對應題目']== q].index)


# In[20]:


o


# In[21]:


oo =list(range(1,count-1))+[ 0, 99]


# In[22]:


oo


# In[23]:


ooo = list(item18.iloc[o,3])


# In[24]:


df = df181[[q]].replace(list(range(1,count-1))+[ 0, 99], list(item18.iloc[o,3]))


# In[25]:


#df2 = pd.DataFrame()
#df2 = pd.concat([df2, df], ignore_index= True, axis= 1)


# # test

# In[26]:


def transdf18(df_q, item):
    df2 = pd.DataFrame()
    for i in range(0,97):
        q = list(item.對應題目.unique())[i]
        count = item[item['對應題目']== q].子題名稱.count()
        o = list(item[item['對應題目']== q].index)
        df = df_q[[q]].replace(list(range(1,count-1))+[ 0, 99], list(item.iloc[o,3]))
        df2 = pd.concat([df2, df], ignore_index= True, axis= 1)
    df2.columns = list(item.調查品項.unique())
    return df2

list(item18.調查品項.unique())
df.rename(columns={'q35' :'q35'}, inplace=True)
# In[27]:


df18 = transdf18(df181, item18)


# In[29]:


df28 = transdf18(df182, item18)


# In[30]:


df38 = transdf18(df183, item18)


# In[31]:


df48 = transdf18(df184, item18)


# In[32]:


print(df18.shape,'\n',df28.shape,'\n', df38.shape,'\n',df48.shape)


# # 2019檔案載入

# In[33]:


df19001 = pd.read_csv('001_win.csv')
df19002 = pd.read_csv('002_win.csv')
df19003 = pd.read_csv('003_win.csv')
df19004= pd.concat([df19001, df19002, df19003], ignore_index= True , axis= 0 ) 


# In[34]:


print(df19001.shape,'\n',df19002.shape,'\n', df19003.shape,'\n',df19004.shape)


# In[35]:


item19 = pd.read_csv('19item.csv')


# In[36]:


df1901 = df19001.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df1902 = df19002.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df1903 = df19003.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df1904 = df19004.drop(['NO','性別','年齡' ,'月收入' ,'居住地' ,'職業', '學歷', '姓名', '地址', '電話'], axis = 1)
df191 = df1901.iloc[:, list(range(0,202,2))]
df192 = df1902.iloc[:, list(range(0,202,2))]
df193 = df1903.iloc[:, list(range(0,202,2))]
df194 = df1904.iloc[:, list(range(0,202,2))]


# In[37]:


print(df191.shape,'\n',df192.shape,'\n', df193.shape,'\n',df194.shape)


# In[38]:


df191.rename(columns={'q35 ':'q35'}, inplace=True)
df191.rename(columns={'q66 ':'q66'}, inplace=True)


# In[39]:


df194.info()


# In[40]:


df192.rename(columns={'q35 ':'q35'}, inplace=True)
df192.rename(columns={'q66 ':'q66'}, inplace=True)


# In[41]:


df193.rename(columns={'q35 ':'q35'}, inplace=True)
df193.rename(columns={'q66 ':'q66'}, inplace=True)


# In[42]:


df194.rename(columns={'q35 ':'q35'}, inplace=True)
df194.rename(columns={'q66 ':'q66'}, inplace=True)


# In[43]:


def transdf19(df_q, item):
    df2 = pd.DataFrame()
    for i in range(0,101):
        q = list(item.對應題目.unique())[i]
        count = item[item['對應題目']== q].子題名稱.count()
        o = list(item[item['對應題目']== q].index)
        df = df_q[[q]].replace(list(range(1,count-1))+[ 0, 99], list(item.iloc[o,3]))
        df2 = pd.concat([df2, df], ignore_index= True, axis= 1)
    df2.columns = list(item.調查品項.unique())
    return df2


# In[44]:


df19 = transdf19(df191, item19)


# In[45]:


df29 = transdf19(df192, item19)


# In[46]:


df39 = transdf19(df193, item19)


# In[47]:


df49 = transdf19(df194, item19)


# In[48]:


print(df19.shape,'\n',df29.shape,'\n', df39.shape,'\n',df49.shape)


# # 2019|合併

# In[49]:


#df19.pivot_table(values=['年龄'], index=['年龄分层'], columns=['性别'], aggfunc=[numpy.size])


# In[50]:


#pd.crosstab(df19['行動電話系統業者'],'行動電話系統業者')


# In[51]:


df119 = df19.groupby(by=['行動電話系統業者'])['行動電話系統業者'].count()
df119 = pd.DataFrame(df119).sort_values(by='行動電話系統業者',ascending=0)
df119['廠商名稱'] = df119.index
#df119['廠商排名'] = df119['行動電話系統業者'].rank(ascending=0,method='min')
#del df119.index.name
#df119 = df119.drop(['行動電話系統業者'], axis = 1)
#df119['調查品項'] = '行動電話系統業者'
#df119 = df119[['調查品項', '廠商名稱', '廠商排名']]
print(df119,'\n',  type(df119))


# # 2019排名

# In[52]:


def df_creat19(df):    
    final_df = pd.DataFrame()
    for i in range(101):       
        df1 = df.groupby(by=[df.columns[i]])[df.columns[i]].count()
        df1 = pd.DataFrame(df1).sort_values(by = df.columns[i],ascending=0)
        df1['19廠商名稱'] = df1.index
        df1 = df1[np.logical_and(df1['19廠商名稱']!= '未填答', df1['19廠商名稱']!= '其他')]
        df1['19廠商排名'] = df1[df.columns[i]].rank(ascending=0,method='min')
        del df1.index.name
        df1 = df1.drop([df.columns[i]], axis = 1)
        df1['19調查品項'] = df.columns[i]
        df1 = df1[['19調查品項', '19廠商名稱', '19廠商排名']]
        final_df = pd.concat([final_df, df1], ignore_index= True , axis= 0 )
    return final_df    


# In[53]:


final191 = df_creat19(df19)
final191[final191['19調查品項']=='茶飲料']


# In[54]:


final192 = df_creat19(df29)
final192.head(3)


# In[55]:


final193 = df_creat19(df39)
final193.head(3)


# In[56]:


final194 = df_creat19(df49)
final194.head(3)


# In[57]:


final191.to_excel('{}.xlsx'.format('final191'),encoding='utf-8', index = False )
final192.to_excel('{}.xlsx'.format('final192'),encoding='utf-8', index = False )
final193.to_excel('{}.xlsx'.format('final193'),encoding='utf-8', index = False )
final194.to_excel('{}.xlsx'.format('final194'),encoding='utf-8', index = False )


# # 2018排名

# In[58]:


def df_creat18(df):    
    final_df = pd.DataFrame()
    for i in range(97):
        df1 = df.groupby(by=[df.columns[i]])[df.columns[i]].count()
        df1 = pd.DataFrame(df1).sort_values(by = df.columns[i],ascending=0)
        df1['18廠商名稱'] = df1.index
        df1 = df1[np.logical_and(df1['18廠商名稱']!= '未填答', df1['18廠商名稱']!= '其他')]
        df1['18廠商排名'] = df1[df.columns[i]].rank(ascending=0,method='min')
        del df1.index.name
        df1 = df1.drop([df.columns[i]], axis = 1)
        df1['18調查品項'] = df.columns[i]
        df1 = df1[['18調查品項', '18廠商名稱', '18廠商排名']]        
        final_df = pd.concat([final_df, df1], ignore_index= True , axis= 0 )
    return final_df 


# In[59]:


final181 = df_creat18(df18)
final181.head(3)


# In[60]:


final182 = df_creat18(df28)
final182.head(3)


# In[61]:


final183 = df_creat18(df38)
final183.head(3)


# In[62]:


final184 = df_creat18(df48)
final184.head(3)


# In[63]:


final184[final184['18調查品項']=='茶飲料']


# In[64]:


final181.to_excel('{}.xlsx'.format('final181'),encoding='utf-8', index = False )
final182.to_excel('{}.xlsx'.format('final182'),encoding='utf-8', index = False )
final183.to_excel('{}.xlsx'.format('final183'),encoding='utf-8', index = False )
final184.to_excel('{}.xlsx'.format('final184'),encoding='utf-8', index = False )


# # 18/19品項比較 001

# In[165]:


final91 = final191[np.logical_and(final191['19調查品項']!='政治人物', final191['19調查品項']!='談話性節目主持人')]


# In[166]:


final91 = final91[np.logical_and(final191['19調查品項']!='綜藝節目主持人', final191['19調查品項']!='吸塵器')]


# In[167]:


len(list(final91['19調查品項'].unique()))


# In[168]:


len(list(final181['18調查品項'].unique()))


# In[169]:


final91.head(7)


# In[170]:


final181.head(7)


# In[171]:


list(final181['18調查品項'].unique())[0]


# In[172]:


final181['18廠商名稱'][0] not in list(final91['19廠商名稱'][0:3])


# In[173]:


final181['18廠商名稱'][0]


# In[174]:


data18 = final181[final181['18調查品項'] == '行動電話系統業者'].reset_index()
data18


# In[175]:


data19 = final91[final91['19調查品項'] == '數據網路服務'].reset_index()
data19


# In[176]:


data19[data19['18廠商名稱']== '行動電話系統業者']['19廠商排名']


# In[110]:


list(final181['18調查品項'].unique())[10]


# In[146]:


data18 = final181[final181['18調查品項'] == '建設公司' ].reset_index()
data18


# In[170]:


data19 = final91[final91['19調查品項'] == '建設公司'].reset_index()
data19


# In[144]:


data18['18廠商名稱'][0]


# In[165]:


int(data19[data19['19廠商名稱']==data18['18廠商名稱'][0]].iloc[:,3])


# In[194]:


result1901 = []
for i in range(50):
    a = list(final181['18調查品項'].unique())[i]##行動電話系統業者、數據網路服務...
    data18 = final181[final181['18調查品項'] == a ].reset_index()## 18調查品項 == 行動電話系統業者...的紫dataframe
    data19 = final91[final91['19調查品項'] == a].reset_index()## 19調查品項 == 行動電話系統業者...的紫dataframe
    #data18['18廠商名稱'][0] not in list(data19['19廠商名稱'][0:3])
    for j in range(3):
        if data18['18廠商名稱'][j] not in list(data19['19廠商名稱'][0:3]):##條件
            bb = data18['18廠商名稱'][j]
            result1901.append(data18['18調查品項'][0])
            result1901.append(bb)
            result1901.append(data18['18廠商排名'][j])
            result1901.append(int(data19[data19['19廠商名稱']==bb].iloc[:,3]))
            if int(data19[data19['19廠商名稱']==bb].iloc[:,3]) <=5:
                result1901.append('否')
            else:
                result1901.append('是')


# In[193]:


resulttest = np.array(result1901)
resulttest


# In[188]:


result1901 = np.array(result1901)
result1901 = result1901.reshape(53,3)
resultdf = pd.DataFrame(result1901, columns=['品項名稱', '品牌', '2018排名'])


# In[189]:


resultdf


# In[191]:


resdf191 = resultdf.drop(resultdf.index[[28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40]]).reset_index()
resdf191= resdf191.drop(['index'], axis = 1)
resdf191.head()


# In[199]:


resdf911 = final91[np.logical_and(final91['19調查品項']=='房屋仲介', final91['19廠商名稱']=='21世紀')]
resdf911.iloc[0]['19廠商排名']


# In[207]:


resdf191_1 = []
for i in range(3):
    dfx = final91[np.logical_and(final91['19調查品項']== resdf191['品項名稱'][i] , final91['19廠商名稱']==resdf191['品牌'][i])]
    resdf191_1.append(dfx.iloc[0]['19廠商排名'])
    if dfx.iloc[0]['19廠商排名'] <= 5:
        resdf191_1.append('否')
    else:
        resdf191_1.append('是')
print(resdf191_1)


# In[184]:


final91.head()


# # 002

# In[ ]:


'政治人物', '談話性節目主持人', '綜藝節目主持人', '吸塵器'


# In[129]:


final191 = final191[np.logical_and(final191['19調查品項']!='政治人物', final191['19調查品項']!='談話性節目主持人')]


# In[130]:


final191 = final191[np.logical_and(final191['19調查品項']!='綜藝節目主持人', final191['19調查品項']!='吸塵器')]


# In[137]:


final191.head(8)


# In[139]:


final181.head(5)


# In[151]:


set(final181['18廠商名稱'][0:3]) 


# In[152]:


set(final191['19廠商名稱'][0:3])


# In[53]:


a = set(final191['19調查品項'].unique())


# In[54]:


b = set(final181['18調查品項'].unique())


# In[55]:


a-b


# # 合併2018/2019排名
final1819001= pd.concat([final191, final181], ignore_index= False , axis= 1 ) 
final1819001.head()#1429() 以下不比final1819002= pd.concat([final192, final182], ignore_index= False , axis= 1 ) 
final1819002.tail()#1429(73) 以下不比final1819003= pd.concat([final193, final183], ignore_index= False , axis= 1 ) 
final1819003.tail(73)#1429(73) 以下不比final1819004= pd.concat([final194, final184], ignore_index= False , axis= 1 ) 
final1819004.tail()#1429(73) 以下不比
# # [more than 2 logical conditions](https://cmsdk.com/python/trying-to-find-python-numpy-indexes-with-more-than-2-logical-conditions.html)

# In[ ]:


w = data[np.where(np.logical_and(data['RA']>=(ra_in-0.1), data['RA']<=(ra_in+0.1), data['DEC']>=(dec_in-0.1), data['DEC']<=(dec_in+0.1)  ))]


# In[ ]:


data[np.where(
    np.logical_and(
        np.logical_and(data['RA']>=(ra_in-0.1), data['RA']<=(ra_in+0.1),
        np.logical_and(data['DEC']>=(dec_in-0.1), data['DEC']<=(dec_in+0.1)
    ))]

