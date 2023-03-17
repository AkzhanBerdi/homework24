from datetime import datetime

class DateTimeError(Exception):
    def __init__(self, year, month, day, hours, minutes, seconds):
        self.date = datetime(year,month,day,hours,minutes,seconds)
        self.message = f'Invalid values: year = {year}, month = {month},\
                      day = {day}, hours = {hours}, minutes = {minutes}, seconds = {seconds}.\
                      Please provide correct values'
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
