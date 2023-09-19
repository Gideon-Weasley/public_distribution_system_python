import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
    print()
    dbpass=input('Enter password for database :')
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password=dbpass)
    database_create='create database if not exists ration'
    table_create='create table if not exists consumer(Rationno int,Name varchar(20),Phonenumber varchar(15),Status char(3),Gender varchar(6))'  
    mySql_insert_query = """INSERT INTO consumer (Rationno, Name, Phonenumber, Status,Gender ) 
                           VALUES 
                           (1023, 'Ramesh Govind','9164645912', 'BPL',"Male"),(2013, 'Suresh Unnikrishnan','7564324132', 'BPL',"Male"),(2133, 'Manoj Prabhakaran', '7459085231', 'BPL', 'Male'),(1098, 'Mohammed Shamil','9863424527','APL','Male'),(3251,'Sharon Cherupushpam','9069785142','BPL','N/A'),(2098,'Smirth Vijaybhaskar','7653490721','APL','Male'),(4056,'Rajat Sreeraj','7843965471','APL','Male'),(9834,'Christy Binson','9069384561','BPL','Female'),(3897,'Subitha Pramod','9123485290','APL','Female'),(4789,'Nakshatra Gopi','7035703421','APL','Female'),(8937,'Gauri Ramakrisnan','7534610982','BPL','Female')  """

    cursor = connection.cursor()
    cursor.execute(database_create)
    cursor.execute('use ration')
    cursor.execute(table_create)
    unique_query='alter table consumer add constraint rationno unique (Rationno)'
    cursor.execute(unique_query)
    cursor.execute(mySql_insert_query)
    connection.commit()
    #print(cursor.rowcount, "Records inserted successfully into consumer table")
    cursor.close()

except mysql.connector.Error as error:
    print()
    #print("Failed to insert record into consumer table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()        
        #print("MySQL connection is closed")
import sys
db=mysql.connector.connect(host='localhost',user='root',passwd=dbpass,database='Ration')
if db.is_connected()==False:
    sys.exit()
mycurs=db.cursor()
mycurs.execute("CREATE TABLE IF NOT EXISTS PRODUCT (P_NO INT(3) PRIMARY KEY,P_NAME VARCHAR(20) UNIQUE,STOCK_LEFT INTEGER NOT NULL,PRICE_APL FLOAT(6,2) NOT NULL,PRICE_BPL FLOAT(6,2) NOT NULL,SUPPLY_PERMONTH INTEGER)") 
mycurs.execute("SELECT* FROM PRODUCT")
rec=mycurs.fetchall()
if rec==[]:
    mycurs.execute("INSERT INTO PRODUCT VALUES(001,'Rice',200,10.00,3.00,10)")
    mycurs.execute("INSERT INTO PRODUCT VALUES(002,'Sugar',125,8.50,13.50,2)")
    mycurs.execute("INSERT INTO PRODUCT VALUES(003,'Wheat',224,5.00,8.50,6)")
    mycurs.execute("INSERT INTO PRODUCT VALUES(004,'Kerosene',150,13.60,17.40,1)")
    mycurs.execute("INSERT INTO PRODUCT VALUES(005,'Atta flour',100,30.00,40.00,3)")
    mycurs.execute("INSERT INTO PRODUCT VALUES(006,'Toor dal',100,15.00,20.00,1)")
    mycurs.execute("INSERT INTO PRODUCT VALUES(007,'Urid dal',100,15.00,20.00,1)")
    db.commit()
    
