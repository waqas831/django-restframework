from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('see',views.see,name="see"),
    path('one/<int:id>',views.seeone,name="one")
]