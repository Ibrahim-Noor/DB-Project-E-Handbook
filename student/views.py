from django.shortcuts import render, redirect
from .rawSQL import *
from .forms import *
import datetime
from index.decorators import *
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@isNotLoggedIn
@isStudentLogin
def studentLoginView(request):
    if request.session.get("student_id"):
       return redirect('studentMainPage')
    context = {}
    form = studentLoginForm()
    if request.method == "POST":
        form = studentLoginForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            row = returnStudent(roll_number)
            if row:
                request.session.flush()
                request.session['student_id'] = row[0]['roll_number']
                print(request.session.keys())
                return redirect('studentMainPage')
        context['error'] = "Invalid Credentials"
    context['form'] = studentLoginForm()
    return render(request, 'student/studentLogin.html', context)


@isLoggedIn
@isStudent
def studentMainPageView(request):
    context ={}
    return render(request, 'student/studentMainPage.html', context)

@isLoggedIn
@isStudent
def coursesTakenView(request):
    context = {}
    roll_number = request.session['student_id']
    row = getCoursesTaken(roll_number)
    context['courses_taken'] = row
    return render(request, 'student/coursesTaken.html', context)

@isLoggedIn
@isStudent
def coursesRequiredView(request):
    context = {}
    roll_number = request.session['student_id']
    creditHoursInfo = getCreditHoursInformation(roll_number)
    context["creditHoursInfo"] = creditHoursInfo[0]
    nonMajorNotTakenCourses = getNonMajorNotTakenCourses(roll_number)
    context["nonMajorNotTakenCourses"] = nonMajorNotTakenCourses
    majorCoresNotTakenCourses = getMajorCoresNotTakenCourses(roll_number)
    context["majorCoresNotTakenCourses"] = majorCoresNotTakenCourses
    majorNotTakenCourses = getMajorNotTakenCourses(roll_number)
    majorNotTakenCoursesNotInMajorCores = [course for course in majorNotTakenCourses if course not in majorCoresNotTakenCourses]
    context["majorNotTakenCourses"] = majorNotTakenCoursesNotInMajorCores
    return render(request, 'student/coursesRequired.html', context)
# SELECT SUM(courses.credit_hours) as total_credits, Major.req_ch from student_course_info INNER JOIN courses on student_course_info.course_id = courses.course_id INNER JOIN students on student_course_info.roll_number = students.roll_number INNER JOIN Major on students.major = Major.id WHERE student_course_info.roll_number = 21100192

@isLoggedIn
@isStudent
def checkPreReqView(request):
    context = {}
    allCourses = getAllCourses()
    context['allCourses'] = allCourses
    if request.method == 'GET':
        return render(request, 'student/checkPreReq.html', context)
    if request.method == 'POST':
        selectedValue = request.POST.get('course')
        preReqs = getPreReq(selectedValue)
        courseName = getCourseName(selectedValue)
        context['queryCourse'] = courseName[0]
        if preReqs:
            context['preReqs'] =preReqs
        else:
            context['preReqs'] = [{"name":"The course does not have any prereq"}]
        return render(request, 'student/checkPreReq.html', context)

@isLoggedIn
@isStudent
def checkAntiReqView(request):
    context = {}
    allCourses = getAllCourses()
    context['allCourses'] = allCourses
    if request.method == 'GET':
        return render(request, 'student/checkAntiReq.html', context)
    if request.method == 'POST':
        selectedValue = request.POST.get('course')
        antiReqs = getAntiReq(selectedValue)
        courseName = getCourseName(selectedValue)
        context['queryCourse'] = courseName[0]
        if antiReqs:
            context['antiReqs'] = antiReqs
        else:
            context['antiReqs'] = [{"name":"The course does not have any antireq"}]
        return render(request, 'student/checkAntiReq.html', context)

@isLoggedIn
@isStudent
def checkCoursesInASemesterView(request):
    context = {}
    now = datetime.datetime.now()
    context["yearList"] = range(now.year - 10, now.year + 2)
    if request.method == 'GET':
        return render(request, 'student/checkCoursesInASemester.html', context)
    if request.method == 'POST':
        selectedSemesterTerm = request.POST.get('semesterTerm')
        selectedSemesterYear = request.POST.get('semesterYear')
        coursesInASemester = getCoursesInASemester(selectedSemesterTerm, selectedSemesterYear)
        print(coursesInASemester)
        context['semesterTerm'] = [selectedSemesterTerm, selectedSemesterYear]
        context['coursesOffered'] = coursesInASemester
        return render(request, 'student/checkCoursesInASemester.html', context)

@isLoggedIn
@isStudent
def viewCoursesMajorWiseView(request):
    context = {}
    allMajors = getAllMajors()
    context['allMajors'] = allMajors
    if request.method == 'GET':
        return render(request, 'student/viewCoursesMajorWise.html', context)
    if request.method == 'POST':
        selectedMajor = request.POST.get('major')
        coursesOfAMajor = getCoursesOfAMajor(selectedMajor)
        majorName = getMajorName(selectedMajor)
        if coursesOfAMajor:
            context['selectedMajor'] = majorName[0]
            context['coursesOffered'] = coursesOfAMajor
        else:
            context['error'] = "This major, {} does not have any course registered under its name".format(majorName[0]['name'])
        return render(request, 'student/viewCoursesMajorWise.html', context)


@isLoggedIn
@isStudent
def checkAdvisorView(request):
    context = {}
    if request.method == 'GET':
        roll_number = request.session['student_id']
        advisor = getAdvisor(roll_number)
        if advisor:
            print(advisor)
            context["advisor"] = advisor
        return render(request, 'student/checkAdvisor.html', context)



@isLoggedIn
@isStudent
def viewCoursesByInstructorView(request):
    context = {}
    allInstructors = getAllInstructors()
    context['allInstructors'] = allInstructors
    if request.method == 'GET':
        return render(request, 'student/viewCoursesByInstructor.html', context)
    if request.method == 'POST':
        selectedValue = request.POST.get('instructor')
        coursesOffered = getCoursesOfferedByInstructor(selectedValue)
        instructorName = getInstructorName(selectedValue)
        if coursesOffered:
            context['instructor'] = instructorName[0]
            context['coursesOffered'] = coursesOffered
        else:
            context['error'] = "The instructor {} does not offer any course.".format(instructorName[0]['name'])
        return render(request, 'student/viewCoursesByInstructor.html', context)
    # if request.method == 'POST':

@isLoggedIn
@isStudent
def viewInstructorsRatingsView(request):
    context = {}
    ratings = getInstructorsRatings()
    context['instructorRatings'] = ratings
    return render(request, 'student/viewInstructorsRatings.html', context)


@isLoggedIn
@isStudent
def viewAllInstructorsView(request):
    context = {}
    allInstructors = getAllInstructors()
    context['allInstructors'] = allInstructors
    return render(request, 'student/viewAllInstructors.html', context)