from bacilo_de_Koch.Modulos.FunGrafTodoEn1 import en1los4
from bacilo_de_Koch.Modulos.FuncionesGenerales import print_resp

# HOST:
# ruta = "/home/david/Desktop/bacilo_de_Koch/data_Koch/tb_functions.pl"
# ruta_glob = "/home/david/Desktop/bacilo_de_Koch/data_Koch/orfs/*"

# GUEST:
ruta = "/usr/src/app/data_Koch/tb_functions.pl"
ruta_glob = "/usr/src/app/data_Koch/orfs/*"

with open(ruta, "r") as tbf:
    lineas = tbf.readlines()

if __name__ == '__main__':
    en1los4(ruta, ruta_glob, lineas)
    print_resp(ruta)
