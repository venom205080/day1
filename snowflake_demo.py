import snowflake.connector
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas


# Create a connection object
conn = snowflake.connector.connect(
    user='VENOM',
    password='123456789@aA',
    account='ofdxezx-lr56952',
    warehouse='COMPUTE_WH',
    database='DEPARTMENT',
    schema='MY_SCHEMA'
)


# Create a cursor object
cur = conn.cursor()

# # Execute a query

cur.execute("CREATE OR REPLACE DATABASE DEPARTMENT")
cur.execute("CREATE OR REPLACE SCHEMA MY_SCHEMA")
cur.execute("CREATE OR REPLACE TABLE EMPLOYEE(ID NUMBER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(25), DEPARTMENT VARCHAR(25))")
cur.execute("INSERT INTO EMPLOYEE VALUES(101, 'RAM', 'LOGISTICS'), (102, 'SHYAM', 'LOGISTICS'), (103, 'MOHAN', 'ADMINISTRATION')")
cur.execute("SELECT * FROM EMPLOYEE")

results = cur.fetchall()

# Print the results
for row in results:
    print(row)
    
    
#--------- extracting data from snowflake to pandas dataframe----------
# 1 . fetch pandas all
# query = "SELECT * FROM EMPLOYEE"
# cur.execute(query)
# emp_df = cur.fetch_pandas_all()
# print(emp_df.head(2))

# 2. fetch pandas batches-->fetches the data row by row 
# for df in cur.fetch_pandas_batches():
#     print(df)

# ----------Writes a pandas DataFrame to a table in a Snowflake database.----------
##note: you might have to use double quote in table name while querying data from dataframe to snowflake 
##explanation -  perhaps the reason for that is that snowflake by default stores table or database or schema name in upper case , so if you name your table/db/schema upper case then you need not to use double quotes but if you give in lower case then you may have to use double quotes with your table or db or schema names.

# Mobile_Price_Prediction_df = pd.read_csv('Mobile-Price-Prediction-cleaned_data.csv')
# # print(salary.columns)
# write_pandas(conn, Mobile_Price_Prediction_df, table_name="mob_price_pred", auto_create_table=True)
# query = 'SELECT * FROM "mob_price_pred"'    #<------ see here we have to use double quotes with table name
# cur.execute(query)
# df = cur.fetch_pandas_all()
# print(df)



# df = pd.DataFrame([('Mark', 10), ('Luke', 20)], columns=['name', 'balance'])
# print(df.columns)
# write_pandas(conn, df, 'customers', auto_create_table=True)
# # Close the cursor and connection
cur.close()
conn.close()