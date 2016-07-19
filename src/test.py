import combined_features as cf

def main():
    final_array = []
    zero = [0] * 5

    x = [zero] * 1

    y = [zero] * 3

    z = [zero] * 4

    #print x
    #print y
    #print z
    final_array = cf.main_combined(x,y,z)



    print len(final_array)

if __name__ == '__main__':
    main()
