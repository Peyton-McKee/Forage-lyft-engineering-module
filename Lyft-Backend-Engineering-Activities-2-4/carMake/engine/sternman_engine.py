from abc import ABC
from car import Car

class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on, tire_wear):
        super().__init__(last_service_date, tire_wear)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
