import requests

# بيانات تسجيل الدخول
data = {
    'uname': 'test',    # اسم المستخدم
    'pass': 'test'      # كلمة المرور
}

# إرسال طلب تسجيل الدخول
response = requests.post('http://testphp.vulnweb.com/login.php', data=data)

# التحقق من النتيجة
if response.status_code == 200:
    if "Logout" in response.text:
        print("✅ تم تسجيل الدخول بنجاح!")
    else:
        print("❌ فشل تسجيل الدخول - بيانات خاطئة")
else:
    print(f"❌ خطأ في الاتصال: {response.status_code}")
