import requests

# OPA server URL
opa_url = "http://localhost:8181/v1/data/my_policy"

# Function to check authorization using OPA
def check_authorization(user, role, permission):
    try:
        payload = {
            "input": {
                "user": user,
                "role": role,
                "permission": permission
            }
        }
        response = requests.post(opa_url, json=payload)
        return response.json().get("result", False)
    except Exception as e:
        print(f"Authorization check error: {str(e)}")
        return False
