# GrowEbuddy_PSA Setup Instructions

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.8 or higher**: Download from [python.org](https://www.python.org/downloads/).
- **PostgreSQL**: Download and install from [postgresql.org](https://www.postgresql.org/download/).
- **pip**: Python package installer (comes with Python).

## Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/GrowEbuddy_PSA.git
cd GrowEbuddy_PSA
```

## Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv myvenv

# Activate the virtual environment
# On Windows
myvenv\Scripts\activate
# On macOS/Linux
source myvenv/bin/activate
```

## Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install the necessary packages:

```bash
pip install django psycopg2 python-decouple dj-database-url
```

## Configure the Database

1. **Create a PostgreSQL Database**:
   - Open the PostgreSQL shell or pgAdmin and create a new database for the project.

2. **Update Database Settings**:
   - Open `backend/backendwithDjango/backendwithDjango/settings.py` and update the `DATABASES` section with your database name, username, and password.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',  # Replace with your database name
        'USER': 'your_username',        # Replace with your database username
        'PASSWORD': 'your_password',    # Replace with your database password
        'HOST': 'localhost',            # Set to 'localhost' or your database host
        'PORT': '5432',                 # Default PostgreSQL port
    }
}
```

## Run Migrations

Apply the database migrations to create the necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## Additional Notes

- To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

- Follow the prompts to set up your admin account.

## Conclusion

You are now set up to run the GrowEbuddy_PSA project! If you encounter any issues, please refer to the documentation or reach out for help.