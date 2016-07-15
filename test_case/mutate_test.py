import unittest
import mutation_funct as mf

class mutate_test(unittest.TestCase):
    def mutate_1_test(self):
        p_1 = [1,1,1,1,1,1,1,1,1,1]
        flag, new_instance = mf.mutate(p_1)
        if flag :
            self.assertNotEqual(p_1,new_instance)
        else:
            self.assertEqual(p_1,new_instance)

    def mutate_2_test(self):
        p_2 = [0,0,0,0,0,0,1,1,0,1]
        flag, new_instance = mf.mutate(p_2)

        if flag:
            self.assertNotEqual(p_2,new_instance)
        else:
            self.assertEqual(p_2,new_instance)
