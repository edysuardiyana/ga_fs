import combined_features as cf

def main():
    final_array = []
    #x = [[0,0],[0,7],[0,10]]
    #y = [[0,7],[0,10],[0,10]]
    #z = [[0,0],[0,0],[0,0],[0,7]]
    #x = [zero] * 2
    #y = [zero] * 1
    #z = [zero] * 2

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

    print x
    print y
    print z
    #final_array = cf.main_combined(x,y,z)


    print final_array

    print len(final_array)

if __name__ == '__main__':
    main()
