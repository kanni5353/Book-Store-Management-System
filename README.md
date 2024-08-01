# Book Store Management System

This project is a Book Store Management System developed using Python and MySQL. It provides functionalities for user signup, login, managing book sales, and tracking stock and sales.

## Overview

The Book Store Management System is designed to help manage the operations of a book store. It includes features for user authentication, managing book inventory, recording sales transactions, and viewing sales records.

## Features

- **User Signup and Login:** Allows new users to sign up and existing users to log in securely.
- **Manage Book Sales:** Facilitates the recording of book sales, including customer details and the books sold.
- **View and Modify Stock:** Enables viewing and updating the inventory of available books.
- **Track Total Sales:** Provides a summary of all sales transactions.

## Requirements

- Python 3.x
- MySQL Connector for Python

## Installation

1. **Install MySQL Connector for Python:**
    ```bash
    pip install mysql-connector-python
    ```

2. **Set up the MySQL database and tables:**
    Run the provided Python script to create the necessary database and tables.

## Usage

1. **Run the main script to start the application:**
    - The application will prompt the user to sign up, log in, or exit.
    - Upon successful login, users can manage book sales, view and modify stock, and track total sales.

## Detailed Functionality

### User Signup and Login

- **Signup:** Users can create a new account by providing a username and password.
- **Login:** Existing users can log in by entering their username and password. The system validates the credentials and grants access if they are correct.

### Manage Book Sales

- **Sell Books:** Users can record sales transactions by entering customer details and the books sold. The system updates the inventory accordingly.

### View and Modify Stock

- **View Stock:** Users can view the current inventory of books, including details such as book ID, name, genre, author, publication, quantity, and price.
- **Modify Stock:** Users can update the inventory by adding or removing books.

### Track Total Sales

- **View Sales Records:** Users can view a summary of all sales transactions, including customer details and the books sold.
