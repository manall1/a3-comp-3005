import psycopg2

# Function to connect to the database
def connect():
    try:
      connection = psycopg2.connect(
          host="localhost",
          database="School",
          user="postgres",
          password="plants"
      )
      return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        exit(1)

# Function to close the connection
def close(con):
    if con is not None:
        con.close()

