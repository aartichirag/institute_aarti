from django.urls import path
from .views import NewCertificate,ViewCertificate,UpdateCertificate,DeleteCertificate

urlpatterns=[
    path("new/",NewCertificate.as_view(),name="certificate-new"),
    path("view/",ViewCertificate.as_view(),name="certificate-view"),
    path("update/<int:pk>",UpdateCertificate.as_view(),name="certificate-update"),
    path("delete/<int:pk>",DeleteCertificate.as_view(),name="certificate-delete"),
]