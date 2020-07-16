from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit_md",views.edit_md,name="edit_md"),
    path("<str:name>",views.page_redirect, name="page_redirect"),
    path("search/",views.search, name="search") 
    
]
