from abc import ABC
from car import Car


class CarriganTire(Car, ABC):
   def __init__(self, last_service_date, tire_wear):
      super().__init__(last_service_date, tire_wear)
      self.tire_wear = tire_wear

   def tires_should_be_serviced(self):
      for tire in self.tire_wear:
         if tire >= .9:
            return True
      return False
