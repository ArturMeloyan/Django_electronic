from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('computer/', views.ComputerListView.as_view(), name='computer'),
    path('contact/', views.ContactListView.as_view(), name='contact'),
    path('laptop/', views.LaptopListView.as_view(), name='laptop'),
    path('product/', views.ProductListView.as_view(), name='product'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout')

]