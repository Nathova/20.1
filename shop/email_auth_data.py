import json

with open('shop/emailconfig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


EMAIL = data['email']
PASSWORD = data['password']
