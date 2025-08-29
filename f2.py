import requests

# The login page URL
login_url = "http://testphp.vulnweb.com/login.php"

# Login credentials - these are the field names and values
login_data = {
    'uname': 'test',     # username field
    'pass': 'test'       # password field
}

# Send login request
response = requests.post(login_url, data=login_data)

# Check if login was successful
if "Logout" in response.text:
    print("✅ Login successful!")
    print("You are now logged in.")
else:
    print("❌ Login failed")
    print("Either username/password is wrong")
    print("or the field names are different.")
