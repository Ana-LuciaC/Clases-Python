from tkinter import *
from empleado import Empleado 
from nomina import Nomina

class Ejercicio1:
    def frame(self):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        frame.config(bg = "blue")
        frame.config(width=480,height=400)
        root.mainloop()

class Ejercicio2:
    def label1(self):
        root = Tk()
        Label(root, text = "Hola Mundo").pack()
        Label(root, text = "Hola Mundo 2").pack()
        Label(root, text = "Ultimolabel").pack()

        labelDiferente = Label(root, text = "Label Diferente")
        labelDiferente.pack(anchor=CENTER)
        labelDiferente.config(
                                fg = "blue",
                                bg = "red",
                                font = ("verdana", 24))
        root.mainloop()

class Ejercicio3: 

    def inputText(self):
        root = Tk()

        #NOMBRE
        frame = Frame(root)
        frame.pack()
        entry = Entry(frame)
        entry.pack(side = RIGHT)
        label = Label(frame, text = "Nombre Empleado")
        label.pack(side = LEFT)

        #APELLIDO
        frame1 = Frame(root)
        frame1.pack()
        entry1 = Entry(frame1)
        entry1.pack(side = RIGHT)
        label1 = Label(frame1, text = "Apellido")
        label1.pack(side = LEFT)

        #CARGO
        frame2 = Frame(root)
        frame2.pack()
        entry2 = Entry(frame2)
        entry2.pack(side = RIGHT)
        label2 = Label(frame2, text = "Cargo")
        label2.pack(side = LEFT)

        root.mainloop()

    def inputText2(self):
        root = Tk()
        label = Label(root, text = "Nombre")
        label.grid(row=0, column=0)

        entry = Entry(root)
        entry.grid(row=0, column=1)

        label2 = Label(root, text = "Apellido")
        label2.grid(row=1, column=0)

        entry2 = Entry(root)
        entry2.grid(row=1, column=1)

        label3 = Label(root, text = "Cargo")
        label3.grid(row=2, column=0)

        entry3 = Entry(root)
        entry3.grid(row=2, column=1)

        root.mainloop()

    def textArea(self):
        root = Tk()
        texto = Text(root)
        texto.pack()
        root.mainloop()

class calculadora:
    r = None
    n1 = None
    n2 = None

    def sumar(self):
        resultado = float(self.n1.get()) + float(self.n2.get())
        self.r.set(resultado)
        self.limpiar()
        
    def limpiar (self):
        self.n1.set("")
        self.n2.set("")
        
    def inicio(self):
        root = Tk()
        self.r = StringVar()
        self.n1 = StringVar()
        self.n2 = StringVar()

        root.config(bd=15)

        Label(root, text="Numero 1").pack()
        Entry(root, justify=CENTER, textvariable = self.n1).pack()

        Label(root, text="\nNumero 2").pack()
        Entry(root, justify=CENTER, textvariable = self.n2).pack()

        Label(root, text="\nResultado").pack()
        Entry(root, justify=CENTER, state=DISABLED, textvariable=self.r).pack()

        Label(root).pack()  # Separador 
        Button(root, text="Sumar", command=self.sumar).pack()

        root.mainloop()

class InterfazNomina:
    def __init__(self):
        self.root = Tk()
        self.root.config(bd = 15)
        self.nombres = StringVar()
        self.apellidos = StringVar()
        self.cargo = StringVar()
        self.salario = StringVar()
        self.nomina = Nomina()
        self.texto = Text(self.root)

    def agregarEmpleado(self):
        empleado = Empleado()
        empleado.setNombre(self.nombres.get())
        empleado.setApellido(self.apellidos.get())
        empleado.setCargo(self.cargo.get())
        empleado.setSueldo(self.salario.get())

        self.nomina.setsalarioBasico(float(self.salario.get()))
        self.nomina.setDiasLiquidados(30)    
        self.limpiar()
        self.texto.insert('insert', empleado)
        self.texto.insert('insert', '\n **************\n')
        self.texto.insert('insert', self.nomina)
        self.texto.insert('insert', '\n **************\n')


        print(empleado)
        print('************************************')
        print(self.nomina)


    def limpiar(self):
       self.nombres.set("")
       self.apellidos.set("")
       self.cargo.set("")
       self.salario.set("")
    def interfaz(self):
        frame = Frame(self.root, width=480, height=320)

        #NOMBRE
        labelEmpleado = Label(frame, text = "Nombre del empleado")
        labelEmpleado.grid(row=0, column=0)
        inputEmpleado = Entry(frame, textvariable = self.nombres)
        inputEmpleado.grid(row=0, column=1)
 

        #APELLIDO
        labelApellido = Label(frame, text = "Apellidos")
        labelApellido.grid(row=1, column=0)
        inputApellido = Entry(frame, textvariable = self.apellidos)
        inputApellido.grid(row=1, column=1)


        #CARGO
        labelCargo = Label(frame, text = "Cargo")
        labelCargo.grid(row=2, column=0)
        inputCargo = Entry(frame, textvariable = self.cargo)
        inputCargo.grid(row=2, column=1)


         #SALARIO
        labelSalario = Label(frame, text = "Salario")
        labelSalario.grid(row=3, column=0)
        inputSalario = Entry(frame, textvariable = self.salario)
        inputSalario.grid(row=3, column=1)

        agregar = Button(frame, text="Agregar", command=self.agregarEmpleado)
        agregar.grid(row=4, column =1)


        frame.pack(fill="both", expand=1)
        self.texto.pack(fill= 'both', expand=1)

        self.root.mainloop()