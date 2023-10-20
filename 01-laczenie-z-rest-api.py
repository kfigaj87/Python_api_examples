import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if (response.status_code != requests.codes.ok):
    print("Coś poszło nie tak")
else:
    print(response.json())


requestBody = {
    'title': 'Nasz tytyl',
    'body': 'Tresc posta',
    'userId': 1
}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts', json=requestBody)

if (response.status_code != requests.codes.created):
    print("Coś poszło nie tak")
else:
    print(response.json())
