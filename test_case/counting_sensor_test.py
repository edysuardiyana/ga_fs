import unittest
import main_detection as md
class counting_sens_test(unittest.TestCase):
    def testing_1_sens_test(self):
        arr = [0]*81
        arr[0] = 1
        tot_sens = md.num_of_sens(arr)

        self.assertEqual(1, tot_sens)
