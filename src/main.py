import cross_over
import fitness_function
import initiate_population
import mutation_funct
import selection_funct
import source_reader as src
import combined_features as cf
import csv

def main():
    combined_array = []
    #read names from list
    name_list = read_name()
    #combined features from three different places
    cf.combined_features(name_list)

    # generate initial population


def read_name():
    name_list = []
    path = src.listname_path()

    with open(path) as obj_name:
        for line in obj_name:
            raw = line.split()
            name = raw[0]
            name_list.append(name)

    return name_list


if __name__ == '__main__':
    main()
