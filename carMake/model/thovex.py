from carMake.battery.nubbin_battery import NubbinBattery
from carMake.engine.capulet_engine import CapuletEngine
from carMake.tires.carrigan_tire import CarriganTire

class Thovex(CapuletEngine, NubbinBattery, CarriganTire):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced() or self.tires_should_be_serviced()
