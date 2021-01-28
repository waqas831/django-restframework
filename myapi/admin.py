from django.contrib import admin
from .models import Student
# Register your models here
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','fname','roll','semester','city']
    list_filter = ['name','city']
    list_per_page = 6

