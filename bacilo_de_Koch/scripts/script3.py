from bacilo_de_Koch.Modulos.FuncionesGenerales import cldim0m
from bacilo_de_Koch.Modulos.FuncionesGraficas import graf3

# HOST (Windows):
# ruta = "C:/Users/dasan/PycharmProjects/bacilo_de_Koch/data_Koch/tb_functions.pl"

# GUEST:
ruta = "/usr/src/app/data_Koch/tb_functions.pl"

with open(ruta, "r") as tbf:
    lineas = tbf.readlines()

graf3(cldim0m(lineas))
