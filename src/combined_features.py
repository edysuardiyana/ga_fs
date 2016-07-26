import csv
import source_reader as src
import statistics as stat

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
                dirt_raw_chest = line_chest.split()
                raw_chest = [float(i) for i in dirt_raw_chest[:len(dirt_raw_chest)]]
                chest_temp.append(raw_chest[:len(raw_chest)-1])

        with open(waist_path) as waist_obj:
            for line_waist in waist_obj:
                dirt_raw_waist = line_waist.split()
                raw_waist = [float(i) for i in dirt_raw_waist[:len(dirt_raw_waist)]]
                waist_temp.append(raw_waist[:len(raw_waist)-1])

        with open(thigh_path) as thigh_obj:
            for line_thigh in thigh_obj:
                dirt_raw_thigh = line_thigh.split()
                raw_thigh = [float(i) for i in dirt_raw_thigh[:len(dirt_raw_thigh)]]
                thigh_temp.append(raw_thigh[:len(raw_thigh)-1])

        final_array = main_combined(chest_temp, waist_temp, thigh_temp)
        chest_temp = []
        waist_temp = []
        thigh_temp = []
        #temp_name = [name,final_array]
        #combined_with_name.append(temp_name)
        write_combined_data(name, final_array)

    num_of_features = len(final_array[0])-1 # do not include annotation

    return num_of_features

def write_combined_data(name, data):

    path = src.combined_path(name)
    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')
    for line in data:
        csv_writer.writerow(line)
    out_file.close()

def main_combined(chest_temp, waist_temp, thigh_temp):
    chest_array = []
    waist_array = []
    thigh_array = []

    final_array = []
    gen_len = len(chest_temp[0])
    while chest_temp:
        #check the chest data
        annot_c = chest_temp[0][gen_len-1]
        count_c = 0
        while count_c < len(chest_temp):
            if chest_temp[count_c][gen_len-1] == annot_c:
                chest_array.append(chest_temp[count_c])
                del chest_temp[count_c]
                if count_c > 0:
                    count_c -= 1
            else:
                count_c += 1

        #check_waist
        count_w = 0
        while count_w < len(waist_temp):
            if waist_temp[count_w][gen_len-1] == annot_c:
                waist_array.append(waist_temp[count_w])
                del waist_temp[count_w]
                if count_w > 0:
                    count_w -= 1
            else:
                count_w += 1
        #check thigh
        count_t = 0
        len_temp_t = len(thigh_temp)
        while count_t < len(thigh_temp):
            if thigh_temp[count_t][gen_len-1] == annot_c:
                thigh_array.append(thigh_temp[count_t])
                del thigh_temp[count_t]
                if count_t > 0 :
                    count_t -= 1
            else:
                count_t += 1

        if len(chest_array) > 0 and len(waist_array) > 0 and len(thigh_array) > 0:
            temp_final = fuse_data(chest_array, waist_array, thigh_array)
            final_array.extend(temp_final)

        chest_array = []
        waist_array = []
        thigh_array = []

    return final_array

def fuse_data(chest, waist, thigh):
    new_c, new_w, new_t = add_miss_val(chest, waist, thigh)
    final_array = []
    gen_len = len(chest[0])
    annot = chest[0][gen_len-1]
    for i in range(len(new_c)):
        temp_final = []

        row_chest = new_c[i]
        row_waist = new_w[i]
        row_thigh = new_t[i]

        temp_final.extend(row_chest[:gen_len-1])
        temp_final.extend(row_waist[:gen_len-1])
        temp_final.extend(row_thigh[:gen_len-1])
        temp_final.append(annot)

        final_array.append(temp_final)

    return final_array


def add_miss_val(chest, waist, thigh):

    #get median for chest
    med_c = calc_median(chest)

    # get median for waist
    med_w = calc_median(waist)

    #get median for thigh
    med_t = calc_median(thigh)

    #get the length from all sensors and find the longest one
    len_coll = [len(chest), len(waist), len(thigh)]
    max_len = max(len_coll)


    diff_len_c = max_len - len(chest)
    diff_len_w = max_len - len(waist)
    diff_len_t = max_len - len(thigh)

    #adding data for chest
    for i in range(diff_len_c):
        chest.append(med_c)

    #adding data for waist
    for j in range(diff_len_w):
        waist.append(med_w)

    #adding data for thigh
    for k in range(diff_len_t):
        thigh.append(med_t)

    return chest, waist, thigh


def calc_median(array):
    med_val = []
    len_array = len(array[0]) #do not include the annotation
    annot = array[0][len_array-1]
    for i in range(len_array):
        temp = []
        for j in range(len(array)):
            row = array[j][i]
            temp.append(row)

        med_temp = stat.median(temp)
        med_val.append(med_temp)

    med_val.append(annot)
    return med_val
