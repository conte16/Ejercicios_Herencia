from jugador_1 import jugador_1
from jugador_2 import jugador_2
from jugador_1 import luchar

class Pelea(jugador_1,jugador_2):
    pass
    def lanzar_Golpe():
        Patricio = 100
        Rambo= 100
        
        lanzargolpe = (Rambo)
        vidaRestada = (Rambo-30)
        totalvida = (vidaRestada)
        return'El jugador 1 {} lanza una patada al jugador 2 {} dejandolo con un total de vida del {}%'.format(jugador_1.luchador1,jugador_2.luchador2, totalvida)
pelea = Pelea
print(pelea.lanzar_Golpe())
