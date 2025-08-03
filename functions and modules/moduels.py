import pandas as pd 
import schedule
import time 
import pyodbc
#connect with microsoft_SQL_Server
conn= pyodbc.connect('driver={ODBC Driver 17 for SQL Server};'
                     'server=DESKTOP-MN97FD4;'
                     'database=ITI;'
                     'trusted_connection=yes'
                     )

query = 'select * from student'
df=pd.read_sql(query,conn)
# data preprocessing 
df['full_name']=(df['St_Fname']+' '+ df['St_Lname'])
df=df.drop(['St_Fname','St_Lname'],axis=1)
df=(df[df['St_Id']!=120])

df['full_name']=df['full_name'].fillna('unknown').str.strip()
df['St_Age']=df['St_Age'].fillna(0)
df['full_name']=df['full_name'].fillna('unknown').str.strip()

df=df[['St_Id','full_name','St_Address','St_Age','Dept_Id','St_super']]

#load data into data_warehouse 
conn_2= pyodbc.connect('driver={ODBC Driver 17 for SQL Server};'
                     'server=DESKTOP-MN97FD4;'
                     'database=ITI_DWH;'
                     'trusted_connection=yes'
                     )
cursor=conn_2.cursor()


try:

    for i, row in df.iterrows():
        try:
            cursor.execute(
                '''INSERT INTO STUDENT_INFO (id, student_name, address, age, dept_id, st_super)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (
                    int(row['St_Id']) if pd.notna(row['St_Id']) else None,
                    row['full_name'],
                    row['St_Address'],
                    int(row['St_Age']) if pd.notna(row['St_Age']) else None,
                    int(row['Dept_Id']) if pd.notna(row['Dept_Id']) else None,
                    int(row['St_super']) if pd.notna(row['St_super']) else None
                )
            )
        except Exception as e:
            print(f" Error inserting row {i}: {e}")
    conn_2.commit()
except Exception as e:
    print(f" Error connecting to database or running the script: {e}") 

