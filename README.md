# Description

## Django Employee Management System

The Django Employee Management System is a powerful web application designed to streamline the process of managing employee records within an organization. Built with Python Django, this system offers a comprehensive solution to efficiently handle various aspects of employee data.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python installed on your local machine.
- pip package manager installed.
  
# Cloning the Repository

You can clone this repository to your local machine using the following command:

```bash
git clone <repository_url>
cd <repository_name>
```

# Installation

To install Django

```bash
pip install django
```
To install Mysqlclient

```bash
pip install mysqlclient
```
Install Django and other dependencies from the requirements.txt file
   
# Configuration and Migration and MySQLClient Setup

In this Django application, we use environment variables for configuration and migration for managing and applying changes to the database schema and MySQLClient for database management.

## Configuration

For Accessing the Database

1. Prerequisites
MySQL Server installed on your system.
MySQL client to interact with the database (e.g., MySQL Workbench, phpMyAdmin, or MySQL command-line client).

Here's a link to the MySQL download page where you can find the appropriate installer for your operating system:

[MySQL Downloads](https://dev.mysql.com/downloads/)

2. Create Database: Once MySQL is installed, create a new database for the Django project. 

3. Update .env File: We utilize the `dotenv/load_dotenv` module to manage environment variables. In the root directory of the project, create a .env file and fill in the following fields with your MySQL database details: DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, and DB_NAME.

## Migration

1. Rename Table in Models: Open the models.py file in your Django app directory and change the table name as needed. For example, if you want to rename the Employee table to Staff, modify the class Meta section of your Employee model as follows:

```bash
$ class Meta:
    db_table = 'staff'
```    

2. Make Migrations: After configuring the database settings in the .env file, navigate to the root directory of your Django project and run the following command to create migrations based on the changes made to your models:

```bash
$ python manage.py makemigrations
```
3. Apply Migrations: Once the migrations are created, apply them to the database to update the schema:

```bash
$ python manage.py migrate
```
This command will create the necessary tables in the MySQL database based on the models defined in your models.py file.

## MySQLClient Setup

MySQLClient is configured to connect to a MySQL database. The configuration is specified in the `Employee_MS/Settings.py` file.

# For Running the Application

```bash
$ python manage.py runserver
```
Once the application is running, open your web browser.

Navigate to the following URL:

http://127.0.0.1:8000/
