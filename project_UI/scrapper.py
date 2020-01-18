from selenium import webdriver
import numpy as np
import pandas as pd
import csv

# To get The Browser
browser = webdriver.Chrome()

# get the path of the website here
path = 'https://www.naukri.com/jobs-in-india'
browser.get(path)

# to count how many pages are thier in our site at specific time
count = browser.find_element_by_class_name('count')
tot_pages = round(int(count.text.split(sep=' ')[2]) / 50)
# print(tot_pages)

cols = ['company','title', 'experience', 'skills',
        'salary', 'location', 'date','job_opening','cand_applied','qualification']
cols_skill=['company','rating','review','Role','IndustryType','Functional_Area',
            'EmploymentType','RoleCategory','location']
# df = pd.DataFrame(columns=cols)
# df_skill=pd.DataFrame(columns=cols_skill)
with open('/home/sunbeam/JOB.csv', 'w', newline='') as csvfile:
    testwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    testwriter.writerow(cols)

with open('/home/sunbeam/SKILL.csv', 'w', newline='') as csvfile:
    skillwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    skillwriter.writerow(cols_skill)
cnt = 1
temp = []
temp_skill = []
# while(cnt<tot_pages):
while (cnt <= 2):
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
    def fun():
        # cols = ['company','title', 'experience', 'skills',
        #         'salary', 'location', 'date','job_opening', 'cand_applied','qualification']
        # cols_skill=['company','role']
        # df = pd.DataFrame(columns=cols)
        # df_skill = pd.DataFrame(columns=cols_skill)

        # temp = []
        header = 1
        urls = browser.find_elements_by_id('jdUrl')
        print(urls)

        list1 = []
        for u in urls:
            # print(u)
            list1.append(u.get_attribute('href'))
        for link in list1:
            try:
                browser.get(link)
            #=================================================================================
            #adding company in 'temp'
                try:
                    company_review_rating=browser.find_element_by_class_name('jd-header-comp-name')
                    company=company_review_rating.find_element_by_class_name('pad-rt-8')
                    temp.append(company.text)
                    temp_skill.append(company.text)
                    try:
                        rating_rev=[]
                        new_tag=company_review_rating.find_elements_by_tag_name('span')
                        for t in new_tag:
                            rating_rev.append(t.text)

                        rating=rating_rev[0]
                        print(rating)
                        review=rating_rev[1]
                        print(review)
                        # rating = company_review_rating.find_element_by_class_name('amb-rating pad-rt-4')
                        temp_skill.append(rating)
                        browser.implicitly_wait(2)
                        # reviewCount=company_review_rating.find_element_by_class_name('amb-reviews pad-rt-4')
                        temp_skill.append(review)
                        browser.implicitly_wait(2)
                    except:
                        temp_skill.append(None)
                        temp_skill.append(None)
                except:
                    continue
                    # temp.append(None)
            # adding role
                try:
                    # bad_chars ="role,"
                    role = []
                    all_tag = browser.find_element_by_class_name('other-details')
                    all = all_tag.find_elements_by_class_name('details')

                    # for i in bad_chars:
                    #     test_string = test_string.str.replace(i, '')

                    for a in all:
                        role.append(a.text)

                    Role=role[0]
                    IndustryType=role[1]
                    Functional_Area=role[2]
                    EmploymentType=role[3]
                    RoleCategory=role[4]
                    temp_skill.append(Role)
                    temp_skill.append(IndustryType)
                    browser.implicitly_wait(2)
                    temp_skill.append(Functional_Area)
                    temp_skill.append(EmploymentType)
                    browser.implicitly_wait(2)
                    temp_skill.append(RoleCategory)
                except:
                    temp_skill.append(None)
                    temp_skill.append(None)
                    temp_skill.append(None)
                    temp_skill.append(None)
                    temp_skill.append(None)

            #adding title in 'temp'
                try:
                    title = browser.find_element_by_class_name('jd-header-title')
                    #print(title.text)
                    temp.append(title.text)
                    browser.implicitly_wait(2)
                except:
                    #title = None
                    temp.append(None)
                    #print(title)

            #adding experience
                try:
                    exp = browser.find_element_by_class_name('exp')
                    temp.append(exp.text)
                    #print("Experience : ", exp.text)
                    browser.implicitly_wait(2)
                except:
                    exp = None
                    print("Experience : ", exp)
                    temp.append(0)

            #adding skill
                try:
                    skills = browser.find_element_by_class_name('key-skill')
                    skill_list = skills.find_elements_by_tag_name('span')

                    skl = []
                    for skill in skill_list:
                        skl.append(skill.text)
                    #print('skills', skl)
                    temp.append(skl)
                    browser.implicitly_wait(2)
                except:
                    skill = None
                    #print('skills', skill)
                    temp.append(None)

            #adding salary:
                try:
                    salary = browser.find_element_by_class_name('salary')
                    #print("salary:", salary.text)
                    temp.append(salary.text)
                    browser.implicitly_wait(2)
                except:
                    salary = None
                    #print("salary:", salary)
                    temp.append(None)

            #adding location
                try:
                    location = browser.find_element_by_class_name('loc')
                    #print("location :", location.text)
                    temp.append(location.text)
                    temp_skill.append(location.text)
                    browser.implicitly_wait(2)
                except:
                    location = None
                    #print("location :", location)
                    temp.append(None)
                    temp_skill.append(None)

            #Adding date posted
                try:
                    post = []
                    time = browser.find_element_by_class_name('jd-stats')
                    post_dates = time.find_elements_by_tag_name('span')
                    for post_date in post_dates:
                        post.append(post_date.text)
                        # print(post)
                    date = []
                    date = post[1].split(sep=' ')
                    job_opening = int(post[3])
                    cand_applied= int(post[5])
                    #print(f"date:{date[0]},job:{job_opening}")
                    temp.append(int(date[0]))
                    temp.append(job_opening)
                    temp.append(cand_applied)
                    #
                    # for i in range(len(temp)):
                    #     print("Test {d}: ".format(d=i), temp[i], type(temp[i]))
                    browser.implicitly_wait(2)
                except:
                    temp.append(None)
                    temp.append(1)
                    temp.append(0)
                    #job_opening = 'NA'
                    #print(date, job_opening)

            #adding qualification
                try:
                    education = browser.find_element_by_class_name('education')
                    qualification = education.find_element_by_class_name("details")
                    #label=qualification.find_elements_by_tag_name('label')
                    qual=education.find_elements_by_tag_name('span')
                    #label_list=[]
                    qual_list = []

                    for q in qual:
                        qual_list.append(q.text)
                        # if(qual_list.size() > 0):
                    UG=qual_list[0]
                    PG=qual_list[1]
                    Doctorate=qual_list[2]

                    # print("qualification :",UG)
                    temp.append(qual_list)
                    browser.implicitly_wait(2)
                except:
                    qualification = None
                    #print("qualifiaction :", qualification)
                    #temp.append(None)
#=======================================================================================
            except:
                print("Not Found-Error")
            try:#making csv
                #csv for all fields
                with open('/home/sunbeam/JOB.csv', 'a', newline='') as csvfile:
                    testwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    testwriter.writerow(temp)
                # csv for skills
                with open('/home/sunbeam/SKILL.csv', 'a', newline='') as csvfile:
                    skillwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    skillwriter.writerow(temp_skill)
                temp.clear()
                temp_skill.clear()
            except ValueError:
                temp.clear()
                temp_skill.clear()
                continue
#===============================================================================
                # df.append(pd.Series(temp, index=cols), ignore_index=True)
                # df_skill.append(pd.Series(temp_skill, index=cols_skill), ignore_index=True)
                #
                # df.to_csv('/tmp/test.csv')
                # df_skill.to_csv('/tmp/skill.csv')
                        # print('\n' * 10)
                        # print(df)
#===============================================================================
      # navigate to link
    print(f"Page {cnt} done SUCCESSFULLY ")
    next = browser.find_element_by_class_name("pagination")
    cnt += 1
    txt = browser.find_element_by_class_name('grayBtn').text

    if (txt == 'Next'):#for first page having only NEXT button for next page navigation
        p = next.find_element_by_tag_name('a')
        path1 = p.get_attribute('href')
        print(path1)
    else:#for both buttons i.e. PREVIOUS and NEXT button
        li = []
        p = next.find_elements_by_tag_name('a')
        #print(p)
        path1 = p[1].get_attribute('href')
        print(path1)
    fun()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    browser.get(path1)
print(cnt)
browser.close()