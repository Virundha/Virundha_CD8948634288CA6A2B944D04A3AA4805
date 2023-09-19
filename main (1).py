







def isleepyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 300 == 0:
    return True
  else:
    return False

year = int(input("Enter a year : "))

if isleepyear(year):
  print('{} is a leep year.'. format(year))
else:
  print('{} is not a leep year.'.format(year))