import snowflake.connector


# Create a connection object
conn = snowflake.connector.connect(
    user='VENOM',
    password='123456789@aA',
    account='ofdxezx-lr56952',
    warehouse='COMPUTE_WH',
    database='department',
    schema='public'
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

# # Close the cursor and connection
cur.close()
conn.close()