import unittest
import detection_rate_src.features_extract as fe

class feature_test(unittest.TestCase):
    def feature_select_test(self):
        data = [1,2,3,4,5,6,7,8,9]
        x = [1,2,3,4,5,6,7,8,9]
        y = [1,2,3,4,5,6,7,8,9]
        z = [1,2,3,4,5,6,7,8,9]
        elem = [1,0,0,0,0,0,0,0,0]

        res = fe.features_calc(data,x,y,z,1,elem)
        self.assertEqual(len(res), 1)

    def feature2_select_test(self):
        data = [1,2,3,4,5,6,7,8,9]
        x = [1,2,3,4,5,6,7,8,9]
        y = [1,2,3,4,5,6,7,8,9]
        z = [1,2,3,4,5,6,7,8,9]
        elem = [1,0,1,0,0,0,0,0,0]

        res = fe.features_calc(data,x,y,z,1,elem)
        self.assertEqual(len(res), 2)

    def feature3_select_test(self):
        data = [1,2,3,4,5,6,7,8,9]
        x = [1,2,3,4,5,6,7,8,9]
        y = [1,2,3,4,5,6,7,8,9]
        z = [1,2,3,4,5,6,7,8,9]
        elem = [0,0,0,0,0,0,0,0,0]

        res = fe.features_calc(data,x,y,z,1,elem)
        self.assertEqual(len(res), 0)

    def feature4_select_test(self):
        data = [1,2,3,4,5,6,7,8,9]
        x = [1,2,3,4,5,6,7,8,9]
        y = [1,2,3,4,5,6,7,8,9]
        z = [1,2,3,4,5,6,7,8,9]
        elem = [1,1,1,1,1,1,1,1,1]

        res = fe.features_calc(data,x,y,z,1,elem)
        self.assertEqual(len(res), 9)

    def feature_main_test(self):
        data = [1,2,3,4,5]
        x = [1,2,3,4,5]
        y = [1,2,3,4,5]
        z = [1,2,3,4,5]
        elem = [0] * 81
        elem[4] =  1

        res,_ = fe.main_features(data,x,y,z,1,elem, "chest")
        self.assertEqual(len(res), 1)
