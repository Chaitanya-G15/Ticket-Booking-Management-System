# 🎟️ Django Ticket Booking Management System

A Django-based web application for managing and booking tickets for events and shows. Users can register, log in, view available shows, and book tickets. Admins can manage show listings through a secure backend panel. The project is containerized using Docker for easy deployment and includes plans for Jenkins-based CI/CD in Phase 2.

---

## 🚀 Features

- User Registration & Authentication
- View and Book Tickets for Shows/Events
- Show Details: Title, Description, Date, Time, Available Seats
- Admin Panel for Managing Shows
- Dynamic Templates using Django Templating Engine
- PostgreSQL Integration
- Docker Support for Easy Deployment
- Jenkins CI/CD Setup 

---

## 🛠️ Tech Stack

- Python 3.10
- Django 4.x
- PostgreSQL (via Docker)
- HTML/CSS (Django Templates)
- Docker + Docker Compose
- Jenkins (coming soon for CI/CD)

---

## 🖥️ Setup Instructions

### ⚙️ Local Development

1. Clone the Repository
   git clone https://github.com/Chaitanya-G15/Ticket-Booking-Management-System.git
   cd Ticket-Booking-Management-System
2. Create virtual environment:
   python -m venv env
   env\Scripts\activate
   
3. Install dependencies:
   pip install -r requirements.txt
   
4. Run migrations:
   python manage.py migrate
   
5. Start development server:
   python manage.py runserver
   
6. Build & start containers:
   docker-compose up --build

7. Run migrations:
   docker-compose run web python manage.py migrate

8. Visit app:
   http://localhost:8000
 
![Screenshot 2025-04-24 210435](https://github.com/user-attachments/assets/04f721e5-ac30-4c53-9f1f-6ae7fe7524f1)
![Screenshot 2025-04-25 112608](https://github.com/user-attachments/assets/c545c7c2-8194-4126-8264-1493a385d424)
![Screenshot 2025-04-25 094541](https://github.com/user-attachments/assets/bd13f11c-3851-4180-89db-d4e2ff7958f5)
![Screenshot 2025-04-25 094532](https://github.com/user-attachments/assets/bd849a11-5ccd-46a7-9cf3-03dd1fe34c6b)
![Screenshot 2025-04-25 094516](https://github.com/user-attachments/assets/c91ae8b1-6669-47cf-be21-3231d6cefcaa)

