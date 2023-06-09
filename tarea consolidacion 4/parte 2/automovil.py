class Vehiculo():
    def __init__(self,marca,modelo,numero_de_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_ruedas = numero_de_ruedas
    def __str__(self):
        return  f"Marca: {self.marca}, modelo: {self.modelo}, {self.numero_de_ruedas} ruedas"
    
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

lista_vehiculos = []
try:
    numero_automoviles = int(input('Ingrese numero de vehiculos '))
except ValueError as f:
    print('Caracter incorrecto, ingrese un numero.')

contador = 0
while contador < numero_automoviles:
    marca = input('Ingrese la marca: ')
    modelo = input('Ingrese el modelo: ')
    numero_de_ruedas = input('Ingrese el numero de ruedas: ')
    cilindrada = input('Ingrese la cilindrada: ')
    velocidad = input('Ingrese la velocidad máxima: ')

    automovil = Automovil(marca,modelo,numero_de_ruedas,cilindrada,velocidad)
    lista_vehiculos.append(automovil)
    contador += 1
i = 0
for auto in lista_vehiculos:
    print(f"Datos del automovil {i+1}:", auto)
    i += 1

particular = AutomovilParticular("Ford", "Fiesta", 4, "180", "500", 5)
carga = AutomovilCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva",21,"DobleViga", "2T")

def impresion_instancias():
    print(particular)
    print(carga)
    print(bicicleta)
    print(motocicleta)

impresion_instancias()

moto_vehi=  isinstance(motocicleta,Vehiculo)
print(f'Motocicleta es instancia con relación a Vehículo: {moto_vehi}')

moto_auto=  isinstance(motocicleta,Automovil)
print(f'Motocicleta es instancia con relación a Automovil: {moto_auto}')

moto_parti=  isinstance(motocicleta,AutomovilParticular)
print(f'Motocicleta es instancia con relación a Vehículo particular:  {moto_parti}')

moto_carga=  isinstance(motocicleta,AutomovilCarga)
print(f'Motocicleta es instancia con relación a Vehículo de Carga: {moto_carga}')

moto_bici=  isinstance(motocicleta,Bicicleta)
print(f'Motocicleta es instancia con relación a Bicicleta:  {moto_bici}')

moto_moto=  isinstance(motocicleta,Motocicleta)
print(f'Motocicleta es instancia con relación a Motocicleta: {moto_moto}')