import combined_features as cf

def main():
    final_array = []
    #x = [[0,0],[0,7],[0,10]]
    #y = [[0,7],[0,10],[0,10]]
    #z = [[0,0],[0,0],[0,0],[0,7]]
    #zero = [0] * 5

    #x = [zero] * 5
    #y = [zero] * 5
    #z = [zero] * 4

    #x = [[0,6],[0,0]]
    #y = [[0,6],[0,0]]
    #z = [[0,0],[0,0],[0,6]]

    #x = [[0,12],[0,13]]
    #y = [[0,0],[0,12],[0,0], [0,0], [0,13]]
    #z = [[0,0],[0,0], [0,12], [0,0], [0,0], [0,13]]

    #x = [[0,6],[0,0]]
    #y = [[0,0],[0,0],[0,6]]
    #z = [[0,6],[0,0]]

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

    print x
    print y
    print z
    new_val = cf.main_combined(x,y,z)
    print len(new_val)

if __name__ == '__main__':
    main()
