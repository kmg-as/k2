"""
Stwórz klase Postać
która ma strybuty
-zycie
-sila
-zwinnosc
-obrona
-imie

*przy użyciu biblioteki Faker stwórz mechanizm tworzenia losowych postaci

pip install faker
"""


class Postac:
    def __init__(self, name, zycie, sila, zwinnosc, obrona):
        self.name = name
        self.zycie = fake.random.radiant(1, 101)
        self.sila = fake.random.radiant(1, 101)
        self.zwinnosc = fake.random.radiant(1, 101)
        self.obrona = fake.random.radiant(1, 101)

    def postac(self):
        from faker import Faker
        fake = Faker("pl_PL")
        print(fake.name)

    @classmethod
    def with_fake_name(cls):
        return cls(fake.name())

    def __str__(self):
        return f"<{self.name}| z:{self.zycie}| z:{self.sila}| z:{self.zwinnosc}| z:{self.obrona}|>"

    @staticmethod
    def walka


class Przedmiot:
    def __init__(self, name, do_sily, do_obrony):
    self.name = name
    self.do_sily = fake.random.radiant(1,20)
    self.do_obrony = fake.random.radiant(1, 20)
    self.polozenie = fake.random.radiant(1, 101)




postac = Postac("Zenek")
print(postac)


class TestPostac:
    def test_init(self):
        assert Postac(Bob, 4, 3, 2, 1)
