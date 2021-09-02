import matplotlib.pyplot as plt
from bacilo_de_Koch.Modulos.FuncionesGenerales import promedio_diccionario


def graf1_1(df):
    """
    Muestra el gráfico del dataframe devuelto por orfs_x_clase(ruta).

    Args:
        df: dataframe de orfs_x_clase(ruta).

    Returns: gráfico del dataframe.
    """
    plt.figure(figsize=(26, 12))
    plt.bar(df["Clases"], df["ORFs"], color="tab:blue")
    plt.title("ORFs por clase")
    plt.xlabel("Clases")
    plt.xticks(rotation=90)
    plt.ylabel("Número de ORFs")
    # plt.savefig("/home/datasci/PycharmProjects/bacilo_de_Koch/Graficos_respuesta/graf1_1.png")
    return plt.show()


def graf2_1(a_prot, b_hydro13):
    """
    Devuelve gráfico con nº clases según ORFs.

    Args:
        a_prot: lista_orf_lista_idcl(prot(lineas), lineas)
        b_hydro13: lista_orf_lista_idcl(hydro13(lineas), lineas)

    Returns: gráfico.
    """
    eje_x = ["Clases >= 1 ORF 'protein'",
             "Clases >= 1 ORF 'hydro' en\npalabra de 13 caracteres"]
    eje_y = [len(a_prot),
             len(b_hydro13)]
    plt.figure(figsize=(6, 7))
    plt.bar(eje_x, eje_y, color="tab:green")
    plt.title("Nº clases según ORFs")
    plt.xlabel("Clases según ORF")
    plt.ylabel("Número de clases")
    for index, value in enumerate(eje_y):
        plt.text(index, value, str(value))
    # plt.savefig("/home/datasci/PycharmProjects/bacilo_de_Koch/Graficos_respuesta/graf2_1.png")
    return plt.show()


def graf2_2(dp, dh):
    """
    Devuelve gráfico del promedio de los valores de 2 diccionarios.

    Args:
        dp: dicc_orf_rel_todos_txt(prot(lineas), ruta_glob)
        dh: dicc_orf_rel_todos_txt(hydro13(lineas), ruta_glob)

    Returns: gráfico.
    """
    pdp = promedio_diccionario(dp)
    pdh = promedio_diccionario(dh)
    eje_x = ["'protein'",
             "'hydro' en palabra\nde 13 caracteres"]
    eje_y = [pdp, pdh]
    plt.figure(figsize=(6, 7))
    plt.bar(eje_x, eje_y, color="tab:red")
    plt.title("Promedio de ORFs con los que se relacionan los ORFs\n\
con el patrón 'protein' o 'hydro' en palabra de 13 caracteres")
    plt.xlabel("Patrón del ORF")
    plt.ylabel("Promedio de ORFs relacionados")
    for index, value in enumerate(eje_y):
        plt.text(index, value, str(round(value, 3)))  # Redondeo a 3 decimales porque queda mejor gráficamente.
    # plt.savefig("/home/datasci/PycharmProjects/bacilo_de_Koch/Graficos_respuesta/graf2_2.png")
    return plt.show()


def graf3(tupla):
    """
    Muestra gráfico con enteros M [2, 9] y nº clases con
    mínimo 1 dimensión > 0 y múltiple de M.

    Args:
        tupla: resultado de cldim0m(lineas).

    Returns: gráfico.
    """
    eje_x = tupla[0]
    eje_y = tupla[1]
    plt.figure(figsize=(15, 8))
    plt.bar(eje_x, eje_y, color="tab:purple")
    plt.title("Enteros M y clases con mínimo 1 dimensión > 0 y múltiple de M")
    plt.xlabel("Enteros M")
    plt.ylabel("Clases con mínimo 1 dimensión > 0 y múltiple de M")
    for index, value in enumerate(eje_y):
        plt.text(index, value, str(value))
    # plt.savefig("/home/datasci/PycharmProjects/bacilo_de_Koch/Graficos_respuesta/graf3.png")
    return plt.show()
