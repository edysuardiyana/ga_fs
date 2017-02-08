import random
import main
import fitness_function as ff
import math

BIN_DIG = 1

def gen_pop(n,nf, listname): #n = number of population, nf = number of features
    pop_array = []
    flag = True
    #for i in range(n):
    while len(pop_array) < n:
        if not pop_array:
            raw_pop = gen_parent(nf)
            temp_pop = ff.main_fitness_cal(listname, raw_pop)
            pop_array.append(temp_pop)
        else:
            #checking similar parents
            while flag:
                temp_raw_pop = gen_parent(nf)
                flag = compare_element(temp_raw_pop, pop_array)

            temp_new_pop = ff.main_fitness_cal(listname,temp_raw_pop)

            pop_array = main.insert_kid(pop_array, temp_new_pop)

    print "this is pop_array"
    print len(pop_array)
    return pop_array

def gen_parent(n): # n is the length of features
    temp_pop = [0] * n

    for i in range(n):
        ran_val = random.uniform(0,2)
        if ran_val < BIN_DIG:
            temp_pop[i] = 1
        else:
            temp_pop[i] = 0

    return temp_pop

def compare_element(x, pop_list):
    count_index = 0
    flag = False
    while not flag and count_index < len(pop_list):
        elem_pop = pop_list[count_index][0]
        count_index = count_index + 1
        counter = 0
        for j in range(len(elem_pop)):
            if x[j] == elem_pop[j]:
                counter = counter + 1
        if counter == len(x):
            flag = True

    return flag
