class Solution:
    def dayOfYear(self, date: str) -> int:
        ymd = [int(d) for d in date.split("-")]
        numOfDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if ymd[1] > 2:
            if (ymd[0]%4==0 and ymd[0]%100 !=0) or ymd[0]%400 ==0:
                numOfDays[2] = 29

        dayCount = ymd[2]
        for month in numOfDays[:ymd[1]]:
            dayCount += month
        
        return dayCount
        

if __name__ == "__main__":
    d = "2019-02-10"
    result = Solution.dayOfYear(d)
    print(result)