from django.db import connection

def returnStudent(roll_number):
    c = connection.cursor()
    c.execute("Select * from students where roll_number=%s",[roll_number])
    # row = c.fetchall()
    columns = [col[0] for col in c.description]
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]

def getCoursesTaken(roll_number):
    c = connection.cursor()
    c.execute("SELECT courses.name, student_course_info.course_gpa, student_course_info.semester, student_course_info.year from student_course_info inner join courses ON student_course_info.course_id = courses.course_id where roll_number = %s ORDER BY student_course_info.year ",[roll_number])
    # row = c.fetchall()
    columns = [col[0] for col in c.description]
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]


def getCreditHoursInformation(roll_number):
    c = connection.cursor()
    c.execute("select students.grad_year, SUM(CASE WHEN students.major = courses.major THEN courses.credit_hours ELSE 0 END) as major_courses_ch, SUM(CASE WHEN students.major != courses.major THEN courses.credit_hours ELSE 0 END) as nonmajor_courses_ch, SUM(courses.credit_hours) as total_credithours_taken ,Major.req_ch from student_course_info INNER JOIN courses on student_course_info.course_id = courses.course_id INNER JOIN students ON student_course_info.roll_number = students.roll_number INNER JOIN Major ON students.major = Major.id WHERE student_course_info.roll_number = %s", [roll_number])
    columns = [col[0] for col in c.description]
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]

def getMajorCoresNotTakenCourses(roll_number):
    c = connection.cursor()
    c.execute("Select courses.name, major_cores.major, courses.credit_hours, courses.school, courses.semester, courses.year, IF(courses.course_id in (SELECT prereqs.course_id from prereqs), IF((SELECT prereqs.prereq_id from prereqs where prereqs.course_id = courses.course_id) in (SELECT student_course_info.course_id from student_course_info where student_course_info.roll_number = %s), 'Yes', 'No'), 'No PreReq') as prereqs_met from major_cores INNER JOIN courses on courses.course_id = major_cores.course_id, students where major_cores.course_id not in( SELECT major_cores.course_id from major_cores INNER join student_course_info on major_cores.course_id = student_course_info.course_id WHERE student_course_info.roll_number = %s) and major_cores.major = students.major and students.roll_number = %s AND major_cores.course_id not in ( SELECT antireqs.antireq_id FROM antireqs INNER JOIN student_course_info ON antireqs.course_id = student_course_info.course_id where student_course_info.roll_number = %s ) and major_cores.course_id not in (SELECT antireqs.course_id FROM antireqs INNER JOIN student_course_info ON antireqs.antireq_id = student_course_info.course_id where student_course_info.roll_number = %s)", [roll_number, roll_number, roll_number, roll_number, roll_number])
    columns = [col[0] for col in c.description]
    columns[0] = 'course_name'
    columns[1] = 'major_name'
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]


def getMajorNotTakenCourses(roll_number):
    c = connection.cursor()
    c.execute("SELECT courses.name, Major.name, courses.credit_hours, courses.school, courses.semester, courses.year, IF(courses.course_id in (SELECT prereqs.course_id from prereqs), IF((SELECT prereqs.prereq_id from prereqs where prereqs.course_id = courses.course_id) in (SELECT student_course_info.course_id from student_course_info where student_course_info.roll_number = %s), 'Yes', 'No'),'No Prereq') as prereqs_met FROM courses INNER JOIN Major ON courses.major = Major.id, students where"+
    " courses.course_id not in (SELECT student_course_info.course_id from student_course_info INNER JOIN students on students.roll_number = student_course_info.roll_number WHERE students.roll_number = %s)"+
    " AND"+
    " courses.course_id not in (SELECT antireqs.antireq_id FROM antireqs INNER JOIN student_course_info ON antireqs.course_id = student_course_info.course_id where student_course_info.roll_number = %s)"+
    " AND"+
    " courses.course_id not in (SELECT antireqs.course_id FROM antireqs INNER JOIN student_course_info ON antireqs.antireq_id = student_course_info.course_id where student_course_info.roll_number = %s)"+
    " AND"+
    " students.major = courses.major AND students.roll_number = %s", [roll_number, roll_number, roll_number, roll_number, roll_number])
    columns = [col[0] for col in c.description]
    columns[0] = 'course_name'
    columns[1] = 'major_name'
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]

def getNonMajorNotTakenCourses(roll_number):
    c = connection.cursor()
    c.execute("SELECT courses.name, Major.name, courses.credit_hours, courses.school, courses.semester, courses.year, IF(courses.course_id in (SELECT prereqs.course_id from prereqs), IF((SELECT prereqs.prereq_id from prereqs where prereqs.course_id = courses.course_id) in (SELECT student_course_info.course_id from student_course_info where student_course_info.roll_number = %s), 'Yes', 'No'),'No Prereq') as prereqs_met FROM courses INNER JOIN Major ON courses.major = Major.id, students where"+
    " courses.course_id not in (SELECT student_course_info.course_id from student_course_info INNER JOIN students on students.roll_number = student_course_info.roll_number WHERE students.roll_number = %s)"+
    " AND"+
    " courses.course_id not in (SELECT antireqs.antireq_id FROM antireqs INNER JOIN student_course_info ON antireqs.course_id = student_course_info.course_id where student_course_info.roll_number = %s)"+
    " AND"+
    " courses.course_id not in (SELECT antireqs.course_id FROM antireqs INNER JOIN student_course_info ON antireqs.antireq_id = student_course_info.course_id where student_course_info.roll_number = %s)"+
    " AND"+
    " students.major != courses.major AND students.roll_number = %s", [roll_number, roll_number, roll_number, roll_number, roll_number])
    columns = [col[0] for col in c.description]
    columns[0] = 'course_name'
    columns[1] = 'major_name'
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]

def getAllCourses():
    c = connection.cursor()
    c.execute("SELECT courses.course_id, courses.name from courses")
    # row = c.fetchall()
    columns = [col[0] for col in c.description]
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]

def getPreReq(course_id):
    c = connection.cursor()
    c.execute("SELECT courses.name from prereqs inner join courses on prereqs.prereq_id = courses.course_id where prereqs.course_id = %s", [course_id])
    # row = c.fetchall()
    columns = [col[0] for col in c.description]
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]

def getCourseName(course_id):
    c = connection.cursor()
    c.execute("SELECT courses.name from courses where courses.course_id = %s", [course_id])
    # row = c.fetchall()
    columns = [col[0] for col in c.description]
    return [
        dict(zip(columns, row))
        for row in c.fetchall()
    ]    

 