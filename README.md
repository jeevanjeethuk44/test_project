# Django Vue Project

This is a project that includes a Django backend with a Vue.js frontend.
The backend provides a REST API for user authentication (signup and login), and the frontend provides the user interface.

## Project Structure

- `myproject/`: Contains the Django backend code.
- `frontend/`: Contains the Vue.js frontend code.

## Local Setup Instructions

1.  **Set up the Backend:**
    - Navigate to the project root.
    - Install Python dependencies: `pip install -r requirements.txt`
    - Navigate into the Django project: `cd myproject`
    - Run database migrations: `python manage.py migrate`

2.  **Set up the Frontend:**
    - Navigate to the frontend directory: `cd frontend`
    - Install Node.js dependencies: `npm install`
    - Build the frontend assets: `npm run build`

3.  **Run the Application:**
    - Navigate back to the Django project directory: `cd ../myproject`
    - Start the Django server: `python manage.py runserver`
    - The application will be available at `http://127.0.0.1:8000/`.
