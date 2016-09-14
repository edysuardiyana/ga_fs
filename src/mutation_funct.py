import random
import source_reader as src

def mutate(instance):

    #P_MUTATE = 0.1 # mutation rate
    p_mutate = src.read_p_mutate()
    test_flag = False #this is just for test case purpose
    temp_instance = []

    for elem in instance:
        temp_instance.append(elem)

    for i in range(len(temp_instance)):
        p_rand = random.uniform(0,1)
        if temp_instance[i] == 0 and p_mutate > p_rand:
            temp_instance[i] = 1
            test_flag = True
        elif temp_instance[i] == 1 and p_mutate > p_rand:
            temp_instance[i] = 0
            test_flag = True

    return test_flag, temp_instance
