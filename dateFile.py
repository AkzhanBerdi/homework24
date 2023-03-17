from datetime import datetime
from dateTimeErrorFile import DateTimeError

class Date:
    def __init__(self,year,month,day) -> None:
        self.date = datetime(year,month,day)

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')

    def date_check(self):
        if self.date.year > 9999 or self.date.year < 0:
            raise DateTimeError(self.date.year)
        elif self.date.month > 12 or self.date.month < 1:
            raise DateTimeError(self.date.month)
        elif self.date.day > 31 or self.date.day < 1:
            raise DateTimeError(self.date.day)