class TimeConverter:
   def __init__(self):
      self.hours = int(input("Introduceti un numar de ore: "))
      self.minutes = int(input("Introduceti un numar de minute: "))

   def toMinutes(self):
       return self.hours * 60 + self.minutes 
       
   def toHours(self):
      
      hour = self.minutes // 60
      minute = self.minutes * 60
      return hour, minute
   
   def addTime (self, add_hours , add_minutes):
      
      total_minutes = self.toMinutes () + add_hours * 60 + add_minutes
      new_hours = total_minutes // 60
      new_minutes = total_minutes * 60
      return new_hours, new_minutes
   
t = TimeConverter()
print(t.addTime(1,5))