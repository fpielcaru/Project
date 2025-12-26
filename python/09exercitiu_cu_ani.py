startDate = 1200
endDate = 2015 
print("********* ALLOWED YEARS *********")
for year in range( startDate, endDate +1):
    if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0):
     print(year)
print("*******************")
