import unittest


class Runner:

    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):

        """ Тест метода walk. Создаем объект класса Runner. Вызываем метод walk 10 раз.
        Сравниваем аттрибут distance этого со значением 50 """

        runner_1 = Runner('Ivan')

        for i in range(10):
            runner_1.walk()

        self.assertEqual(runner_1.distance, 50)

    def test_run(self):

        """ Тест метода run. Вызываем метод run 10 раз. Создаем объект класса Runner.
        Сравниваем аттрибут distance этого со значением 100 """

        runner_2 = Runner('Elena')

        for i in range(10):
            runner_2.run()

        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):

        """ Тест методов run и walk. Создаем два объекта класса Runner. Вызываем метод run для первого объекта 10 раз.
        Вызываем метод walk для второго объекта 10 раз. Сравниваем аттрибуты distance этих методов.
        Они не должны совпадать """

        runner_3 = Runner('Petr')
        runner_4 = Runner('Anna')

        for i in range(10):
            runner_3.walk()
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == '__main__':
    unittest.main()