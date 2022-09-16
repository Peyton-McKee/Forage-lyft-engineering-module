from Car.Battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()
