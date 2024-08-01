# Book-Store-Management-System

This script is designed to manage a bookstore's inventory, sales, and user authentication using MySQL. The main functionalities include user signup, login, selling books, managing stock, and viewing total sales.

Prerequisites
Python 3.x
MySQL Server
MySQL Connector for Python
Installation
Install MySQL Server: Follow the instructions for your operating system to install MySQL Server.

Install MySQL Connector:

sh
Copy code
pip install mysql-connector-python
Setup
Database and Table Creation:
The script automatically creates a database named store if it doesn't exist.
It also creates three tables: signup, Available_Books, and Sales if they don't exist.
How to Run
Run the Script:

sh
Copy code
python bookstore_management.py
User Menu:
Upon running the script, you will be presented with the following menu:

makefile
Copy code
1: Signup
2: Login
3: Exit
Signup: Create a new user account.
Login: Log in with an existing user account.
Exit: Exit the application.
After Login:
Upon successful login, you will see the following menu:

markdown
Copy code
1. Sell
2. Stock
3. Total Sales
4. Exit
Features
1. Signup
Prompts the user to enter a username and password.
Inserts the new user's credentials into the signup table.
2. Login
Prompts the user to enter a username.
Checks if the username exists in the signup table.
Prompts for a password and verifies it.
Upon successful login, presents the main menu.
3. Sell
Prompts for customer name, phone number, book ID, book name, quantity, and price.
Checks if the requested quantity is available in the inventory.
Updates the inventory and inserts the sale record into the Sales table.
4. Stock
View: Displays all books in the inventory.
Modify: Allows adding or subtracting stock for a specific book.
5. Total Sales
Displays all sales records.
Exit
Allows the user to exit to the login menu or exit the application completely.
Database Schema
signup Table
Column Name	Data Type
username	VARCHAR(20)
password	VARCHAR(20)
Available_Books Table
Column Name	Data Type	Constraints
Bookid	VARCHAR(10)	PRIMARY KEY
BookName	VARCHAR(30)	
Genre	VARCHAR(20)	
Quantity	INT(3)	
Author	VARCHAR(20)	
Publication	VARCHAR(30)	
Price	INT(7)	
Sales Table
Column Name	Data Type	Constraints
CustomerName	VARCHAR(20)	
PhoneNumber	CHAR(10)	UNIQUE KEY
Bookid	VARCHAR(10)	FOREIGN KEY (Bookid) REFERENCES Available_Books(Bookid)
BookName	VARCHAR(30)	
Quantity	INT(100)	
Price	INT(7)	
Make sure to have MySQL running and accessible with the provided credentials before running the script. Adjust the connection parameters (host, user, password) as needed.

Happy managing your bookstore!
