class Categorias:
    def __init__(self, accion, comedia,terror):
        self.accion= accion
        self.comedia=comedia
        self.terror=terror
    
    def obtenerCategoria(self):
        return'Categorias disponibles: {}, {} y {}'.format(self.accion, self.comedia,self.terror)

categoria = Categorias("Accion", "Comedia", "Terror")
print(categoria.obtenerCategoria())
        