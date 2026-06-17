# Django Blog & User Profile Application

A robust, full-stack web application built with Python and Django. This project features a dynamic blogging platform integrated with an automated user profile system, custom media/file uploads, and structured database relationships.

## 🚀 Features

- **User Authentication:** Built-in secure user registration, login, and logout.
- **Automated Profiles:** Utilizes Django **Signals** (`post_save`) to automatically instantiate a user profile upon registration.
- **Custom Profiles:** Users can personalize their accounts with a custom bio and profile picture avatar.
- **Dynamic Media Handling:** Secure storage and delivery configuration for user-uploaded files (`multipart/form-data`).
- **Styling:** Styled with a modern, clean UI powered by Tailwind CSS.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL / SQLite (Default)
- **Frontend:** HTML5, Tailwind CSS

---

## 📋 Prerequisites

Ensure you have the following installed on your local machine:
- Python 3.10+
- pip (Python package installer)

---

## ⚙️ Installation & Setup

Follow these steps to get your development environment up and running:

### 1. Clone the Repository
```bash
git clone (https://github.com/rojeshdahal/blog_project.git)
cd blog_project
2. Set Up a Virtual Environment
Bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
3. Install Dependencies
Install Django 

Bash
pip install django
4. Run Migrations
Apply the database migrations for core Django apps, the custom blog posts, and the accounts app:

Bash
python3 manage.py makemigrations
python3 manage.py migrate
5. Create a Superuser
Create an administrative account to access the Django admin dashboard:

Bash
python3 manage.py createsuperuser
6. Start the Development Server
Bash
python3 manage.py runserver
Once started, navigate to http://127.0.0.1:8000/ in your web browser.
