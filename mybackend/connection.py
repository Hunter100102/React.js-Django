import pyodbc

server = 'mydatabase.c3oaikac2rh2.us-east-2.rds.amazonaws.com'
database = 'mydatabase'
username = 'admin'
password = 'Reaper100102!'
driver = '{ODBC Driver 18 for SQL Server}'

try:
    connection = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
