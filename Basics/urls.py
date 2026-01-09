from django.urls import path
from Basics import views
urlpatterns = [
    path('Sum/',views.Sum),
    path('Calculator/',views.Calculator),
    path('Largest/',views.Largest),
    path("nlp/",views.nlp_query, name="nlp_query"),
]