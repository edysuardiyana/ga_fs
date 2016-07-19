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
            # if chest produce peak but the other sensors don't
            #print "get here"

            waist_annot_temp = waist_temp[0][len(waist_temp[0])-1]
            thigh_annot_temp = thigh_temp[0][len(thigh_temp[0])-1]

            #print "this is chest : " + str(annot_ct)
            #print "this is waist : " + str(waist_annot_temp)
            #print "this is thigh: "+ str(thigh_annot_temp)

            if annot_ct != waist_annot_temp and annot_ct != thigh_annot_temp and thigh_annot_temp == waist_annot_temp:
                count_waist_temp = 1
                count_thigh_temp = 1

                while waist_annot_temp == waist_temp[count_waist_temp][len(waist_temp[0])-1]:
                    count_waist_temp += 1

                while thigh_annot_temp == thigh_temp[count_thigh_temp][len(thigh_temp[0])-1]:
                    count_thigh_temp += 1

                if annot_ct == waist_temp[count_waist_temp][len(waist_temp[0])-1] or annot_ct == thigh_temp[count_thigh_temp][len(thigh_temp[0])-1]:
                    #print "get second the special if"
                    wt_t, waist_temp = check_next_sensor(waist_temp, annot_ct)

                    tt_t, thigh_temp = check_next_sensor(thigh_temp, annot_ct)

                    temp_final = combined_funct(ct_t, wt_t, tt_t)
                    final_array.extend(temp_final)
                    ct_t = []
                    wt_t = []
                    tt_t = []

                    #get the new sample
                    annot_ct = row_chest[len(row_chest)-1]
                    count_chest += 1
                    ct_t.append(row_chest)
                else:
                    #print "get first if"
                    count_chest += 1
                    annot_ct = row_chest[len(row_chest)-1]

            else:
                #print "get second if"
                wt_t, waist_temp = check_next_sensor(waist_temp, annot_ct)

                tt_t, thigh_temp = check_next_sensor(thigh_temp, annot_ct)
                temp_final = combined_funct(ct_t, wt_t, tt_t)
                final_array.extend(temp_final)
                ct_t = []
                wt_t = []
                tt_t = []

                #get the new sample
                annot_ct = row_chest[len(row_chest)-1]
                count_chest += 1
                ct_t.append(row_chest)
        #print "current annot: " + str(row_chest[len(row_chest)-1])
        #print "saved annot: " + str(annot_ct)

    #condition for the last elements
    if ct_t:
        #print "come here"
        print "waist: "
        wt_t, waist_temp = check_next_sensor(waist_temp, annot_ct)
        print wt_t
        print "thigh: "
        tt_t, thigh_temp = check_next_sensor(thigh_temp, annot_ct)
        #print tt_t
        temp_final = combined_funct(ct_t, wt_t, tt_t)
        final_array.extend(temp_final)

    return final_array


def combined_funct(chest, waist, thigh):
    final_array = []
    temp_final = []
    temp_chest = []
    temp_waist = []
    temp_thigh = []
    for i in range(len(chest)):
        elem_chest = chest[i]
        annot = elem_chest[len(elem_chest)-1]
        for ii in range(len(elem_chest)-1):
            temp_chest.append(elem_chest[ii])

        for j in range(len(waist)):
            elem_waist = waist[j]
            for jj in range(len(elem_waist)-1):
                temp_waist.append(elem_waist[jj])

            for k in range(len(thigh)):
                elem_thigh = thigh[k]
                for kk in range(len(elem_thigh)-1):
                    temp_thigh.append(elem_thigh[kk])

                temp_final.extend(temp_chest)
                temp_final.extend(temp_waist)
                temp_final.extend(temp_thigh)
                temp_final.append(annot)
                final_array.append(temp_final)

                temp_final = []
                temp_thigh = []

            temp_waist = []
        temp_chest = []

    return final_array

def check_next_sensor(array, annot):
    new_temp = []
    flag_count = True
    #print "this is array length: " + str(len(array))
    #print "this is count: " + str(count)
    #temp_row = array[count]
    #temp_annot = temp_row[len(temp_row)-1]
    print array
    while flag_count and len(array) > 0:
        temp_row = array[0]
        temp_annot = temp_row[len(temp_row)-1]
        print temp_row
        if len(new_temp) == 0:
            print "count is zero"
            if temp_annot != annot:
                print "count is zero and annots are not the same"
                del array[0]
            else:
                print "count is zero and annots are the same"
                new_temp.append(temp_row)
                del array[0]
        else:
            if temp_annot == annot :
                print "count is not zero and annot is the same"
                temp_row = array[0]
                temp_annot = temp_row[len(temp_row)-1]
                new_temp.append(temp_row)
                del array[0]
            else:
                print "flag"
                flag_count = False
        print "this is len array: " + str(len(array))
    return new_temp, array
