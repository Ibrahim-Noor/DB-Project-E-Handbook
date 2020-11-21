from django.shortcuts import render, redirect
from .raw_sql import *
from .forms import *

# Create your views here.
def loginView(request):
    context = {}
    form = loginForm()
    if request.method == "POST":
        context = {}
        form = loginForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            row = returnStudent(roll_number)
            if row:
                request.session['student_id'] = row[0]['roll_number']
                return redirect('mainPage')
        context['error'] = "Invalid Credentials"
    context['form'] = loginForm()
    return render(request, 'student/login.html', context)

def mainPageView(request):
    context ={}
    return render(request, 'student/mainPage.html', context)

def coursesTakenView(request):
    context = {}
    roll_number = request.session['student_id']
    row = getCoursesTaken(roll_number)
    context['courses_taken'] = row
    print(context['courses_taken'])
    return render(request, 'student/coursesTaken.html', context)

def coursesRequiredView(request):
    context = {}
    roll_number = request.session['student_id']
    creditHoursInfo = getCreditHoursInformation(roll_number)
    context["creditHoursInfo"] = creditHoursInfo[0]
    nonMajorNotTakenCourses = getNonMajorNotTakenCourses(roll_number)
    # print(nonMajorNotTakenCourses)
    context["nonMajorNotTakenCourses"] = nonMajorNotTakenCourses
    majorCoresNotTakenCourses = getMajorCoresNotTakenCourses(roll_number)
    context["majorCoresNotTakenCourses"] = majorCoresNotTakenCourses
    majorNotTakenCourses = getMajorNotTakenCourses(roll_number)
    majorNotTakenCoursesNotInMajorCores = [course for course in majorNotTakenCourses if course not in majorCoresNotTakenCourses]
    context["majorNotTakenCourses"] = majorNotTakenCoursesNotInMajorCores
    print(context)
    return render(request, 'student/coursesRequired.html', context)
# SELECT SUM(courses.credit_hours) as total_credits, Major.req_ch from student_course_info INNER JOIN courses on student_course_info.course_id = courses.course_id INNER JOIN students on student_course_info.roll_number = students.roll_number INNER JOIN Major on students.major = Major.id WHERE student_course_info.roll_number = 21100192

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
        context['preReqs'] = courseName + preReqs
        return render(request, 'student/checkPreReq.html', context)
