# members/urls.py

from django.urls import path
from members import views

urlpatterns = [
    path("", views.members_page, name="members"),
    path("groups/", views.members_groups, name="groups"),
    path("military/", views.members_military, name="military"),
    path("person/", views.members_person, name="person"),
]
