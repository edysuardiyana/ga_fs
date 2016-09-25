import cross_over as cov
import fitness_function as ff
import initiate_population as ip
import mutation_funct as mut
import source_reader as src
import combined_features as cf
import csv
import main_detection
import selection_funct as sf


#NUM_OF_FEATS = 81 #each sensors uses 27 features, 3 sensors (chest, waist, and thigh) are used
def main():
    num_sim = src.read_num_of_exp()
    tot_f = []
    for i in range(num_sim):
        print "experiment number: " +str(i)
        temp_f = main_ga()
        tot_f.append(temp_f)

    write_result(tot_f)

def main_ga():
    pop_fit = []
    # generate initial population
    print "generate individual for initial population"
    num_of_pop = src.read_num_pop()
    num_of_feats = src.read_gen_size()
    population = ip.gen_pop(num_of_pop, num_of_feats)

    #read names from list
    listname = read_name()

    #calculate fitness from each individual from pop
    for elem in population:
        if check_elem(elem):
            temp_enf = ff.main_fitness_cal(listname, elem)
        else:
            temp_enf = [elem,0,0,0,0,0,0]

        pop_fit.append(temp_enf)

    #sort (decreasing style) the individual based on fitnes function
    sorted_pop = sort_pop(pop_fit)

    tot_pop = src.read_tot_pop_size()
    tot_gen = src.read_tot_gen()

    counter_gen = 0
    print "==================================== start GA ======================"
    while len(sorted_pop) < tot_pop and counter_gen < tot_gen:
        print "generation: " + str(counter_gen)
        counter_gen += 1
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
        if check_elem(m_child1):
            child1_fit = ff.main_fitness_cal(listname,m_child1)
        else:
            child1_fit = [m_child1,0,0,0,0,0,0]

        if check_elem(m_child2):
            child2_fit = ff.main_fitness_cal(listname,m_child2)
        else:
            child2_fit = [m_child2,0,0,0,0,0,0]

        #inserting new childs into pop
        #first kid
        sorted_pop = insert_kid(sorted_pop,child1_fit)

        #second kid
        sorted_pop = insert_kid(sorted_pop, child2_fit)

        #delete the weakest individual (last elem because the sorted pop is in decreasing-style)
        del sorted_pop[len(sorted_pop)-1]

    print sorted_pop[0]
    return sorted_pop[0]

def write_result(array):
    path = src.read_temp_fscore()
    temp_line = []
    final_line =  []
    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')

    for i in range(len(array)):
        line = array[i]
        for j in range(len(line)):
            if j == 0:
                line2 = line[j]
                for k in range(len(line2)):
                    temp_line.append(line2[k])
            else:
                temp_line.append(line[j])

        final_line.append(temp_line)
        temp_line = []
    for elem in final_line:
        csv_writer.writerow(elem)
    out_file.close()


def check_elem(elem):
    counter = 0
    for line in elem:
        if line == 1:
            counter += 1

    if counter>0:
        flag = True
    else:
        flag = False
    return flag

def insert_kid(pop, new_kid):

    flag = True
    counter = 0
    init_pop = len(pop)
    #print "this is new kid: " + str(new_kid[len(new_kid)-1])
    while flag and counter < len(pop):

        if pop[counter][len(pop[counter])-1] <= new_kid[len(new_kid)-1]:
            pop.insert(counter,new_kid)
            flag = False
        else:
            counter += 1

    if init_pop == len(pop):
        pop.append(new_kid)

    return pop

def sort_pop(pop_fit):
    for i in range(len(pop_fit)-1,0,-1):
        j = i
        while j > 0 and pop_fit[j-1][len(pop_fit[j-1])-1] < pop_fit[j][len(pop_fit[j])-1]:
            temp = pop_fit[j]
            pop_fit[j] = pop_fit[j-1]
            pop_fit[j-1] = temp
            j -= 1
    return pop_fit

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
