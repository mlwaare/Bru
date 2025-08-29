import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

data = {'uname': 'test', 'pass': 'test'}
url = "http://testphp.vulnweb.com/login.php"

response = requests.post(url, data=data, headers=headers)

if "Logout" in response.text:
    print("✅ دخلنا!")
else:
    print("❌ مفيش، جرب بيانات تانية")
