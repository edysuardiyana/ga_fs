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

        self.assertEqual(len(final_array),2)

    def combined_4_test(self):
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
            if j == 1:
                y_zero[len(y_zero)-1] = 1
                y.append(y_zero)
            else:
                y.append(zero)


        z_zero = [0] * 2
        for k in range(4):
            if k == 2 or k == 3 :
                z_zero[len(z_zero)-1] = 1
                z.append(z_zero)
            else:
                z.append(zero)


        final_array = cf.main_combined(x,y,z)

        self.assertEqual(len(final_array),2)
