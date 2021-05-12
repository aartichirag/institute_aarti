from django.urls import path
from .views import NewStudent,ViewStudent,UpdateStudent,DeleteStudent,StudentDetail
urlpatterns=[
    path("new/",NewStudent.as_view(),name="student-new"),
    path("view/",ViewStudent.as_view(),name="student-view"),
    path("update/<int:pk>",UpdateStudent.as_view(),name="student-update"),
    path("delete/<int:pk>",DeleteStudent.as_view(), name="student-delete"),
    path("detail/<int:pk>",StudentDetail.as_view(), name="student-detail")
]