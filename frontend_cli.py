import mysql.connector
conn = mysql.connector.connect(user = 'root', password = "Sumeethld*13", host = "localhost", database = "shlok", port = 3306)
cursor = conn.cursor()

while True:
    print("Following are the SQL queies: ")
    print("1. TO GET ALL NAMES AND STOCK OF PRODUCTS WHOSE STOCK IS >50: select Prod_Name,Prod_Stock from Products where Prod_Stock>50 group by Prod_Name,Prod_Stock;")
    print("2. TO GROUP THE PRODUCTS BY NAME AND THEN CALCULATE THE TOTAL STOCK AND AVERAGE PRICE OF EACH PRODUCT: SELECT Prod_Name, SUM(Prod_Stock) AS Total_Stock, AVG(Prod_Price) AS AvgPrice FROM Products GROUP BY Prod_Name;")
    print("3. TO SHOW THE TOTAL NUMBER OF UNIQUE CUSTOMERS, CONTACT NUMBERS AND ADDRESSES ASSOCIATED WITH EACH NAME: SELECT C_Name,  COUNT(DISTINCT C_ID) AS Num_Customers, COUNT(DISTINCT Contact_Num) AS Num_Contacts, COUNT(DISTINCT Address) AS Num_Addresses FROM  Customer_F GROUP BY  C_Name;")
    print("4. TO SHOW THE NUMBER OF UNIQUE EMPLOYEES IN THE SYSTEM AS WELL AS THE AVG, MIN AND MAX SALARIES FOR ALL EMPLOYEES: SELECT  COUNT(DISTINCT E_ID) AS Num_Employees,  AVG(Salary) AS Avg_Salary,  MIN(Salary) AS Min_Salary,  MAX(Salary) AS Max_Salary  FROM  Employees")
    print("Enter the query you want to run")
    i = input()
    if(i==0):
        break
    else:
        try:
            cursor.execute(i)
            res = cursor.fetchall()
            for i in res:
                print(i)
        except Exception as e:
            print("Error!!: ", e)

cursor.close()
conn.close()


    