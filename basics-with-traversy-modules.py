#A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules.

#available by default through python

import datetime
#or you could import only "date" from import
from datetime import date
from time import time

today = datetime.date.today()
today2 = date.today()

print(today)
print(today2)

timestamp = time()
print(timestamp)