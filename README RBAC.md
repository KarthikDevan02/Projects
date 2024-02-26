Role-Based Access Control (RBAC) with Keycloak, OPA, and Flask


This project demonstrates Role-Based Access Control (RBAC) implementation using Keycloak, Open Policy Agent (OPA), and Flask. It allows access to protected resources based on user roles and permissions defined in Keycloak, with additional access control enforcement through OPA.

Project Structure
The project consists of the following files:

keycloak_config.py: Configuration file for Keycloak integration.
opa_integration.py: Integration with Open Policy Agent for access control enforcement.
logging_config.py: Configuration file for logging access attempts and errors.
app.py: Main Flask application for providing access to protected resources.
Usage
Ensure you have Keycloak, OPA, and Flask installed and configured in your environment.
Replace the placeholder values in keycloak_config.py with your actual Keycloak configuration (client ID, realm name, and client secret key).
Adjust the OPA server URL in opa_integration.py according to your OPA setup.
Run the Flask application using python app.py.
Access the protected resources using appropriate access tokens.
Implementation Details
Keycloak is used for user authentication and management of roles and permissions.
OPA is employed to enforce fine-grained access control policies based on user context and attributes.
Logging is configured to record access attempts, errors, and warnings for auditing and monitoring purposes.
