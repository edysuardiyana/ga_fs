import unittest
import selection_funct as sf

class fitness_test(unittest.TestCase):
    def select_par_test(self):
        n = 10
        p1, p2 = sf.select_parent(n)
        self.assertNotEqual(p1, p2)
