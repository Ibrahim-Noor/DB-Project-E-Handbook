from student.rawSQL import *

def insertStudentCourseInfo(rn, cid, gpa, sem, year):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO student_course_info (roll_number, course_id, course_gpa, semester, year) VALUES (%s, %s, %s, %s, %s)",[rn, cid, gpa, sem, year])
        return "Course Information Inserted Successfully"
    except Exception as e:
        return e

def removeCourseOfStudent(rn, cid):
    c = connection.cursor()
    try:
        s = c.execute("DELETE FROM student_course_info WHERE student_course_info.roll_number = %s AND student_course_info.course_id = %s",[rn, cid])
        return "Course deleted Successfully"
    except Exception as e:
        return e   

 
def insertInstructorInfo(id, name, depart, rat, school):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO instructor (instructor_id, name, department, rating, school) VALUES (%s, %s, %s, %s, %s)",[id, name, depart, rat, school])
        return "Instructor Inserted Successfully"
    except Exception as e:
        return e

def removeInstructor(iid):
    c = connection.cursor()
    try:
        s = c.execute("DELETE FROM instructor WHERE instructor.instructor_id = %s",[iid])
        return "Instructor deleted Successfully"
    except Exception as e:
        return e   

def addCourse(c_id, name, school, major, instructor, courseCap, semester, year, creditHours):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO courses (course_id, name, school, major, instructor, course_cap, semester, year, credit_hours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",[c_id, name, school, major, instructor, courseCap, semester, year, creditHours])
        return "Course Inserted Successfully"
    except Exception as e:
        return e

def removeCourseOffering(c_id):
    c = connection.cursor()
    try:
        c.execute("DELETE FROM courses WHERE courses.course_id = %s",[c_id])
        return "Course Deleted Successfully"
    except Exception as e:
        return e

def updateInstructorRating(i_id, rating):
    c = connection.cursor()
    try:
        c.execute("UPDATE instructor SET instructor.rating = %s WHERE instructor.instructor_id = %s",[rating, i_id])
        return "Rating Updated Successfully"
    except Exception as e:
        return e

def addStudent(rn, name, gradYear, cgpa, chTaken, major):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO students (roll_number, full_name, grad_year, cgpa, ch_taken, major) VALUES (%s, %s, %s, %s, %s, %s)",[rn, name, gradYear, cgpa, chTaken, major])
        return "Student Data Inserted Successfully"
    except Exception as e:
        return e