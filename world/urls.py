from django.urls import path
from django.views.generic import TemplateView

from world import views


urlpatterns = [
    path("", views.HomeView.as_view() , name="home"),

    path("updatedb/", views.update_location, name="updatedb"),
    path("notedb/", views.note, name="notedb"),


]


