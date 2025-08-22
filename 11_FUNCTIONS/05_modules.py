# Two types of modules in Python:
#  - Build in Modules
#  - External Modules
#  List of all the built in Modules: https://docs.pythojn.org/3/
import math
import os
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)
