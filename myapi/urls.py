from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('data',views.viewdata,name="data"),
    path('view/<int:id>',views.singleview,name="view")
]