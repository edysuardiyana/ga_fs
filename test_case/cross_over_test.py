import unittest
import cross_over as co

class cross_over_test(unittest.TestCase):
    def select_par_1_test(self):
        p_1 = [1,1,1,1,1,1,1,1,1,1]
        p_2 = [0,0,0,0,0,0,0,0,0,0]
        new_p1, new_p2 = co.cross_over_funct(p_1,p_2)
        self.assertFalse(p_1 == new_p1)
        self.assertFalse(p_2 == new_p2)

    def select_par_2_test(self):
        p_1 = [1,1,1,1,1,0,0,0,0,0]
        p_2 = [0,0,0,0,0,0,1,1,0,1]
        new_p1, new_p2 = co.cross_over_funct(p_1,p_2)
        self.assertFalse(p_1 == new_p1)
        self.assertFalse(p_2 == new_p2)
