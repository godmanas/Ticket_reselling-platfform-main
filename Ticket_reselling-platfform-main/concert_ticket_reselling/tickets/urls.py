from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_seller, name='register_seller'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('login/', views.seller_login, name='seller_login'),
    path('about/', views.about, name='about'),
     path('password_reset/', CustomPasswordResetView.as_view(template_name='tickets/registration/password_reset.html'), name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='tickets/registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    
]
