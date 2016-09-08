import source_reader as src
import accuracy_metrics_check

def main_fitness_cal(pop):
    pop_array = []

    for elem in pop:
        #calc accuracy for each individual
        elem_accuracy = accuracy_check(elem)

        #calc runtime
        elem_runtime = asdas()

        


def calc_fitness(f_score, energy, obst):

    W_OBSTRUSIVE = 0.25 #for the number of sensors
    W_ENERGY = 0.25 # for the computational cost
    W_ACCURACY = 0.5
    TOT_SENS = 3 # in this case the total number of sensors is 3

    fit_val = (W_ACCURACY * f_score/100) - ((W_OBSTRUSIVE * obst / TOT_SENS) + (W_ENERGY * energy)) #fscore is divided to 100 to discard the percentage
    return fit_val
