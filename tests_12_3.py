from module12_1 import Runner
import unittest
from lesson3 import Tournament
from lesson3 import Runner

class RunnerTest(unittest.TestCase):
    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = Runner('Nik')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Runner('Julia')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Nik')
        runner2 = Runner('Julia')
        for _ in range(10):
            runner1.walk()
            runner2.run()
            if runner1.distance == runner2.distance:
                message = 'equal'
            else:
                message = 'not equal'
        self.assertNotEqual(runner1.distance, runner2.distance, message)

if __name__ == '__main__':
    unittest.main()



class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        tour = Tournament(90, self.runner1, self.runner3)
        result = tour.start()
        self.all_results['method1'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        result = tour.start()
        self.all_results['method2'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        tour = Tournament(90, self.runner2, self.runner3, self.runner1)
        result = tour.start()
        self.all_results['method3'] = {k: str(v) for k, v in result.items()}
        self.assertTrue(result[max(result)] == 'Ник')


if __name__ == "__main__":
    unittest.main()
