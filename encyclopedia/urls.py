from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<str:page>",views.edit, name="edit"),
    path("<str:name>",views.page_redirect, name="page_redirect"),
    path("save_changes/<str:page_name>",views.save_changes,name="save_changes"),
    path("search/",views.search, name="search"),
    path("create/",views.create,name="create")
    
]
