# JOBZ API

## This work exposes endpoints for job listings and integrates JWT authentication

### Getting Started

1. Clone the repository
```
git clone https://github.com/journpy/jobz-api.git
```

2. Install project dependencies
```
pip install -r requirements.txt
```

3. Run migrations
```
python manage.py migrate
```

4. Create a superuser account
```
python manage.py createsuperuser
```

5. Optionally Sign up for a user account. 
```
/api/auth/registration/
```
*Email authentication is used with JWT.*

6. Login to use the app
```
/api/auth/login/
```
*This should spit out access and refresh tokens.*

7. Load jobs to database
```
python manage.py loadjobs
```

8. Spin up the development server
```
python manage.py runserver
```

9. Find Endpoints on Swagger UI
```
/swagger-ui/
```
10. Homepage for easy access http://127.0.0.1:8000/


### Contact the Author
Please [find my email here](https://mailhide.io/en/e/sXPUdBJS) or 
visit my [website](https://lwu.pythonanywhere.com/).




