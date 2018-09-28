
import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

print(r.status_code)
print(r.text)

data = r.json()
# We have Data

for user in data:
    print(user)

for user in data:
    print(user['name'])


# Lets see how we can control the data
for user in data:
    name = user['name']
    email = user['email']
    company = user['company']['name']

    print("Name: {}\nEmail: {}\nCompany: {}".format(name, email, company))
    print("----")


# Lets move the data into a dict for later use
from collections import defaultdict

user_data = lambda: defaultdict(dict)
users = user_data()

for user in data:
    name = user['name']
    email = user['email']
    company = user['company']['name']
    users[name]['email'] = email
    users[name]['company'] = company


import pprint
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(users)