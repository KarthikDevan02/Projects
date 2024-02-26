from flask import Flask, request, jsonify
from keycloak_config import keycloak_openid
from opa_integration import check_authorization
import logging_config

# Define the Flask application with the name "SecureAPI"
app = Flask("SecureAPI")

# Dummy SQL database to store roles and permissions
sql_db = {
    "roles": {
        "Raul": ["admin"],
        "Simon": ["manager"],
        "Ronaldo": ["employee"],
        "Messi": ["customer"],
        "Aguero": ["guest"]
    }
}

# Function to validate token and get user info
def validate_token(access_token):
    try:
        userinfo = keycloak_openid.userinfo(access_token)
        return userinfo
    except Exception as e:
        logging.error(f"Token validation error: {str(e)}")
        return None

# Endpoint for accessing protected resource
@app.route("/protected_resource", methods=["GET"])
def protected_resource():
    access_token = request.headers.get("Authorization")
    if not access_token:
        logging.warning("Unauthorized access attempt - No access token provided")
        return jsonify({"message": "Unauthorized"}), 401

    userinfo = validate_token(access_token)
    if not userinfo:
        logging.warning("Unauthorized access attempt - Invalid access token")
        return jsonify({"message": "Unauthorized"}), 401

    role = userinfo.get("role", "")
    permission = request.args.get("permission", "")

    if role in sql_db["roles"] and permission in sql_db["roles"][role]:
        authorized = check_authorization(userinfo["sub"], role, permission)
        if authorized:
            logging.info(f"Access granted - User: {userinfo['sub']}, Role: {role}, Permission: {permission}")
            return jsonify({"message": "Access granted"})
    logging.warning(f"Access denied - User: {userinfo['sub']}, Role: {role}, Permission: {permission}")
    return jsonify({"message": "Access denied"}), 403

if __name__ == "__main__":
    app.run(debug=True)
