from django.urls import path
from .views import NewAddmission,ViewAddmission,UpdateAddmission,DeleteAddmission,DetailAddmission

urlpatterns=[
    path("new/",NewAddmission.as_view(),name="addmission-new"),
    path("view/",ViewAddmission.as_view(),name="addmission-view"),
    path("update/<int:pk>",UpdateAddmission.as_view(),name="addmission-update"),
    path("delete/<int:pk>",DeleteAddmission.as_view(),name="addmission-delete"),
    path("detail/<int:pk>",DetailAddmission.as_view(),name="addmission-detail")
]