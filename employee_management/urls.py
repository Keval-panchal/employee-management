from django.urls import path 
from  . import views
urlpatterns = [
    path('',views.Employee_add ),
    path('views/',views.Employee_view)

]