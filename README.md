# Django Portfolio

This is a portfolio website built using Django, a high-level Python web framework. The purpose of this project is to showcase your projects, skills, and experience in a professional and visually appealing manner.

## Features

- **Project Showcase**: Display your projects with detailed descriptions, screenshots, and links.
- **Skill Highlight**: Highlight your skills and expertise in various technologies.
- **About Me**: Introduce yourself and provide information about your background and experience.
- **Contact Information**: Make it easy for visitors to get in touch with you.
- **Responsive Design**: Ensure a seamless experience across different devices and screen sizes.

## Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/leoamato/django-portfolio.git
   cd django-portfolio
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:
* On windows:
    ```bash
    env\Scripts\activate
    ```
* On macOS and Linux:
    ```bash
    source env/bin/activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations
    ```bash
    python manage.py makemigrations
    ```

6. Create an admin user:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Configure your portfolio.
    * Open http://127.0.0.1:8000/admin.
    * Create a profile and add your data.

8. Open http://127.0.0.1:8000/< your_email > in your web browser to view the website.

## Usage

* Customize the project by adding your own projects, skills, and information.
* Modify the templates and styles to match your preferences and branding.
* Deploy the website to a web hosting service to make it accessible to others.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request. 

