#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import numpy as np


# In[2]:


URL='https://nycrtspublicportal.azurewebsites.net/data/summary'
response=requests.get(URL)


# In[3]:


doc=response.json()


# In[4]:


table1=doc[0]
table2=doc[1]
table3=doc[2]
table4=doc[3]


# In[5]:


# create a table for reported cases

#create an empty list and dictionary
table1_list=[]
table1_dict={}

table1_dict['date']=table1['title']
table1_dict['total_reported_cases']=table1['rows'][0][0]
table1_dict['total_student_cases']=table1['rows'][0][1]
table1_dict['total_staff_cases']=table1['rows'][0][2]

table1_list.append(table1_dict)
data1=pd.DataFrame(table1_list)
data1.to_csv("data/reported_covid_cases.csv", index=False)


# In[6]:


#create an empty list and dictionary
table2_list=[]
table2_dict={}

table2_dict['date']=table2['title']
table2_dict['cum_reported_cases']=table2['rows'][0][0]
table2_dict['cum_student_cases']=table2['rows'][0][1]
table2_dict['cum_staff_cases']=table2['rows'][0][2]

table2_list.append(table2_dict)
data2=pd.DataFrame(table2_list).replace(",","", regex=True)
data2.to_csv("data/cum_covid_cases.csv", index=False)


# In[7]:


column_names=[table3['header'][0], table3['header'][1],table3['header'][2],table3['header'][3]]
data3=pd.DataFrame(table3['rows'])
data3.columns=column_names
trans_data3=data3.set_index('Action').T.reset_index().rename(columns={
    'index':'doe_dece_schools'}).replace(",","", regex=True)
trans_data3['date']=trans_data3.doe_dece_schools.str.split('as', expand=True)[0][0].replace('<br>',"")
trans_data3.to_csv('data/doe_dece_actions.csv', index=False)


# In[8]:


column_names=[table4['header'][0], table4['header'][1],table4['header'][2],table4['header'][3]]
data4=pd.DataFrame(table4['rows'])
data4.columns=column_names
trans_data4=data4.set_index('Action').T.reset_index().rename(columns={
    'index':'charter_action'}).replace(",","", regex=True)
trans_data4['date']=trans_data4.charter_action.str.split('as', expand=True)[0][0].replace('<br>',"")
trans_data4.to_csv('data/charter_actions.csv', index=False)


# In[ ]:




