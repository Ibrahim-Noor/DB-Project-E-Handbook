# from django.db import models

# # Create your models here.

# class Major(models.Model):
#     name = models.CharField(max_length=30, blank=False, null=False)
#     school = models.CharField(max_length=200, blank=False, null=False)
#     req_ch = models.IntegerField(blank=False, null=False)

# class Student(models.Model):
#     roll_number = models.IntegerField(primary_key=True)
#     full_name = models.CharField(max_length=50, blank=False)
#     grad_year = models.IntegerField(blank=False)
#     cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
#     ch_taken = models.IntegerField(default=0)
#     major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)

# class Instructor(models.Model):
#     instructor_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     department = models.CharField(max_length=200)
#     rating = models.IntegerField(default=0)
#     school = models.CharField(max_length=200)

# class Course(models.Model):
#     course_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     school = models.CharField(max_length=200)
#     course_cap = models.IntegerField()
#     semester = models.CharField(max_length=100)
#     year = models.IntegerField
#     credit_hours = models.IntegerField
#     major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)
#     Instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)

# class Minor(models.Model):
#     minor_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     school = models.CharField(max_length=200)
#     req_ch = models.IntegerField()

# class minorCourses(models.Model):
#     minor = models.ForeignKey(Minor, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

# class majorCourses(models.Model):
#     major = models.ForeignKey(Major, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

# class Advisor(models.Model):
#     roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
#     advisor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)


# class studentCourseInfo(models.Model):
#     roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     course_gpa = models.DecimalField(max_digits=4, decimal_places=2)
#     semester = models.CharField(max_length=100)
#     year = models.IntegerField()

#     class Meta:
#         unique_together = (('roll_number', 'course'),)

# class antiReqs(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     antiReq = models.ForeignKey(Course, related_name="antireqcourse", on_delete=models.SET_NULL, null=True)

#     class Meta:
#         unique_together = (('course', 'antiReq'),)

# class preReqs(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     preReq = models.ForeignKey(Course, related_name="prereqcourse" ,on_delete=models.SET_NULL, null=True)

#     class Meta:
#         unique_together = (('course', 'preReq'),)