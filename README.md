# [Django API Generator](https://github.com/app-generator/django-api-generator) `Sample`

Minimal **Django** project with `Docker` support - actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

> Features - see **[video](https://www.youtube.com/watch?v=fkjvhFejEv8)** presentation

- ✅ `Up-to-date Dependencies`
- ✅ `Docker`
- ✅ Integrates [API Generator](https://github.com/app-generator/django-api-generator) Library for Django

<br />

## ✨ Start the app in Docker

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/core-django.git
$ cd core-django
```

<br />

> 👉 **Step 2** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/core-django.git
$ cd core-django
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create SuperUser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Generate the API for `Books` model

```bash
$ python manage.py generate-api
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/` and the API is usable `http://127.0.0.1:8000/api/books/`

<br />

![Django API Generator - DRF Interface (open-source tool).](https://user-images.githubusercontent.com/51070104/197181145-f7458df7-23c3-4c14-bcb1-8e168882a104.jpg)

<br />

---
[Django API Generator](https://github.com/app-generator/django-api-generator) `Sampl` - Minimal **Django** starter provided by **[AppSeed](https://appseed.us/)**
