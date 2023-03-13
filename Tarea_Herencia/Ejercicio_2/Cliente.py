from categorias import Categorias
from Peliculas import Peliculas

class cliente(Categorias,Peliculas):
    pass
    def seleccionarCategoria():
      
       x = "accion"
       z = "comedia"
       y = "terror"

       if x =="comediar":
        print("Rapidos y furiosos, categoaria accion")
       elif z == "comedia":
        print("Luna de miel en familia-categoria comedia")
       elif y == "terror":
         print("Hereditary, categoria terror")
       else:
        print("Seleccione una categoria disponible")

seleccion = cliente
print("Su elecion de pelicula según categoria fue:")
print(seleccion.seleccionarCategoria())



