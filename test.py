import datetime
class Solution:
    def dayOfTheWeek(day,month,year):
        daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        dateObj = datetime.date(year,month,day)
        dayOfWeek = dateObj.weekday(dateObj)
        return daysOfWeek[dayOfWeek]
