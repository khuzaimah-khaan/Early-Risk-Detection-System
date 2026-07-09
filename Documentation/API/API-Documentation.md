# API Documentation
This document describes the APIs used in the Early Risk Detection and Prediction System for Software Project Management.
## 1. Predict API

### Purpose
Predict the risk level of a software project using project metrics.

### URL
/predict

### HTTP Method
POST
### Input

json
{
  "team_size": 10,
  "total_tasks": 100,
  "completed_tasks": 70,
  "bug_count": 25,
  "overdue_tasks": 10,
  "commit_frequency": "High"
}


### Output

json
{
  "risk_level": "Medium",
  "risk_score": 72,
  "explanation": [
    "Bug count is moderate",
    "Completion rate is acceptable"
  ],
  "recommendation": [
    "Increase testing",
    "Monitor overdue tasks"
  ]
}
### Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Prediction successful |
| 400 | Invalid input data |
| 500 | Internal server error |

### Possible Errors

- Missing required fields
- Invalid data format
- Server error
## 2. Upload API
### Purpose
Upload a CSV file containing software project data for risk analysis.

### URL
`/upload`

### HTTP Method
`POST`

### Input

```text
CSV File
```

### Output

```json
{
  "message": "File uploaded successfully"
}
```

### Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | File uploaded successfully |
| 400 | Invalid file format |
| 500 | Internal server error |

### Possible Errors

- No file selected
- Invalid CSV format
- Server error
## 3. Dashboard API
### Purpose
Retrieve dashboard statistics and project health information.

### URL
`/dashboard`

### HTTP Method
`GET`

### Input

No input required.

### Output

```json
{
  "project_health": "Good",
  "risk_level": "Low",
  "risk_score": 25,
  "completed_tasks": 80,
  "pending_tasks": 20,
  "bug_count": 10
}
```

### Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Dashboard data retrieved successfully |
| 500 | Internal server error |

### Possible Errors

- Dashboard data not found
- Server error
## 4. History API
### Purpose
Retrieve the history of previous project risk predictions.

### URL
`/history`

### HTTP Method
`GET`

### Input

No input required.

### Output

```json
[
  {
    "project_name": "Project A",
    "risk_level": "High",
    "risk_score": 85,
    "prediction_date": "2026-07-08"
  },
  {
    "project_name": "Project B",
    "risk_level": "Low",
    "risk_score": 20,
    "prediction_date": "2026-07-05"
  }
]
```

### Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | History retrieved successfully |
| 500 | Internal server error |

### Possible Errors

- No prediction history available
- Server error