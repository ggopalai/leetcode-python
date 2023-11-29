class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d = {
            1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31
        }
        
        # count the number of days from 1971
        def daysSince1971(year):
            totalYears = year - 1971 + 1
            leapCount = 0

            # calculate number of leap years
            for i in range(1971, year + 1):
                if i % 4 == 0:
                    leapCount += 1
            
            return leapCount * 366 + (totalYears - leapCount) * 365
        
        year1 = int(date1[:4])
        year2 = int(date2[:4])

        d1_prev = daysSince1971(year1 - 1)
        d2_prev = daysSince1971(year2 - 1)

        # find number of days in current year
        m1, m2 = int(date1[5:7]), int(date2[5:7])
        d1, d2 = int(date1[8:]), int(date2[8:])

        # current year is a leap year and date is after feb
        if int(m1) > 2 and year1 % 4 == 0 and year1 != 2100:
            d1 += 1
        if int(m2) > 2 and year2 % 4 == 0 and year2 != 2100:
            d2 += 1

        # find number of days in current year
        cur_days_1 = 0
        cur_days_2 = 0
        for i in range(1, m1):
            cur_days_1 += d[i]
        cur_days_1 += d1
        
        for i in range(1, m2):
            cur_days_2 += d[i]
        cur_days_2 += d2
        

        final_days_1 = d1_prev + cur_days_1
        final_days_2 = d2_prev + cur_days_2
  
        return abs(final_days_1 - final_days_2)