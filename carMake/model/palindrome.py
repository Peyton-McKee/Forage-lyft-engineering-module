from carMake.battery.spindler_battery import SpindlerBattery
from carMake.engine.sternman_engine import SternmanEngine
from carMake.tires.carrigan_tire import CarriganTire

class Palindrome(SternmanEngine, SpindlerBattery,  CarriganTire):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced() or self.tires_should_be_serviced()
