
def calc_fitness(f_score, energy, obst):

    W_OBSTRUSIVE = 0.5 #for the number of sensors
    W_ENERGY = 0.5 # for the computational cost
    #W_ACC =

    fit_val = f_score - ( W_OBSTRUSIVE * obst + W_ENERGY * energy)

    return fit_val
