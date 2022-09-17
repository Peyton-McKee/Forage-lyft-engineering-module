from carMake.battery.nubbin_battery import NubbinBattery
from carMake.engine.willoughby_engine import WilloughbyEngine
from carMake.tires.octoprime_tire import OctoprimeTire

class Rorschach(WilloughbyEngine, NubbinBattery, OctoprimeTire):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced() or self.tires_should_be_serviced()
