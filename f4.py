import requests

# Just one simple attempt
data = {'uname': 'test', 'pass': 'test'}
result = requests.post('http://testphp.vulnweb.com/login.php', data=data)

if "Logout" in result.text:
    print("WORKING! ✅")
else:
    print("NOT WORKING! ❌")
