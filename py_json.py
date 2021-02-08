# JSON is commonly used with APIS. Here how we can parse JSON into a python dictionary

import json

userJSON = '{"first_name": "TK", "last_name": "Joe", "age": 24}'

# Parse to dict
user = json.loads(userJSON)
print(user)