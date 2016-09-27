import unittest
import features_extract as fe

class feature_test(unittest.TestCase):
    def feature_select1_test(self):
        data = [1,2,3,4,5,6,7,8,9,10]
        x = [1,2,3,4,5,6,7,8,9,10]
        y = [1,2,3,4,5,6,7,8,9,10]
        z = [1,2,3,4,5,6,7,8,9,10]
        elem = [1,0,0,0,0,0,0,0,0,0]

        res = fe.features_calc(data,x,y,z,2,elem)
        self.assertEqual(len(res), 1)

    def feature2_select2_test(self):
        data = [1,2,3,4,5,6,7,8,9,10]
        x = [1,2,3,4,5,6,7,8,9,10]
        y = [1,2,3,4,5,6,7,8,9,10]
        z = [1,2,3,4,5,6,7,8,9,10]
        elem = [1,0,1,0,0,0,0,0,0,0]

        res = fe.features_calc(data,x,y,z,2,elem)
        self.assertEqual(len(res), 2)

    def feature3_select3_test(self):
        data = [1,2,3,4,5,6,7,8,9,10]
        x = [1,2,3,4,5,6,7,8,9,10]
        y = [1,2,3,4,5,6,7,8,9,10]
        z = [1,2,3,4,5,6,7,8,9,10]
        elem = [0,0,0,0,0,0,0,0,0,0]

        res = fe.features_calc(data,x,y,z,2,elem)
        self.assertEqual(len(res), 0)

    def feature4_select4_test(self):
        data = [1,2,3,4,5,6,7,8,9,10]
        x = [1,2,3,4,5,6,7,8,9,10]
        y = [1,2,3,4,5,6,7,8,9,10]
        z = [1,2,3,4,5,6,7,8,9,10]
        elem = [1,1,1,1,1,1,1,1,1,1]

        res = fe.features_calc(data,x,y,z,2,elem)
        self.assertEqual(len(res), 9)

    def feature_main5_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[4] =  1

        res,_ = fe.main_features(data,x,y,z,2,elem, "chest")
        self.assertEqual(len(res), 1)

    def feature_main6_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[4] =  1
        elem[5] = 1
        elem[10] = 1

        res,_ = fe.main_features(data,x,y,z,2,elem, "chest")
        self.assertEqual(len(res), 3)

    def feature_main7_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        #elem[4] =  1

        res,_ = fe.main_features(data,x,y,z,2,elem, "chest")
        self.assertEqual(len(res), 0)

    def feature_main8_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[80] =  1

        res,_ = fe.main_features(data,x,y,z,2,elem, "chest")
        self.assertEqual(len(res), 0)

    def feature_main9_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[4] =  1

        res,_ = fe.main_features(data,x,y,z,2,elem, "waist")
        self.assertEqual(len(res), 0)

    def feature_main10_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[30] = 1

        res,_ = fe.main_features(data,x,y,z,2,elem, "waist")
        self.assertEqual(len(res), 1)

    def feature_main11_test(self):
        data = [1]*81
        x = [1]*81
        y =[1]*81
        z = [1]*81
        elem = [0] * 81
        elem[30] = 1
        elem[50] = 1

        res,_ = fe.main_features(data,x,y,z,2,elem, "waist")
        self.assertEqual(len(res), 2)

    def feature_main12_test(self):
        data =[1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[4] =  1

        res,_ = fe.main_features(data,x,y,z,2,elem, "thigh")
        self.assertEqual(len(res), 0)

    def feature_main13_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z = [1]*81
        elem = [0] * 81
        elem[4] =  1
        elem[54] = 1
        res,_ = fe.main_features(data,x,y,z,2,elem, "thigh")
        self.assertEqual(len(res), 1)

    def feature_main14_test(self):
        data = [1]*81
        x = [1]*81
        y = [1]*81
        z =[1]*81
        elem = [0] * 81
        elem[55] =  1
        elem[77] = 1

        res,_ = fe.main_features(data,x,y,z,2,elem, "thigh")
        self.assertEqual(len(res), 2)
