# Django Vue Project

This is a project that includes a Django backend with a Vue.js frontend.
The backend provides a REST API for user authentication using a phone number and a One-Time Password (OTP). The frontend provides the user interface for this two-step login process.

### Authentication Flow
1. The user enters their phone number.
2. The backend generates an OTP and sends it to the user's phone via SMS.
3. The user enters the OTP from the SMS into the frontend.
4. If the OTP is correct, the user is logged in.

## Environment Variables

To run this project, you will need to set up environment variables for the Twilio integration.

Create a file named `.env` in the main project root (the same directory as this `README.md` file) and add your credentials like this:

```
# .env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

The application will load these variables automatically. Make sure the `.env` file is included in your `.gitignore` to avoid committing secrets.

## Project Structure

- `myproject/`: Contains the Django backend code.
- `frontend/`: Contains the Vue.js frontend code.

## Local Setup Instructions

1.  **Set up the Backend:**
    - Navigate to the project root.
    - Create and activate a Python virtual environment:
      ```bash
      # On macOS and Linux:
      python3 -m venv venv
      source venv/bin/activate

      # On Windows:
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - Install Python dependencies into your virtual environment:
      ```bash
      pip install -r requirements.txt
      ```
    - Navigate into the Django project:
      ```bash
      cd myproject
      ```
    - Run database migrations:
      ```bash
      python manage.py migrate
      ```

2.  **Set up the Frontend:**
    - Navigate to the frontend directory: `cd frontend`
    - Install Node.js dependencies: `npm install`
    - Build the frontend assets: `npm run build`

3.  **Run the Application:**
    - Navigate back to the Django project directory: `cd ../myproject`
    - Start the Django server: `python manage.py runserver`
    - The application will be available at `http://127.0.0.1:8000/`.
