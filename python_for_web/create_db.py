import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="thirty_days_of_python"
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE thirty_days_of_python")
# my_cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),country VARCHAR(255),city VARCHAR(255),age VARCHAR(255))")
# my_cursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# my_cursor.execute("DROP TABLE students")

# my_cursor.execute("SHOW DATABASES")
# my_cursor.execute("SHOW TABLES")
my_cursor.execute("SELECT * from students")
result = my_cursor.fetchall() 

# for db in my_cursor:
#     print(db)

for row in result: 
    print(row, '\n') 