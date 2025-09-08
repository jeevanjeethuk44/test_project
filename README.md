# Django Vue Project

This is a project that includes a Django backend with a Vue.js frontend.
The backend provides a REST API for user authentication using a phone number and a One-Time Password (OTP). The frontend provides the user interface for this two-step login process.

### Authentication Flow
1. The user enters their phone number.
2. The backend generates an OTP and prints it to the server console.
3. The user enters the OTP from the console into the frontend.
4. If the OTP is correct, the user is logged in.

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
