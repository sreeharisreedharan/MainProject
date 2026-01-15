from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import*
from User.models import*
from django.http import JsonResponse
# Create your views here.

def District(request):
    districtdata=tbl_district.objects.all()
    if request.method =="POST":
        district=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=district)
        return render(request,"Admin/District.html",{'msg':"Data Inserted.."})
        # return redirect("Admin:District")
    else:
        return render(request,"Admin/District.html",{'district':districtdata})

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")

def editdistrict(request,eid):
    editdata = tbl_district.objects.get(id=eid)
    districtdata=tbl_district.objects.all()

    if request.method == "POST":
        district=request.POST.get("txt_district")
        editdata.district_name = district
        editdata.save()
        return render(request,"Admin/District.html",{'msg':"Data Updated.."})
    else:
        return render(request,"Admin/District.html",{'editdata':editdata,'district':districtdata})


def AdminRegistration(request):
    admindata=tbl_admin.objects.all()
    if request.method =="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)

        return render(request,"Admin/AdminRegistration.html",{'msg':"Data Inserted.."})
    else:
        return render(request,"Admin/AdminRegistration.html",{'admin':admindata})

def deladmin(request,aid):
    tbl_admin.objects.get(id=aid).delete()
    return redirect("Admin:AdminRegistration")

def editadmin(request,eaid):
    editadata=tbl_admin.objects.get(id=eaid)
    admindata=tbl_admin.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        editadata.admin_name = name
        editadata.admin_email = email
        editadata.admin_password = password
        editadata.save()
        return render(request, "Admin/AdminRegistration.html",{'msg':"Data Updated"})
    else:
        return render(request,"Admin/AdminRegistration.html",{'editadata':editadata,'admin':admindata })

def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_category")
        tbl_category.objects.create(category_name=name)
        return render(request,"Admin/Category.html",{'msg':"Data Inserted.."})
    else:
        return render(request,"Admin/Category.html",{'category':categorydata})
def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Admin:Category")

def editcategory(request,ecid):
    editcdata = tbl_category.objects.get(id=ecid)
    categorydata=tbl_category.objects.all()

    if request.method == "POST":
        category=request.POST.get("txt_category")
        editcdata.category_name = category
        editcdata.save()
        return render(request, "Admin/Category.html",{'msg':"Data updated"} )
    else:
        return render(request, "Admin/Category.html",{'editcdata':editcdata,'category':categorydata})

def Place(request):
    disdata=tbl_district.objects.all()#dropdown
    placedata=tbl_place.objects.all()#place data select
    if request.method == "POST":
        place=request.POST.get("txt_place")
        disid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=place,district=disid)
        return render(request,"Admin/Place.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Place.html",{'dis':disdata,'plc':placedata})

def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")

def editplace(request,eid):
    editdata = tbl_place.objects.get(id=eid)
    dis=tbl_district.objects.all()
    if request.method =='POST':
        place = request.POST.get('txt_place')
        editdata.disid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editdata.place_name = place
        editdata.save()
        return render(request, "Admin/Place.html", {'msg':"Data Updated"})
    else:
        return render(request, "Admin/Place.html", {'editdata':editdata,'dis':dis})

def Subcategory(request):
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()
    if request.method == 'POST':
        subcategory=request.POST.get("txt_subcategory")
        categoryid=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=subcategory,category=categoryid)
        return render(request, "Admin/Subcategory.html", {'msg':"Data Inserted" })
    else:
        return render(request, "Admin/Subcategory.html", {'cat':categorydata,'scat':subcategorydata})

def delsub(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("Admin:Subcategory")

def editsub(request,eid):
    editdata=tbl_subcategory.objects.get(id=eid)
    cat=tbl_category.objects.all()
    if request.method == 'POST':
        subcategory=request.POST.get("txt_subcategory")
        category=tbl_category.objects.get(id=request.POST.get("sel_category"))
        editdata.categor=category
        editdata.subcategory_name = subcategory
        editdata.save()
        return render(request, "Admin/Subcategory.html", {'msg':"Data Updated"})
    else:
        return render(request, "Admin/Subcategory.html", {'editdata':editdata,'cat':cat})

def HomePage(request):
    return render(request, 'Admin/HomePage.html')

def UserList(request):
    departmentdata=tbl_department.objects.all()
    coursedata=tbl_course.objects.all()
    semesterdata=tbl_semester.objects.all()
    if request.method =="POST":
        department=request.POST.get('sel_department')
        course=request.POST.get('sel_course')
        semester=request.POST.get('sel_semester')
        data=tbl_user.objects.filter(assignclass__classid__course=course)
        return render(request, "Admin/UserList.html", {'data':data,'departmentdata':departmentdata,'coursedata':coursedata,'semesterdata':semesterdata})
    else:
        return render(request,"Admin/UserList.html",{'departmentdata':departmentdata,'coursedata':coursedata,'semesterdata':semesterdata})

def ViewComplaint(request):
    data=tbl_complaint.objects.all()
    return render(request, "Admin/ViewComplaint.html", {'data':data})

def Reply(request,id):
    editdata=tbl_complaint.objects.get(id=id)
    if request.method == "POST":
        reply=request.POST.get("txt_reply")
        editdata.complaint_status = 1
        editdata.complaint_reply = reply
        editdata.save()
        return render(request, "Admin/Reply.html", {'msg':"Reply Passed"})
    else:
        return render(request, "Admin/Reply.html", {'editdata':editdata})

def ViewFeedback(request):
    data=tbl_feedback.objects.all()
    return render(request, "Admin/ViewFeedback.html", {'data':data})

def Department(request):
    departmentdata=tbl_department.objects.all()
    if request.method == "POST":
        department=request.POST.get("txt_department")
        tbl_department.objects.create(department_name=department)
        return render(request, "Admin/Department.html", {'msg':"Data Inserted"})
    else:
        return render(request, "Admin/Department.html", {'department':departmentdata})

def Course(request):
    departmentdata=tbl_department.objects.all()
    coursedata=tbl_course.objects.all()
    if request.method == "POST":
        course=request.POST.get("txt_course")
        amount=request.POST.get("txt_amount")
        departmentid=tbl_department.objects.get(id=request.POST.get("sel_department"))
        tbl_course.objects.create(course_name=course,course_amount=amount,department=departmentid)
        return render(request, "Admin/Course.html", {'msg':"Data Inserted"})
    else:
        return render(request, "Admin/Course.html", {'departmentdata':departmentdata,'coursedata':coursedata})

def deldepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect("Admin:Department")

def editdepartment(request,eid):
    editdata=tbl_department.objects.get(id=eid)
    data=tbl_department.objects.all()
    if request.method == "POST":
        department=request.POST.get("txt_department")
        editdata.department_name=department
        editdata.save()
        return render(request, "Admin/Department.html", {'msg':"Data Updated"})
    else:
        return render(request, "Admin/Department.html", {'editdata':editdata,'department':data})

def delcourse(request,did):
    tbl_course.objects.get(id=did).delete()
    return redirect("Admin:Course")

def editcourse(request,eid):
    coursedata=tbl_course.objects.all()
    editdata=tbl_course.objects.get(id=eid)
    departmentdata=tbl_department.objects.all()
    if request.method == "POST":
        course=request.POST.get("txt_course")
        amount=request.POST.get("txt_amount")
        editdata.departmentid=tbl_department.objects.get(id=request.POST.get("sel_department"))
        editdata.course_name=course
        editdata.course_amount=amount
        editdata.save()
        return render(request, "Admin/Course.html", {'msg':"Data Updated"})
    else:
        return render(request, "Admin/Course.html", {'editdata':editdata,'departmentdata':departmentdata,'coursedata':coursedata})


def StaffRegistration(request):
    staff=tbl_staff.objects.all()
    departmentdata=tbl_department.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        photo=request.FILES.get("file_photo")
        gender=request.POST.get("txt_gender")
        dob=request.POST.get("txt_date")
        qualification=request.POST.get("txt_qualification")
        role=request.POST.get("txt_role")
        departmentid=tbl_department.objects.get(id=request.POST.get("sel_department"))
        password=request.POST.get("txt_password")
        tbl_staff.objects.create(staff_name=name,staff_email=email,staff_contact=contact,staff_photo=photo,staff_gender=gender,staff_dob=dob,staff_qualification=qualification,staff_role=role,department=departmentid,staff_password=password)
        return render(request, "Admin/StaffRegistration.html", {'msg':"Data Inserted"})
    else:
        return render(request, "Admin/StaffRegistration.html",{'staff':staff,'departmentdata':departmentdata})

def delstaff(request,did):
    tbl_staff.objects.get(id=did).delete()
    return redirect("Admin:StaffRegistration")

def Semester(request):
    semesterdata=tbl_semester.objects.all()
    if request.method == "POST":
        semester=request.POST.get("txt_semester")
        tbl_semester.objects.create(semester_name=semester)
        return render(request, "Admin/Semester.html", {'msg':"Data Inserted"})
    else:
        return render(request, "Admin/Semester.html",{'semester':semesterdata})

def delsemester(request,did):
    tbl_semester.objects.get(id=did).delete()
    return redirect("Admin:Semester")

def AcademicYear(request):
    data=tbl_academicyear.objects.all()
    if request.method == "POST":
        academic=request.POST.get("txt_academicyear")
        tbl_academicyear.objects.create(academicyear_year=academic)
        return render(request, "Admin/AcademicYear.html", {'msg':"Data Inserted"})
    else:
        return render(request, "Admin/AcademicYear.html",{'data':data})

def delyear(request,did):
    tbl_academicyear.objects.get(id=did).delete()
    return redirect("Admin:AcademicYear")

def Subject(request):
    departmentdata=tbl_department.objects.all()
    coursedata=tbl_course.objects.all()
    semesterdata=tbl_semester.objects.all()
    subject=tbl_subject.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_subject")
        courseid=tbl_course.objects.get(id=request.POST.get("sel_course"))
        semesterid=tbl_semester.objects.get(id=request.POST.get("sel_semester"))
        tbl_subject.objects.create(subject_name=name,course=courseid,semester=semesterid)
        return render(request,"Admin/Subject.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Subject.html",{'departmentdata':departmentdata,'coursedata':coursedata,'semesterdata':semesterdata,'subject':subject})

def delsubjects(request,did):
    tbl_subject.objects.get(id=did).delete()
    return redirect("Admin:Subject")

def AjaxCourse(request):
    course=tbl_course.objects.filter(department=request.GET.get('dpid'))
    return render(request,"Admin/AjaxCourse.html",{'data':course})

def Class(request):
    departmentdata=tbl_department.objects.all()
    coursedata=tbl_course.objects.all()
    semesterdata=tbl_semester.objects.all()
    classdata=tbl_class.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_class")
        courseid=tbl_course.objects.get(id=request.POST.get("sel_course"))
        tbl_class.objects.create(class_name=name,course=courseid)
        return render(request,"Admin/Class.html",{'msg':"Data Inserted"})
    else:
        return render(request, "Admin/Class.html",{'departmentdata':departmentdata,'coursedata':coursedata,'data':classdata})

def delclass(request,did):
    tbl_class.objects.get(id=did).delete()
    return redirect("Admin:Class")

def StaffList(request):
    data=tbl_staff.objects.all()
    return render(request, "Admin/StaffList.html", {'data':data})

def AssignClass(request,aid):
    departmentdata=tbl_department.objects.all()
    coursedata=tbl_course.objects.all()
    academicyeardata=tbl_academicyear.objects.all()
    classdata=tbl_class.objects.all()
    if request.method == "POST":
        staffid=tbl_staff.objects.get(id=aid)
        academicyearid=tbl_academicyear.objects.get(id=request.POST.get("sel_academicyear"))
        classid=tbl_class.objects.get(id=request.POST.get("sel_class"))
        tbl_assignclass.objects.create(staff=staffid,classid=classid,academicyear=academicyearid)
        return render(request, "Admin/AssignClass.html",{'msg':"Data Inserted"})
    else:
        return render(request, "Admin/AssignClass.html", {'departmentdata':departmentdata, 'coursedata':coursedata, 'academicyeardata':academicyeardata, 'classdata':classdata})

def AjaxClass(request):
    classdata=tbl_class.objects.filter(course=request.GET.get('cid'))
    return render(request,"Admin/AjaxClass.html",{'data':classdata})

def AssignSubject(request,aid):
    departmentdata=tbl_department.objects.all()
    coursedata=tbl_course.objects.all()
    semesterdata=tbl_semester.objects.all()
    subjectdata=tbl_subject.objects.all()
    assignsubject=tbl_assignsubject.objects.all()
    if request.method == "POST":
        staffid=tbl_staff.objects.get(id=aid)
        subjectid=tbl_subject.objects.get(id=request.POST.get("sel_subject"))
        tbl_assignsubject.objects.create(staff=staffid,subject=subjectid)
        return render(request,"Admin/AssignSubject.html",{'msg':"Data Inserted",'Subdata':assignsubject})
    else:
        return render(request,"Admin/AssignSubject.html", {'departmentdata':departmentdata,'coursedata':coursedata,'semesterdata':semesterdata,'subjectdata':subjectdata,'subdata':assignsubject})

def AjaxSubject(request):
    subjectdata=tbl_subject.objects.filter(course=request.GET.get('cid'),semester = request.GET.get("semid"))
    return render(request,"Admin/AjaxSubject.html",{'data':subjectdata})

def delsubject(request,did):
    tbl_assignsubject.objects.get(id=did).delete()
    return redirect("Admin:StaffList")

def Exam(request):
    departmentdata=tbl_department.objects.all()
    semesterdata=tbl_semester.objects.all()
    coursedata=tbl_course.objects.all()
    academicyeardata=tbl_academicyear.objects.all()
    examdata=tbl_exam.objects.all()
    if request.method =="POST":
        exam=request.POST.get("txt_type")
        date=request.POST.get("txt_date")
        semesterid=tbl_semester.objects.get(id=request.POST.get("sel_semester"))
        courseid=tbl_course.objects.get(id=request.POST.get("sel_course"))
        academicyearid=tbl_academicyear.objects.get(id=request.POST.get("sel_academicyear"))
        tbl_exam.objects.create(exam_date=date,exam_type=exam,semester=semesterid,course=courseid,academicyear=academicyearid)
        return render(request,"Admin/Exam.html",{'msg':"Data Inserted",'examdata':examdata})
    else:
        return render(request,"Admin/Exam.html",{'departmentdata':departmentdata,'coursedata':coursedata,'semesterdata':semesterdata,'academicyeardata':academicyeardata,'examdata':examdata})

def delexam(request,did):
    tbl_exam.objects.get(id=did).delete()
    return redirect("Admin:Exam")

def ViewCertificateRequest(request):
    data=tbl_certificaterequest.objects.all()
    return render(request,"Admin/ViewCertificateRequest.html",{'data':data})

def Accept(request,aid):
    data = tbl_certificaterequest.objects.get(id=aid)
    data.certificaterequest_status = 1
    data.save()
    return redirect("Admin:ViewCertificateRequest")

def Reject(request,aid):
    data = tbl_certificaterequest.objects.get(id=rid)
    data.certificaterequest_status = 2
    data.save()
    return redirect("Admin:ViewCertificateRequest")

def ViewExamRegistration(request):
    data=tbl_examregistration.objects.all()
    return render(request,"Admin/ViewExamRegistration.html",{'data':data})

def Genre(request):
    data=tbl_genre.objects.all()
    if request.method =="POST":
        name=request.POST.get("txt_genre")
        tbl_genre.objects.create(genre_name=name)
        return render(request,"Admin/Genre.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Genre.html",{'data':data})

def delgenre(request,did):
    tbl_genre.objects.get(id=did).delete()
    return redirect("Admin:Genre")


def Book(request):
    genredata=tbl_genre.objects.all()
    bookdata=tbl_book.objects.all()
    if request.method =="POST":
        title=request.POST.get("txt_title")
        details=request.POST.get("txt_details")
        photo=request.FILES.get("file_photo")
        author=request.POST.get("txt_author")
        genreid=tbl_genre.objects.get(id=request.POST.get("sel_genre"))
        tbl_book.objects.create(book_title=title,book_details=details,book_photo=photo,book_author=author,genre=genreid)
        return render(request,"Admin/Book.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Book.html",{'genredata':genredata,'bookdata':bookdata})

def delbook(request,did):
    tbl_book.objects.get(id=did).delete()
    return redirect("Admin:Book")

def BookStock(request,bid):
    bookdata=tbl_stock.objects.all()
    if request.method =="POST":
        stock=request.POST.get("txt_stock")
        bookid=tbl_book.objects.get(id=bid)
        tbl_stock.objects.create(stock_count=stock,book=bookid)
        return render(request,"Admin/BookStock.html",{'msg':"Data Inserted",'data':bookdata})
    else:
        return render(request,"Admin/BookStock.html",{'data':bookdata})

def delstock(request,did):
    tbl_stock.objects.get(id=did).delete()
    return redirect("Admin:Book")


DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

HOURS = [
    ("1", "10:00 - 10:55"),
    ("2", "10:55 - 11:50"),
    ("3", "12:05 - 01:00"),
    ("4", "02:00 - 3:00"),
    ("5", "03:00 - 04:00"),
    
]


def timetable(request):
    department =  tbl_department.objects.all()
    courses = tbl_course.objects.all()
    semesters = tbl_semester.objects.all()

    course_id = request.GET.get("course")
    semester_id = request.GET.get("semester")

    subjects = tbl_subject.objects.none()
    timetable_data = tbl_timetable.objects.none()

    if course_id and semester_id:
        subjects = tbl_subject.objects.filter(
            course_id=course_id,
            semester_id=semester_id
        )
        timetable_data = tbl_timetable.objects.filter(
            course_id=course_id,
            semester_id=semester_id
        )

    return render(request, "Admin/Timetable.html", {
        "departmentdata":department,
        "courses": courses,
        "semesters": semesters,
        "subjects": subjects,
        "timetable": timetable_data,
        "days": DAYS,
        "hours": HOURS,
        "course_id": course_id,
        "semester_id": semester_id
    })

def save_timetable(request):
    academicyear = tbl_academicyear.objects.order_by('-id').first()
    tbl_timetable.objects.update_or_create(
        course_id=request.GET["course"],
        semester_id=request.GET["semester"],
        day=request.GET["day"],
        hour=request.GET["hour"],
        academicyear= academicyear,
        defaults={
            "subject_id": request.GET["subject"],
            "staff_id": tbl_assignsubject.objects.get(
                subject_id=request.GET["subject"]
            ).staff_id
        }
    )
    return JsonResponse({"status": "success"})


# def admin_view_timetable(request):
#     departmentdata = tbl_department.objects.all()
#     semesters = tbl_semester.objects.all()
#     courses = tbl_course.objects.all()

#     course_id = request.GET.get("course")
#     semester_id = request.GET.get("semester")

#     academicyear = tbl_academicyear.objects.order_by('-id').first()

#     timetable = tbl_timetable.objects.none()
#     subjects = tbl_subject.objects.none()

#     if course_id and semester_id and academicyear:
#         timetable = tbl_timetable.objects.filter(
#             course_id=course_id,
#             semester_id=semester_id,
#             academicyear=academicyear
#         )

#         subjects = tbl_subject.objects.filter(
#             course_id=course_id,
#             semester_id=semester_id
#         )

#     return render(request, "Admin/ViewTimeTable.html", {
#         "departmentdata": departmentdata,
#         "courses": courses,
#         "semesters": semesters,
#         "timetable": timetable,
#         "subjects": subjects,
#         "days": DAYS,
#         "hours": HOURS,
#         "course_id": course_id,
#         "semester_id": semester_id,
#         "academicyear": academicyear,
#     })



def admin_view_timetable(request):
    departmentdata = tbl_department.objects.all()
    semesters = tbl_semester.objects.all()
    courses = tbl_course.objects.all()

    course_id = request.GET.get("course")
    semester_id = request.GET.get("semester")
    edit = request.GET.get("edit")  # Edit mode flag

    academicyear = tbl_academicyear.objects.order_by('-id').first()

    timetable = tbl_timetable.objects.none()
    subjects = tbl_subject.objects.none()

    if course_id and semester_id and academicyear:
        timetable = tbl_timetable.objects.filter(
            course_id=course_id,
            semester_id=semester_id,
            academicyear=academicyear
        )

        subjects = tbl_subject.objects.filter(
            course_id=course_id,
            semester_id=semester_id
        )

    return render(request, "Admin/ViewTimeTable.html", {
        "departmentdata": departmentdata,
        "semesters": semesters,
        "courses": courses,
        "timetable": timetable,
        "subjects": subjects,
        "days": DAYS,
        "hours": HOURS,
        "course_id": course_id,
        "semester_id": semester_id,
        "academicyear": academicyear,
        "edit": edit
    })

def ViewLeaveRequest(request):
    data=tbl_leave.objects.all()
    return render(request,"Admin/ViewLeaveRequest.html",{'data':data})

def Accept(request,aid):
    data = tbl_leave.objects.get(id=aid)
    data.leave_status = 1
    data.save()
    return redirect("Admin:ViewLeaveRequest")

def Reject(request,rid):
    data = tbl_leave.objects.get(id=rid)
    data.leave_status = 2
    data.save()
    return redirect("Admin:ViewLeaveRequest")

def Announcement(request):
    data=tbl_info.objects.all()
    if request.method =="POST":
        title=request.POST.get("txt_title")
        details=request.POST.get("txt_details")
        file=request.FILES.get("file_information")
        tbl_info.objects.create(info_title=title,info_details=details,info_file=file)
        return render(request,"Admin/Announcement.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Announcement.html",{'data':data})

def delinfo(request,did):
    tbl_info.objects.get(id=did).delete()
    return redirect("Admin:Announcement")


