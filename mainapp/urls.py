from django.conf.urls.static import static
from django.urls import path
from . import views
from NewClass import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('employees', views.all_employees, name="all"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('search', views.search_employees, name="search"),
    path('employees/<int:emp_id>', views.employee_details, name="details"),
    path('employees/delete/<int:emp_id>', views.employee_delete, name="delete"),
    path('employees/update/<int:emp_id>', views.employee_update, name="update"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)