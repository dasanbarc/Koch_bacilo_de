from bacilo_de_Koch.Modulos.FunGrafTodoEn1 import en1los4

ruta = "C:/Users/dasan/PycharmProjects/bacilo_de_Koch/data_Koch/tb_functions.pl"
ruta_glob = "C:/Users/dasan/PycharmProjects/bacilo_de_Koch/data_Koch/orfs/*"
with open(ruta, "r") as tbf:
    lineas = tbf.readlines()

if __name__ == '__main__':
    en1los4(ruta, ruta_glob, lineas)
