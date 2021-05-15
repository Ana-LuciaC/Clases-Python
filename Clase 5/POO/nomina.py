from Indicadores import Indicadores
class Nomina(Indicadores):
    def __init__(self):
        self.__salarioBasico = 0
        self.__diasLiquidados = 0
        self.__smlv = self.salariominimo()
        self.__auxilioT = 106454

    def setsalarioBasico(self, salarioBasico):
        if str(type(salarioBasico)) == "<class 'int'>" or str(type(salarioBasico)) == "<class 'float'>":
            print(salarioBasico)
            print(self.salariominimo())
            if salarioBasico >= self.salariominimo():
                 self.__salarioBasico = salarioBasico
            else:
                print("El salario basico no puede ser inferior al SM legal vigente")
        else: 
            print("error")

    def getsalarioBasico(self):
        return self.__salarioBasico
    def setDiasLiquidados(self, diasliquidados):
        self.__diasLiquidados = diasliquidados
    def salarioDevengado(self):
        try:
            return(self.__salarioBasico / 30)* self.__diasLiquidados
        except:
            print("Error al calcular salario Devengado")
    def getDiasLiquidados(self):
            return self.__diasLiquidados
    def auxilioTransporte(self):
        if self.__salarioBasico > (self.__smlv *2):
            return 0
        else:
            return self.__auxilioT / 30 * self.__diasLiquidados
    def totalDevengado(self):
        return self.salarioDevengado() + self.auxilioTransporte()
    def __str__(self):
        return str("salario Básico: {} \n"
                    "Dias Liquidados: {} \n"
                    "Salario Devengado: {} \n "
                    "Auxilio de TRansporte:{} \n"
                    "Total Devengado: {} \n").format(
                    self.__salarioBasico,
                    self.__diasLiquidados,
                    self.salarioDevengado(),
                    self.auxilioTransporte(),
                    self.auxilioTransporte(),
                    self.totalDevengado())
