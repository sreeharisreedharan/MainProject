from django.shortcuts import render,redirect
from Guest.models import *
from User.models import*
from Staff.models import*
from Admin.models import*
# Create your views here.

def HomePage(request):
    return render(request, 'User/HomePage.html')

def MyProfile(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    return render(request, 'User/MyProfile.html',{'data':data})

def EditProfile(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    userp=data.user_photo
    if request.method=='POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("file_photo")
        data.user_name=name
        data.user_email=email
        data.user_contact=contact
        data.user_address=address
        if not photo:
            data.user_photo=userp
        else:
            data.user_photo=photo
        data.save()
        return render(request, 'User/EditProfile.html',{'data':data ,'msg':"Data Updated"})
    else:
        return render(request, 'User/EditProfile.html',{'data':data})

def ChangePassword(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    dbpass=data.user_password
    if request.method == 'POST':
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if dbpass == oldpassword:
            data.user_password=repassword
            data.save()
            return render(request, 'User/ChangePassword.html', {'msg':"Password Updated"})   
        else:
            return render(request, 'User/ChangePassword.html', {'msg':"Password Incorrect"})     

    return render(request, 'User/ChangePassword.html')

def Complaint(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    complaintdata=tbl_complaint.objects.filter(user=request.session['uid'])
    if request.method == 'POST':
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=data)
        return render(request, 'User/Complaint.html', {'msg':"Complaint Registered",'data':data})
    else:
        return render(request, 'User/Complaint.html', {'complaintdata':complaintdata})

def delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:Complaint")

def editcomplaint(request,eid):
    editdata=tbl_complaint.objects.get(id=eid)
    complaintdata=tbl_complaint.objects.filter(user=request.session['uid'])

    if request.method == 'POST':
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        editdata.complaint_title = title
        editdata.complaint_content = content
        editdata.save()
        return render(request, "User/Complaint.html", {'msg':"Data Updated"})
    else:
        return render(request, "User/Complaint.html", {'editdata':editdata,'complaintdata':complaintdata})

def Feedback(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        feedback=request.POST.get("txt_feedback")
        tbl_feedback.objects.create(feedback_content=feedback,user=data)
        return render(request, "User/Feedback.html", {'msg':"Feedback Inserted",'data':data})
    else:
        return render(request, "User/Feedback.html")

def CertificateRequest(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    certificatedata=tbl_certificaterequest.objects.filter(user=request.session['uid'])
    if request.method =="POST":
        certificatetype=request.POST.get("txt_type")
        content=request.POST.get("txt_content")
        tbl_certificaterequest.objects.create(certificaterequest_type=certificatetype,certificaterequest_content=content,user=data)
        return render(request,"User/CertificateRequest.html",{'msg':"Request Submitted"})
    else:
        return render(request,"User/CertificateRequest.html",{'certificatedata':certificatedata})

def delcertificate(request,did):
    tbl_certificaterequest.objects.get(id=did).delete()
    return redirect("User:CertificateRequest")

def ViewExam(request):
    examdata=tbl_exam.objects.all()
    return render(request,"User/ViewExam.html",{'examdata':examdata})

def apply(request,eid):
    data=tbl_user.objects.get(id=request.session['uid'])
    examid=tbl_exam.objects.get(id=eid)
    tbl_examregistration.objects.create(student=data,exam=examid)
    return render(request,"User/ViewExam.html",{'msg':"Applied Successfully"})

def ViewBook(request):
    genredata=tbl_genre.objects.all()
    bookdata=tbl_book.objects.all()
    if request.method =="POST":
        name=request.POST.get("txt_name")
        genreid=request.POST.get("sel_genre")
        if genreid != "":
            book=tbl_book.objects.filter(genre=genreid)
            return render(request,"User/ViewBook.html",{'book':book,'genredata':genredata})
        elif name != "" and genreid == "":
            book = tbl_book.objects.filter(book_title__icontains=name)
            return render(request,"User/ViewBook.html",{'book':book,'genredata':genredata})
        elif genreid !="" and name != "":
            book  = tbl_book.objects.filter(book_title__icontains=name,generid=gener)
            return render(request,"User/ViewBook.html",{'book':book,'genredata':genredata})
    else:
        return render(request,"User/ViewBook.html",{'genredata':genredata,'book':bookdata})

def ViewNotes(request):
    semesterdata=tbl_semester.objects.all()
    notesdata=tbl_notes.objects.all()
    return render(request,"User/ViewNotes.html",{'notesdata':notesdata,'semesterdata':semesterdata})

def AjaxNotes(request):
    assign = tbl_user.objects.get(id=request.session['uid'])
    notesdata=tbl_notes.objects.filter(semester=request.GET.get('semid'),staff__tbl_assignclass__classid__course_id=assign.assignclass.classid.course)
    return render(request,"User/AjaxNotes.html",{'data':notesdata})
    
def ViewAssignments(request):
    studentdata=tbl_user.objects.get(id=request.session['uid'])
    assignclassid=studentdata.assignclass.id
    assignclassdata=tbl_assignclass.objects.get(id=assignclassid)
    staffid=assignclassdata.staff
    # print(staffid)
    assignmentdata=tbl_assignments.objects.filter(staff=staffid)
    return render(request,"User/ViewAssignments.html",{'assignmentdata':assignmentdata})

def UploadAssignment(request,aid):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        file=request.FILES.get("file_assignment")
        assignmentid=tbl_assignments.objects.get(id=aid)
        tbl_assignmentbody.objects.create(assignmentbody_file=file,user=user,assignment=assignmentid)
        return render(request,"User/UploadAssignment.html",{'msg':"Assignment Submitted"})
    else:
        return render(request,"User/UploadAssignment.html")

def MyAssignments(request):
    assignmentbodydata=tbl_assignmentbody.objects.filter(user=request.session['uid'])
    return render(request,"User/MyAssignments.html",{'data':assignmentbodydata})

def MyInternalMark(request):
    semesterdata=tbl_semester.objects.all()
    subjectdata=tbl_subject.objects.all()
    if request.method == "POST":
        semester=request.POST.get("sel_semester")
        subject=request.POST.get("sel_subject")
        subid=tbl_subject.objects.get(id=subject)
        if semester !="" and subject != "":
            internalmark  = tbl_internalmark.objects.filter(student=request.session['uid'],subject=subid)
            return render(request,"User/MyInternalMark.html",{'internalmark':internalmark,'semester':semesterdata})
        else:
            return render(request,"User/MyInternalMark.html",{'semester':semesterdata})
    else:
        return render(request,"User/MyInternalMark.html",{'semester':semesterdata})

def AjaxSubject(request):
    subjectdata=tbl_subject.objects.filter(semester=request.GET.get("semid"))
    return render(request,"User/AjaxSubject.html",{'data':subjectdata})


   

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

HOURS = [
    ("1", "10:00 - 10:55"),
    ("2", "10:55 - 11:50"),
    ("3", "12:05 - 01:00"),
    ("4", "02:00 - 03:00"),
    ("5", "03:00 - 04:00"),
]

def ViewTimeTable(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    assignclass = user.assignclass
    course = assignclass.classid.course
    current_semester = tbl_classsem.objects.order_by('assignclass_id').last()
    academicyear = tbl_academicyear.objects.order_by('-id').first()

    timetable = tbl_timetable.objects.none()

    if current_semester and academicyear:
        timetable = tbl_timetable.objects.filter(
            course=course,
            semester=current_semester.semester,
            academicyear=academicyear
        )

    return render(request, "User/ViewTimeTable.html", {
        "user": user,
        "timetable": timetable,
        "days": DAYS,
        "hours": HOURS,
        "semester": current_semester,
        "course": course,
        "academicyear": academicyear
    })

def ViewAnnouncement(request):
    data=tbl_info.objects.all()
    return render(request,"User/ViewAnnouncement.html",{'data':data})
