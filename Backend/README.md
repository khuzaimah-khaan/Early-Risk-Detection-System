# Backend Setup Instructions

## Project Name
Early Risk Detection and Prediction System for Software Project Management

## Technologies Used
- Python
- Flask
- REST API

## Requirements
- Python 3 installed
- Visual Studio Code

## Installation Steps

### Step 1: Open the Project
Open the project folder in Visual Studio Code.

### Step 2: Open Terminal
Open Terminal in Visual Studio Code.

### Step 3: Go to Backend Folder
Run this command:

```powershell
cd Backend
```

### Step 4: Install Flask
Run this command:

```powershell
python -m pip install flask
```
python -m pip install -r requirements.txt
### Step 5: Start the Backend
Run this command:

```powershell
python app.py
```

### Step 6: Check Backend
Open this URL in your browser:

http://127.0.0.1:5000/health

Expected response:

```json
{
  "status": "Backend is running"
}
```

## Available APIs

- GET /health — Checks backend status.
- POST /assess — Returns a mock project risk assessment.

## Important Note
The assessment API currently returns a mock risk level. The actual machine learning model will be integrated later.