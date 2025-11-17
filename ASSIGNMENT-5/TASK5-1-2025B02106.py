import logging

logging.basicConfig(level=logging.WARNING)

users = {}   # dictionary to store username and password

# Registration
new_username = input("Enter new username: ")
new_password = input("Enter new password: ")

users[new_username] = new_password
print("Registration successful")

# Login
login_username = input("Enter username to login: ")
login_password = input("Enter password: ")

# Check if username exists
if login_username not in users:
    logging.warning(f"Login attempt for non-existent user: {login_username}")
    print("Login failed")
else:
    # Check password
    if users[login_username] == login_password:
        print("Login successful")
    else:
        print("Incorrect password")
        print("Login failed")