from animal import Animal

Animales = []
x = ""
while x != "x":
    nombre = input("Ingrese el nombre del animal:\n ")
    especie = input("Ingrese la especie del animal:\n ")
    numero_patas = int(input("Ingrese el numero de patas del animal:\n "))
    tiene_alas = input("Ingrese si el animal tiene alas (s/n): \n ")
    genero = input("Ingrese el genero del animal:\n ")
    edad = int(input("Ingrese la edad animal:\n "))

    if tiene_alas == "s":
        alas = "tengo alas"
    elif tiene_alas == "n":
        alas = "no tengo alas"

    animal_nuevo = Animal(nombre, especie, numero_patas, alas, genero, edad)
    Animales.append(animal_nuevo)

    x = input("Ingrese x para dejar de agregar animales, ingrese cualquier otra cosa si desea continuar \n")

for animal in Animales:
    animal.descripcion()

for animal in Animales:
    cambio_nombre = input("Desea cambiar el nombre de " + animal.nombre + "?(s/n)\n")
    if cambio_nombre == "s":
        nuevo_nombre = input("Ingrese el nombre nuevo \n")
        animal.cambiar_nombre(nuevo_nombre)


for animal in Animales:
    cambio_especie = input("Desea cambiar la especie de " + animal.especie + "?(s/n)\n")
    if cambio_especie == "s":
        nueva_especie = input("Ingrese el nombre nuevo \n")
        animal.cambiar_especie(nueva_especie)

for animal in Animales:
    animal.descripcion()

