from carMake.battery.spindler_battery import SpindlerBattery
from carMake.engine.willoughby_engine import WilloughbyEngine
from carMake.tires.octoprime_tire import OctoprimeTire


class Glissade(WilloughbyEngine, SpindlerBattery, OctoprimeTire):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced() or self.tires_should_be_serviced()
