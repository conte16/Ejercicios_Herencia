from Estudiante import Estudiante
from Materias import Materias
from Materias import notaMateria

class Notas(Estudiante, Materias):
    pass

    def notasLaboratorio_Parcial():
        nota1 = 10.0
        nota2= 10.0
        nota3 = 10.0
        notaParcial = 9.0
        notaLaboratorioFinal = (nota1+nota2+nota3)/3*0.4
        notaParcialFinal = (notaParcial)*0.6
        notaFinal = (notaLaboratorioFinal+notaParcialFinal)
        return'Registro nota: Estudiante {}, {} Nota final : {}'.format(Estudiante.nombre,Estudiante.carrera,notaFinal)
nota = Notas
print(nota.notasLaboratorio_Parcial())
    