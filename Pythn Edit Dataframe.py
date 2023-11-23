## Code to connect to postgresql database dvdrental on localhost        
import psycopg2
import pandas as pd     
from sqlalchemy import create_engine    

# Connect to the database    
conn = psycopg2.connect(
    host="localhost",
    database="dvdrental",
    user="postgres",
    password="password"
)

# Create a cursor object    

cur = conn.cursor() 

# Execute a query
cur.execute("select * from actor")
            
#fetch the query output in dataframe

dfTest = pd.DataFrame(cur.fetchall())

#print the dataframe  

print(dfTest)

"""
Gave the  dataframe a name same as table's columns
"""

dfTest.columns = ['actor_id', 'first_name', 'last_name', 'last_update']


