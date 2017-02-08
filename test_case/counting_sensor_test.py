import unittest
import fitness_function as ff
class counting_sens_test(unittest.TestCase):
    def testing_1_sens:
        arr = [0]*81
        arr[0] = 1
        tot_sens = ff.calc_num_of_sens(arr)

        self.assertEqual(1, tot_sens)
