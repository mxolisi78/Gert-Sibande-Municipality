from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reports/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reports/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reports/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reports/password_reset_complete.html'), name='password_reset_complete'),

    # Reports (all protected by @login_required)
    path('report/', views.report_issue, name='report'),
    path('track/', views.track_issue, name='track'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:issue_id>/', views.edit_issue, name='edit_issue'),
    path('delete/<int:issue_id>/', views.delete_issue, name='delete_issue'),
    
    # Admin
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-update-status/<int:issue_id>/', views.update_issue_status, name='update_issue_status'),
]