# djangohelp


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
- [Django Official Documentation](https://docs.djangoproject.com/en/stable/)
- [Tutorial: Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- Also check out the PDF slides in the readme-images directory



---

Happy coding! If you have any questions, feel free to open an issue.
