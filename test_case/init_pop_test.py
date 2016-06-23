import unittest
import initiate_population as ip

class init_pop_test(unittest.TestCase):
    def zero_pop_test(self):
        pop_array = ip.gen_pop(0,0)
        self.assertEqual(0, len(pop_array))

    def ten_three_pop_test(self):
        pop_array = ip.gen_pop(10,3)
        elem = pop_array[0]

        self.assertEqual(10, len(pop_array))
        self.assertEqual(3, len(elem))

    def three_ten_pop_test(self):
        pop_array = ip.gen_pop(3,10)
        elem = pop_array[0]

        self.assertEqual(3, len(pop_array))
        self.assertEqual(10, len(elem))
