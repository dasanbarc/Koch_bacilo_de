import unittest
from bacilo_de_Koch.Modulos.FuncionesGenerales import orfs_x_clase, prot, hydro13, lista_orf_lista_idcl, tttevalue,\
    apert1str, lista_tuplas_1str_liorf, dicc_orf_rel_todos_txt, promedio_diccionario, cldim0m
from bacilo_de_Koch.Modulos.FuncionesGraficas import graf1_1, graf2_1, graf2_2, graf3

# Nueva ruta de archivo reducido para pasar test a las funciones:
ruta = "/home/datasci/PycharmProjects/bacilo_de_Koch/tests/datos_reducidos_test/dsb_muestra_functions.txt"

# Nueva ruta de archivo reducido para pasar test a las funciones:
ruta_orfs = '/home/datasci/PycharmProjects/bacilo_de_Koch/tests/datos_reducidos_test/dsb_muestra_orfs.txt'

# Nueva ruta de carpeta con 4 archivos reducidos para tests:
ruta_carpeta = '/home/datasci/PycharmProjects/bacilo_de_Koch/tests/datos_reducidos_test/dsb_orfs/*'


class TestKoch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(ruta, 'r') as cfl:
            cls._todas_las_lineas = cfl.readlines()

    def test_prot(self):
        self.assertEqual(prot(self._todas_las_lineas), ['tb1853', 'tb1851'])
        self.assertTrue(type(prot(self._todas_las_lineas)) == list)

    def test_hydro13(self):
        self.assertEqual(hydro13(self._todas_las_lineas)[2], 'tb2780')
        self.assertNotIn('tb2531', hydro13(self._todas_las_lineas))

    def test_lista_orf_lista_idcl(self):
        self.assertIn('[1,1,1,0]', lista_orf_lista_idcl(hydro13(self._todas_las_lineas), self._todas_las_lineas))
        self.assertNotIn('[1,0,0,0]', lista_orf_lista_idcl(hydro13(self._todas_las_lineas), self._todas_las_lineas))

    def test_cldim0m(self):
        self.assertIn('M=5', cldim0m(self._todas_las_lineas)[0])
        self.assertTrue(max(cldim0m(self._todas_las_lineas)[1]) == 1)


class TestKoch2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(ruta_orfs, 'r') as rorfs:
            cls._txt1str = rorfs.read()

    def test_tttevalue(self):
        self.assertTrue(sum(tttevalue(self._txt1str, ['tb14', 'tb32']).values()) == 48)
        self.assertNotIn(30, tttevalue(self._txt1str, ['tb14', 'tb32']).values())


class TestKoch3(unittest.TestCase):

    def test_orfs_x_clase(self):
        self.assertEqual(len(orfs_x_clase(ruta)), 4)
        self.assertTrue(orfs_x_clase(ruta).loc[orfs_x_clase(ruta).Clases == '[1,1,1,0]', ["ORFs"]].iloc[0, 0] == 5)

    def test_apert1str(self):
        self.assertTrue(type(apert1str(ruta_orfs)) == str)
        self.assertFalse(apert1str(ruta_orfs).count('begin(model') == 5)

    def test_lista_tuplas_1str_liorf(self):
        self.assertTrue(len(lista_tuplas_1str_liorf(ruta_carpeta, ['tb14', 'tb32'])) == 4)
        self.assertTrue(type(lista_tuplas_1str_liorf(ruta_carpeta, ['tb14', 'tb32'])[0]) == tuple)

    def test_dicc_orf_rel_todos_txt(self):
        self.assertIn(20, dicc_orf_rel_todos_txt(['tb14', 'tb32', 'tb333', 'tb666'], ruta_carpeta).values())
        self.assertNotIn('tb777', dicc_orf_rel_todos_txt(['tb14', 'tb32', 'tb333', 'tb666'], ruta_carpeta).keys())

    def test_promedio_diccionario(self):
        self.assertTrue(promedio_diccionario(dicc_orf_rel_todos_txt(['tb14', 'tb32', 'tb333', 'tb666'],
                                                                    ruta_carpeta)) == 22)
        self.assertTrue(promedio_diccionario(dicc_orf_rel_todos_txt(['tb32', 'tb333', 'tb666'], ruta_carpeta)) == 20)

    def test_graf1_1(self):
        with self.assertRaises(TypeError):
            graf1_1([1, 2, 3])

    def test_graf2_1(self):
        with self.assertRaises(TypeError):
            graf2_1(2, 3)

    def test_graf2_2(self):
        with self.assertRaises(ZeroDivisionError):
            graf2_2({}, {})

    def test_graf3(self):
        with self.assertRaises(TypeError):
            graf3(12)


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestKoch1))
suite.addTest(unittest.makeSuite(TestKoch2))
suite.addTest(unittest.makeSuite(TestKoch3))
unittest.TextTestRunner(verbosity=2).run(suite)
