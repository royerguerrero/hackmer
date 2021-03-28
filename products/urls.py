"""Products urls"""

# Django
from django.urls import path

# Views
from products import views

urlpatterns = [
    path('<slug:slug>/', views.ProductDetail.as_view(), name="product")
]