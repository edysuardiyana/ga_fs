import combined_features as cf

def main():
    final_array = []
    zero = [0] * 5
    x = [[0,0],[0,7],[0,10]]
    y = [[0,7],[0,10],[0,10]]
    z = [[0,0],[0,0],[0,0],[0,7]]
    #x = [zero] * 2
    #y = [zero] * 1
    #z = [zero] * 2

    print x
    print y
    print z
    final_array = cf.main_combined(x,y,z)


    print final_array

    print len(final_array)

if __name__ == '__main__':
    main()
