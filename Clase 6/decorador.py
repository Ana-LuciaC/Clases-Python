def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("Vamos a realizar un cálculo")
        funcion_parametro()
        print("Terminé el cálculo")
    return funcion_interior

@funcion_decoradora
def suma():
    print(15 + 20)

def resta()
    print(30 - 10)
@funcion_decoradora
suma()
resta()