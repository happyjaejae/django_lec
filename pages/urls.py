from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('customer_service_center/', views.customer_service_center),
    path('existing_product/', views.existing_product),
]