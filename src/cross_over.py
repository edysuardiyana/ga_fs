from random import randint

def cross_over_funct(parent_1, parent_2):
    new_child_1 = []
    new_child_2 = []
    cross_index = 0
    while cross_index == 0 or cross_index == len(parent_1)-1:
        cross_index = randint(0, len(parent_1)-1)

    for k in range(len(parent_1)):
        new_child_1.append(parent_1[k])
        new_child_2.append(parent_2[k])
    for i in range(cross_index, len(parent_1)):
        temp_1 = new_child_1[i]
        temp_2 = new_child_2[i]

        new_child_1[i] = temp_2
        new_child_2[i] = temp_1

    return new_child_1, new_child_2
