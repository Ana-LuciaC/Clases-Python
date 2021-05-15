
'''
from nomina import Nomina
n = Nomina()
n.setsalarioBasico(2500000)
n.setDiasLiquidados(20)
print(n.getsalarioBasico())
print(n.salarioDevengado())
'''

from nomina import Nomina
nominas = []

while True:
    print("1. Ingresanomina")
    print("2.salir")

    opcion = input("Ingrese la opcion: ")

    if opcion == '1':
        renglon = []
        n = Nomina()
        salario = float(input("Ingrese el sueldo basico:"))
        diasL = float(input("Ingrese los dias liquidados: "))
        n.setsalarioBasico(salario)
        n.setDiasLiquidados(diasL)

        renglon.append({'variable': 'Salario Basico', 'Resultado': n.getsalarioBasico()})
        renglon.append({'variable': 'Dias Liquidados', 'Resultado': n.getDiasLiquidados()})
        renglon.append({'variable': 'Salario Devengado', 'Resultado': n.salarioDevengado()})
        renglon.append({'variable': 'Auxilio Transporte', 'Resultado': n.auxilioTransporte()})
        renglon.append({'variable': 'Total devengado', 'Resultado': n.totalDevengado()})
        nominas.append(renglon)
       
    elif opcion == '2':
        print("Saliendo")
        break

ef = pd.DataFrame(nominas)
print(df.head())

#Escribir un archivo plano
f = open('nominas.txt','w')
for i in nominas: 
    f.write('*******************************')
    for j in i:
        f.write(str(j) + "\n")
f.close()