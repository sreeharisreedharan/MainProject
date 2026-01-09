from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name = models.CharField(max_length=50)

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_email = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)

class tbl_course(models.Model):
    course_name=models.CharField(max_length=50)
    course_amount=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)

class tbl_staff(models.Model):
    staff_name=models.CharField(max_length=50)
    staff_email=models.CharField(max_length=50)
    staff_contact=models.CharField(max_length=50)
    staff_photo=models.FileField(upload_to="Assets/Staff/Photo/")
    staff_gender=models.CharField(max_length=200)
    staff_dob=models.DateField()
    staff_qualification=models.CharField(max_length=200)
    staff_role=models.CharField(max_length=200)
    staff_password=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)

class tbl_semester(models.Model):
    semester_name=models.CharField(max_length=50)

class tbl_academicyear(models.Model):
    academicyear_year=models.CharField(max_length=50)

class tbl_subject(models.Model):
    subject_name=models.CharField(max_length=50)
    course=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    semester=models.ForeignKey(tbl_semester,on_delete=models.CASCADE)

class tbl_class(models.Model):
    class_name=models.CharField(max_length=50)
    course=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
   
class tbl_assignclass(models.Model):
    classid=models.ForeignKey(tbl_class,on_delete=models.CASCADE)
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)
    academicyear=models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)

class tbl_assignsubject(models.Model):
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)

class tbl_exam(models.Model):
    exam_date=models.DateField()
    exam_type=models.CharField(max_length=50)
    course=models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    semester=models.ForeignKey(tbl_semester,on_delete=models.CASCADE)
    academicyear=models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)

class tbl_genre(models.Model):
    genre_name=models.CharField(max_length=50)  

class tbl_book(models.Model):
    book_title=models.CharField(max_length=50)
    book_details=models.CharField(max_length=200)
    book_photo=models.FileField(upload_to="Assets/Book/Photos/")
    book_author=models.CharField(max_length=50)
    book_status=models.IntegerField(default=0)
    genre=models.ForeignKey(tbl_genre,on_delete=models.CASCADE)




class tbl_timetable(models.Model):
    course = models.ForeignKey(tbl_course,on_delete=models.CASCADE)
    semester = models.ForeignKey(tbl_semester,on_delete=models.CASCADE)
    academicyear = models.ForeignKey(tbl_academicyear,on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    hour = models.CharField(max_length=5)
    subject = models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    staff = models.ForeignKey(tbl_staff,on_delete=models.CASCADE)

class tbl_info(models.Model):
    info_title=models.CharField(max_length=50)
    info_details=models.CharField(max_length=200)
    info_file=models.FileField(upload_to="Assets/Admin/Photo")

    