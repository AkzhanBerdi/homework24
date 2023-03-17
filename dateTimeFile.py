from datetime import datetime
from dateFile import Date
from dateTimeErrorFile import DateTimeError

class DateTime(Date):
    def __init__(self,year,month,day,hours,minutes,seconds) -> None:
        super().__init__(year,month,day)
        self.date = datetime(year,month,day,hours,minutes,seconds)
    
    def __str__(self):
        return super().__str__() + ' ' + self.date.strftime('%H:%M:%S')

    def time_check(self):
        if self.date.hour > 23 or self.date.hour < 0:
            raise DateTimeError(self.date.year,self.date.month,self.date.day,self.date.hour,self.date.minute,self.date.second)
        elif self.date.minute > 59 or self.date.minute < 0:
            raise DateTimeError(self.date.year,self.date.month,self.date.day,self.date.hour,self.date.minute,self.date.second)
        elif self.date.second > 59 or self.date.second < 0:
            raise DateTimeError(self.date.year,self.date.month,self.date.day,self.date.hour,self.date.minute,self.date.second)
