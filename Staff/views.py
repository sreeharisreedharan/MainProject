from django.shortcuts import render,redirect
from Admin.models import*
from Staff.models import*
from User.models import*
from django.utils import timezone
from datetime import datetime


# Create your views here.

def HomePage(request):
    return render(request,'Staff/HomePage.html')

def MyProfile(request):
    data=tbl_staff.objects.get(id=request.session['sid'])
    return render(request, 'Staff/MyProfile.html',{'data':data})

def EditProfile(request):
    data=tbl_staff.objects.get(id=request.session['sid'])
    staffp=data.staff_photo
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        photo=request.FILES.get("file_photo")
        data.staff_name=name
        data.staff_email=email
        data.staff_contact=contact
        if not photo:
            data.staff_photo=staffp
        else:
            data.staff_photo=photo
        data.save()
        return render(request, 'Staff/EditProfile.html', {'data':data,'msg':"Profile Updated"})  
    else:
        return render(request, 'Staff/EditProfile.html', {'data':data})

def ChangePassword(request):
    data=tbl_staff.objects.get(id=request.session['sid'])
    dbpass=data.staff_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassord=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if dbpass == oldpassword:
            data.staff_password=repassword
            data.save()
            return render(request, 'Staff/ChangePassword.html', {'msg':"Password Updated"})
        else:
            return render(request, 'Staff/ChangePassword.html' ,{'msg':"Password Incorrect"})

    return render(request, 'Staff/ChangePassword.html')

def ViewAssignedClass(request):
    data=tbl_assignclass.objects.filter(staff=request.session['sid'])
    return render(request,'Staff/ViewAssignedClass.html',{'data':data})

def StudentRegistration(request):
    assignclass = tbl_assignclass.objects.filter(staff=request.session['sid']).last()
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method == 'POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        gender=request.POST.get("txt_gender")
        dob=request.POST.get("txt_date")
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        photo=request.FILES.get("file_photo")
        password=request.POST.get("txt_password")
        repassword=request.POST.get("txt_repassword")
        if password == repassword:
            studentdata=tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_gender=gender,user_dob=dob,place=place,user_photo=photo,assignclass=assignclass,user_password=password)
            classsem= tbl_classsem.objects.filter(assignclass=assignclass).last()
            tbl_payment.objects.create(student=studentdata,semester=classsem.semester)
            return render(request, "Staff/StudentRegistration.html", {'msg':"Data Inserted"})
        else:
            return render(request, "Staff/StudentRegistration.html", {'msg':"Password Mismatched"})

    else:
        return render(request, "Staff/StudentRegistration.html", {'dis':districtdata,'plc':placedata})

def AjaxPlace(request):
    place=tbl_place.objects.filter(district=request.GET.get('disid'))
    return render(request,"Staff/AjaxPlace.html",{'data':place})

def ViewMySubject(request):
    data=tbl_assignsubject.objects.filter(staff=request.session['sid'])
    return render(request,'Staff/ViewMySubject.html',{'data':data})

def ClassSem(request,aid):
    semesterdata=tbl_semester.objects.all()
    classsemdata=tbl_classsem.objects.all()
    if request.method =="POST":
        semester=tbl_semester.objects.get(id=request.POST.get('sel_semester'))
        assignclassid=tbl_assignclass.objects.get(id=aid)
        tbl_classsem.objects.create(semester=semester,assignclass=assignclassid)
        return render(request,'Staff/ClassSem.html',{'msg':"Data Inserted",'semesterdata':semesterdata})
    else:
        return render(request,'Staff/ClassSem.html',{'semesterdata':semesterdata,'classsemdata':classsemdata})

def delclasssem(request,did):
    tbl_classsem.objects.get(id=did).delete()
    return redirect("Staff:ViewAssignedClass")

def Notes(request):
    staff = tbl_staff.objects.get(id=request.session['sid'])
    coursedata=tbl_course.objects.filter(department=staff.department.id)
    semesterdata=tbl_semester.objects.all()
    notesdata=tbl_notes.objects.filter(id=request.session['sid'])
    if request.method =="POST":
        title=request.POST.get("txt_title")
        file=request.FILES.get("file_notes")
        subjectid=tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        semesterid=tbl_semester.objects.get(id=request.POST.get('sel_semester'))
        tbl_notes.objects.create(notes_title=title,notes_file=file,subject=subjectid,staff=staff,semester=semesterid)
        return render(request,'Staff/Notes.html',{'msg':"Notes Inserted"})
    else:
        return render(request, 'Staff/Notes.html',{'coursedata':coursedata,'semesterdata':semesterdata,'notesdata':notesdata})

def AjaxSubject(request):
    subjectdata=tbl_assignsubject.objects.filter(subject__course=request.GET.get('cid'),subject__semester = request.GET.get("semid"),staff = request.session['sid'])
    return render(request,"Staff/AjaxSubject.html",{'data':subjectdata})

def delnotes(request,did):
    tbl_notes.objects.get(id=did).delete()
    return redirect("Staff:Notes")

def Assignments(request):
    staffid = tbl_staff.objects.get(id=request.session['sid'])
    assignmentdata=tbl_assignments.objects.all()
    if request.method =="POST":
        title=request.POST.get("txt_title")
        topic=request.FILES.get("file_topic")
        lastdate=request.POST.get("txt_date")
        tbl_assignments.objects.create(assignments_title=title,assignments_topic=topic,assignments_duedate=lastdate,staff=staffid)
        return render(request,"Staff/Assignments.html",{'msg':"Assignment Inserted"})
    else:
        return render(request,"Staff/Assignments.html",{'assignmentdata':assignmentdata})

def delassignments(request,did):
    tbl_assignments.objects.get(id=did).delete()
    return redirect("Staff:Assignments")

def ViewUploads(request,aid):
    assignmentbodydata=tbl_assignmentbody.objects.filter(assignment=aid)
    return render(request,"Staff/ViewUploads.html",{'data':assignmentbodydata})  

def Mark(request,id):
    editdata=tbl_assignmentbody.objects.get(id=id)
    if request.method =="POST":
        mark=request.POST.get('txt_mark')
        editdata.assignmentbody_status = 1
        editdata.assignmentbody_mark = mark
        editdata.save()
        return render(request,"Staff/Mark.html",{'msg':"Mark Inserted"})  
    else:
        return render(request,"Staff/Mark.html")


def MyStudents(request):
    studentdata=tbl_user.objects.filter(assignclass__staff=request.session['sid'])
    return render(request,"Staff/MyStudents.html",{'data':studentdata})

def ViewStudents(request,id):
    studentdata=tbl_user.objects.filter(assignclass=id)
    return render(request,"Staff/ViewStudents.html",{'data':studentdata})

def ViewClass(request):
    staff=tbl_staff.objects.get(id=request.session['sid'])
    coursedata=tbl_course.objects.filter(department=staff.department.id)
    academicdata=tbl_academicyear.objects.all()
    return render(request,"Staff/ViewClass.html",{'coursedata':coursedata,'data':academicdata})

def AjaxClass(request):
    classdata=tbl_class.objects.filter(course=request.GET.get('cid'))
    return render(request,"Staff/AjaxClass.html",{'data':classdata})

def AjaxClasses(request):
    if request.GET.get('cid') !="" and request.GET.get('aid') !="":
        classdata=tbl_assignclass.objects.filter(classid=request.GET.get('cid'),academicyear=request.GET.get('aid'))
        return render(request,"Staff/AjaxClasses.html",{'data':classdata})
    else:
        return render(request,"Staff/AjaxClasses.html")

def InternalMark(request,sid):
    semesterdata=tbl_semester.objects.all()
    subjectdata=tbl_subject.objects.all()
    internalmarkdata=tbl_internalmark.objects.filter(student=sid)
    if request.method =="POST":
        mark=request.POST.get('txt_mark')
        subjectid=tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        studentid=tbl_user.objects.get(id=sid)
        tbl_internalmark.objects.create(internalmark_mark=mark,subject=subjectid,student=studentid)
        return render(request,"Staff/InternalMark.html",{'msg':"Internal Mark Inserted"})
    else:
        return render(request,"Staff/InternalMark.html",{'subject':subjectdata,'semester':semesterdata,'internalmark':internalmarkdata})

def AjaxSubjects(request):
    assignsubjectdata=tbl_assignsubject.objects.filter(staff=request.session['sid'],subject__semester=request.GET.get("semid"))
    return render(request,"Staff/AjaxSubjects.html",{'data':assignsubjectdata})


def delinternalmark(request,did):
    tbl_internalmark.objects.get(id=did).delete()
    return redirect("Staff:ViewClass")


DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

HOURS = [
    ("1", "10:00 - 10:55"),
    ("2", "10:55 - 11:50"),
    ("3", "12:05 - 01:00"),
    ("4", "02:00 - 03:00"),
    ("5", "03:00 - 04:00"),
]

def ViewTimeTable(request):
    staff = tbl_staff.objects.get(id=request.session["sid"])
    academicyear = tbl_academicyear.objects.order_by('-id').first()
    timetable = tbl_timetable.objects.none()
    if academicyear:
        timetable = tbl_timetable.objects.filter(
            staff=staff,
            academicyear=academicyear
        )
    return render(request, "Staff/ViewTimeTable.html", {
        "staff": staff,
        "timetable": timetable,
        "days": DAYS,
        "hours": HOURS,
        "academicyear": academicyear
    })



def staff_mark_attendance(request):
    staff = tbl_staff.objects.get(id=request.session["sid"])
    academicyear = tbl_academicyear.objects.order_by('-id').first()
    today_day = timezone.now().strftime("%A")  # Monday, Tuesday etc.
    current_hour = get_current_hour()  # helper function we define below

    # Get timetable for today and this hour
    timetable_entries = tbl_timetable.objects.filter(
        staff=staff,
        academicyear=academicyear,
        day=today_day,
        hour=current_hour
    )

    attendance_data = []
    for t in timetable_entries:
        # Get students of this class
        students = tbl_user.objects.filter(assignclass__classid=t.course)
        for s in students:
            # Get existing attendance if exists
            att = tbl_attendance.objects.filter(
                student=s,
                subject=t.subject,
                staff=staff,
                course=t.course,
                semester=t.semester,
                academicyear=academicyear,
                date=timezone.now().date(),
                hour=current_hour
            ).first()
            attendance_data.append({
                "student": s,
                "subject": t.subject,
                "attendance": att.status if att else "Absent"
            })

    return render(request, "Staff/MarkAttendance.html", {
        "staff": staff,
        "attendance_data": attendance_data,
        "current_hour": current_hour,
        "day": today_day
    })



# def save_attendance(request):
#     if request.method == "POST":
#         staff = tbl_staff.objects.get(id=request.session["sid"])
#         academicyear = tbl_academicyear.objects.order_by('-id').first()
#         today_day = request.POST.get("day")
#         hour = request.POST.get("hour")
#         date_today = timezone.now().date()

#         # Find timetable entries for this staff and hour
#         timetable_entries = tbl_timetable.objects.filter(
#             staff=staff,
#             academicyear=academicyear,
#             day=today_day,
#             hour=hour
#         )

#         for t in timetable_entries:
#             students = tbl_user.objects.filter(assignclass__classid=t.course)
#             for s in students:
#                 status = "Present" if request.POST.get(f"student_{s.id}") else "Absent"
#                 tbl_attendance.objects.update_or_create(
#                     student=s,
#                     subject=t.subject,
#                     staff=staff,
#                     course=t.course,
#                     semester=t.semester,
#                     academicyear=academicyear,
#                     date=date_today,
#                     hour=hour,
#                     defaults={"status": status}
#                 )

#         return redirect("Staff:mark_attendance")


# def get_current_hour():
#     now = timezone.localtime()
#     hour_min = now.hour * 60 + now.minute

#     if 10*60 <= hour_min < 10*60 + 55:    return "1"
#     elif 10*60+55 <= hour_min < 11*60+50: return "2"
#     elif 12*60+5 <= hour_min < 13*60:     return "3"
#     elif 14*60 <= hour_min < 15*60:       return "4"
#     elif 15*60 <= hour_min < 16*60:       return "5"
#     else: return None




def staff_attendance(request):
    staff = tbl_staff.objects.get(id=request.session["sid"])
    academicyear = tbl_academicyear.objects.order_by('-id').first()

    departments = tbl_department.objects.all()
    semesters = tbl_semester.objects.all()
    courses = tbl_course.objects.none()

    selected_students = []

    selected_department = request.GET.get("department")
    selected_course = request.GET.get("course")
    selected_semester = request.GET.get("semester")
    selected_hour = request.GET.get("hour")
    selected_day = request.GET.get("day")

    # Filter courses by department
    if selected_department:
        courses = tbl_course.objects.filter(department_id=selected_department)

    # Load students only if all required selections exist
    if all([selected_course, selected_semester, selected_hour, selected_day]):

        timetable_entries = tbl_timetable.objects.filter(
            staff=staff,
            course_id=selected_course,
            semester_id=selected_semester,
            hour=selected_hour,
            day=selected_day,
            academicyear=academicyear
        )

        for tt in timetable_entries:
            students = tbl_user.objects.filter(
                assignclass__classid__course=tt.course
            )

            for student in students:
                attendance = tbl_attendance.objects.filter(
                    student=student,
                    subject=tt.subject,
                    staff=staff,
                    course=tt.course,
                    semester=tt.semester,
                    academicyear=academicyear,
                    date=timezone.now().date(),
                    hour=selected_hour
                ).first()

                selected_students.append({
                    "student": student,
                    "subject": tt.subject,
                    "attendance": attendance.status if attendance else 0
                })

    return render(request, "Staff/MarkAttendance.html", {
        "staff": staff,
        "departments": departments,
        "courses": courses,
        "semesters": semesters,
        "days": DAYS,
        "hours": HOURS,

        "selected_students": selected_students,
        "selected_department": selected_department,
        "selected_course": selected_course,
        "selected_semester": selected_semester,
        "selected_hour": selected_hour,
        "selected_day": selected_day,
    })


def save_attendance_selection(request):
    if request.method == "POST":

        staff = tbl_staff.objects.get(id=request.session["sid"])
        academicyear = tbl_academicyear.objects.order_by('-id').first()

        hour = request.POST.get("hour")
        day = request.POST.get("day")
        course_id = request.POST.get("course")
        semester_id = request.POST.get("semester")
        today = timezone.now().date()

        timetable_entries = tbl_timetable.objects.filter(
            staff=staff,
            course_id=course_id,
            semester_id=semester_id,
            hour=hour,
            day=day,
            academicyear=academicyear
        )

        for tt in timetable_entries:
            students = tbl_user.objects.filter(
                assignclass__classid__course=tt.course
            )

            for student in students:
                # ✅ FIXED NAME
                status = request.POST.get(
                    f"attendance_{student.id}", "0"
                )

                tbl_attendance.objects.update_or_create(
                    student=student,
                    subject=tt.subject,
                    staff=staff,
                    course=tt.course,
                    semester=tt.semester,
                    academicyear=academicyear,
                    date=today,
                    hour=hour,
                    defaults={"status": int(status)}
                )

        return redirect("Staff:staff_attendance")




def Leave(request):
    staffid = tbl_staff.objects.get(id=request.session['sid'])
    leavedata=tbl_leave.objects.filter(staff=request.session['sid'])
    if request.method =="POST":
        fromdate=request.POST.get('txt_date')
        todate=request.POST.get('txt_date')
        reason=request.POST.get('txt_reason')
        tbl_leave.objects.create(leave_fromdate=fromdate,leave_todate=todate,leave_reason=reason,staff=staffid)
        return render(request,"Staff/Leave.html",{'msg':"Leave request Submitted"})
    else:
        return render(request,"Staff/Leave.html",{'data':leavedata})

def delleave(request,did):
    tbl_leave.objects.get(id=did).delete()
    return redirect("Staff:Leave")

def IssuedBooks(request):
    issuedata=tbl_issue.objects.all()
    return render(request,"Staff/IssuedBooks.html",{'data':issuedata})

def returnbook(request,id):
    data = tbl_issue.objects.get(id=id)
    data.issue_status = 0
    data.save()
    return redirect("Staff:IssuedBooks")

