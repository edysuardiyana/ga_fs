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
        print "Combinining: " + name
        chest_path = src.feat_path(name, "chest")
        waist_path = src.feat_path(name, "waist")
        thigh_path = src.feat_path(name, "thigh")
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

def main_combined(chest, waist, thigh):

    main_flag =  True
    chest_temp = []
    waist_temp = []
    thigh_temp = []
    final_array = []
    annot = None
    while main_flag:

        len_chest = len(chest)
        len_waist = len(waist)
        len_thigh = len(thigh)

        if len_chest > 0 or len_waist > 0 or len_thigh:
            main_flag = True
            if len_chest > 0:
                #take annot from chest
                annot = chest[0][len(chest[0])-1] #annotation is placed two places from right
            elif len_waist > 0:
                #take annot from waist
                annot = waist[0][len(waist[0])-1]
            else:
                #take annot from thigh
                annot = thigh[0][len(thigh[0])-1]
        else:
            main_flag = False

        #take sample from chest
        count_chest = 0
        while count_chest < len(chest):
            line_chest = chest[count_chest]
            annot_c = line_chest[len(line_chest)-1]
            if annot_c == annot:
                #same annotation
                chest_temp.append(line_chest)
                del chest[count_chest]
                if count_chest > 0:
                    count_chest -= 1
            else:
                count_chest += 1

        #take sample from waist
        count_waist = 0
        while count_waist < len(waist):
            line_waist = waist[count_waist]
            annot_w = line_waist[len(line_waist)-1]
            if annot_w == annot:
                waist_temp.append(line_waist)
                del waist[count_waist]
                if count_waist > 0:
                    count_waist -= 1
            else:
                count_waist += 1

        #take sample from thigh
        count_thigh = 0
        while count_thigh < len(thigh):
            line_thigh = thigh[count_thigh]
            annot_t = line_thigh[len(line_thigh)-1]
            if annot_t == annot:
                thigh_temp.append(line_thigh)
                del thigh[count_thigh]
                if count_thigh > 0:
                    count_thigh -= 1
            else:
                count_thigh += 1

        if chest_temp and waist_temp and thigh_temp:
            new_fuse = fuse_data(chest_temp, waist_temp, thigh_temp)
            final_array.extend(new_fuse)
        chest_temp = []
        waist_temp = []
        thigh_temp = []

    return final_array

def fuse_data(chest, waist, thigh):

    new_c, new_w, new_t = add_miss_val(chest, waist, thigh)
    final_array = []

    if new_c:
        gen_len = len(new_c[0])
        annot = new_c[0][gen_len - 1]
        len_loop = len(new_c)
    elif new_w:
        gen_len = len(new_w[0])
        annot = new_w[0][gen_len - 1]
        len_loop = len(new_w)
    else:
        gen_len = len(new_t[0])
        annot = new_t[0][gen_len - 1]
        len_loop = len(new_t)

    for i in range(len_loop):
        temp_final = []

        if new_c:
            row_chest = new_c[i]
            temp_final.extend(row_chest[:len(row_chest)-1])

        if new_w:
            row_waist = new_w[i]

            temp_final.extend(row_waist[:len(row_waist)-1])

        if new_t:
            row_thigh = new_t[i]

            temp_final.extend(row_thigh[:len(row_thigh)-1])

        temp_final.append(annot)
        final_array.append(temp_final)

    return final_array


def add_miss_val(chest, waist, thigh):

    #get median for chest
    if chest:
        med_c = calc_median(chest)

    # get median for waist
    if waist:
        med_w = calc_median(waist)

    #get median for thigh
    if thigh:
        med_t = calc_median(thigh)

    #get the length from all sensors and find the longest one
    len_coll = [len(chest), len(waist), len(thigh)]
    max_len = max(len_coll)

    if chest:
        diff_len_c = max_len - len(chest)
        #adding data for chest
        for i in range(diff_len_c):
            chest.append(med_c)
    if waist:
        diff_len_w = max_len - len(waist)
        #adding data for waist
        for j in range(diff_len_w):
            waist.append(med_w)
    if thigh:
        diff_len_t = max_len - len(thigh)
        #adding data for thigh
        for k in range(diff_len_t):
            thigh.append(med_t)

    return chest, waist, thigh


def calc_median(array):

    med_val = []
    len_array = len(array[0])
    annot = array[0][len_array-1]
    for i in range(len_array-1): #do not include the annotation
        temp = []
        for j in range(len(array)):
            row = array[j][i]
            temp.append(row)

        med_temp = stat.median(temp)
        med_val.append(med_temp)

    med_val.append(annot)
    return med_val
