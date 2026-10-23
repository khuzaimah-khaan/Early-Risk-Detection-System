# API Specification

## 1. Project Information

Project Name: Early Risk Detection and Prediction System for Software Project Management

Backend Framework: Python Flask

## 2. Health Check API

Endpoint: /health

Method: GET

Purpose: Checks whether the backend is running.

Successful Response:
{
  "status": "Backend is running"
}

## 3. Project Assessment API

Endpoint: /assess

Method: POST

Purpose: Receives a project name and returns a mock risk assessment.

Request Body:
{
  "project_name": "Demo Project"
}

Successful Response:
{
  "project_name": "Demo Project",
  "risk_level": "Medium",
  "message": "Mock assessment response",
  "is_mock": true
}

## 4. Validation Errors

If the request body is missing or empty:

{
  "error": "Request body must contain JSON data"
}

If project_name is missing or empty:

{
  "error": "project_name is required"
}
If project_name is not a text value:

{
  "error": "project_name must be a text value"
}

## 5. Important Note

The assessment response is currently a mock response.
The actual machine learning model will be integrated later.