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

  # Check if the email already exists in the database
  cursor.execute("SELECT * FROM students WHERE email = %s", (email,))
  if cursor.fetchone() is not None:
      print("Email already exists")
      return

  # If the email does not exist, add the student to the database
  cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
  print("Student added successfully")
  connection.commit()
  close(connection)

def updateStudentEmail(student_id, new_email):
  connection = connect()
  cursor = connection.cursor()

  # Check if the new email already exists in the database
  cursor.execute("SELECT * FROM students WHERE email = %s", (new_email,))
  if cursor.fetchone() is not None:
      print("New email already exists, please use a different email.")
      return
  
  # If the new email does not exist, update the email for the student
  cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
  print("Email updated successfully")
  connection.commit()
  close(connection)

def deleteStudent(student_id):
  connection = connect()
  cursor = connection.cursor()

  # Check if the student exists in the database
  cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
  if cursor.fetchone() is None:
      print("Student with this ID does not exist")
      return

  cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
  print("Student deleted successfully")
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

   # Update the email for student with student_id 1
  print("\n Updating the email for student with student_id 1")
  updateStudentEmail(1, "johndoe@example.com")
  print("\n All the students in this school after updating the email for student with student_id 1: ")
  displayAllStudents()

  # Delete the student with student_id 1
  print("\n Deleting the student with student_id 2")
  deleteStudent(2)
  print("\n All the students in this school after deleting the student with student_id 2: ")
  displayAllStudents()

main()


