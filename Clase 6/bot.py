from threading import *
from datetime import datetime
import time
import requests

class Bot:
    def observadorRelog(self):
        while(True):
            time.sleep(1)
            now = datetime.now()
            horaActual = now.strftime('%H:%M:%S')
            
            if horaActual == '16:32:00':
                self.saludarSuperHeroe("batman")    
    def saludarSuperHeroe(self, nombre):
        url = str('http://localhost:4000/saludo/{}').format(nombre)
        r = requests.get(url) 
        if r.status_code == 200:
            print(r.text)

    def iniciar(self):
        t = Timer(1.0, self.observadorReloj)
        t,start()

def main():
    b= Bot()
    b.iniciar

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()