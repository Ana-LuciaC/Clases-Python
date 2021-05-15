import psycopg2

class Conector:
    def__init__(self):
        self.database = 'db_analucia'
        self.user = 'postgres'
        self.password = 'Clase Python'
        self.host = '34.69.92.174'
        self.port = '5432'
    def descargarDta(self, sql):
        c = psycopg2.connect(database = self.database, user= self.user,
        password = self.password, host = self.host, port = self.port)

        try: 
            with c.cursor() as cursor: 
                cursor.execute(sql)

                for i in cursor:
                    print(i)

                cursor.close()
                c.close()
        finally:
            pass


if __name__ == '__main__':
    try:
        c = conector()
        c,descargarData('select * from nomina.empleados;')
    except KeyboardInterrupt:
        print("saliendo")
        exit()
                

    