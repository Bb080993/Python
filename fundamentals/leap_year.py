def is_leap_year(year):
        if year%400==0:
            print("It's a leap year")
        elif year%100!=0:
            print("Not a leap year")
        elif year%4==0:
            print("Is a leap year!")
        else:
            print("Not a leap year")
for i in range(1800,1809):
     is_leap_year(i)



is_leap_year(1000)
is_leap_year(2023)
is_leap_year(2024)
is_leap_year(3001)
is_leap_year(1997)
is_leap_year(2001)