import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

# con.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, major string)")
# con.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name TEXT, major string, year INTEGER)")
# con.execute("CREATE TABLE students_on_courses (student_id INTEGER, course_id INTEGER)")

# con.execute("INSERT INTO students (name, major) VALUES ('John', 'CS')")
# con.execute("INSERT INTO students (name, major) VALUES ('Jane', 'CS')")
# con.execute("INSERT INTO students (name, major) VALUES ('Jack', 'DS')")
# con.execute("INSERT INTO students (name, major) VALUES ('Jill', 'CS')")

# con.execute("INSERT INTO courses (name, major, year) VALUES ('Python1', 'CS', 2024)")
# con.execute("INSERT INTO courses (name, major, year) VALUES ('Python2', 'CS', 2024)")
# con.execute("INSERT INTO courses (name, major, year) VALUES ('Python3', 'CS', 2025)")
# con.execute("INSERT INTO courses (name, major, year) VALUES ('Data Science', 'DS', 2025)")

# con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (1, 1)")
# con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (1, 2)")
# con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (2, 2)")
# con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (3, 3)")
# con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (4, 3)")


# con.commit()

cursor = con.execute("SELECT * FROM students WHERE major = 'CS'")
for row in cursor:
    print(row)

cursor = con.execute("SELECT Name FROM students WHERE Name like '%a%'")
for row in cursor:
    print(row)

cursor = con.execute("SELECT s.* FROM students s "
                     "JOIN students_on_courses soc ON s.id = soc.student_id "
                     "JOIN courses c ON soc.course_id = c.id "
                     "WHERE c.name = 'Python1' AND c.year = '2024'")
for row in cursor:
    print(row)