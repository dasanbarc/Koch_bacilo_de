from bacilo_de_Koch.Modulos.FuncionesGenerales import prot, hydro13, lista_orf_lista_idcl
from bacilo_de_Koch.Modulos.FuncionesGraficas import graf2_1

ruta = "C:/Users/dasan/PycharmProjects/bacilo_de_Koch/data_Koch/tb_functions.pl"

# Abro el archivo 'tb_functions.pl' y lo guardo en 'lineas',
# que contiene una lista con todas las líneas del archivo.
with open(ruta, "r") as tbf:
    lineas = tbf.readlines()

graf2_1(lista_orf_lista_idcl(prot(lineas), lineas),
        lista_orf_lista_idcl(hydro13(lineas), lineas))
