from django.shortcuts import render,redirect
from Guest.models import *
from Staff.models import*

# Create your views here.


def Login(request):
    if request.method == 'POST':
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        staffcount=tbl_staff.objects.filter(staff_email=email,staff_password=password).count()
        if admincount > 0:
            adminData=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=adminData.id
            return redirect('Admin:HomePage')
        if usercount > 0:
            userData=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userData.id
            return redirect('User:HomePage')
        if staffcount > 0:
            staffdata=tbl_staff.objects.get(staff_email=email,staff_password=password)
            request.session['sid']=staffdata.id
            return redirect('Staff:HomePage')
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid Login"})
    else:
        return render(request,"Guest/Login.html")





