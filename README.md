How To Use

Clone project & Install Requirements

Make sure you have already installed python3 and git.

$ git clone https://github.com/Shivamsethss82/BugTrackerApplication.git

$ pip install -r requirements.txt

Change Directory:-

cd bugtracker

Migrate & Create Admin User

$ python manage.py migrate

$ python manage.py createsuperuser

Run Server

$ python manage.py runserver

Enter your browser http://localhost:8000/. 

You can login via admin in http://localhost:8000/admin/.
