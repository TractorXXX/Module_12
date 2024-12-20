import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner('Усэйн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print()
            print(f'Забег {i}:')
            for key, value in j.items():
                print(f'{key}: {value.name}')


    def test_zabeg_1(self):
        tour_90 = Tournament(90, self.run_1, self.run_3)
        all_results = tour_90.start()
        self.all_results[1] = all_results
        self.assertTrue(all_results[2] == 'Ник')

    def test_zabeg_2(self):
        tour_90 = Tournament(90, self.run_2, self.run_3)
        all_results = tour_90.start()
        self.all_results[2] = all_results
        self.assertTrue(all_results[2] == 'Ник')

    def test_zabeg_3(self):
        tour_90 = Tournament(90, self.run_1, self.run_2, self.run_3)
        all_results = tour_90.start()
        self.all_results[3] = all_results
        self.assertTrue(all_results[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()