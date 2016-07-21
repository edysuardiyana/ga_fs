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

    print x
    print y
    print z
    final_array = cf.main_combined(x,y,z)


    print final_array

    print len(final_array)

if __name__ == '__main__':
    main()
