from carMake.battery.spindler_battery import SpindlerBattery
from carMake.engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        return self.engine_should_be_serviced() or self.battery_should_be_serviced()
