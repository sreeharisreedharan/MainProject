from django.db import models
from Admin.models import *

# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=200)
    user_gender=models.CharField(max_length=200)
    user_dob=models.DateField()
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to="Assets/User/Photo")
    user_password=models.CharField(max_length=50)
    assignclass=models.ForeignKey(tbl_assignclass,on_delete=models.CASCADE)

class tbl_classsem(models.Model):
    semester=models.ForeignKey(tbl_semester,on_delete=models.CASCADE)   
    assignclass=models.ForeignKey(tbl_assignclass,on_delete=models.CASCADE) 

class tbl_notes(models.Model):
    notes_title=models.CharField(max_length=200)
    notes_file=models.FileField(upload_to="Assets/Staff/Photo")
    notes_status=models.IntegerField(default=0)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)
    semester=models.ForeignKey(tbl_semester,on_delete=models.CASCADE)

class tbl_assignments(models.Model):
    assignments_title=models.CharField(max_length=200)
    assignments_topic=models.FileField(upload_to="Assets/Staff/Photo")
    assignments_date=models.DateField(auto_now_add=True)
    assignments_duedate=models.DateField()
    assignments_status=models.IntegerField(default=0)
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)

class tbl_internalmark(models.Model):
    internalmark_date=models.DateField(auto_now_add=True)
    internalmark_mark=models.CharField(max_length=200)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    student=models.ForeignKey(tbl_user,on_delete=models.CASCADE)


class tbl_attendance(models.Model):
    student = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    subject = models.ForeignKey(tbl_subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    course = models.ForeignKey(tbl_course, on_delete=models.CASCADE)
    semester = models.ForeignKey(tbl_semester, on_delete=models.CASCADE)
    academicyear = models.ForeignKey(tbl_academicyear, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    hour = models.CharField(max_length=2)  # 1-5
    status = models.IntegerField(default=0)

class tbl_leave(models.Model):
    leave_date=models.DateField(auto_now_add=True)
    leave_fromdate=models.DateField()
    leave_todate=models.DateField()
    leave_reason=models.CharField(max_length=200)
    leave_status=models.IntegerField(default=0)
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)

class tbl_fee(models.Model):
    student = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    semester = models.ForeignKey(tbl_semester, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
