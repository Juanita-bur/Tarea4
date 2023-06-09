from clase import *
import csv


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

particular.guardar_datos_csv('vehiculos.csv')
carga.guardar_datos_csv('vehiculos.csv')
bicicleta.guardar_datos_csv('vehiculos.csv')
motocicleta.guardar_datos_csv('vehiculos.csv')
particular.leer_datos_csv('vehiculos.csv')
carga.leer_datos_csv('vehiculos.csv')
bicicleta.leer_datos_csv('vehiculos.csv')
motocicleta.leer_datos_csv('vehiculos.csv')

