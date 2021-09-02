import matplotlib  # GUEST
matplotlib.use('TkAgg')  # GUEST
import matplotlib.pyplot as plt
from bacilo_de_Koch.Modulos.FuncionesGenerales import orfs_x_clase, prot, hydro13, lista_orf_lista_idcl,\
    dicc_orf_rel_todos_txt, promedio_diccionario, cldim0m

def en1los4(ruta, ruta_glob, lineas):
    fig = plt.figure(figsize=(15, 10), constrained_layout=False)
    gs = fig.add_gridspec(3, 3)
    fig.suptitle('Todas las respuestas gráficas en 1 imagen', fontsize=15)

    # graf1_1:
    x1_1 = orfs_x_clase(ruta)["Clases"]
    y1_1 = orfs_x_clase(ruta)["ORFs"]
    ax1_1 = fig.add_subplot(gs[0, :])
    ax1_1.bar(x1_1, y1_1, color="tab:blue")
    ax1_1.set_title('ORFs por clase')
    ax1_1.set(xlabel='Clases', ylabel='Número de ORFs')
    ax1_1.tick_params(axis='x', rotation=90, labelsize=6)
    ax1_1.set_position([0.125, 0.6535294117647059, 0.7750000000000001, 0.25])

    # graf2_1:
    x2_1 = ["Clases >= 1 ORF 'protein'",
            "Clases >= 1 ORF\n'hydro' en palabra\nde 13 caracteres"]
    y2_1 = [len(lista_orf_lista_idcl(prot(lineas), lineas)),
            len(lista_orf_lista_idcl(hydro13(lineas), lineas))]
    ax2_1 = fig.add_subplot(gs[1:, 0])
    ax2_1.bar(x2_1, y2_1, color="tab:green")
    ax2_1.set_title("Nº clases según ORFs")
    ax2_1.set(xlabel='Clases según ORF', ylabel='Número de clases')
    for index, value in enumerate(y2_1):
        ax2_1.text(index, value, str(value))
    ax2_1.set_position([0.125, 0.10999999999999999, 0.22794117647058826, 0.35])

    # graf2_2:
    x2_2 = ["'protein'",
            "'hydro' en palabra\nde 13 caracteres"]
    y2_2 = [promedio_diccionario(dicc_orf_rel_todos_txt(prot(lineas), ruta_glob)),
            promedio_diccionario(dicc_orf_rel_todos_txt(hydro13(lineas), ruta_glob))]
    ax2_2 = fig.add_subplot(gs[1:, 1])
    ax2_2.bar(x2_2, y2_2, color="tab:red")
    ax2_2.set_title("Promedio de ORFs con los que\nse relacionan los ORFs con el patrón 'protein'\no 'hydro' en \
palabra de 13 caracteres")
    ax2_2.set(xlabel='Patrón del ORF', ylabel='Promedio de ORFs relacionados')
    for index, value in enumerate(y2_2):
        ax2_2.text(index, value, str(round(value, 3)))
    ax2_2.set_position([0.3985294117647059, 0.10999999999999999, 0.2279411764705882, 0.35])

    # graf3:
    x3 = cldim0m(lineas)[0]
    y3 = cldim0m(lineas)[1]
    ax3 = fig.add_subplot(gs[1:, 2])
    ax3.bar(x3, y3, color="tab:purple")
    ax3.set_title("Enteros M y clases con mínimo\n1 dimensión > 0 y múltiple de M")
    ax3.set(xlabel="Enteros M", ylabel="Clases >= 1 dimensión > 0 y múltiple de M")
    for index, value in enumerate(y3):
        ax3.text(index, value, str(value))
    ax3.set_position([0.6720588235294118, 0.10999999999999999, 0.2279411764705882, 0.35])

    # GUEST:
    # plt.savefig("/usr/src/app/Graficos_respuesta/4graf_en1.png")

    # HOST:
    # plt.savefig("/home/david/Desktop/bacilo_de_Koch/Graficos_respuesta/4graf_en1.png")
    plt.show()

# Bibliografía:
# https://stackoverflow.com/questions/48682892/relative-coordinates-using-get-and-set-axes-methods-in-matplotlib
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.set_position.html
# https://matplotlib.org/3.1.1/tutorials/intermediate/constrainedlayout_guide.html
# https://matplotlib.org/3.1.1/tutorials/intermediate/gridspec.html
# https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.add_subplot

# Aprendizajes:
# Axes.set_position([left, bottom, width, height]),
# donde 'left, bottom, width, height' sale de Axes.get_position().bounds
