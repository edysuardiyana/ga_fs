import csv
import source_reader as sc

def combined_features(list_name):
    combined_path = src.combined_path()
    combined_with_name = []
    chest_temp = []
    waist_temp = []
    thigh_temp = []
    final_array = []
    for name in list_name:
        chest_path = src.chest_path(name)
        waist_path = src.waist_path(name)
        thigh_path = src.thigh_path(name)
        with open(chest_path) as chest_obj:
            for line_chest in chest_obj:
                raw_chest = line_chest.split()
                chest_temp.append(raw_chest)

        with open(waist_path) as waist_obj:
            for line_waist in waist_obj:
                raw_waist = line_waist.split()
                waist_temp.append(raw_waist)

        with open(thigh_path) as thigh_obj:
            for line_thigh in thigh_obj:
                raw_thigh = line_thigh.split()
                thigh_temp.append(raw_thigh)

        final_array = main_combined(chest_temp, waist_temp, thigh_temp)
        del chest_temp[:]
        del waist_temp[:]
        del thigh_temp[:]
        temp_name = [name,final_array]
        combined_with_name.append(temp_name)

    return combined_with_name



def main_combined(chest_temp, waist_temp, thigh_temp):
    combined_data = []
    com_temp = []
    count_chest = 0
    count_waist = 0
    count_thigh = 0

    ct_t = []
    wt_t = []
    tt_t = []

    final_array = []


    while count_chest < len(chest_temp):

        row_chest = chest_temp[count_chest]

        if count_chest == 0: # first samples
            annot_ct = row_chest[len(row_chest)-1]
            count_chest += 1
            ct_t.append(row_chest)
        elif row_chest[len(row_chest)-1] == annot_ct: # if same annot
            ct_t.append(row_chest)
            count_chest += 1
        else: # different annot
            wt_t, waist_temp = check_next_sensor(waist_temp, annot_ct)
            tt_t, thigh_temp = check_next_sensor(thigh_temp, annot_ct)
            temp_final = combined_funct(ct_t, wt_t, tt_t)
            final_array.extend(temp_final)
            del ct_t[:]
            del wt_t[:]
            del tt_t[:]

            #get the new sample
            annot_ct = row_chest[len(chest_temp)-1]
            count_chest += 1
            ct_t.append(row_chest)

    #condition for the last elements
    if ct_t:

        wt_t, waist_temp = check_next_sensor(waist_temp, annot_ct)
        tt_t, thigh_temp = check_next_sensor(thigh_temp, annot_ct)
        temp_final = combined_funct(ct_t, wt_t, tt_t)
        final_array.extend(temp_final)

    return final_array


def combined_funct(chest, waist, thigh):
    final_array = []
    temp_final = []
    for i in range(len(chest)):
        temp_final.extend(chest[i])
        for j in range(len(waist)):
            temp_final.extend(waist[j])
            for k in range(len(thigh)):
                temp_final.extend(thigh[k])
                final_array.append(temp_final)

    return final_array

def check_next_sensor(array, annot):
    new_temp = []
    count = 0
    flag_count = True
    temp_row = array[count]
    temp_annot = temp_row[len(temp_row)-1]

    while flag_count:
        if count == 0:
            while temp_annot != annot:
                del array[count]
                count += 1
                temp_row = array[count]
                temp_annot = temp_row[len(temp_row)-1]
                new_temp.append(temp_row)
            else:
                while temp_annot == annot and count < len(array):
                    temp_row = array[count]
                    temp_annot = temp_row[len(temp_row)-1]
                    new_temp.append(temp_row)
                    count += 1

                flag_count = False

    print new_temp
    return new_temp, array
