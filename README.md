# Ticket-Management
🎫 Ticket Management API (Django + DRF + JWT)

A RESTful Ticket Management System built using Django, Django REST Framework, PostgreSQL, and JWT Authentication.
This API allows authenticated users to:
Create tickets
View tickets
Update tickets
Delete tickets
Filter, search, order, and paginate tickets

🚀 Features

✅ JWT Authentication (Login & Token Refresh)
✅ Protected API Endpoints
✅ Ticket CRUD Operations
✅ Filtering (category, status)
✅ Search (title & description)
✅ Ordering (any field)
✅ Pagination
✅ Caching (60 seconds)
✅ PostgreSQL Database

🛠️ Tech Stack
Python
Django 6.x
Django REST Framework
Simple JWT
PostgreSQL
LocMem Cache

📂 Project Structure

ticket/
│
├── ticket/                
│   ├── settings.py
│   ├── urls.py
│
├── ticketraiser/          
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── manage.py
└── README.md

Allowed Choices
1.Category
-> classroom
-> hostel
-> network
2.Priority
->low
->medium
->high
3.Status
->open
->in-progress
->closed

📄 Pagination
-> Page size: 2 tickets per page

⚡ Caching
GET requests cached for 60 seconds
Uses Local Memory Cache

🧠 API Flow
Client Request
    ↓
JWT Authentication
    ↓
Filtering / Search / Ordering
    ↓
Pagination
    ↓
Serialization
    ↓
Database
    ↓
JSON Response
