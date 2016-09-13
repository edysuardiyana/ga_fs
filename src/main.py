import cross_over
import fitness_function as ff
import initiate_population as ip
import mutation_funct
import selection_funct
import source_reader as src
import combined_features as cf
import csv
import main_detection

NUM_OF_FEATS = 81 #each sensors uses 27 features, 3 sensors (chest, waist, and thigh) use

def main():
    pop_fit = []
    # generate initial population
    num_of_pop = src.read_num_pop()
    population = ip.gen_pop(num_of_pop, NUM_OF_FEATS)

    #read names from list
    name_list = read_name()
    for elem in population:
        temp_enf = ff.main_fitness_cal(listname, elem)
        pop_fit.append(temp_enf)

    




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
