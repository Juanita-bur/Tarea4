import csv 
with open("vehiculos.csv", "w") as archivo:

    archivo.write("")
class Vehiculo():
    def __init__(self,marca,modelo,numero_de_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_ruedas = numero_de_ruedas
    def __str__(self):
        return  f"Marca: {self.marca}, modelo: {self.modelo}, {self.numero_de_ruedas} ruedas"
    
    def guardar_datos_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'a') as f:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(f)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print('No se ha encontrado el archivo.')
        except Exception as error:
            print('Se ha generado un error no previsto', type(error).__name__)
    
    def leer_datos_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo,'r') as archivo:
                vehiculos = csv.reader(archivo)
                print(f"\n Lista de vehiculos: {type(self).__name__}")
                for vehiculo in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in vehiculo:
                        print(vehiculo[1])
        except Exception as error:
            print('Se ha generado un error no previsto', type(error).__name__)


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, cilindrada, velocidad):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.cilindrada = cilindrada
        self.velocidad = velocidad
    def __str__(self):
        return  super().__str__() + f", {self.velocidad}Km/h, cilindrada: {self.cilindrada}cc"

class AutomovilParticular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, cilindrada, velocidad, numero_puestos):
        super().__init__(marca, modelo, numero_de_ruedas, cilindrada, velocidad)
        self.numero_puestos = numero_puestos
    def __str__(self):
        return  super().__str__() + f", Puestos: {self.numero_puestos}"

class AutomovilCarga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, cilindrada, velocidad, peso_carga):
        super().__init__(marca, modelo, numero_de_ruedas, cilindrada, velocidad)
        self.peso_carga = peso_carga
    def __str__(self):
        return  super().__str__() + f", Carga: {self.peso_carga}Kg"

class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,numero_de_ruedas, tipo):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo= tipo
    def __str__(self):
        return  super().__str__() + f", Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self,marca,modelo,numero_de_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
    def __str__(self):
        return  super().__str__() + f", Motor: {self.motor}T, Cuadro: {self.cuadro}, Nro radios: {self.nro_radios}"
