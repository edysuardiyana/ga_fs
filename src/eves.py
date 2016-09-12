import features_extract as ft_stage
import math
import operator
import matplotlib.pyplot as plt
import timeit
import time


FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])


def eves_window(data_x, data_y, data_z, annot, freq_rate, elem_pop, pos):
    size_active_win = (3 * freq_rate) + 1
    feature_win = 5 * freq_rate
    buffer_size = freq_rate
    buffer_x = []
    buffer_y = []
    buffer_z = []
    buffer_vm= []
    buffer_annot = []
    annot_num = 0
    annot_flag = 0
    run_time_seq = []
    instances_seq = []

    temp_max = 0
    temp_max_2 = 1.6
    index_temp_2 = 0
    state_1 = False
    state_2 = False
    state_3 = False

    state_2_flag = False
    for i in range(0,len(data_x)):
        buffer_x.append(data_x[i])
        buffer_y.append(data_y[i])
        buffer_z.append(data_z[i])
        svm_val = l2norm(data_x[i], data_y[i], data_z[i])
        buffer_vm.append(svm_val)
        buffer_annot.append(annot[i])

        if not state_1:
            if len(buffer_vm) == buffer_size + 1:
                state_1 = True
            else:
                state_1 = False

        if state_1:
            state_2_flag = False
            if buffer_vm[len(buffer_vm)-1] > 1.6:
                state_2 = True
                state_1 = False
                temp_max = buffer_vm[len(buffer_vm)-1]
            else:

                del buffer_vm[0]
                del buffer_x[0]
                del buffer_y[0]
                del buffer_z[0]
                del buffer_annot[0]
                state_1 = False

        elif state_2:
            state_2_flag = False
            if buffer_vm[len(buffer_vm)-1] > temp_max:
                temp_max = buffer_vm[len(buffer_vm)-1]
                del buffer_vm[:len(buffer_vm)-(buffer_size + 1)]
                del buffer_x[:len(buffer_x)-(buffer_size + 1)]
                del buffer_y[:len(buffer_y)-(buffer_size + 1)]
                del buffer_z[:len(buffer_z)-(buffer_size + 1)]
                del buffer_annot[:len(buffer_annot)-(buffer_size + 1)]
            else:
                if len(buffer_vm) == size_active_win:
                    state_2 = False
                    state_3 = True
        elif state_3 :
            if len(buffer_vm) == feature_win + 1:
                instance, runtime = ft_stage.main_features(
                buffer_vm[:len(buffer_vm)-1],
                buffer_x[:len(buffer_x)-1],
                buffer_y[:len(buffer_y)-1],
                buffer_z[:len(buffer_z)-1],
                freq_rate, elem_pop, pos)
                instance.append(buffer_annot[freq_rate])
                if buffer_annot[freq_rate] in FALL_SET:
                    instance.append(1)
                else:
                    instance.append(0)

                temp_runtime = [0,runtime] # to avoid error in writing into CSV
                instances_seq.append(instance)
                run_time_seq.append(temp_runtime)

                temp_max = temp_max_2
                if state_2_flag:
                    state_2 = True
                    del buffer_vm[:index_temp_2 - buffer_size]
                    del buffer_x[:index_temp_2 - buffer_size]
                    del buffer_y[:index_temp_2 - buffer_size]
                    del buffer_z[:index_temp_2 - buffer_size]
                    del buffer_annot[:index_temp_2 - buffer_size]
                else:
                    del buffer_vm[:len(buffer_vm) - buffer_size]
                    del buffer_x[:len(buffer_x) - buffer_size]
                    del buffer_y[:len(buffer_y) - buffer_size]
                    del buffer_z[:len(buffer_z) - buffer_size]
                    del buffer_annot[:len(buffer_annot) - buffer_size]

                    state_1 = True

                state_3 = False
            else:
                if buffer_vm[len(buffer_vm)-1] > temp_max_2:
                    temp_max_2 = buffer_vm[len(buffer_vm)-1]
                    index_temp_2 = len(buffer_vm)-1
                    state_2_flag = True
    return instances_seq,run_time_seq

def l2norm(x, y, z):
    return math.sqrt(x * x + y * y + z * z)
