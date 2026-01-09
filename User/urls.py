from django.urls import path
from User import views

app_name = "User"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('editcomplaint/<int:eid>',views.editcomplaint,name="editcomplaint"),
    path('delcomplaint/<int:did>',views.delcomplaint,name="delcomplaint"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('CertificateRequest/',views.CertificateRequest,name="CertificateRequest"),
    path('delcertificate/<int:did>',views.delcertificate,name="delcertificate"),
    path('ViewExam/',views.ViewExam,name="ViewExam"),
    path('apply/<int:eid>',views.apply,name="apply"),
    path('ViewBook/',views.ViewBook,name="ViewBook"),
    path('ViewNotes/',views.ViewNotes,name="ViewNotes"),
    path('AjaxNotes/',views.AjaxNotes,name="AjaxNotes"),
    path('ViewAssignments/',views.ViewAssignments,name="ViewAssignments"),
    path('UploadAssignment/',views.UploadAssignment,name="UploadAssignment"),
    path('UploadAssignment/<int:aid>',views.UploadAssignment,name="UploadAssignment"),
    path('MyAssignments/',views.MyAssignments,name="MyAssignments"),
    path('MyInternalMark/',views.MyInternalMark,name="MyInternalMark"),
    path('AjaxSubject/',views.AjaxSubject,name="AjaxSubject"),

    path("ViewTimeTable/", views.ViewTimeTable, name="ViewTimeTable"),
    path("ViewAnnouncement/",views.ViewAnnouncement,name="ViewAnnouncement"),

]
    