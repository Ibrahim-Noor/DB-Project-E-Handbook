from student.rawSQL import *

def insertStudentCourseInfo(rn, cid, gpa, sem, year):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO student_course_info (roll_number, course_id, course_gpa, semester, year) VALUES (%s, %s, %s, %s, %s)",[rn, cid, gpa, sem, year])
        return "Data Inserted Successfully"
    except Exception as e:
        return e

def removeCourse(rn, cid):
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
        return "Data Inserted Successfully"
    except Exception as e:
        return e

def removeInstructor(iid):
    c = connection.cursor()
    try:
        s = c.execute("DELETE FROM instructor WHERE instructor.instructor_id = %s",[iid])
        return "Instructor deleted Successfully"
    except Exception as e:
        return e   