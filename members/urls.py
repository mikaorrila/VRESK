# members/urls.py

from django.urls import path
from members import views

urlpatterns = [
    path("", views.members_page, name="members"),
]
