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
print(f'Datos del automovil ingresado {lista_vehiculos}')