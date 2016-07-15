import cross_over
import fitness_function
import initiate_population
import mutation_funct
import selection_funct
import source_reader as sc


def main():
    #read names from list
    name_list = read_name()

    #combined features from three different places


    # generate initial population


def read_name():
    name_list = []
    path = sc.listname_path()

    with open(path) as obj_name:
        for line in obj_name:
            raw = line.split()
            name = raw[0]
            name_list.append(name)

    return name_list

def combined_feat():

if __name__ == '__main__':
    main()
