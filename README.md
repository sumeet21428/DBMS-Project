# DBMS-Project
An e2e based database application for a dairy product company, as part of our DBMS course project.
![Screenshot](Screenshot%202023-05-29%20at%207.33.01%20PM.png)

### Shlok Vinodkumar Mehroliya (2021421) 
### Sumeet Mehra (2021428)

Dairy Product Management System

## Project Scope:
In this project we are designing and developing an e2e db application for
the dairy company IDA(Indian Dairy Authority)which will be used for various
purposes including but not limited to inventory management,serializing and
categorizing products and managing the company sales dynamically while
also giving them notifications if a product is going out of stock,is out of
stock or is being procured by customers at a rapid pace as the interface is
being used.We hope to create a experience through which both the user
gets a smooth ride through the website and one where the company is able
to manage their products with ease1

## TECHSTACK:
### Front End:
We will be using DJANGO for the front end of our program to create a
smooth GUI for our customers

### Middleware:
We will be using a python-sql connecter to help join both
python-Django(running queries and GUI)and mysql(will contain the
database)

### BackEnd:
MySql,Python,Django

## Technical Requirements:

1. Customer can only view and purchase products and cannot add or
remove products
2. Vendor can't add negative items to a store
3. Vendors cannot have access to private information like user login
password
4. One product can only belong to one category
5. Users can only browser and purchase products after logging in/
signing up with the correct information
6. Users need to provide an accurate delivery address in order to place
order
7. There cannot be multiple email addresses/ phone numbers linked to
one account
8. Once purchased, user cannot cancel an order

## Function Requirements:

### Backend:
For our backend we will be using Mysql for the database and python to run
queries:
This will include but not be limited to:
● Signing up(Customer)
● Logging in(Customer and Company)
● Adding new products to the product catalog (only company can add
products, not the customer)
● Adding new Categories (if and when required)
● Running queries to single out different categories and products
● Storing database in a standard format for easy access and running
queries

### MiddleWare:
We will be using python-sql connector to merge databases with python to
run queries and also use an interactive GUI to make customers' experience
smoother.

### Front End:
For Front End we would like to,
● Making an interactive user interface
● Using login feature to verify users or for staff to do inventory
management
● Display products in a desirable way for customers to purchase
● Make receipts and also show when stock for certain product is
increasing or decreasing
● Procure receipts for purchases after the purchase has been fully
processed
● Making different pages for different category products or different
requirements from each page. One products can be in different
categories.

