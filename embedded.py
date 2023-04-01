
# import pymysql
import mysql.connector

# Connect to the database
i = mysql.connector.connect(host='localhost', user='root', port="3306", password='Sumeethld*13', db='shlok')

while True:
    print("Select the query you want to run : \n Press 1 for - Query to retrieve all columns from the Store table where no. of workers is greater than or equal to 100, less than 150, and store id is greater than 150.\n Press 2 for - Query to retrieve the number of payments made for each unique combination of Payment_Status and Payment_Type in the Payment_Portal table")
    x = int(input())
    if(x==1):

        #Embedded Query 1

        # create a cursor object
        cursor = i.cursor()

        # execute the embedded SQL query
        cursor.execute("SELECT * FROM Store WHERE Num_Workers >= %s AND Num_Workers < %s AND S_ID > %s", (100, 150, 150))

        # fetch the query results
        res = cursor.fetchall()

        # print the results
        for row in res:
            print(row)

        # close the database connection
        i.close()
        
    elif(x==2):
        #Embedded Query 2

        # create a cursor object
        cursor = i.cursor()

        # execute the embedded SQL query
        cursor.execute("SELECT * FROM Store WHERE Num_Workers >= %s AND Num_Workers < %s AND S_ID > %s", (100, 150, 150))

        # fetch the query results
        res = cursor.fetchall()

        # print the results
        for row in res:
            print(row)

        # close the database connection
        i.close()

    else:
        print("enter only 1 or 2, try again!!!")



