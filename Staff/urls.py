from django.urls import path
from Staff import views

app_name = "Staff"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('ViewAssignedClass/',views.ViewAssignedClass,name="ViewAssignedClass"),
    path('StudentRegistration/',views.StudentRegistration,name="StudentRegistration"),
    path('AjaxPlace/',views.AjaxPlace,name="AjaxPlace"),
    path('ViewMySubject/',views.ViewMySubject,name="ViewMySubject"),
    path('ClassSem/',views.ClassSem,name="ClassSem"),
    path('ClassSem/<int:aid>',views.ClassSem,name="ClassSem"),
    path('delclasssem/<int:did>',views.delclasssem,name="delclasssem"),
    path('Notes/',views.Notes,name="Notes"),
    path('AjaxSubject/',views.AjaxSubject,name="AjaxSubject"),
    path('delnotes/<int:did>',views.delnotes,name="delnotes"),
    path('Assignments/',views.Assignments,name="Assignments"),
    path('delassignments/<int:did>',views.delassignments,name="delassignments"),
    path('ViewUploads/',views.ViewUploads,name="ViewUploads"),
    path('ViewUploads<int:aid>/',views.ViewUploads,name="ViewUploads"),
    path('Mark/',views.Mark,name="Mark"),
    path('Mark<int:id>/',views.Mark,name="Mark"),
    path('MyStudents/',views.MyStudents,name="MyStudents"),
    path('ViewStudents/',views.ViewStudents,name="ViewStudents"),
    path('ViewClass/',views.ViewClass,name="ViewClass"),
    path('AjaxClass/',views.AjaxClass,name="AjaxClass"),
    path('AjaxClasses/',views.AjaxClasses,name="AjaxClasses"),
    path('ViewStudents<int:id>',views.ViewStudents,name="ViewStudents"),
    path('InternalMark/',views.InternalMark,name="InternalMark"),
    path('AjaxSubjects/',views.AjaxSubjects,name="AjaxSubjects"),
    path('InternalMark<int:sid>/',views.InternalMark,name="InternalMark"),
    path('delinternalmark/<int:did>',views.delinternalmark,name="delinternalmark"),

    path("ViewTimeTable/", views.ViewTimeTable, name="ViewTimeTable"),
    path("staffattendance/", views.staff_attendance, name="staff_attendance"),
    path("staffattendance/save/", views.save_attendance_selection, name="save_attendance_selection"),
    path("staff_mark_attendance/",views.staff_mark_attendance,name="staff_mark_attendance"),
    path('Leave/',views.Leave,name="Leave"),
    path('delleave/<int:did>',views.delleave,name="delleave"),



      
]