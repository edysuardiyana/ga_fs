import source_reader as src
import main_detection as md

def main_fitness_cal(listname, elem):

    f_score, runtime, sens_place = md.main_detection(listname, elem)
    temp_fitness = calc_fitness(f_score, runtime, sens_place)
    indi_and_fit = [elem, f_score, runtime, sens_place, temp_fitness]

    return indi_and_fit

def calc_fitness(f_score, energy, obst):

    W_OBSTRUSIVE = 0.25 #for the number of sensors
    W_ENERGY = 0.25 # for the computational cost
    W_ACCURACY = 0.5
    TOT_SENS = 3 # in this case the total number of sensors is 3

    fit_val = (W_ACCURACY * f_score/100) - ((W_OBSTRUSIVE * obst / TOT_SENS) + (W_ENERGY * energy)) #fscore is divided to 100 to discard the percentage
    return fit_val
