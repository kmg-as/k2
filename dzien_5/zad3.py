#klasa ElectricCar odwzorowujaca zachowanie samochodu elektrycznego
#klasa powinna umozliwiać pokonanie zadanego dystansu, który nie może przekroczyc maksymalnego zasięgu, zdefniowanego
#dla samochodu. Samochód powinien mieć takze możliwość naładowania baterii

class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self._traveled=0
    def drive(self,range):
        if self._traveled + range < self.max_range:
            self._traveled +=range
            return range
        to_travel=self.max_range - self._traveled
        self._traveled=self.max_range
        return to_travel
    def charge(self):
        self._traveled=0

class TestElectricCar:
    def test__init__(self):
        car=ElectricCar(100)
        assert car
    def test_drive(self):
        car=ElectricCar(100)
        assert car.drive(70)==70
        assert car.drive(10) == 10
        assert car.drive(30) == 20
        assert car.drive(30) == 0
    def test_charge(self):
        car=ElectricCar(150)
        assert car.drive(150) == 150
        assert car.drive(150) == 0
        car.charge()
        assert car.drive(150) == 150