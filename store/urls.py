from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='HomePage'),
    path('productDetails/<slug:slug>/', views.ProductDetailView.as_view(), name='productDetails'),
]
