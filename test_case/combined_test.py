import unittest
import combined_features as cf

class combined_test(unittest.TestCase):
    def combined_1_test(self):
        final_array = []
        zero = [0] * 5

        x = [zero] * 1

        y = [zero] * 3

        z = [zero] * 4

        final_array = cf.main_combined(x,y,z)

        self.assertEqual(len(final_array),12)


    def combined_2_test(self):
        final_array = []
        zero = [0] * 5

        x = [zero] * 2

        y = [zero] * 3

        z = [zero] * 4

        final_array = cf.main_combined(x,y,z)

        self.assertEqual(len(final_array),24)

    def combined_3_test(self):
        final_array = []
        zero = [0] * 2
        x = []
        y = []
        z = []

        x_zero = [0] * 2
        for i in range(1):
            x_zero[len(x_zero)-1] = 1
            x.append(x_zero)

        y_zero = [0] * 2
        for j in range(2):
            if j == 0:
                y_zero[len(y_zero)-1] = 1
                y.append(y_zero)
            else:
                y.append(zero)


        z_zero = [0] * 2
        for k in range(4):
            if k == 0 or k == 1 :
                z_zero[len(z_zero)-1] = 1
                z.append(z_zero)
            else:
                z.append(zero)


        final_array = cf.main_combined(x,y,z)

        self.assertEqual(len(final_array),4)


    def combined_4_test(self):
        final_array = []
        zero = [1] * 2
        x = []
        y = []
        z = []

        for i in range(1):
            x.append(zero)

        for j in range(3):
            y.append(zero)

        for k in range(2):
            z.append(zero)

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array),6)

    def combined_6_test(self):
        final_array = []
        zero = [0] * 2
        one = [1] * 2
        x = []
        y = []
        z = []

        for i in range(2):
            if i == 0:
                x.append(one)
            else:
                x.append(zero)

        for j in range(4):
            if j == 0 or j == 1:
                y.append(one)
            else:
                y.append(zero)

        for k in range(6):
            if k == 0 or k == 1 or k == 2:
                z.append(one)
            else:
                z.append(zero)

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array),12)

    def combined_7_test(self):
        final_array = []
        zero = [0] * 2
        one = [1] * 2
        x = []
        y = []
        z = []

        for i in range(3):
            if i == 0 or i == 2:
                x.append(one)
            else:
                x.append(zero)

        for j in range(6):
            if j == 0 or j == 1 or j==4 or j==5:
                y.append(one)
            else:
                y.append(zero)

        for k in range(9):
            if k == 0 or k == 1 or k == 2 or k == 6 or k == 7 or k == 8 :
                z.append(one)
            else:
                z.append(zero)

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 18)

    def combined_8_test(self):
        final_array = []
        zero = [0] * 2
        one = [1] * 2
        x = []
        y = []
        z = []

        for i in range(1):
            if i == 0 :
                x.append(one)
            else:
                x.append(zero)

        for j in range(2):
            if j == 0 :
                y.append(zero)
            else:
                y.append(one)

        for k in range(3):
            z.append(one)

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array),4)

    def combined_9_test(self):
        final_array = []
        zero = [0] * 2
        one = [1] * 2
        x = []
        y = []
        z = []

        for i in range(1):
            if i == 0 :
                x.append(one)
            else:
                x.append(zero)

        for j in range(2):
            y.append(one)

        for k in range(4):
            if k == 0:
                z.append(zero)
            else:
                z.append(one)

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 7)

    def combined_10_test(self):
        final_array = []
        zero = [0] * 5
        #x = [[0,12],[0,3],[0,0],[0,0],[0,13]]
        #y = [[0,12],[0,0],[0,0],[0,13]]
        #z = [[0,12],[0,0],[0,0],[0,0],[0,0],[0,13]]
        x = [zero] * 4
        y = [zero] * 1
        z = [zero] * 4

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 16)

    def combined_11_test(self):
        final_array = []
        zero = [0] * 5
        x = [[0,12],[0,3],[0,0],[0,0],[0,13]]
        y = [[0,12],[0,0],[0,0],[0,13]]
        z = [[0,12],[0,0],[0,0],[0,0],[0,0],[0,13]]


        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 13)

    def combined_12_test(self):
        final_array = []
        x = [[0,6],[0,0]]
        y = [[0,6],[0,0]]
        z = [[0,0],[0,0],[0,6]]

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 4)

    def combined_13_test(self):
        final_array = []
        x = [[0,0],[0,0],[0,6]]
        y = [[0,6],[0,0]]
        z = [[0,6],[0,0]]

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 4)

    def combined_14_test(self):
        final_array = []
        x = [[0,6],[0,0]]
        y = [[0,0],[0,0],[0,6]]
        z = [[0,6],[0,0]]

        final_array = cf.main_combined(x,y,z)
        self.assertEqual(len(final_array), 4)
