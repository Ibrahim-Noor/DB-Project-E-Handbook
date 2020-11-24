from django.urls import path
from .views import *

urlpatterns = [
    path('', studentLoginView, name="studentLogin"),
    path('student-mainpage/', adminMainPageView, name="studentMainPage"),
    path('courses-taken/', coursesTakenView, name='coursesTaken'),
    path('courses-required/', coursesRequiredView, name='coursesRequired'),
    path('check-prereqs/', checkPreReqView, name="checkPreReq"),
    path('check-antireqs/', checkAntiReqView, name="checkAntiReq"),
    path('check-semester-courses/', checkCoursesInASemesterView, name="checkCoursesInASemester"),
    path('check-advisor/', checkAdvisorView, name="checkAdvisor"),
    path('view-courses-by-instructor/', viewCoursesByInstructorView, name="viewCoursesByInstructor"),
    path('view-instructors-ratings/', viewInstructorsRatingsView, name="viewInstructorsRatings"),
    path('view-courses-major/', viewCoursesMajorWiseView, name="viewCoursesMajorWise"),
    path('view-instructors/', viewAllInstructorsView, name="viewAllInstructors")
]