from django.urls import path
from .views import addMissingChild, allFoundChild, nameFoundChild, FoundChild, index

urlpatterns=[
    path("addMissingChild/", addMissingChild),
    path("allFoundChild/", allFoundChild),
    path("nameFoundChild/", nameFoundChild),
    path("FoundChild/", FoundChild),
    path("", index),
]