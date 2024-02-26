from flask import Flask, request, jsonify
from keycloak_config import keycloak_openid
from opa_integration import check_authorization
import logging_config

# I am initializing a Flask application named "SecureAPI"
app = Flask("SecureAPI")

# I have a dummy SQL database to store roles and permissions
sql_db = {
    "roles": {
        "Raul": ["admin"],
        "Simon": ["manager"],
        "Ronaldo": ["employee"],
        "Messi": ["customer"],
        "Aguero": ["guest"]
    }
}

# This function validates the token and retrieves user information
def validate_token(access_token):
    try:
        userinfo = keycloak_openid.userinfo(access_token)
        return userinfo
    except Exception as e:
        # I handle any errors that occur during token validation
        logging.error(f"Token validation error: {str(e)}")
        return None

# This endpoint allows access to protected resources
@app.route("/protected_resource", methods=["GET"])
def protected_resource():
    access_token = request.headers.get("Authorization")
    if not access_token:
        # I log a warning if no access token is provided
        logging.warning("Unauthorized access attempt - No access token provided")
        return jsonify({"message": "Unauthorized"}), 401

    userinfo = validate_token(access_token)
    if not userinfo:
        # I log a warning if the access token is invalid
        logging.warning("Unauthorized access attempt - Invalid access token")
        return jsonify({"message": "Unauthorized"}), 401

    role = userinfo.get("role", "")
    permission = request.args.get("permission", "")

    if role in sql_db["roles"] and permission in sql_db["roles"][role]:
        authorized = check_authorization(userinfo["sub"], role, permission)
        if authorized:
            # I log access granted to the user with their role and permission
            logging.info(f"Access granted - User: {userinfo['sub']}, Role: {role}, Permission: {permission}")
            return jsonify({"message": "Access granted"})
    # I log access denied for the user with their role and permission
    logging.warning(f"Access denied - User: {userinfo['sub']}, Role: {role}, Permission: {permission}")
    return jsonify({"message": "Access denied"}), 403

if __name__ == "__main__":
    # I run the Flask application in debug mode
    app.run(debug=True)
