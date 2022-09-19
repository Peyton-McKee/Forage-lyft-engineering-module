from abc import ABC
from car import Car


class OctoprimeTire(Car, ABC):
   def __init__(self, last_service_date, tire_wear):
      super().__init__(last_service_date, tire_wear)
      self.tire_wear = tire_wear

   def tires_should_be_serviced(self):
      total = 0
      for tire in self.tire_wear:
         total += tire
      print(total >= 3)
      return total >= 3
