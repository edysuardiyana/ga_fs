import cross_over as cov
import fitness_function as ff
import initiate_population as ip
import mutation_funct as mut
import source_reader as src
import combined_features as cf
import csv
import main_detection
import selection_funct as sf


NUM_OF_FEATS = 81 #each sensors uses 27 features, 3 sensors (chest, waist, and thigh) use

def main():
    pop_fit = []
    # generate initial population
    num_of_pop = src.read_num_pop()
    population = ip.gen_pop(num_of_pop, NUM_OF_FEATS)

    #read names from list
    name_list = read_name()

    #calculate fitness from each individual from pop
    for elem in population:
        temp_enf = ff.main_fitness_cal(listname, elem)
        pop_fit.append(temp_enf)

    #sort (decreasing style) the individual based on fitnes function
    sorted_pop = sort_pop(pop_fit)

    #select 2 parents:
    p1_index, p2_index = sf.select_parent(len(sorted_pop))
    p1 = sorted_pop[p1_index][0]
    p2 = sorted_pop[p2_index][0]

    #crossover process
    child1, child2 = cov.cross_over_funct(p1,p2)

    #mutate childs
    _,m_child1 = mut.mutate(child1)
    _,m_child2 = mut.mutate(child2)

    #calculate fitness function of the new childs
    child1_fit = ff.main_fitness_cal(listname,m_child1)
    child2_fit = ff.main_fitness_cal(listname,m_child2)

    #inserting new childs into pop
    #first kid
    pop = insert_kid(pop,child1_fit)

    #second kid
    pop = insert_kid(pop, child2_fit)

    #delete the weakest individual (last elem because the sorted pop is in decreasing-style)
    del pop[len(pop)-1]



def insert_kid(pop, new_kid):

    flag = True
    counter = 0
    while flag:
        if pop[counter][1] <= new_kid[1]:
            pop.insert(i,new_kid)
            flag = False
        else:
            counter += 1

    return pop

def sort_pop(pop_fit):
    for i in range(len(pop_fit)-1,0,-1):
        j = i
        while j > 0 and pop_fit[j-1][1] < pop_fit[j][1]:
            temp = pop_fit[j]
            pop_fit[j] = pop_fit[j-1]
            pop_fit[j-1] = temp
            j -= 1
print pop_fit

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
