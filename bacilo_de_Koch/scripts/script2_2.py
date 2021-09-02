from bacilo_de_Koch.Modulos.FuncionesGenerales import prot, dicc_orf_rel_todos_txt, hydro13
from bacilo_de_Koch.Modulos.FuncionesGraficas import graf2_2

ruta = "C:/Users/dasan/PycharmProjects/bacilo_de_Koch/data_Koch/tb_functions.pl"
ruta_glob = "C:/Users/dasan/PycharmProjects/bacilo_de_Koch/data_Koch/orfs/*"
with open(ruta, "r") as tbf:
    lineas = tbf.readlines()  # Explicado en script previo

if __name__ == '__main__':
    graf2_2(dicc_orf_rel_todos_txt(prot(lineas), ruta_glob), dicc_orf_rel_todos_txt(hydro13(lineas), ruta_glob))