import combined_features as cf

def main():
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

    print x
    print y
    print z

    final_array = cf.main_combined(x,y,z)


    print len(final_array)
    print final_array

if __name__ == '__main__':
    main()
