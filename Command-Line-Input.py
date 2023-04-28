import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    user='root',
    password='Sumeethld*13',
    host='localhost',
    database='shlok',
    port=3306
)


cursor = conn.cursor()


# Display and get user's choice for which transaction to run
choice = int(input("Enter the transaction you want to execute:\n1. Insert a product\n2. Update price of all product by reducing them by 50%\n3. Update payment status of a specific payment type as paid in Payment_Portal\n4. Delete a Store with less than a specific no. of workers\n"))

# Executing user's transaction
try:
    cursor.execute("BEGIN")
    if choice == 1:
        # Prompt the user to enter the values for the new entry
        prod_id = input("Enter the Product ID: ")
        prod_name = input("Enter the Product Name: ")
        prod_type = input("Enter the Product Type: ")
        prod_price = input("Enter the Product Price: ")
        prod_stock = input("Enter the Product Stock: ")
        
        # Insert the new entry into the Products table
        cursor.execute(f"INSERT INTO Products VALUES ({prod_id}, '{prod_name}', '{prod_type}', {prod_price}, {prod_stock})")
        
    elif choice == 2:
        # Update the Products table
        cursor.execute("UPDATE Products SET Prod_price = Prod_price*0.5 WHERE Prod_Stock > 0")
        
    elif choice == 3:
        # Update the Payment_Portal table
        payment_type = input("Enter the Payment Type: ")
        cursor.execute(f"UPDATE Payment_Portal SET Payment_Status = 'PAID' WHERE Payment_Type = '{payment_type}'")
        
    elif choice == 4:
        # Delete data from the Store table
        num_workers = input("Enter the number of workers: ")
        cursor.execute(f"DELETE FROM Store WHERE Num_Workers < {num_workers}")
        
    else:
        print("Invalid transaction number entered. Please enter a valid transaction number.")
        cursor.close()
        conn.close()
        exit()
        
    conn.commit()
    print("Transaction successfully completed!")
    
except mysql.connector.Error as error:
    # Rollback transaction in case of an error
    print("Transaction rolled back due to error:", error)
    conn.rollback()

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
