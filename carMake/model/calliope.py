from carMake.battery.spindler_battery import SpindlerBattery
from carMake.engine.capulet_engine import CapuletEngine
from carMake.tires.carrigan_tire import CarriganTire

class Calliope(CapuletEngine, SpindlerBattery, CarriganTire):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced() or self.tires_should_be_serviced()
