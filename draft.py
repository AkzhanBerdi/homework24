from datetime import datetime
from dateFile import Date
from dateTimeFile import DateTime
from dateTimeErrorFile import DateTimeError

def check():
    try:
        a = Date(2023,3,15)
        b = DateTime(2023,3,15,25,59,60)
    except DateTimeError as e:
        print(e.__str__())
        print("Object accomplished")
    except ValueError as r:
        print(r.__str__())
        print("It's Value Error, you need your custom one")
    else:
        print('else')
    finally:
        print("Object is not accomplished yet")

check()