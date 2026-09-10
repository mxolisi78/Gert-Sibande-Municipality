
# Gert Sibande District Municipal Service Management System

![Django](https://img.shields.io/badge/Django-Web%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20Bootstrap-E34F26?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

## Overview

The **Gert Sibande District Municipal Service Management System** is a web-based municipal service platform developed using Django.

The system is designed to provide residents with a convenient digital platform for accessing municipal information, submitting service-related reports, tracking reported issues, and interacting with municipal services.

The project focuses on improving the digital experience between residents and the municipality by providing a structured, accessible, and user-friendly interface for reporting and managing municipal service requests.

---

## Project Purpose

The purpose of this project is to demonstrate how modern web technologies can be used to improve municipal service delivery and citizen engagement.

The system provides a centralized platform where residents can:

- Access municipal information
- Submit service-related issues
- Track submitted reports
- View the status of reported issues
- Manage their accounts
- Interact with municipal services through a digital platform

Municipal staff can use the system to manage submitted reports and monitor service requests.

---

## Key Features

### Resident Features

- User registration and authentication
- Secure login and logout
- Resident profile management
- Submit municipal service reports
- Provide descriptions of reported problems
- Track submitted reports
- View report status
- View previously submitted reports
- Access municipal information
- Responsive web interface

### Municipal Management Features

- Administrative dashboard
- View submitted service reports
- Manage reported issues
- Update report statuses
- Monitor service requests
- Manage registered users
- Centralized database management

### Report Management

The reporting functionality allows residents to submit issues that may require municipal attention.

Examples include:

- Water and sanitation problems
- Electricity-related issues
- Roads and potholes
- Waste management
- Street lighting
- Public infrastructure
- Other municipal service-related problems

---

## System Workflow

The general system workflow is:

```text
Resident
   |
   v
Register / Login
   |
   v
Resident Dashboard
   |
   v
Submit Municipal Report
   |
   v
Report Stored in Database
   |
   v
Municipal Staff Review
   |
   v
Status Updated
   |
   v
Resident Tracks Report

Technology Stack
Backend
Python
Django
Frontend
HTML5
CSS3
JavaScript
Bootstrap
Database
SQLite
Development Tools
Visual Studio Code
Git
GitHub
Python Virtual Environment
PowerShell

Project Structure

The project follows a Django-based structure similar to:

gert_sibande_system/
│
├── manage.py
│
├── gert_sibande_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── reports/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
├── static/
│
├── media/
│
├── db.sqlite3
│
├── requirements.txt
│
├── .gitignore
│
└── README.md



Installation and Setup

Follow the steps below to run the project locally.

1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/gert-sibande-system.git

Navigate into the project:

cd gert-sibande-system
2. Create a Virtual Environment

Windows:

python -m venv venv
3. Activate the Virtual Environment

PowerShell:

venv\Scripts\Activate.ps1

If activation is successful, the terminal should display:

(venv)

before the PowerShell prompt.

4. Install Dependencies

If requirements.txt is available:

pip install -r requirements.txt

Alternatively, install Django:

pip install django
5. Apply Database Migrations

Run:

python manage.py migrate
6. Create an Administrator Account

Create a Django superuser:

python manage.py createsuperuser

Follow the instructions displayed in the terminal.

7. Start the Development Server

Run:

python manage.py runserver

The application should then be available at:

http://127.0.0.1:8000/

Open the address in your web browser.

Django Administration

The Django administration interface can be accessed through:

http://127.0.0.1:8000/admin/

Administrators can use the Django admin interface to manage system data and monitor application records.

User Roles

The system is designed around different types of users.

Resident

Residents can:

Create an account
Log into the system
Submit municipal reports
View submitted reports
Track report progress
Manage their account information
Municipal Staff / Administrator

Authorized municipal users can:

View submitted reports
Manage reports
Update report statuses
Monitor service requests
Manage system information
Report Status

A municipal report can move through different stages of processing.

Example:

Submitted
    |
    v
Under Review
    |
    v
Assigned
    |
    v
In Progress
    |
    v
Resolved

This allows residents to understand the progress of their submitted service requests.

Security

The application uses Django's built-in security mechanisms, including:

User authentication
Password hashing
CSRF protection
Session management
Permission-based access
Django authentication middleware
Form validation

Sensitive configuration values should not be committed to GitHub.

Environment Variables

For production deployment, sensitive configuration should be stored using environment variables rather than directly inside the source code.

Examples include:

SECRET_KEY
DEBUG
DATABASE_URL
ALLOWED_HOSTS

A .env file should not be committed to GitHub.

Development Guidelines

When contributing to the project:

Create a separate branch for new features.
Write clean and readable code.
Follow Django conventions.
Test new functionality before committing.
Keep database migrations synchronized.
Write meaningful Git commit messages.
Do not commit passwords, API keys, or other secrets.

Example:

git checkout -b feature/report-tracking

Make changes and then:

git add .
git commit -m "Add report tracking functionality"
git push origin feature/report-tracking
Testing

Django tests can be executed using:

python manage.py test

Testing should be performed after implementing major functionality or modifying existing features.

Future Improvements

The project can be expanded with additional functionality such as:

Email notifications
SMS notifications
Report priority levels
Report assignment to municipal departments
Image uploads for service reports
GPS/location information
Interactive municipal dashboard
Advanced analytics
Search and filtering
Report export to PDF
Automated notifications when report status changes
REST API integration
Mobile application
PostgreSQL production database
Cloud deployment
Role-based permissions
Audit logging
Project Goals

The main goals of the project are to:

Improve digital access to municipal services
Provide residents with a simple reporting platform
Improve transparency in service-request management
Demonstrate practical Django development skills
Apply Human-Computer Interaction principles
Develop a realistic full-stack ICT project
Demonstrate database and web application development
Build a portfolio-ready software solution
Academic Context

This project was developed as part of an academic Human-Computer Interaction and web development context.

The system applies software development and HCI principles to a realistic municipal service-delivery scenario.

The project considers important usability principles including:

Simplicity
Accessibility
Consistency
Visibility of system status
User feedback
Clear navigation
Error prevention
Responsive design
Learning Outcomes

Through this project, the following technical skills are demonstrated:

Django web development
Python programming
Database design
Django ORM
User authentication
CRUD operations
HTML and CSS
Responsive web design
Git and GitHub
Software project organization
Human-Computer Interaction
User-centered design
Web application testing
Screenshots

Screenshots of the application will be added here as the system develops.

Home Page

Add screenshot here.

Login Page

Add screenshot here.

Registration Page

Add screenshot here.

Resident Dashboard

Add screenshot here.

Report Submission

Add screenshot here.

Report Tracking

Add screenshot here.

Administrator Dashboard

Add screenshot here.

Project Status

Current Status: 🚧 In Development

The core Django application is being developed and tested. Additional functionality, UI improvements, testing, and deployment features will be added progressively.

Author

Mxolisi Maseko

ICT Applications Development

Sol Plaatje University

License

This project is developed for educational and portfolio purposes.

If the project is later released as open source, an appropriate open-source license such as the MIT License can be added.

Acknowledgements

This project makes use of the following technologies and resources:

Django
Python
HTML5
CSS3
JavaScript
Bootstrap
SQLite
Git
GitHub
Disclaimer

This system is a software development and academic prototype and is not an official Gert Sibande District Municipality service platform unless formally authorized and deployed by the municipality.

Contact

For questions, suggestions, or collaboration regarding this project, please use the project's GitHub repository issue tracker or contact the project author.


### One important correction

You wrote **`ReadMe.dm`**. The correct filename is:

```text
README.md

Not:

ReadMe.dm

GitHub automatically recognizes README.md and displays it on the repository homepage.

Recommended next step

Once you've added the README, your project root should look roughly like:

gert_sibande_system/
│
├── manage.py
├── README.md        ← THIS FILE
├── requirements.txt
├── .gitignore
├── db.sqlite3
│
├── gert_sibande_system/
├── users/
├── reports/
├── templates/
└── static/

Then commit it:

git add README.md
git commit -m "Add professional project documentation"
git push