from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('customer_service_center/', views.customer_service_center),
    path('customer_3/', views.customer_3),
    path('q_a/', views.q_a),
    path('gaesipan/', views.gaesipan),
    path('existing_product/', views.existing_product),
    path('exist_detail/', views.exist_detail),
]