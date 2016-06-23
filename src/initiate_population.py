import random

BIN_DIG = 1

def gen_pop(n,nf): #n = number of features, nf = number of features
    pop_array = []
    for i in range(n):
        if not pop_array:
            pop_array.append(gen_parent(nf))
        else:
            temp_new_pop = gen_parent(nf)
            pop_array.append(temp_new_pop)
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
        elem_pop = pop_list[count_index]
        count_index = count_index + 1
        counter = 0
        for j in range(len(elem_pop)):
            if x[j] == elem_pop[j]:
                counter = counter + 1
            if counter == len(x):
                flag = True

    return flag

def main():
    print gen_parent(10)

if __name__ == '__main__':
    main()
