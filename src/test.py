import main as mn

def main():
    pop = [[[1,0,0,0,1],6],[[1,0,0,0,1],5],[[1,0,0,0,1],4],[[1,0,0,0,1],3],[[1,0,0,0,1],2]]
    kid = [[1,0,0,0,1],7]

    new_pop = mn.insert_kid(pop, kid)
    print new_pop

def replace_x(x):
    x.append(0)

    return x


if __name__ == '__main__':
    main()
