Car Enthusiasts Conversation Platform

For an in-depth write-up about this project, check out the [Blog Post](BLOG.md).

A Django-based web application that allows car enthusiasts to create and join rooms to discuss specific car types. This project focuses on backend development, providing secure user authentication and features for managing conversations.

Features
Room Creation: Users can create rooms with a topic and description to discuss specific car types.
User Management:
Register with profile picture upload.
Secure login and logout functionalities.
View and edit user profiles, including personal messages.
Message Management:
Logged-in users can post, edit, and delete messages.
Proper error messages are displayed for invalid actions (e.g., trying to access deleted messages).
Search Functionality: Search for rooms or messages by keyword on the homepage.
Authenticated URLs: All URLs are protected to ensure secure access.
Tech Stack
Backend: Python, Django
Database: SQLite (default for Django projects)
Deployment: Circumveo hosting
Frontend: Django templating (basic design)
Key Learning Points
Mastered Django templating to dynamically render data on web pages.
Enhanced backend security by authenticating all endpoints.
Improved error handling for seamless user experience.
Deployed the project on a Django hosting platform (Circumveo).
Installation and Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/project-repo.git  
Navigate to the project directory:

bash
Copy code
cd project-repo  
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv  
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Apply migrations and start the server:

bash
Copy code
python manage.py migrate  
python manage.py runserver  
Access the application at:

arduino
Copy code
http://127.0.0.1:8000/  
Challenges Overcome
Corrected a bug where deleting a message and pressing the back button caused an error page. Implemented proper error messages for user guidance.
Gained a deeper understanding of Django’s templating system.
Future Enhancements
Improve frontend design using modern frameworks like React or Bootstrap.
Add real-time chat functionality for more dynamic interactions.
Migrate to a scalable hosting solution like AWS or Heroku.
Live Demo
Check out the live project here: https://g9k-reliable-watt.circumeo-apps.net/
