# pip install requests

import requests

result = requests.get('https://jsonplaceholder.typicode.com/posts') # şu anda result 200 yani durum başarılı http kodudur
result = result.text # bize dönen cevap(text)
print(result)