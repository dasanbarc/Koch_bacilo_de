import re
import pandas as pd
import glob
from multiprocessing import Pool
import ast


def orfs_x_clase(ruta):
    """
    Devuelve, tras leer el fichero, un dataframe con clases
    y ORFs por clase.

    Args:
        ruta (string con la ruta del archivo).

    Returns: dataframe (clases y cantidad de ORFs por clase).
    """
    lista_cf = []  # lista con los identificadores de clase.
    with open(ruta, "r") as tbf:
        lineas = tbf.readlines()
        for linea in lineas:
            idcl = re.search(r"\[[0-9]+,[0-9]+,[0-9]+,[0-9]+]",
                             linea).group(0)
            lista_cf.append(idcl)
    lista_clases = []  # lista con las clases.
    lista_orfs = []  # lista con cuántos ORFs tiene cada clase.
    for i in set(lista_cf):
        lista_clases.append(i)
        lista_orfs.append(lista_cf.count(i) - 1)
    # dataframe con clases y cantidad de ORFs por cada clase
    df_co = pd.DataFrame({"Clases": pd.Series(lista_clases),
                          "ORFs": pd.Series(lista_orfs)})
    return df_co


def print_resp(ruta):
    """
    Lee archivo, imprime clases 'Respiration' con su cantidad de ORFs.

    Args:
        ruta (string con la ruta del archivo).
    """
    lista_resp = []  # Contendrá clases con 'Respiration' en su descripción.
    with open(ruta, "r") as tbf:
        lineas = tbf.readlines()
        for linea in lineas:
            if linea.startswith("class"):
                if re.findall(r'Respiration',
                              linea,
                              re.IGNORECASE):
                    a = re.search(r"\[[0-9]+,[0-9]+,[0-9]+,[0-9]+]",
                                  linea).group(0)
                    lista_resp.append(a)
    nudf = orfs_x_clase(ruta)  # Es el dataframe resultante de la
    # función orfs_x_clase().
    for i in lista_resp:
        ind_cl = nudf.loc[nudf.Clases == i, ["ORFs"]].index[0]
        print("La clase {}, descrita como 'Respiration', engloba {} ORFs."
              .format(i, nudf.loc[ind_cl, "ORFs"]))


def prot(lineas):
    """
    Del archivo 'tb_functions.pl' devuelve lista de ORFs con 'protein'.

    Args:
        lineas: lista de todas las líneas del archivo 'tb_functions.pl'.

    Returns: lista de ORFs con 'protein'.
    """
    lista_orf_prot = []
    for linea in lineas:
        if linea.startswith("function") and re.findall(r'protein', linea,
                                                       re.IGNORECASE) != []:
            orf_prot = re.search(r'tb[0-9]+', linea).group(0)
            lista_orf_prot.append(orf_prot)
    return lista_orf_prot


def hydro13(lineas):
    """
    Del archivo 'tb_functions.pl' devuelve lista de ORFs
    con 'hydro' en una palabra de 13 caracteres.

    Args:
        lineas: lista de todas las líneas del archivo 'tb_functions.pl'.

    Returns: lista de ORFs con 'hydro' en una palabra de 13 caracteres.
    """
    lista_orf_hydro = []
    for linea in lineas:
        if linea.startswith("function"):
            lista_hydro_linea = re.findall(
                r'[a-z]*hydro[a-z]*', linea, re.IGNORECASE)
            if lista_hydro_linea != [] and [i for i in lista_hydro_linea
                                            if len(i) == 13] != []:
                orf_hydro = re.search(r'tb[0-9]+', linea).group(0)
                lista_orf_hydro.append(orf_hydro)
    return lista_orf_hydro


def lista_orf_lista_idcl(lista_orfs, lineas):
    """
    De lista de ORFs devuelve lista de clases no repetidas.

    Args:
        lista_orfs: lista de ORFs.
        lineas: lista de todas las líneas del archivo 'tb_functions.pl'.

    Returns:
        lista_idcl: lista de clases no repetidas.
    """
    lista_idcl = []
    for linea in lineas:
        for orf in lista_orfs:
            if linea.startswith("function(" + orf + ",["):
                idcl = re.search(r"\[[0-9]+,[0-9]+,[0-9]+,[0-9]+]",
                                 linea).group(0)
                if idcl not in lista_idcl:
                    lista_idcl.append(idcl)
    return lista_idcl


def tttevalue(todo_1_str, lista_orfs):
    """
    De 1 string y 1 lista ORFs devuelve un diccionario {"ORF": relaciones}
    si ORF en ambos argumentos.

    Args:
        todo_1_str: archivo tb_data_xx.txt convertido a 1 string.

        lista_orfs: lista de ORFs.

    Returns: diccionario {"ORF": relaciones}.
    """
    dicc_orf_rels = {}
    for i in lista_orfs:
        h = "begin(model(" + i + "))."
        if h in todo_1_str:
            j = "begin\(model\(" + i + "\)\)|end\(model\(" + i + "\)\)"
            k = re.split(j, todo_1_str)[1].count("tb_to_tb_evalue")
            dicc_orf_rels[i] = k
    return dicc_orf_rels


def apert1str(rutarch):
    """
    Devuelve el archivo en 1 string.

    Args:
        rutarch: ruta de archivo tb_data_xx.txt.

    Returns: todo el archivo en 1 string.
    """
    with open(rutarch, "r") as orfp:
        todo_1_str = orfp.read()
    return todo_1_str


def lista_tuplas_1str_liorf(ruta1, lista_orfs):
    """
    Convierte en 1 string cada archivo, devuelve lista de
    tuplas '(str, lista_orfs)' con tantas tuplas como archivos.

    Args:
        ruta1: ruta de carpeta (acabada en '/*') que contiene los archivos
        tb_data_xx.txt.

        lista_orfs: lista de ORFs.

    Returns: lista de tuplas '(str, lista_orfs)'.
    """
    apert_glob = map(apert1str, glob.glob(ruta1))
    lista_apert_glob = list(apert_glob)
    lista_tuplas = []
    for i in lista_apert_glob:
        tupla = (i, lista_orfs)
        lista_tuplas.append(tupla)
    return lista_tuplas


def dicc_orf_rel_todos_txt(lista_orfs, ruta1):
    """
    De lista ORFs devuelve diccionario {"ORF": relaciones}.

    Extrae la información de todos los archivos tb_data_xx.txt
    en ejecución paralela.

    Args:
        lista_orfs: lista de ORFs (hydro13(lineas) ó prot(lineas)).

        ruta1: ruta de carpeta (acabada en '/*') que contiene los archivos
        tb_data_xx.txt.

    Returns: diccionario {"ORF": relaciones}
    """
    pool = Pool(processes=None)
    lista_dicts = pool.starmap(tttevalue, lista_tuplas_1str_liorf(ruta1, lista_orfs))
    pool.close()

    dict_todo = {k: v for dicc in lista_dicts for k, v in dicc.items()}
    return dict_todo


def promedio_diccionario(diccionario):
    """
    Obtiene promedio de valores por clave de diccionario
    cuyos valores son números.

    Args:
        diccionario {clave: número}

    Returns: promedio de valores por clave.
    """
    return sum(diccionario.values()) / len(diccionario)


def cldim0m(lineas):
    """
    Devuelve 1 tupla con lista de 'M= ' (enteros M en [2, 9]) y lista
    de cuántas clases con mínimo 1 dimensión > 0 y múltiple de M.

    Args:
        lineas: lista de líneas de 'tb_functions.pl'.

    Returns:
        tupla (lista de 'M= ', lista de cuántas clases con mínimo 1 dimensión > 0 y múltiple de M).
    """
    lista_idcls_as_list = []
    for linea in lineas:
        if linea.startswith("class(["):
            idcl = re.search(r"\[[0-9]+,[0-9]+,[0-9]+,[0-9]+]",
                             linea).group(0)
            idcl_as_list = ast.literal_eval(idcl)
            lista_idcls_as_list.append(idcl_as_list)
    lista_m = []
    lista_clases = []
    for M in range(2, 10):
        cont = 0
        for id_cl in lista_idcls_as_list:
            for i in range(0, 4):
                if id_cl[i] > 0 and not id_cl[i] % M:
                    cont += 1
                    break
        lista_m.append("M={}".format(M))
        lista_clases.append(cont)
    return lista_m, lista_clases
