## Import Datetime

#Type 1

import datetime
today = datetime.date.today()
print(today)

#Type 2 

import datetime
today = datetime.datetime.today()
print(today)

#Type 3

from datetime import datetime
d = datetime.today()
print(d)