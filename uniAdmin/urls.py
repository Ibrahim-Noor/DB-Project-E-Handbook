from django.urls import path
from .views import *

urlpatterns = [
    path('', adminLoginView, name="adminLogin"),
    path('admin-mainpage/', adminMainPageView, name="adminMainPage"),
    path('admin-addstudent-course/', addCourseStudentView, name="addCourseStudent"),
    path('admin-remove-course-roll_number', removeCourseStudentHelperView, name="removeCourseStudentHelper"),
    path('admin-remove-course-of-student/', removeCourseStudentView, name="removeCourseStudent"),
    path('admin-add-instructor/', addInstructorView, name="addInstructor"),
    path('admin-remove-instructor/', removeInstructorView, name="removeInstructor"),
    path('admin-add-course-offering/', addCourseOfferingView, name="addCourseOffering"),
    path('admin-remove-course-offering/', removeCourseOfferingView, name="removeCourseOffering"),
    path('admin-update-instructor-rating/', updateInstructorRatingView, name="updateInstructorRating"),
    path('admin-add-student/', addStudentView, name="addStudent"),
    ]
    