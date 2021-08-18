import math
import sys

import requests

# name = input('Your name? ')
# print("Hello", name)

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting

def new_func():
    test = "test"


# print(greet('World'))
# print(greet('Simon'))
r = requests.get("https://drsimonskalicky.com.au")
print(r.status_code)
