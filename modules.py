# A Module is a file containing a set of functions to include in your application. There are core python modules, you can install using 
# pip package manager (including Django) as well as custom modules.


# CORE MODULES
# Import datetime 
import datetime
# Or 
from datetime import date
# Import time
import time
# OR

# Import custom modules

from validator import validate_email

from time import time

today= datetime.date.today()

timestamp = time()

print(timestamp)

# PIP MOCULES

# This module turns the first words into capital letter.
from camelcase import CamelCase

c= CamelCase()
print(c.hump('hello world'))


# How to validate an email

email= 'test@gmail.com'
if validate_email(email):
    print('Email is valide')
else:
    print('Not Valide')

