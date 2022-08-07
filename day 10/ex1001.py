def is_leap(year):
  ''' its a doc string for function is_leap() it will check that if the year pass to it is a leap year or not '''
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap(year)
    if leap and month-1 == 1 :
        return('it is leap year and this month has 29 days')
    return(f'its {leap} that its leap year and we have {month_days[month-1]} in it')

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)