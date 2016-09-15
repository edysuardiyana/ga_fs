import unittest
import main

class main_test(unittest.TestCase):
    def check_elem1_test(self):
        x = [1,0,0,0,0,1]

        flag = main.check_elem(x)

        self.assertTrue(flag)

    def check_elem2_test(self):
        x = [0,0,0,0,0]

        flag = main.check_elem(x)

        self.assertFalse(flag)

    def check_elem3_test(self):
        x = []
        flag = main.check_elem(x)

        self.assertFalse(flag)

    def insert_kid1_test(self):
        pop = [[[1,0,0,0,1],6],[[1,0,0,0,1],5],[[1,0,0,0,1],4],[[1,0,0,0,1],3],[[1,0,0,0,1],2]]
        kid = [[1,0,0,0,1],1]

        new_pop = main.insert_kid(pop, kid)
        self.assertEqual(new_pop[len(new_pop)-1][1], 1)

    def insert_kid2_test(self):
        pop = [[[1,0,0,0,1],6],[[1,0,0,0,1],5],[[1,0,0,0,1],4],[[1,0,0,0,1],3],[[1,0,0,0,1],2]]
        kid = [[1,0,0,0,1],3]

        new_pop = main.insert_kid(pop, kid)
        self.assertEqual(new_pop[3][1],3)

    def insert_kid3_test(self):
        pop = [[[1,0,0,0,1],6],[[1,0,0,0,1],5],[[1,0,0,0,1],4],[[1,0,0,0,1],3],[[1,0,0,0,1],2]]
        kid = [[1,0,0,0,1],3.5]

        new_pop = main.insert_kid(pop, kid)
        self.assertEqual(new_pop[3][1],3.5)

    def insert_kid4_test(self):
        pop = [[[1,0,0,0,1],6],[[1,0,0,0,1],5],[[1,0,0,0,1],4],[[1,0,0,0,1],3],[[1,0,0,0,1],2]]
        kid = [[1,0,0,0,1],7]

        new_pop = main.insert_kid(pop, kid)
        self.assertEqual(new_pop[3][1],4)

    def sort1_test(self):
        pop = [[[1,0,0,0,1],6],[[1,0,0,0,1],5],[[1,0,0,0,1],4],[[1,0,0,0,1],3],[[1,0,0,0,1],2]]
        new_pop = main.sort_pop(pop)

        self.assertEqual(new_pop[0][1],6)

    def sort2_test(self):
        pop = [[[1,0,0,0,1],1],[[1,0,0,0,1],2],[[1,0,0,0,1],3],[[1,0,0,0,1],4],[[1,0,0,0,1],5]]
        new_pop = main.sort_pop(pop)

        self.assertEqual(new_pop[0][1],5)

    def sort3_test(self):
        pop = [[[1,0,0,0,1],3],[[1,0,0,0,1],1],[[1,0,0,0,1],2],[[1,0,0,0,1],5],[[1,0,0,0,1],4]]
        new_pop = main.sort_pop(pop)

        self.assertEqual(new_pop[0][1],5)
