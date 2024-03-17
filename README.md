# **Database Interaction with PostgreSQL and Python**

#### This  is a Python application designed to interact with a PostgreSQL database for managing student records. It supports basic CRUD (Create, Read, Update, Delete) operations on student data, including adding new students, displaying all student records, updating student emails, and deleting students.

###### **Manal Hassan - 101263813**


## Requirenments 
Ensure you have the following installed
- Python 3.x
- PostgreSQL

## Application Set up
- **Clone Repo to local machine**
  - ```git clone https://github.com/manall1/a3-comp-3005.git```
- **Install psycopg2 from the terminal**
  - ```pip3 install psycopg2-binary```

## Database Set up
- **Create and name a database using pgAdmin (or PostgreSQL command line)**
  - In the browser panel on the left, right-click on Databases and select Create > Database
  - Name the new database "School" and click Save (Note you can name whatever you want)
- **Run the SQL commands in the commands.sql to set up database schema and insert initial data**
  - Right-click on the database name in pgAdmin.
  - Choose Query Tool to open an SQL editor window.
  - In the Query Tool, click on the Open File button and choose the ```commands.sql``` file in the database directory
  - Once the file is open in the editor, click on the green Run button to execute the SQL commands

## Running Application
#### 1. Configure Database Connection
  - Open databaseConnection.py in the /src directory.
    - ```cd src```
  - Replace the placeholder values for host, database, user, and password with your actual PostgreSQL database connection details.
#### 2. Run the application
  - Navigate to the '/src' directory
  - Run the studentManagementSystem.py file
    - ```python studentManagementSystem.py``` or ```python3 studentManagementSystem.py```

## YouTube Link
[Video Demonstration](https://youtu.be/SSBJVHoHRkw)







 
