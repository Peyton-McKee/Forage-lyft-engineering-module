import unittest
from datetime import datetime
from carMake.model.calliope import Calliope
from carMake.model.glissade import Glissade
from carMake.model.palindrome import Palindrome
from carMake.model.rorschach import Rorschach
from carMake.model.thovex import Thovex

class TestCalliope(unittest.TestCase):
    def test_new_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Calliope(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_new_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Calliope(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Calliope(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Calliope(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.9, .3, .8, .2]

        car = Calliope(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.2, .3, .8, .2]

        car = Calliope(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_new_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Glissade(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_new_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Glissade(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Glissade(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Glissade(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.7, .7, .8, .8]

        car = Glissade(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.9, .3, .8, .2]

        car = Glissade(last_service_date, current_mileage,
                       last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_new_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 7)
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]

        car = Palindrome(last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_new_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]

        car = Palindrome(last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_wear = [0, 0, 0, 0]

        car = Palindrome(last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear = [0, 0, 0, 0]

        car = Palindrome(last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        tire_wear = [.9, .1, .8, .9]

        car = Palindrome(last_service_date, warning_light_is_on, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        tire_wear = [.8, .8, .8, .8]

        car = Palindrome(last_service_date, warning_light_is_on, tire_wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Rorschach(last_service_date, current_mileage,
                        last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Rorschach(last_service_date, current_mileage,
                        last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Rorschach(last_service_date, current_mileage,
                        last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Rorschach(last_service_date, current_mileage,
                        last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.9, .97, .41, .81]

        car = Rorschach(last_service_date, current_mileage,
                        last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.92, .14, .23, .28]

        car = Rorschach(last_service_date, current_mileage,
                        last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Thovex(last_service_date, current_mileage,
                     last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Thovex(last_service_date, current_mileage,
                     last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Thovex(last_service_date, current_mileage,
                     last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = Thovex(last_service_date, current_mileage,
                     last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())

    def test_tires_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.9, .3, .8, .2]

        car = Thovex(last_service_date, current_mileage,
                     last_service_mileage, tire_wear)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tire_wear = [.77, .56, .89, .28]

        car = Thovex(last_service_date, current_mileage,
                     last_service_mileage, tire_wear)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()