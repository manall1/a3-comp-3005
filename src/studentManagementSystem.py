# import the connection functions from the databaseConnection.py file
from databaseConnection import connect, close

# Functions to manage student data

# Display and retrieve all records from the student table
def displayAllStudents():
  dataBaseConnection = connect()
  cursor = dataBaseConnection.cursor()
  cursor.execute("SELECT * FROM students")
  students = cursor.fetchall()
  for student in students:
    print(student)
  close(dataBaseConnection)

# call the function
def main():
  print("All the students in this school: ")
  displayAllStudents()

main()


