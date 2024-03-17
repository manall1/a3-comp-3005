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

# Add a student to the student table
def addStudent(first_name, last_name, email, enrollment_date):
  connection = connect()
  cursor = connection.cursor()

  # First, check if the email already exists in the database
  cursor.execute("SELECT * FROM students WHERE email = %s", (email,))
  if cursor.fetchone() is not None:
      print("Email already exists")
      return

  # If the email does not exist, add the student to the database
  cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
  print("Student added successfully")
  connection.commit()
  close(connection)
  
  
# call the function
def main():
  # Display all the students in the school
  print("All the students in this school: ")
  displayAllStudents()

  # Add a student to the school
  print("\n Adding student Manal to the school:")
  addStudent("Manal", "Hassan", "manal@carleton.ca", "2021-09-01")
  print("\n All the students in this school after adding Manal: ")
  displayAllStudents()

main()


