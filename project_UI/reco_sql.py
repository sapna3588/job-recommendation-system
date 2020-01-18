
import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="dbda", passwd="dbda", database="project")

# creating the cursor object
cur = myconn.cursor()

try:
    # Creating a table with name Employee having four columns i.e., name, id, salary, and department id
    dbs = cur.execute(
        "select company,jobtitle,count(numberofpositions) as Openings from file_path where industry='IT-Software / Software Services' AND joblocation_address='Bengaluru' AND skills='ITES' OR avg_experienvce=1 group by company,jobtitle")
except:
    myconn.rollback()

myconn.close()
