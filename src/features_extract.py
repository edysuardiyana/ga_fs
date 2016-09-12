import numpy as np
import math
from numpy import sqrt
import scipy.stats as st
import timeit
import time
import source_reader as src
import warnings

NUM_OF_STAGES = 3

def main_features(data_vm, data_x, data_y, data_z, freq_rate, elem_pop, pos):
    pre_win= freq_rate
    imp = 3 * freq_rate
    post_win = 5 * freq_rate

    num_of_seg = len(elem_pop)/src.read_num_position()
    instance = []
    if pos == "chest":
        chest_elem = elem_pop[:num_of_seg]
        num_stage = len(chest_elem)/NUM_OF_STAGES

        start_time = timeit.default_timer()
        pre_chest = features_calc(data_vm[:pre_win], data_x[:pre_win], data_y[:pre_win], data_z[:pre_win], freq_rate, chest_elem[:num_stage])
        imp_chest = features_calc(data_vm[pre_win : imp], data_x[pre_win : imp], data_y[pre_win : imp], data_z[pre_win : imp], freq_rate, chest_elem[num_stage:num_stage * 2])
        post_chest = features_calc(data_vm[imp:post_win], data_x[imp:post_win], data_y[imp:post_win], data_z[imp:post_win], freq_rate, chest_elem[num_stage * 2 : num_stage * 3])
        end_time = timeit.default_timer() #time.clock()
        run_time = end_time - start_time

        instance.extend(pre_chest)
        instance.extend(imp_chest)
        instance.extend(post_chest)

    elif pos == "waist":
        waist_elem = elem_pop[num_of_seg:num_of_seg * 2]
        num_stage = len(waist_elem)/NUM_OF_STAGES

        start_time = timeit.default_timer()
        pre_waist = features_calc(data_vm[:pre_win], data_x[:pre_win], data_y[:pre_win], data_z[:pre_win], freq_rate, waist_elem[:num_stage])
        imp_waist = features_calc(data_vm[pre_win:imp], data_x[pre_win:imp], data_y[pre_win:imp], data_z[pre_win:imp], freq_rate, waist_elem[num_stage:num_stage * 2])
        post_waist = features_calc(data_vm[imp:post_win], data_x[imp:post_win], data_y[imp:post_win], data_z[imp:post_win], freq_rate, waist_elem[num_stage * 2:num_stage * 3])
        end_time = timeit.default_timer() #time.clock()
        run_time = end_time - start_time


        instance.extend(pre_waist)
        instance.extend(imp_waist)
        instance.extend(post_waist)

    else:
        thigh_elem = elem_pop[num_of_seg * 2 : num_of_seg * 3]
        num_stage = len(thigh_elem)/NUM_OF_STAGES
        start_time = timeit.default_timer()
        pre_thigh = features_calc(data_vm[:pre_win], data_x[:pre_win], data_y[:pre_win], data_z[:pre_win], freq_rate, thigh_elem[:num_stage])
        imp_thigh = features_calc(data_vm[pre_win : imp], data_x[pre_win : imp], data_y[pre_win : imp], data_z[pre_win : imp], freq_rate, thigh_elem[num_stage:num_stage * 2])
        post_thigh = features_calc(data_vm[imp:post_win], data_x[imp:post_win], data_y[imp:post_win], data_z[imp:post_win], freq_rate, thigh_elem[num_stage * 2 : num_stage * 3])
        end_time = timeit.default_timer() #time.clock()
        run_time = end_time - start_time

        instance.extend(pre_thigh)
        instance.extend(imp_thigh)
        instance.extend(post_thigh)

    #warnings.simplefilter("error") #this error only appears if the sampling rate is 1
    return instance, run_time

def features_calc(data,x,y,z,freq_rate, elem):
    inst = []
    new_array = np.array(data)
    power_by_two = np.array(data)**2
    means_array = power_by_two.mean()
    for i in range(len(elem)):
        if i == 0 and elem[i] == 1:
            mean = round(new_array.mean(),6)
            inst.append(mean)
        elif i == 1 and elem[i] == 1:
            variance = round(np.var(data, ddof=1),6)
            inst.append(variance)
        elif i == 2 and elem[i] == 1:
            max_val = round(max(data),6)
            inst.append(max_val)
        elif i == 3 and elem[i] == 1:
            min_val = round(min(data),6)
            inst.append(min_val)
        elif i == 4 and elem[i] == 1:
            rms = round(sqrt(means_array),6)
            inst.append(rms)
        elif i == 5 and elem[i] == 1:
            raw_velo = integrate(data, freq_rate)
            velo = round(raw_velo,6)
            inst.append(velo)
        elif i == 6 and elem[i] == 1:
            raw_sma = smafeat(x,y,z,freq_rate)
            sma = round(raw_sma,6)
            inst.append(sma)
        elif i == 7 and elem[i] == 1:
            raw_ema = ema_calc(data)
            ema = round(raw_ema,6)
            inst.append(ema)
        elif i == 8 and elem[i] == 1:
            raw_energy = energyCalc(x,y,z, freq_rate)
            energy = round(raw_energy,6)
            inst.append(energy)

    return inst

def ema_calc(arrdat):
    CONST_ALPHA =  0.01 #float(2)/(len(arrdat)+1) # this is calculated by : 2/N+1 where N is total number of the data
    sem=[]

    for i in range(0,len(arrdat)):

        if i == 0:
            sval = 0

        else:
            sval = (CONST_ALPHA * arrdat[i]) + (1-CONST_ALPHA) * sem[i-1]

        sem.append(sval)


    emval = sem[len(sem)-1]

    return emval

def integrate(arrdat, freq_rate):

    Tperiod = 1/float(freq_rate) #calculate period

    velocity = 0; #initial value of velocity

    for n in range(0,len(arrdat)):

        velocity = velocity + arrdat[n] * Tperiod

    return velocity

def smafeat(datXa,datYa,datZa, freq_rate):

    dataXsq1 = sqrt(np.array(datXa) ** 2)
    dataYsq1 = sqrt(np.array(datYa) ** 2)
    dataZsq1 = sqrt(np.array(datZa) ** 2)


    dataXc1 = integrate(dataXsq1, freq_rate)
    dataYc1 = integrate(dataYsq1, freq_rate)
    dataZc1 = integrate(dataZsq1, freq_rate)
    sma = (dataXc1 + dataYc1 + dataZc1) / float(len(dataXsq1))

    return sma

def energyCalc(array1,array2,array3, freq_rate):

  totEnergy = integrate(np.array(array1) ** 2, freq_rate) + integrate(np.array(array2) ** 2, freq_rate) + integrate(np.array(array3) ** 2, freq_rate)

  return totEnergy
