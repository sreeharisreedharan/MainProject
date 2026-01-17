from django.db import models
from Guest.models import*
from Staff.models import*

# Create your models here.

class tbl_complaint(models.Model):
    complaint_title = models.CharField(max_length=50)
    complaint_content = models.CharField(max_length=200)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content = models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)


class tbl_certificaterequest(models.Model):
    certificaterequest_type = models.CharField(max_length=50)
    certificaterequest_content = models.CharField(max_length=200)
    certificaterequest_date = models.DateField(auto_now_add=True)
    certificaterequest_status = models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_examregistration(models.Model):
    examregistration_date = models.DateField(auto_now_add=True)
    examregistration_status = models.IntegerField(default=0)
    exam=models.ForeignKey(tbl_exam,on_delete=models.CASCADE)
    student=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    examregistration_hallticket = models.CharField(null=True)

class tbl_assignmentbody(models.Model):
    assignmentbody_file = models.FileField(upload_to="Assets/User/Photo")
    assignmentbody_status = models.IntegerField(default=0)
    assignmentbody_date = models.DateField(auto_now_add=True)
    assignmentbody_mark = models.CharField(null=True)
    assignment=models.ForeignKey(tbl_assignments,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_payment(models.Model):
    fee = models.ForeignKey(tbl_fee, on_delete=models.CASCADE, related_name="payments")
    amount = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True)


class tbl_issue(models.Model):
    issue_date=models.DateField(auto_now_add=True)
    issue_status=models.IntegerField(default=1)
    book=models.ForeignKey(tbl_book,on_delete=models.CASCADE)
    student=models.ForeignKey(tbl_user,on_delete=models.CASCADE)




