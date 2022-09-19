from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date, tire_wear):
        self.last_service_date = last_service_date
        self.tire_wear = tire_wear

    @abstractmethod
    def needs_service(self):
        pass
