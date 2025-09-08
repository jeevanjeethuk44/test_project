# MyProject

This is a base Django project.

## Local Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and activate a virtual environment

On macOS and Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

First, navigate to the `myproject` directory where `manage.py` is located:
```bash
cd myproject
```

Then, run the migrations:
```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.
