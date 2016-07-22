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

    x = [[0,0],[0,0],[0,6]]
    y = [[0,6],[0,0]]
    z = [[0,6],[0,0]]


    print x
    print y
    print z
    final_array = cf.main_combined(y,x,z)


    print final_array

    print len(final_array)

if __name__ == '__main__':
    main()
