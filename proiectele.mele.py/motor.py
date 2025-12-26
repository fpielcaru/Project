class Motor:
    def __init__(self, serie_motor, putere, km_parcursi):
        self.__serie_motor = serie_motor
        self.__putere = putere
        self.__km_parcursi = km_parcursi
    @property
    def serie_motor(self):
        return self.__serie_motor
    @serie_motor.setter
    def serie_motor(self, value):
        self._serie_motor = value
    @property
    def putere(self):
        return self.__putere
    
    @putere.setter
    def putere(self, value):
        self._putere = value
    @property
    def km_parcursi(self):
        return self.__km_parcursi
    @km_parcursi.setter
    def km_parcursi(self, value):
        self.km_parcursi = value

    def afisare_motor(self):
        return f"Serie motor: {self.serie_motor}, puterea motorului : {self.putere}, km_parcursi: {self.km_parcursi}"
    

motor1 = Motor("AB1256CD", 150, 500000)
print(motor1.afisare_motor())