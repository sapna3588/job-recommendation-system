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
    df['joblocation_address'] = df['joblocation_address'].str.strip()
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Delhi NC).+','NCR',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Bengaluru/Bangalore).+','Bangalore',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Bengalur).+','Bangalore',regex=True)
    df['joblocation_address']=df['joblocation_address'].str.replace(r'(Gurgaon).+','NCR',regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Hyderabad / Secunderabad).+','Hyderabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace( r'(Mumbai , Mumbai).+', 'Mumbai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bengaluru/Bangalore).+', 'Bangalore',regex= True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bengalur).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Gurgaon).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Noida).+','NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Delhi).+','NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Delhi/NCR(National Capital Region)).+','NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Noida/Greater Noida).+','NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace( r'(NCR/NCR(National Capital Region)).+','NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(NCR/Greater NCR).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bangalore / Bangalore).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(karnataka).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bengaluru).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Visakhapatnam/Vizag).+', 'Visakhapatnam', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Hyderabad/Secunderabad).+', 'Hyderabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bengaluru Bangalore).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Surat).+', 'Ahmedabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Vijayawada).+', 'Pune', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Mangalore).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Ghaziabad).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Faridabad).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Trivandrum).+', 'Visakhapatnam', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Mumbai Suburbs).+', 'Mumbai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Mysore).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bellary).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Ernakulam / Kochi/ Cochin).+', 'Kochi', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Hubli).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bengaluru / Bangalore).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Visakhapatnam).+', 'Visakhapatnam', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Ludhiana).+', 'Chandigarh', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Tirupati).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Vadodara).+', 'Ahmedabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Warangal).+', 'Hyderabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Greater Noida).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Chennai Bangalore).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Thane).+', 'Mumbai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Chennai Mumbai).+', 'Mumbai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Delhi/NCR).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(haryana).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Hyderabad Kolkata).+', 'Hyderabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bangalore Hyderabad).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bangalore Kolkata).+', 'Bangalore', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(PUNE Delhi).+', 'Pune', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Mumbai PUNE).+', 'Pune', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Bangalore PUNE).+', 'Pune', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Chennai Coimbatore).+', 'Chennai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Chennai Hyderabad).+', 'Chennai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Chennai Kolkata).+', 'Chennai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Cochin/ Kochi/ Ernakulam).+', 'Kochi', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Coimbatore Mumbai).+', 'Mumbai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Haryana Other).+', 'NCR', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Hyderabad Bangalore).+', 'Hyderabad', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Kolkata Mumbai).+', 'Mumbai', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(Kolkata PUNE).+', 'Pune', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(PUNE Mumbai).+', 'Pune', regex=True)
    df['joblocation_address'] = df['joblocation_address'].str.replace(r'(18).+', 'pune', regex=True)
#
    # df1['State'] = df1['State'].str.strip()
    print(df['joblocation_address'])

    df['joblocation_address'] = df['joblocation_address'].str.strip()
    df.to_csv('/home/sunbeam/project_clean_final.csv')
    return df

clean_loc()
df=replace()