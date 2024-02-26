from keycloak import KeycloakOpenID

# Initialize Keycloak client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="my_client_app",
                                 realm_name="my_realm",
                                 client_secret_key="my_secret_key")
