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
- Also check out the PDF slides in the readme-images directory

---

Happy coding! If you have any questions, feel free to open an issue.


## Slides from Lecture

![Slide One](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.001.jpeg)
![Slide Two](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.002.jpeg)
![Slide Three](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.003.jpeg)
![Slide Four](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.004.jpeg)
![Slide Five](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.005.jpeg)
![Slide Six](https://raw.githubusercontent.com/5pence/djangohelp/main/readme-images/DjangoMVT.006.jpeg)