import unittest
import combined_features as cf

class combined_test(unittest.TestCase):
    def median_1_test(self):
        x = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

        med_val = cf.calc_median(x)

        for i in range(len(med_val)):
            self.assertEqual(med_val[i],1.0)

    def median_2_test(self):
        x = [[1,1,1],[2,1,1],[3,1,1],[4,1,1]]
        med_val = cf.calc_median(x)

        for i in range(len(med_val)):
            if i == 0:
                self.assertEqual(med_val[i],2.5)
            else:
                self.assertEqual(med_val[i],1.0)

    def median_3_test(self):
        x = [[1,1,1],[1,2,1],[1,3,1],[1,4,1]]
        med_val = cf.calc_median(x)

        for i in range(len(med_val)):
            if i == 1:
                self.assertEqual(med_val[i],2.5)
            else:
                self.assertEqual(med_val[i],1.0)

    def median_4_test(self):
        x = [[1,1,1,0],[1,1,2,0],[1,1,3,0],[1,1,4,0]]
        med_val = cf.calc_median(x)
        for i in range(len(med_val)):
            if i == 2:
                self.assertEqual(med_val[i],2.5)
            elif i == 3:
                self.assertEqual(med_val[i],0)
            else:
                self.assertEqual(med_val[i],1.0)

    def add_miss_1_test(self):
        zero = [0] * 3
        x = [zero]*3
        y = [zero]*6
        z = [zero]*10

        x_new, y_new, z_new = cf.add_miss_val(x,y,z)
        self.assertEqual(len(x_new), 10)
        self.assertEqual(len(y_new), 10)
        self.assertEqual(len(z_new), 10)

    def add_miss_2_test(self):
        zero = [0] * 3
        x = [zero]*5
        y = [zero]*6
        z = [zero]*20

        x_new, y_new, z_new = cf.add_miss_val(x,y,z)
        self.assertEqual(len(x_new), 20)
        self.assertEqual(len(y_new), 20)
        self.assertEqual(len(z_new), 20)

    def combined_val_1_test(self):
        x = []
        y = []
        z = []
        for i in range(5):
            temp_x = [0] * 5
            if i == 0 or i == 1:
                temp_x[len(temp_x)-1] = 1

            x.append(temp_x)

        for j in range(7):
            temp_y = [0] * 5
            if j == 0 or j == 1 or j == 2:
                temp_y[len(temp_y)-1] = 1

            y.append(temp_y)

        for k in range(10):
            temp_z = [0] * 5
            if k == 0 or k == 1 or k == 2 or k == 3:
                temp_z[len(temp_z)-1] = 1

            z.append(temp_z)
        #print x
        #print y
        #print z
        new_val = cf.main_combined(x,y,z)

        self.assertEqual(len(new_val), 10)

    def combined_val_2_test(self):
        x = []
        y = []
        z = []
        for i in range(5):
            temp_x = [0] * 5
            if i == 0 or i == 1:
                temp_x[len(temp_x)-1] = 1

            x.append(temp_x)

        for j in range(7):
            temp_y = [0] * 5
            if j == 0 or j == 1 or j == 2:
                temp_y[len(temp_y)-1] = 1

            y.append(temp_y)

        for k in range(10):
            temp_z = [0] * 5
            if k == 0 or k == 1 or k == 2 or k == 3:
                temp_z[len(temp_z)-1] = 1
            elif k == 5:
                temp_z[len(temp_z)-1] = 2

            z.append(temp_z)

        new_val = cf.main_combined(x,y,z)

        self.assertEqual(len(new_val), 9)

    def combined_val_3_test(self):
        x = []
        y = []
        z = []
        for i in range(5):
            temp_x = [0] * 5
            if i == 0 or i == 1:
                temp_x[len(temp_x)-1] = 1
            elif i == 3:
                temp_x[len(temp_x)-1] = 2

            x.append(temp_x)

        for j in range(7):
            temp_y = [0] * 5
            if j == 0 or j == 1 or j == 2:
                temp_y[len(temp_y)-1] = 1
            y.append(temp_y)

        for k in range(10):
            temp_z = [0] * 5
            if k == 0 or k == 1 or k == 2 or k == 3:
                temp_z[len(temp_z)-1] = 1
            z.append(temp_z)

        new_val = cf.main_combined(x,y,z)

        self.assertEqual(len(new_val), 10)

    def combined_val_4_test(self):
        x = [[1,2,3,0], [1,2,3,0], [1,2,3,0],[4,5,6,1], [4,5,6,1], [4,5,6,1]]
        y = [[11,10,9,0], [11,10,9,0], [11,10,9,0], [11,10,9,0], [11,10,9,0], [20,40,50,1], [20,40,50,1],
        [20,40,50,1], [20,40,50,1]]
        z = [[20,21,22,23,0],[20,21,22,23,0], [20,21,22,23,0], [20,21,22,23,0],
        [20,21,22,23,0], [20,21,22,23,0], [30,31,32,33,1], [30,31,32,33,1], [30,31,32,33,1],
        [30,31,32,33,1], [30,31,32,33,1], [30,31,32,33,1]]

        new_val = cf.main_combined(x,y,z)

        line = new_val[0]
        # total  = [1,2,3,11,10,9,20,21,22,23,0]
        self.assertEqual(line[3],11)
        self.assertEqual(line[2],3)
        self.assertEqual(line[len(line)-1],0)
