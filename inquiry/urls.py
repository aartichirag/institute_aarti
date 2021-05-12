from django.urls import path
from .views import NewInquiry,ViewInquiry,UpdateInquiry,DetailInquiry

urlpatterns=[
    path("new/",NewInquiry.as_view(), name="inquiry-new"),
    path("view/",ViewInquiry.as_view(), name="inquiry-view"),
    path("update/<int:pk>",UpdateInquiry.as_view(), name="inquiry-update"),
    path("detail/<int:pk>",DetailInquiry.as_view(), name="inquiry-detail")
]