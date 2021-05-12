from django.urls import path
from .views import NewPayment,ViewPayment,UpdatePayment,DetailPayment,DeletePayment

urlpatterns=[
    path("new/",NewPayment.as_view(),name="payment-new"),
    path("view/",ViewPayment.as_view(),name="payment-view"),
    path("update/<int:pk>",UpdatePayment.as_view(),name="payment-update"),
    path("detail/<int:pk>",DetailPayment.as_view(),name="payment-detail"),
    path("delete/<int:pk>",DeletePayment.as_view(),name="payment-delete"),
]