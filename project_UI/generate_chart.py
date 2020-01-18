import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def load_data():
    path = './final_clean_csv.csv'
    df=pd.read_csv(path)
    # print(df.head())
    return df

def company_cont_plot(df):
    df['company'].value_counts().head(10)
    plt.title('company count')
    plt.xlabel('company')
    plt.ylabel('count')
    df['company'].value_counts().head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='green')
    # return plt.show()
    plt.savefig('static/company.png')

def jobtittle_plot(df):
    df['jobtitle'].value_counts().head(10)
    plt.title('job tittle count')
    plt.xlabel('job tittle')
    plt.ylabel('count')
    df['jobtitle'].value_counts().head(10).plot(kind='bar', figsize=(15, 10), legend=True, fontsize=12,color='green')
    # return plt.show()
    plt.savefig('static/jobtitle.png')

def industry_based_plot(df):
    df['industry'].value_counts().head(10)
    plt.title('industry count')
    plt.xlabel('industry')
    plt.ylabel('count')
    df['industry'].value_counts().head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12)
    # return plt.show()
    # for val in df['industry']:
    #      print(f"{val}:{df['industry'].value_counts()}")
    plt.savefig('static/industry.png')


# def industry_based_plot(df):
#     import matplotlib.pyplot as plt
#     v = df['industry'].value_counts()
#     plt.title('industry count')
#     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#     #print(v)
#     plt.xlabel('industry',rotation=0)
#     plt.ylabel('count')
#     v.head(10).plot(kind='barh',legend=True, figsize=(10,7),color="coral", fontsize=13)
#
#     list=[]
#
#     for p in v:
#         list.append(p)
#
#     for i, z in enumerate(list):
#         plt.text(z+3, i+.25, str(z), color='blue', fontweight='bold')
#     plt.savefig('static/industry.png')




# def location_wise_job(df):
#     replacements = {
#         'joblocation_address': {
#             r'(Bengaluru/Bangalore)': 'Bangalore',
#             r'Bengaluru': 'Bangalore',
#             r'Hyderabad / Secunderabad': 'Hyderabad',
#             r'Mumbai , Mumbai': 'Mumbai',
#             r'Noida': 'NCR',
#             r'Delhi': 'NCR',
#             r'Gurgaon': 'NCR',
#             r'Delhi/NCR(National Capital Region)': 'NCR',
#             r'Delhi , Delhi': 'NCR',
#             r'Noida , Noida/Greater Noida': 'NCR',
#             r'Ghaziabad': 'NCR',
#             r'Delhi/NCR(National Capital Region) , Gurgaon': 'NCR',
#             r'NCR , NCR': 'NCR',
#             r'NCR/NCR(National Capital Region)': 'NCR',
#             r'NCR , NCR/Greater NCR': 'NCR',
#             r'NCR/NCR(National Capital Region) , NCR': 'NCR',
#             r'NCR , NCR/NCR(National Capital Region)': 'NCR',
#             r'Bangalore , Bangalore / Bangalore': 'Bangalore',
#             r'Bangalore , karnataka': 'Bangalore',
#             r'NCR/NCR(National Capital Region)': 'NCR',
#             r'NCR/Greater NCR': 'NCR',
#             r'NCR/NCR(National Capital Region) , NCR': 'NCR'
#
#         }
#         }
#     df.replace(replacements, regex=True, inplace=True)
#     y = df['joblocation_address'].value_counts()
#     print("count  :",y)
#     plt.title(' most_job_posting_city')
#     plt.xlabel('location')
#     plt.ylabel('count')
#     most_job_posting_city=df['joblocation_address'].value_counts().head()
#     most_job_posting_city.plot(kind = 'bar',figsize=(15, 10), legend=True, fontsize=12)
#     return plt.plot

def industry_wise_salary(df):
    plt.title(' industry_wise_min_pay')
    plt.xlabel('industry')
    plt.ylabel('salary')
    df[['salary', 'industry']].groupby(["industry"]).median().sort_values(by='salary', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='lightgreen')
    return plt.show()
#================================================================================================================================

def jobtittle_wise_salary(df):
    plt.title(' jobtittle_wise_min_pay')
    plt.xlabel('jobtittle')
    plt.ylabel('salary')
    df[['salary', 'jobtitle']].groupby(["jobtitle"]).median().sort_values(by='salary', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='lightgreen')
    return plt.show()

#======================================================================================================================================

def skill_wise_salary(df):
    plt.title(' skill_wise_min_pay')
    plt.xlabel('skills')
    plt.ylabel('salary')
    df[['salary', 'skill']].groupby(["skills"]).median().sort_values(by='salary', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='lightgreen')
    return plt.show()

#================================================================================================================================

def skill_plot(df):
    df['skills'].value_counts().head(10)
    plt.title('skill count')
    plt.xlabel('skills')
    plt.ylabel('count')
    df['skills'].value_counts().head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12)
    plt.legend()
    return plt.show()

#=====================================================================================================
# def industry_wise_max_pay(df):
#     plt.title(' industry_wise_max_pay')
#     plt.xlabel('industry')
#     plt.ylabel('max_pay')
#     df[['max_pay', 'industry']].groupby(["industry"]).median().sort_values(by='max_pay', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='lightblue')
#     return plt.show()


#================================================================================================================================
#
#
# def skill_wise_max_pay(df):
#     plt.title(' skill_wise_max_pay')
#     plt.xlabel('skill')
#     plt.ylabel('max_pay')
#     df[['max_pay', 'skill']].groupby(["skill"]).median().sort_values(by='max_pay', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='lightblue')
#     return plt.show()




#================================================================================================================================
#
#
# def jobtittle_wise_max_pay(df):
#     plt.title(' jobtittle_wise_max_pay')
#     plt.xlabel('jobtittle')
#     plt.ylabel('max_pay')
#     df[['max_pay', 'jibtittle']].groupby(["jibtittle"]).median().sort_values(by='max_pay', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='lightblue')
#     return plt.show()

#================================================================================================================================
#
#
# def skill_wise_avg_pay(df):
#     plt.title(' skill_wise_avg_pay')
#     plt.xlabel('skill')
#     plt.ylabel('agv_pay')
#     df[['avg_pay', 'skills']].groupby(["skills"]).median().sort_values(by='avg_pay', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='blue')
#     return plt.show()
#

#================================================================================================================================
#
#
# def jobtittle_wise_avg_pay(df):
#     plt.title(' jobtittle_wise_avg_pay')
#     plt.xlabel('jobtittle')
#     plt.ylabel('agv_pay')
#     df[['avg_pay', 'jobtitle']].groupby(["jobtitle"]).median().sort_values(by='avg_pay', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='y')
#     return plt.show()


#================================================================================================================================
#
#
# def industry_wise_avg_pay(df):
#     plt.title(' industry_wise_avg_pay')
#     plt.xlabel('industry')
#     plt.ylabel('agv_pay')
#     df[['avg_pay', 'industry']].groupby(["industry"]).median().sort_values(by='avg_pay', ascending=False).head(10).plot(kind='bar',figsize=(15, 10), legend=True, fontsize=12,color='y')
#     return plt.show()

df = load_data()
company_cont_plot(df)
jobtittle_plot(df)
industry_based_plot(df)
# skill_plot(df)
# industry_wise_min_pay(df)
# industry_wise_max_pay(df)
# industry_wise_avg_pay(df)
# skill_wise_min_pay(df)
# skill_wise_max_pay(df)
# skill_wise_avg_pay(df)
# jobtittle_wise_min_pay(df)
# jobtittle_wise_max_pay(df)
# jobtittle_wise_avg_pay(df)
# location_wise_job(df)