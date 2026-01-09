from django.db import models

# Create your models here.
from django.db import models

class tbl_student(models.Model):
    student_name = models.CharField(max_length=30)
    student_department = models.CharField(max_length=30)
    student_course = models.CharField(max_length=30)
    student_sem = models.CharField(max_length=30)
    student_email = models.CharField(max_length=100)
    student_contact = models.CharField(max_length=20)
    student_address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


class tbl_mark(models.Model):
    student = models.ForeignKey(tbl_student, on_delete=models.CASCADE)
    mark_subject = models.CharField(max_length=100)
    mark_total = models.IntegerField()
    mark_sem = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.student_name} - {self.mark_subject}"
