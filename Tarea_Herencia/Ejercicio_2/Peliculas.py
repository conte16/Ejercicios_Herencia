class Peliculas:
    def __init__(self, pelicula_accion,pelicula_comedia,pelicula_terror):
        self.accion= pelicula_accion
        self.comedia=pelicula_comedia
        self.terror=pelicula_terror
    
    def obtenerPelicula(self):
        return'pelicula disponible segun categoria, Accion: {}, Comedia:{} y Terror:{}'.format(self.accion, self.comedia,self.terror)

pelicula = Peliculas("Rapidos y furiosos", "Luna de miel en Familia", "Hereditary")
print(pelicula.obtenerPelicula())
        