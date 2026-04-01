from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db import models
from .models import Issue
from datetime import datetime
import uuid


def home(request):
    """Home page - public access"""
    return render(request, 'reports/home.html')


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'reports/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'reports/register.html')
        
        if email and User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'reports/register.html')
        
        role = request.POST.get('role', 'user')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()
        
        # Log the user in after registration
        login(request, user)
        messages.success(request, f'Account created successfully! Welcome, {username}!')
        return redirect('dashboard')
    
    return render(request, 'reports/register.html')


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            
            # Redirect to the page user was trying to access
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'reports/login.html')


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    """User dashboard showing their reported issues - REQUIRES LOGIN"""
    # Get all issues for the logged-in user
    issues = Issue.objects.filter(user=request.user)
    
    # Statistics
    total_issues = issues.count()
    pending = issues.filter(status='Pending').count()
    in_progress = issues.filter(status='In Progress').count()
    resolved = issues.filter(status='Resolved').count()
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        issues = issues.filter(
            models.Q(tracking_id__icontains=search_query) |
            models.Q(issue_type__icontains=search_query) |
            models.Q(location__icontains=search_query) |
            models.Q(description__icontains=search_query)
        )
    
    context = {
        'issues': issues,
        'total_issues': total_issues,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
        'search_query': search_query,
    }
    return render(request, 'reports/dashboard.html', context)


@login_required(login_url='login')
def report_issue(request):
    """Report an issue - REQUIRES LOGIN"""
    if request.method == 'POST':
        issue_type = request.POST.get('issue_type')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number', '')
        
        # Validation
        if not issue_type or not description or not location:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'reports/report.html')
        
        # Create the issue with the logged-in user
        issue = Issue.objects.create(
            user=request.user,
            issue_type=issue_type,
            description=description,
            location=location,
            contact_number=contact_number,
            status='Pending'
        )
        
        messages.success(request, f'Issue reported successfully! Your tracking ID: {issue.tracking_id}')
        return render(request, 'reports/report.html', {'tracking_id': issue.tracking_id})
    
    return render(request, 'reports/report.html')


@login_required(login_url='login')
def track_issue(request):
    """Track an issue - REQUIRES LOGIN"""
    status = None
    issue_details = None
    
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')
        try:
            # Users can only track their own issues
            issue = Issue.objects.get(tracking_id=tracking_id, user=request.user)
            status = issue.status
            issue_details = {
                'tracking_id': issue.tracking_id,
                'issue_type': issue.issue_type,
                'description': issue.description,
                'location': issue.location,
                'status': issue.status,
                'created_at': issue.created_at,
                'updated_at': issue.updated_at,
            }
            messages.success(request, f'Found issue: {tracking_id}')
        except Issue.DoesNotExist:
            messages.error(request, 'No issue found with that tracking ID. Please check and try again.')
    
    return render(request, 'reports/track.html', {'status': status, 'issue_details': issue_details})


@login_required(login_url='login')
def edit_issue(request, issue_id):
    """Edit an existing issue - REQUIRES LOGIN"""
    issue = get_object_or_404(Issue, id=issue_id, user=request.user)
    
    if request.method == 'POST':
        issue.issue_type = request.POST.get('issue_type', issue.issue_type)
        issue.description = request.POST.get('description', issue.description)
        issue.location = request.POST.get('location', issue.location)
        issue.contact_number = request.POST.get('contact_number', issue.contact_number)
        issue.save()
        
        messages.success(request, 'Issue updated successfully!')
        return redirect('dashboard')
    
    return render(request, 'reports/edit_issue.html', {'issue': issue})


@login_required(login_url='login')
def delete_issue(request, issue_id):
    """Delete an issue - REQUIRES LOGIN"""
    issue = get_object_or_404(Issue, id=issue_id, user=request.user)
    
    if request.method == 'POST':
        issue.delete()
        messages.success(request, 'Issue deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'reports/delete_issue.html', {'issue': issue})


@user_passes_test(lambda u: u.is_superuser or u.is_staff, login_url='login')
def admin_dashboard(request):
    """Admin dashboard showing all reported issues"""
    issues = Issue.objects.all()
    
    # Statistics
    total_issues = issues.count()
    pending = issues.filter(status='Pending').count()
    in_progress = issues.filter(status='In Progress').count()
    resolved = issues.filter(status='Resolved').count()
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        issues = issues.filter(
            models.Q(tracking_id__icontains=search_query) |
            models.Q(issue_type__icontains=search_query) |
            models.Q(location__icontains=search_query) |
            models.Q(description__icontains=search_query) |
            models.Q(user__username__icontains=search_query)
        )
    
    context = {
        'issues': issues,
        'total_issues': total_issues,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
        'search_query': search_query,
    }
    return render(request, 'reports/admin_dashboard.html', context)


@user_passes_test(lambda u: u.is_superuser or u.is_staff, login_url='login')
def update_issue_status(request, issue_id):
    """Update status of an issue from the admin dashboard"""
    issue = get_object_or_404(Issue, id=issue_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'In Progress', 'Resolved']:
            issue.status = new_status
            issue.save()
            messages.success(request, f'Status for {issue.tracking_id} updated to {new_status}.')
        else:
            messages.error(request, 'Invalid status selection.')
            
    return redirect('admin_dashboard')