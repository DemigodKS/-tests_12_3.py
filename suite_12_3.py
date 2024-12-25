import unittest

import tests_12_1
import tests_12_2
import tests_12_3

#создаем тест
calcST = unittest.TestSuite()
#обавляем наши тесты
#calcST.addTest(unittest.makeSuite(test_calc.CalcTest))

#другой способ добавить тесты
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

#настраиваем запуск тестов
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)
