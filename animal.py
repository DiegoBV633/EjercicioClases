class Animal:
    def __init__(self, nombre, especie, numero_patas, alas, genero, edad):
        self.nombre = nombre
        self.especie = especie
        self.numero_patas = numero_patas
        self.alas = alas
        self.genero = genero
        self.edad = edad

    def descripcion(self):
        print("Mi nombre es %s, mi especie es %s, tengo %i patas, %s, mi genero es %s, y mi edad es de: %i" % (self.nombre, self.especie, self.numero_patas, self.alas, self.genero, self.edad))

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_especie(self, nueva_especie):
        self.especie = nueva_especie