from django.contrib import admin
from .models import Detail
# Register your models here.
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['id','name','fname','age','address','city']
    list_filter = ['name','city']
    list_per_page = 5

