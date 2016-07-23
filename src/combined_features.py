import csv
import source_reader as src

def combined_features(list_name):
    combined_with_name = []
    chest_temp = []
    waist_temp = []
    thigh_temp = []
    final_array = []
    for name in list_name:
        print name
        chest_path = src.chest_path(name)
        waist_path = src.waist_path(name)
        thigh_path = src.thigh_path(name)
        with open(chest_path) as chest_obj:
            for line_chest in chest_obj:
                raw_chest = line_chest.split()
                chest_temp.append(raw_chest[:len(raw_chest)-1])

        with open(waist_path) as waist_obj:
            for line_waist in waist_obj:
                raw_waist = line_waist.split()
                waist_temp.append(raw_waist[:len(raw_waist)-1])

        with open(thigh_path) as thigh_obj:
            for line_thigh in thigh_obj:
                raw_thigh = line_thigh.split()
                thigh_temp.append(raw_thigh[:len(raw_thigh)-1])

        final_array = main_combined(chest_temp, waist_temp, thigh_temp)
        chest_temp = []
        waist_temp = []
        thigh_temp = []
        #temp_name = [name,final_array]
        #combined_with_name.append(temp_name)
        write_combined_data(name, final_array)
    #return combined_with_name

def write_combined_data(name, data):

    path = src.combined_path(name)
    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')
    for line in data:
        csv_writer.writerow(line)
    out_file.close()

def main_combined(chest_temp, waist_temp, thigh_temp):

    general_length = len(chest_temp[0])

    ct = []
    wt = []

    while chest_temp or waist_temp or ct or wt:
        final_array = []
        ct_annot = chest_temp[0][general_length-1]
        wt_annot = waist_temp[0][general_length-1]

        while chest_temp[0][general_length-1] == ct_annot:
            ct.append(chest_temp[count_c])
            del chest_temp[0]

        while waist_temp[0][general_length-1] == wt_annot:
            wt.append(waist_temp(count_w))
            del waist_temp[0]

        if ct_annot == w_annot:
            temp_fin = combined_funct(ct, wt)

    return final_array


def combined_funct(x, y):
    final_array = []
    temp_final = []
    temp_x = []
    temp_y = []

    for i in range(len(x)):
        elem_x = x[i]

        annot = elem_x[len(elem_x)-1]

        for j in range(len(y)):
            elem_y = y[j]
            temp_final.extend(elem_x[:len(elem_x)-1])
            temp_final.extend(elem_y[:len(elem_y)-1])
            temp_final.append(annot)
            final_array.append(temp_final)
            temp_final = []

    return final_array
