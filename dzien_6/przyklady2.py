class Pojazd:
    def poruszaj_sie(self):
        print("Porusza się")

    def stop(self):
        print("Pojazd zatrzymał się")


class Statek(Pojazd):
    pass

prom=Statek()
prom.poruszaj_sie()