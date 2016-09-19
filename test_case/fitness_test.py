import unittest
import fitness_function as ff

class fitness_test(unittest.TestCase):

    def three_sens_test(self):
        f_score = 98.0
        run_time = 0.5
        obst = 3
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertAlmostEqual(fit_val, 0.115)

    def two_sens_test(self):
        f_score = 98
        run_time = 0.5
        obst = 2
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertAlmostEqual(fit_val, 0.1983333)

    def run_time_over_test(self):
        f_score = 98
        run_time = 15
        obst = 3
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertEqual(fit_val, -3.51)
