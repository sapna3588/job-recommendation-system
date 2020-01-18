import pandas as pd
from collections import defaultdict
from collections import OrderedDict
import numpy as np
def clean_loc():
    df=pd.read_csv('/home/sunbeam/Desktop/Project_Naukri/project_new_24_12_2.csv')

    list1=[]
    for val in df['company']:
        list1.append(val)
    # print(list1)

    temp = defaultdict(lambda: len(temp))
    res = [temp[ele] for ele in list1]
    # print("The ids of original company is : " + list1)
    # print("The ids of assigned values is : " + res)
    df['company_id']=res

    # print(df['company_id'])


    dict1={}

    for (val, i) in zip(df['company'], res):
        # print(f"{val}:{i}")
        dict1[val] = i
        df[id]=i
    print(type(df['joblocation_address']))




    reshaped = \
    (df.set_index(df.columns.drop('joblocation_address',1).tolist())
       .joblocation_address.str.split(',', expand=True)
       .stack()
       .reset_index()
       .rename(columns={0:'joblocation_address'})
       .loc[:, df.columns]
    )


    pd.set_option('display.max_columns', 5)
    pd.set_option('display.max_rows', 4)
    pd.set_option('display.width', 1000)
    print(reshaped)
    # list1=[]
    # for val in df['joblocation_address']:
    #      str(val)
    #      list1.append(val)
    # print(type(val))
    # df['location']=list1
    # print(type(df['location']))
    reshaped.to_csv('/home/sunbeam/Desktop/Project_Naukri/project_new_26_12_6.csv')
def replace():
    df=pd.read_csv('/home/sunbeam/Desktop/Project_Naukri/project_new_26_12_5.csv')

    df['joblocation_address']=df['joblocation_address'].str.replace(r'Delhi NC.+','NCR',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Bengaluru/Bangalore).+','Bangalore',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Bengaluru/Bangalore).+','Bangalore',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'Bengalur.+','Bangalore',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Gurgaon).+','NCR',regex=True)
    v=df['joblocation_address'].strip()
    print(v)

    # df['joblocation_address']=df['joblocation_address'].replace(to_replace=['Delhi NCR',' Delhi'],value='NCR',regex=True,inplace=True)
    # df['new_loc']=df.loc[df['joblocation_address'].isin(['Delhi NCR' , ' Delhi'])]='NCR'
    # print(df['joblocation_address'])
    # replacements = {
    #     'joblocation_address': {
    #         r'Delhi NCR':'NCR',
    #         r'(Bengaluru/Bangalore)': 'Bangalore',
    #         r'Bengaluru': 'Bangalore',
    #         r'Hyderabad / Secunderabad': 'Hyderabad',
    #         r'Mumbai , Mumbai': 'Mumbai',
    #         r'Noida': 'NCR',
    #         r'Delhi': 'NCR',
    #         r'Gurgaon': 'NCR',
    #         r'Delhi/NCR(National Capital Region)': 'NCR',
    #         r'Delhi , Delhi': 'NCR',
    #         r'Noida , Noida/Greater Noida': 'NCR',
    #         r'Ghaziabad': 'NCR',
    #         r'Delhi/NCR(National Capital Region) , Gurgaon': 'NCR',
    #         r'NCR , NCR': 'NCR',
    #         r'NCR/NCR(National Capital Region)': 'NCR',
    #         r'NCR , NCR/Greater NCR': 'NCR',
    #         r'NCR/NCR(National Capital Region) , NCR': 'NCR',
    #         r'NCR , NCR/NCR(National Capital Region)': 'NCR',
    #         r'Bangalore , Bangalore / Bangalore': 'Bangalore',
    #         r'Bangalore , karnataka': 'Bangalore',
    #         r'NCR/NCR(National Capital Region)': 'NCR',
    #         r'NCR/Greater NCR': 'NCR',
    #         r'NCR/NCR(National Capital Region) , NCR': 'NCR'
    #
    #     }
    #     }
    # df.replace(replacements, regex=True, inplace=True)
    return df
df=replace()
# clean_loc()

