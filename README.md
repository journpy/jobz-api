# JOBZ API

## This work exposes endpoints for job listings and integrates JWT authentication

### Getting Started

1. Clone the repository
```
git clone https://github.com/journpy/jobz-api.git
```

2. Run migrations
```
python manage.py migrate
```

3. Create a superuser account
```
python manage.py createsuperuser
```

4. Optionally Sign up for a user account. 
```
/api/auth/registration/
```
*Email authentication is used with JWT.*

5. Login to use the app
```
/api/auth/login/
```
*This should spit out access and refresh tokens.*

6. Load jobs to database
```
python manage.py loadjobs
```

7. Spin up the development server
```
python manage.py runserver
```

8. Find Endpoints on Swagger UI
```
/swagger-ui/
```
9. Homepage for easy access http://127.0.0.1:8000/



To contact me, [find my email here](https://mailhide.io/en/e/sXPUdBJS) or 
visit my [website](https://lwu.pythonanywhere.com/).




