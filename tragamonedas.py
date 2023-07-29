import random
class NoHayMonedaException(Exception):
    pass
class NoHayMonedasParaPremioException(Exception):
    pass

class Tragamonedas():
    def __init__(self) -> None:
        self.monedas = int
        self.monedas_tirada = 0
        self.tirada = [2,2,2]
    
    def insertar_moneda(self):
        if self.monedas_tirada*10+10 > self.monedas:
            raise NoHayMonedasParaPremioException()
        self.monedas +=1
        self.monedas_tirada +=1
    
    def tirar(self):
        premio = 0
        if self.monedas_tirada == 0:
            raise NoHayMonedaException()
#        for i in range(3):
#            self.tirada.append(random.randinit(1,5))
        if self.tirada[0] == self.tirada[1] == self.tirada[2]:
            premio = self.monedas_tirada * self.tirada[0]
            self.monedas -= premio
        self.monedas_tirada = 0
        return premio



