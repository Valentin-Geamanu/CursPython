import requests
"""
doubleD =[[1, 2, 3],[4, 5, 6], [-1, -2, -4, -7], [0, 0, 0 ]]
print(doubleD[0][1])
print(doubleD[0])

for item in doubleD:
    for seconditem in item:
        print(seconditem)
        
"""

response = requests.get('https://jsonplaceholder.typicode.com/posts')

print(response)
print(response.json())

for item in response.json():
    if item['userId'] == 1 and item['id'] == 9:
        print(item)


response2 = requests.get('https://jsonplaceholder.typicode.com/albums')

print(response2)
print(response2.json())

for item in response2.json():
    if item['userId'] == 1 and item['title'] == 9:
        print(item['albums'])


response3 = requests.get('https://jsonplaceholder.typicode.com/todos')

print(response3)
print(response3.json())

for item in response3.json():
    if item['userId'] == 1 and item['completed'] == 9:
        print(item['todos'])
