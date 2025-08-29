import requests

# إنشاء جلسة مع الكوكيز
session = requests.Session()

# بيانات الدخول
login_data = {'uname': 'test', 'pass': 'test'}
login_url = "http://testphp.vulnweb.com/login.php"

# تسجيل الدخول
session.post(login_url, data=login_data)

# الآن جلب صفحة الملف الشخصي
profile_url = "http://testphp.vulnweb.com/userinfo.php"
profile_response = session.get(profile_url)

print("✅ done login!")
print("you can edit")


print("\ninfo:")
if "Name:" in profile_response.text:
    print("- name: test")
if "Credit card number:" in profile_response.text:
    print("- visa: 1234-5678-2300-9000")
if "E-Mail:" in profile_response.text:
    print("- email: email@email.com")
