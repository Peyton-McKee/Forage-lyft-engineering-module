from Car.Battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()
