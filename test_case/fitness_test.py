import unittest
import fitness_function as ff

class fitness_test(unittest.TestCase):
    def select_feature_1_test(self):
        elem = [1,0,1]
        array =[1,2,3]

        res = ff.select_feature(array,elem)

        self.assertEqual(len(res),2)

    def select_feature_2_test(self):
        elem = [0,0,1]
        array =[1,2,3]

        res = ff.select_feature(array,elem)

        self.assertEqual(len(res),1)

    def select_feature_3_test(self):
        elem = [0,0,0]
        array =[1,2,3]

        res = ff.select_feature(array,elem)

        self.assertEqual(len(res),0)

    def three_sens_test(self):
        f_score = 98
        run_time = 0.5
        obst = 3
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertEqual(fit_val, 96.25)

    def two_sens_test(self):
        f_score = 98
        run_time = 0.5
        obst = 2
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertEqual(fit_val, 96.75)

    def run_time_over_test(self):
        f_score = 98
        run_time = 15
        obst = 3
        fit_val = ff.calc_fitness(f_score, run_time, obst)
        self.assertEqual(fit_val, 89.0)
