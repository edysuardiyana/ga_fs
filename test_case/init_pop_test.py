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

    def compare_elem1_test(self):
        elem = [1,1,1,1]
        pop = [[1,1,1,1],[1,1,1,0],[1,0,1,1],[0,0,0,0]]

        flag = ip.compare_element(elem,pop)
        self.assertTrue(flag)

    def compare_elem2_test(self):
        elem = [1,1,1,1]
        pop = [[1,0,1,0],[1,1,1,0],[1,0,1,1],[0,0,0,0]]

        flag = ip.compare_element(elem,pop)
        self.assertFalse(flag)
