# djangohelp

![Site pic](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/sitepic.png)

## Introduction

Welcome to the `djangohelp` repository! This project is designed to help learners understand the basics of Django, a powerful web framework for Python. Whether you are new to Django or looking to reinforce your skills, this repository provides a hands-on approach to learning.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/5pence/djangohelp.git
    cd djangohelp
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Project
1. **Navigate to the Project Directory**
    ```bash
    cd mysite
    ```

2. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

3. **Run the Server**
    ```bash
    python manage.py runserver
    ```
    Open your browser and go to `http://127.0.0.1:8000/blog` to see your Django project in action.

## Project Structure
- `mysite/` - Main project directory containing settings and configuration files.
- `blog/` - Example app directory demonstrating a simple blog application.
- `manage.py` - Command-line utility for interacting with the project.

## Learning Resources
- [Django Official Documentation](https://docs.djangoproject.com/en/5.0/)
- [Tutorial: Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Querysets](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#methods-that-return-new-querysets)
- [Django Template Language](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
- [Class-based generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
- [Extending the user model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)
- Also check out the PDF slides at the footer of this doc

## Questions I've asked about this:

### How do I do a profile

You extend the Django User model, I show you how here:

I usually name the Django Model as `Profile`:

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=400, blank=True)
    location = models.CharField(max_length=25, blank=True)
```

Now define signals so my `Profile` model will be automatically created and updated when I create/update `User` instances.

```python
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=400, blank=True)
    location = models.CharField(max_length=25, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

So by hooking the `create_user_profile` and `save_user_profile` methods to the `User` model, whenever a save event occurs. This kind of signal is called `post_save`.

---

Happy coding! If you have any questions, feel free to open an issue.

## Slides from Lecture

![Slide One](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.001.jpeg)
![Slide Two](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.002.jpeg)
![Slide Three](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.003.jpeg)
![Slide Four](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.004.jpeg)
![Slide Five](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.005.jpeg)
![Slide Six](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.006.jpeg)