#### Proyecto bacilo_de_Koch

# DOCKER:
	Ejecuta en el terminal: xhost +
	Luego ejecuta también en el terminal: docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY <nombre de la imagen> bash
	Finalmente, ejecuta dentro del contenedor: python -m bacilo_de_Koch.scripts.scripts_all

Da respuesta mediante scripts a las preguntas de la PEC4.
Los scripts y los módulos están dentro de la carpeta "bacilo_de_Koch".
Por ejemplo, el script1_1.py, ejecutado en el terminal, responde a la pregunta 1.1 de la PEC4.
Los scripts 1_1, 2_1, 2_2 y 3 dan respuestas gráficas con la información pedida;
el script 1_2 muestra su respuesta en el propio terminal; script4grafEn1 da todas las respuestas gráficas;
scripts_all da todas las respuestas gráficas más la respuesta escrita en el terminal.

En la carpeta 'tests' está el script con los tests, que ofrecen una cobertura del 70%:

datasci@datasci:~/PycharmProjects/bacilo_de_Koch$ coverage report
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
bacilo_de_Koch/Modulos/FuncionesGenerales.py     105     12    89%   43-58
bacilo_de_Koch/Modulos/FuncionesGraficas.py       45     33    27%   16-21, 38-46, 60-73, 87-96
bacilo_de_Koch/Modulos/__init__.py                 0      0   100%
----------------------------------------------------------------------------
TOTAL                                            150     45    70%


He usado la sintaxis "with open" para leer los archivos porque considero que es lo más eficiente en este caso, donde
cada línea contiene información que hay que clasificar usando expresiones regulares (no es un .csv, donde podría
organizar los datos en un dataframe, aunque tampoco sería idóneo por el gran volumen de datos).

Respecto a las gráficas, he usado barplots, pues creo que transmiten con claridad la información solicitada.


#### Bibliografía:

https://stackabuse.com/read-a-file-line-by-line-in-python/

https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf

https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python

https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/

https://docs.python.org/3/tutorial/controlflow.html

https://www.geeksforgeeks.org/python-merging-two-dictionaries/

https://docs.python.org/3/library/multiprocessing.html

https://stackoverflow.com/questions/3494906/how-do-i-merge-a-list-of-dicts-into-a-single-dict

https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments

https://docs.python.org/dev/library/multiprocessing.html#multiprocessing.pool.Pool.starmap

https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000129550-How-can-I-install-the-TKinter-in-Pycharm

https://docs.python.org/3.8/library/unittest.html#unittest.TestCase.debug

https://docs.python.org/3.8/library/unittest.html#unittest.TestCase.assertRaises

https://www.analyticslane.com/2020/03/13/cobertura-de-las-pruebas-unitarias-en-python-creacion-de-paquetes-de\
-python-4a-parte/

https://coverage.readthedocs.io/en/coverage-4.0.3/config.html

https://www.kite.com/python/answers/how-to-display-the-value-of-each-bar-in-a-bar-chart-using-matplotlib-in-python

https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html

https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

https://docs.python-guide.org/writing/license/

https://choosealicense.com/

https://www.py4u.net/discuss/142482  # Docker graph display

https://stackoverflow.com/questions/55811545/importerror-cannot-load-backend-tkagg-which-requires-the-tk-interactive-fra

https://youtu.be/NVvZNmfqg6M
