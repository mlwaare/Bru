import requests

# 1. بيانات الدخول
data = {
    'uname': 'test',
    'pass': 'test'
}

# 2. إرسال طلب الدخول
url = "http://testphp.vulnweb.com/login.php"
response = requests.post(url, data=data)

# 3. شوف النتيجة
print("كود الاستجابة:", response.status_code)
print("هل في كلمة Logout؟", "Logout" in response.text)

# 4. لو عايز تشوف الصفحة كاملة
print("=" * 50)
print(response.text[:1000])  # أول 1000 حرف فقط
