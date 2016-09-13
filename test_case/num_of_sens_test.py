import unittest
import main_detection as md

class num_of_sens_test(unittest.TestCase):
    def num_1_test(self):
        array = [0] * 81
        array[3] = 1
        array[80] = 1

        tot_num = md.num_of_sens(array)
        self.assertEqual(tot_num, 2)

    def num_2_test(self):
        array = [0] * 81
        array[3] = 1
        array[4] = 1
        array[80] = 1

        tot_num = md.num_of_sens(array)
        self.assertEqual(tot_num, 2)

    def num_3_test(self):
        array = [0] * 81
        array[3] = 1
        array[40] = 1
        array[80] = 1

        tot_num = md.num_of_sens(array)
        self.assertEqual(tot_num, 3)

    def num_4_test(self):
        array = [0] * 81
        array[3] = 1
        array[4] = 1
        array[6] = 1

        tot_num = md.num_of_sens(array)
        self.assertEqual(tot_num, 1)

    def num_5_test(self):
        array = [0] * 81
        array[27] = 1
        array[28] = 1
        array[30] = 1

        tot_num = md.num_of_sens(array)
        self.assertEqual(tot_num, 1)

    def num_6_test(self):
        array = [0] * 81
        array[54] = 1
        array[55] = 1
        array[56] = 1

        tot_num = md.num_of_sens(array)
        self.assertEqual(tot_num, 1)
