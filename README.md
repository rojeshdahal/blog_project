Django Blog Project
A modular, database-driven blogging platform built with Django. This project features dynamic content routing, a custom blog post management workflow, and a fully integrated user authentication system (registration, login, and logout) leveraging Django's built-in security features.

🚀 Features
Dynamic Blog Routing: Complete split-architecture setup where individual blog posts are dynamically fetched and rendered via unique URL paths (e.g., /posts/<id>/).

User Authentication System: Secure user registration using Django's UserCreationForm, alongside built-in, pre-secured login/logout views.

Secure Content Creation: Implements ModelForms and the @login_required decorator to ensure only authenticated users can author blog posts.

Automatic Author Attribution: Uses commit=False architectural design to automatically map the currently logged-in user as the author of a post upon database insertion.

CSRF Protection: Native security tokens embedded across all user-facing forms to prevent Cross-Site Request Forgery attacks.