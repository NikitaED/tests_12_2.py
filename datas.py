import unittest
from runner_and_tournament import Tournament
from runner_and_tournament import Runner
class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.usein = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)


    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"Место {key}: {value}")


    def test_race_usein_nik(self):
        tournament = Tournament(90, self.usein, self.nik)
        results = tournament.start()
        last_place_runner = results[max(results.keys())]
        self.all_results[max(results.keys())] = last_place_runner
        self.assertTrue(last_place_runner.name == "Ник")


    def test_race_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        last_place_runner = results[max(results.keys())]
        self.all_results[max(results.keys())] = last_place_runner
        self.assertTrue(last_place_runner.name == "Ник")


    def test_race_usein_andrey_nik(self):
        tournament = Tournament(90, self.usein, self.andrey, self.nik)
        results = tournament.start()
        last_place_runner = results[max(results.keys())]
        self.all_results[max(results.keys())] = last_place_runner
        self.assertTrue(last_place_runner.name == "Ник")
