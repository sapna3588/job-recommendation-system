import numpy as np
import  pandas as pd
from datetime import datetime
import datetime as dt
from collections import defaultdict




def load_data():
    # reading data
    df = pd.read_csv('/home/sunbeam/Desktop/Project_Naukri/project.csv')
    df=clean_data(df)
    return df

def clean_data(df):

    #dropping unused columns:
    df.drop(["jobdescription", "jobid","uniq_id","site_name"], axis = 1, inplace = True)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #Cleaning 'EXPERIENCE column'

    #df['experience']=df['experience'].fillna(value=0, inplace=True)
    df['experience']=df['experience'].str.replace('Not Mentioned','0')

    splitted_dataframe= df['experience'].str.split("-", n = 1, expand = True)
    maxsplitted_dataframe= df['experience'].str.split(" ", n = 1, expand = True)

    df['minExperience'] = splitted_dataframe[0]
    df['minExperience'] = pd.to_numeric(df['minExperience'], errors='coerce').fillna(0)
    df['minExperience']=df['minExperience'].astype('int')
    # print(df['minExperience'])
    # print(splitted_dataframe[1])

    df['maxExperience']=maxsplitted_dataframe[0]
    df['maxExperience'] = pd.to_numeric(df['maxExperience'], errors='coerce').fillna(0)
    df['maxExperience'] = df['maxExperience'].astype('int')
    df['avg_experience']= (df['minExperience'] + df['maxExperience'])/2
    #print(df['maxExperience'])
    df.drop(['experience'], axis=1, inplace=True)
    df.drop(["minExperience"], axis=1, inplace=True)
    df.drop(["maxExperience"], axis=1, inplace=True)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # values = {'industry': 'Other', 'skills': 'ANY'}
    # df.fillna(value=values)

    #df['industry']=df['industry'].fillna(, inplace = True)

    df['industry'].fillna(df['industry'].mode().values[0], inplace=True)
    # print(df['industry'].isnull().values.ravel().sum())
    #df['industry'] = pd.to_numeric(df['industry'], errors='coerce').fillna('OTHER')
    df['skills'].fillna(df['skills'].mode().values[0], inplace=True)
    # print(df['skills'])
    # print(df['skills'].isnull().values.ravel().sum())

    df['joblocation_address']=df['joblocation_address'].str.replace('View More','')




    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #cleaning 'joblocation_address' column
    df['numberofpositions'] = pd.to_numeric(df['numberofpositions'], errors='coerce').fillna(1)
    df['numberofpositions']=df['numberofpositions'].astype(int)
    #print(df['numberofpositions'])

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #cleaning 'DATE' column
    df['postdate'] = df['postdate'].apply(lambda x : pd.to_datetime(str(x)))
    df['postdate'] = df['postdate'].dt.date
    df['postdate']= pd.to_datetime(df['postdate'])
    # print(df['postdate'])
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #cleaning payrate: finding 'AVGERAGE-SALARY'
    # pay_split = df['payrate'].str[1:-1].str.split('-', expand=True)
    pay_split = df['payrate'].str.split('-', expand=True)
    pay_split.head()
    # remove space in left and right
    pay_split[0] = pay_split[0].str.strip()
    # remove comma
    pay_split[0] = pay_split[0].str.replace(',', '')
    # remove all character in two condition
    # 1 remove if only character
    # 2 if start in number remove after all character
    pay_split[0] = pay_split[0].str.replace(r'\D.*', '')
    # remove space in left and right
    pay_split[1] = pay_split[1].str.strip()
    # remove comma
    pay_split[1] = pay_split[1].str.replace(',', '')
    # print(pay_split[1].head())
    # remove all character in two condition
    # 1 remove if only character
    # 2 if start in number remove after all character
    pay_split[1] = pay_split[1].str.replace(r'\D.*', '')
    pay_split[0] = pd.to_numeric(pay_split[0], errors='coerce').fillna(0.0)
    pay_split[1] = pd.to_numeric(pay_split[1], errors='coerce').fillna(0.0)
    print(f"{pay_split[0]}:,{pay_split[1]}")
    df['salary'] = (pay_split[0] + pay_split[1])/2
    df.drop(['payrate'], axis=1, inplace=True)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #separating Education into Categories:
    return df
def education(df):
    d1 = []
    # df['education'].fillna(df['education'].mode().values[0], inplace=True)
    # df['education'].fillna(0, inplace=True)
    d = df['education'].str.replace("UG", '')
    d1 = d.str.replace("PG", '')
    d2 = d1.str.replace("Doctorate", '')
    d3 = d2.str.split(":", n=3, expand=True)

    pd.set_option('display.max_columns', 5)
    pd.set_option('display.max_rows', 4)
    pd.set_option('display.width', 1000)
    df['UG']=d3[1]
    print(df['UG'])
    df['PG']=d3[2]
    df['Doctorate']=d3[3]

    # df['UG']=df['UG'].replace(to_replace=["B.Tech/B.E.- AnySpecialization", " Any Graduate - Any Specialization"],value="1")

    #
    # for val in ug_uniq:
    #     df['UG']=df['UG'].replace(val,1)

    # df['UG']=df['UG'].replace('B.Tech/B.E.+','1',regex=True)
    # df['UG']=df['UG'].replace('Diploma.+','1',regex=True)
    df['Doctorate']=df['Doctorate'].str.replace(r' Not.+','0',regex=True)
    df['Doctorate'] = df['Doctorate'].str.replace(r'Any.+','1')

    df['UG'] = df['UG'].fillna(0)
    df['PG'] = df['PG'].fillna(0)
    df['Doctorate'] = df['Doctorate'].fillna(0)

    for index in range(len(df['UG'])):
        if df['UG'][index] != 0 :
            df['UG'][index] = 1
        # print(df['UG'][index])

    for index in range(len(df['PG'])):
        if df['PG'][index] != 0 :
            df['PG'][index] = 1
        # print(df['PG'][index])

    for index in range(len(df['Doctorate'])):
        if df['Doctorate'][index] != 0 :
            df['Doctorate'][index] = 1
    #print(ug_uniq)

    print(df['UG'])
    # df['UG']=df['UG'].fillna('NOT_MENTIONED', inplace = True)

    df.drop(["education"], axis=1, inplace=True)

    #=============================================================================================================
def location(df):
    location_list=[]
    new_list_uniq=[]
    new_set=set()
    loc = df['joblocation_address']
    location_list = loc.tolist()
    loc_list=[]
    count=0
    for l in location_list:
        if type(l)==str:
            loc_list=l.split(",")
            for i in loc_list:
                new_set.add(i.strip())
                count+=1
    print(new_set)
    print(count)

def loc(df):
    list1 = []
    for val in df['company']:
        list1.append(val)
    # print(list1)

    temp = defaultdict(lambda: len(temp))
    res = [temp[ele] for ele in list1]
    # print("The ids of original company is : " + list1)
    # print("The ids of assigned values is : " + res)
    df['company_id'] = res
    dict1 = {}
    for (val, i) in zip(df['company'], res):
        # print(f"{val}:{i}")
        dict1[val] = i
        df[id] = i
    print(type(df['joblocation_address']))

    reshaped = \
        (df.set_index(df.columns.drop('joblocation_address', 1).tolist())
             .joblocation_address.str.split(',', expand=True)
             .stack()
             .reset_index()
             .rename(columns={0: 'joblocation_address'})
             .loc[:, df.columns]
             )
    # pd.set_option('display.max_columns', 5)
    # pd.set_option('display.max_rows', 4)
    # pd.set_option('display.width', 1000)
    # print(reshaped)

    reshaped.to_csv('/home/sunbeam/Desktop/Project_Naukri/project_new_26_12_5.csv')
#===================================================================================
def file_to_csv(df):
    df.to_csv('/home/sunbeam/Desktop/Project_Naukri/project_new_24_12_2.csv')


# df.rename(columns={'joblocation_address': 'location'})
df=load_data()
# location(df)
loc(df)
education(df)
file_to_csv(df)