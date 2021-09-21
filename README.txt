#### Proyecto bacilo_de_Koch

Los datos a analizar son proporcionados en dos colecciones de datos separadas (en la carpeta data_Koch):
tb_functions.pl y orfs/tb_data_0x.pl. Estos datos provienen del repositorio UCI Machine Learning y tienen
formato de datalog; tb_functions.pl contiene información general sobre los genes y sus clases funcionales, mientras
que tb_data_0X.pl contiene información detallada sobre todos los genes indicados.

El archivo tb_functions.pl contiene información sobre 123 clases funcionales de ORFs, donde hay dos tipos de entrada:
	
	- class: tiene 2 elementos separados por comas siempre presentados en el siguiente orden: * identi-
	ficador de la clase: lista de 4 números que describe la clase en 4 dimensiones diferentes (separados
	por comas y entre corchetes), y * descripción de la clase: string que contiene la descripción de la
	clase, ninguna clase comparte descripción con otra clase (string entre comillas dobles).
	
	- function: tiene 4 elementos separados por comas siempre presentados en el siguiente orden: *
	ORF: pauta abierta de lectura (en inglés open reading frame) (string sin comillas), * identificador
	de la clase: lista de 4 números que describe la clase en 4 dimensiones diferentes (separados por
	comas y entre corchetes), * nombre del gen: nombre del gen o valor null si el gen no tiene nombre
	(string entre comillas simples), y * descripción ORF: descripción de la pauta de lectura (string
	entre comillas dobles).
	
Los archivos tb_data_0X.pl tienen la siguiente estructura: los datos para un único ORF están capturados entre los
delimitadores begin(model(ORF)) y end(model(ORF)) y el atributo tb_tono_tb_evalue(ORF, E-value) muestra la relación con otros ORFs.

Los scripts y los módulos están dentro de la carpeta bacilo_de_Koch.

Se plantean las siguientes preguntas:

	1.1. Calcular cuántos ORFs pertenecen a cada clase.

	1.2. Mostrar por pantalla cuántos ORFs pertenecen a la clase que tiene Respiration como descripción.

	2.1. Para cada patrón listado*, calcular el número de clases que contienen como mínimo un ORF con el patrón
	indicado en su descripción.

	2.2. Para cada patrón listado*, calcular el número promedio de ORFs con los cuales se relacionan los ORFs con
	el patrón indicado en su descripción.
	
		* Los patrones para los cuales tendréis que resolver los cálculos 2.1 y 2.2 son:
			- La descripción contiene el término protein.
			- La descripción contiene una palabra de 13 caracteres y esta contiene el término hydro.
			
	3. Para cada entero M entre 2 y 9 (ambos incluidos), calcula el número de clases que tienen como
	mínimo una dimensión mayor estricta (>) que 0 y a la vez múltiple de M. Con el término
	dimensión nos referimos a cada uno de los 4 números que forman el identificador de la clase
	(explicado en la sección anterior). Este cálculo tendrá que resultar en algo como:
		
		M=2: ? clases
		M=3: ? clases
		...
		M=9: ? clases
		
		donde ? representa un entero.

Los scripts script1_1.py, script1_2.py, script2_1.py, script2_2.py y script3.py dan respuesta a las respectivas preguntas.
El script scripts_all.py da todas las respuestas gráficas más la respuesta escrita en el terminal.

Con Docker (para el script scripts_all.py):
	Ejecuta en el terminal: xhost +
	Luego ejecuta en el terminal: docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY <nombre de la imagen> bash
	Finalmente, ejecuta dentro del contenedor: python -m bacilo_de_Koch.scripts.scripts_all

En la carpeta 'tests' está el script con los tests, que ofrecen una cobertura del 70%:

datasci@datasci:~/PycharmProjects/bacilo_de_Koch$ coverage report
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
bacilo_de_Koch/Modulos/FuncionesGenerales.py     105     12    89%   43-58
bacilo_de_Koch/Modulos/FuncionesGraficas.py       45     33    27%   16-21, 38-46, 60-73, 87-96
bacilo_de_Koch/Modulos/__init__.py                 0      0   100%
----------------------------------------------------------------------------
TOTAL                                            150     45    70%

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
