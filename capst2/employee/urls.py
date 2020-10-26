from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_employees,name='all_Employees'),
    path('home/', views.home_view, name='Home'),
    path('EmployeeAdd/', views.add_employees,name='Employee_Add'),
    path('EmployeeEdit/<int:id>', views.edit_employees,name='Employee_Edit'),
    path('EmployeeView/<int:id>', views.one_employee,name='Employee_View'),
    path('EmployeeDelete/<int:id>', views.delete_employee,name='Employee_Delete'),
]
