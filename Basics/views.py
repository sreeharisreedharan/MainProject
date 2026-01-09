from django.shortcuts import render

# Create your views here.

def Sum(request):
    if request.method == "POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        result=num1+num2
        return render(request,"Basics/Sum.html",{"result":result})
    else:
        return render(request,"Basics/Sum.html")
def Calculator(request):
    if request.method == "POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        op=request.POST.get("btn_submit")
        if op == "+":
            result=num1+num2
        elif op == "-":
            result=num1-num2
        elif op == "*":
            result=num1*num2
        elif op == "/":
            result=num1/num2    
        return render(request,"Basics/Calculator.html",{"result":result})
    else:
        return render(request,"Basics/Calculator.html")
def Largest(request):
    if request.method == "POST":
        num1=int(request.POST.get("txt_num1"))
        num2=int(request.POST.get("txt_num2"))
        num3=int(request.POST.get("txt_num3"))
        if num1 > num2:
            if num1 > num3:
                return render(request,"Basics/Largest.html",{"largest":num1})
            else:
                return render(request,"Basics/Largest.html",{"largest":num3})
        else:
            if num2 > num3:
                return render(request,"Basics/Largest.html",{"largest":num2})
            else:
                return render(request,"Basics/Largest.html",{"largest":num3})
    else:
        return render(request,"Basics/Largest.html")

from django.shortcuts import render
from .models import tbl_student, tbl_mark
from Basics.nlp_engine import *

def nlp_query(request):
    q = request.GET.get("q", "")
    parsed = parse_query(q)

    intent = parsed.get("intent")
    student = parsed.get("student")
    sem = parsed.get("semester")
    dept = parsed.get("department")

    context = {
        "query": q,
        "intent": intent,
        "student": student,
        "semester": sem,
        "department": dept,
        "results": None
    }

    # ---- 1. Marks query ----
    if intent == "get_marks" and student and sem:
        marks = tbl_mark.objects.filter(
            student__student_name__icontains=student,
            mark_sem=sem
        ).values("mark_subject", "mark_total")

        context["results"] = list(marks)
        context["type"] = "marks"
        return render(request, "Basics/nlp_results.html", context)

    # ---- 2. Student details ----
    if intent == "get_student" and student:
        details = tbl_student.objects.filter(
            student_name__icontains=student
        ).values()

        context["results"] = list(details)
        context["type"] = "student_details"
        return render(request, "Basics/nlp_results.html", context)

    # ---- 3. Department students ----
    if intent == "get_department" and dept:
        students = tbl_student.objects.filter(
            student_department__icontains=dept
        ).values()

        context["results"] = list(students)
        context["type"] = "department_students"
        return render(request, "Basics/nlp_results.html", context)

    # ---- 4. Unknown ----
    context["type"] = "unknown"
    return render(request, "Basics/nlp_results.html", context)
