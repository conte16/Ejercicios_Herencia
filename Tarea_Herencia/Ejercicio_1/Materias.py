class Materias:
    def __init__(self, materia1):
        self.materia1 = materia1
        

    def obtenerMateria ( self):
        return'Materia : {}'.format(self.materia1)

notaMateria= Materias("Programacion Orientada a Objetos")
print(notaMateria.obtenerMateria())