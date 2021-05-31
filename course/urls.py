from django.urls import path
from .views import NewCourse,ViewCourse,UpdateCourse,DeleteCourse,get_fees,DetailCourse
from .views import get_course_chart_data
urlpatterns=[
    path("new/",NewCourse.as_view(), name="course-new"),
    path("view/",ViewCourse.as_view(), name="course-view"),
    path("update/<int:pk>",UpdateCourse.as_view(), name="course-update"),
    path("delete/<int:pk>",DeleteCourse.as_view(),name="course-delete"),
    path("detail/<int:pk>",DetailCourse.as_view(),name="course-detail"),
    path("get_fees/<int:course_id>/",get_fees,name="get_fees"),
    path("get_course_chart",get_course_chart_data,name="course-chart")
]