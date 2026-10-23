from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "Backend is running"
    }), 200


@app.route("/assess", methods=["POST"])
def assess_project():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Request body must contain JSON data"
        }), 400

    project_name = data.get("project_name")

    if not isinstance(project_name, str) or not project_name.strip():
        return jsonify({
            "error": "project_name is required"
        }), 400

    return jsonify({
        "project_name": project_name.strip(),
        "risk_level": "Medium",
        "message": "Mock assessment response",
        "is_mock": True
    }), 200


if __name__ == "__main__":
    app.run(debug=True)