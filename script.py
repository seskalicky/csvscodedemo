import math
import sys

import requests

# name = input('Your name? ')
# print("Hello", name)




# print(greet('World'))
# print(greet('Simon'))
r = requests.get("https://drsimonskalicky.com.au")
print(r.status_code)
print(r.ok)