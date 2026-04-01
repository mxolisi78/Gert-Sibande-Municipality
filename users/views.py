from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue  # You'll need to create this model
import uuid
from datetime import datetime



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
            return render(request, 'users/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'users/register.html')
        
        if email and User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'users/register.html')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Log the user in after registration
        login(request, user)
        messages.success(request, f'Account created successfully! Welcome, {username}!')
        return redirect('dashboard')
    
    return render(request, 'users/register.html')


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
    
    return render(request, 'users/login.html')


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    """User dashboard showing their reported issues"""
    # Get all issues for the logged-in user
    issues = Issue.objects.filter(user=request.user).order_by('-created_at')
    
    # Statistics
    total_issues = issues.count()
    pending = issues.filter(status='Pending').count()
    in_progress = issues.filter(status='In Progress').count()
    resolved = issues.filter(status='Resolved').count()
    
    # Search functionality
    search_query = request.GET.get('q', '')
    if search_query:
        issues = issues.filter(
            tracking_id__icontains=search_query
        ) | issues.filter(
            issue_type__icontains=search_query
        ) | issues.filter(
            location__icontains=search_query
        )
    
    context = {
        'issues': issues,
        'total_issues': total_issues,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
        'search_query': search_query,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def report_issue(request):
    """Report an issue - requires authentication"""
    if request.method == 'POST':
        issue_type = request.POST.get('issue_type')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number', '')
        
        # Validation
        if not issue_type or not description or not location:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'report.html')
        
        # Generate a unique tracking ID
        tracking_id = f"GTS-{datetime.now().strftime('%Y%m')}-{uuid.uuid4().hex[:6].upper()}"
        
        # Create the issue with the logged-in user
        issue = Issue.objects.create(
            tracking_id=tracking_id,
            user=request.user,
            issue_type=issue_type,
            description=description,
            location=location,
            contact_number=contact_number,
            status='Pending'
        )
        
        messages.success(request, f'Issue reported successfully! Your tracking ID: {tracking_id}')
        return render(request, 'report.html', {'tracking_id': tracking_id})
    
    return render(request, 'report.html')


@login_required(login_url='login')
def track_issue(request):
    """Track an issue - requires authentication"""
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
    
    return render(request, 'track.html', {'status': status, 'issue_details': issue_details})


@login_required(login_url='login')
def edit_issue(request, issue_id):
    """Edit an existing issue - requires authentication"""
    issue = get_object_or_404(Issue, id=issue_id, user=request.user)
    
    if request.method == 'POST':
        issue.issue_type = request.POST.get('issue_type', issue.issue_type)
        issue.description = request.POST.get('description', issue.description)
        issue.location = request.POST.get('location', issue.location)
        issue.contact_number = request.POST.get('contact_number', issue.contact_number)
        issue.save()
        
        messages.success(request, 'Issue updated successfully!')
        return redirect('dashboard')
    
    return render(request, 'edit_issue.html', {'issue': issue})


@login_required(login_url='login')
def delete_issue(request, issue_id):
    """Delete an issue - requires authentication"""
    issue = get_object_or_404(Issue, id=issue_id, user=request.user)
    
    if request.method == 'POST':
        issue.delete()
        messages.success(request, 'Issue deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'delete_issue.html', {'issue': issue})


def home(request):
    """Home page - public access"""
    return render(request, 'home.html')


def about(request):
    """About page - public access"""
    return render(request, 'about.html')


def contact(request):
    """Contact page - public access"""
    return render(request, 'contact.html')