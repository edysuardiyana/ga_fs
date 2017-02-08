import unittest
import fitness_function as ff

class fitness_test(unittest.TestCase):

    def three_sens_test(self):
        f_score = 98.0
        run_time = [0.1,0.1,0.3]#0.5
        obst = 3
        fit_val = ff.calc_fitness(f_score, run_time, obst)

        self.assertAlmostEqual(fit_val, 0.23)

    def two_sens_test(self):
        f_score = 98.0
        run_time = [0.1,0.1,0.3]#0.5
        obst = 2
        fit_val = ff.calc_fitness(f_score, run_time, obst)

        self.assertAlmostEqual(fit_val, 0.39666666666)

    def run_time_over_test(self):
        f_score = 98.0
        run_time = [5,5,5]#15
        obst = 3
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertEqual(fit_val, -7.02)
