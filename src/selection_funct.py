import math
import random

def select_parent(n): # Number parent population array
    Q_VAL = 0.25
    total_value = 0
    array_val = []
    parent_1 = 0
    parent_2 = 0
    temp = 0
    #calculate accumulative probabilities
    for i in range(n):
        i_new = i + 1

        temp_val = 1 - 0.25
        non_round_val = temp + 0.25 * math.pow(temp_val, (i_new-1))
        val = round(non_round_val,2)

        array_val.append(val)
        temp = val

    while parent_1 == parent_2:
        parent_1 = pick_parrent(array_val)
        parent_2 = pick_parrent (array_val)

    return parent_1 , parent_2 #choosen_parent_1, choosen_parent_2


def pick_parrent(array_val):

    counter = 0
    flag = False
    parent_index = random.uniform(0, array_val[len(array_val)-1])

    while not flag:
        if counter == 0:
            if parent_index < array_val[counter]:
                flag = True
                chosen_parent = counter
            else:
                counter = counter + 1
        else:
            if parent_index < array_val[counter] and parent_index > array_val[counter-1]:
                chosen_parent = counter
                flag = True
            else:
                counter = counter + 1

    return counter
