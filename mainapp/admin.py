from django.contrib import admin
from . models import Employee

admin.site.site_header = "Wezesha System"

admin.site.index_title = "Wezesha"



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "dob", "disabled"]
    search_fields = ["name", "email"]
    list_filter = ["disabled"]

admin.site.register(Employee, EmployeeAdmin)
