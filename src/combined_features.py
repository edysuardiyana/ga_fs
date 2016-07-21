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
    ct = []
    wt = []
    tt = []
    final_array = []
    annot_c = chest_temp[0][len(chest_temp[0])-1]
    annot_w = waist_temp[0][len(waist_temp[0])-1]
    annot_t = thigh_temp[0][len(thigh_temp[0])-1]
    general_length = len(chest_temp[0])-1
    while chest_temp or waist_temp or thigh_temp or wt or ct or tt:
        #print "final array"
        #print final_array
        #collecting data from chest sensor

        if not ct and chest_temp :
            c_flag = True
            while c_flag :
                if chest_temp:
                    if annot_c == chest_temp[0][general_length]:
                        ct.append(chest_temp[0])
                        del chest_temp[0]
                    else:
                        c_flag = False
                else:
                    c_flag = False
        elif not ct and not chest_temp:
            if waist_temp:
                c_zero = [0] * (general_length)
                c_zero.append(annot_w)
                annot_c = annot_w
            else:
                c_zero = [0] * (general_length)
                c_zero.append(annot_t)
                annot_c = annot_t
            ct.append(c_zero)


        #collecting data from waist sensor
        if not wt and waist_temp:
            w_flag = True
            while w_flag:
                if waist_temp:
                    if annot_w == waist_temp[0][general_length]:
                        wt.append(waist_temp[0])
                        del waist_temp[0]
                    else:
                        w_flag = False
                else:
                    w_flag = False
        elif not wt and not waist_temp:
            if chest_temp:
                w_zero = [0] * (general_length)
                w_zero.append(annot_c)
                annot_w = annot_c
            else:
                w_zero = [0] *(general_length)
                w_zero.append(annot_t)
                annot_w = annot_c
            wt.append(w_zero)

        #collecting data from thigh
        if not tt and thigh_temp:
            t_flag = True
            while t_flag:
                if thigh_temp:
                    if annot_t == thigh_temp[0][general_length]:
                        tt.append(thigh_temp[0])
                        del thigh_temp[0]
                    else:
                        t_flag = False
                else:
                    t_flag = False
        elif not tt and not thigh_temp:
            if chest_temp:
                t_zero = [0] * (general_length)
                t_zero.append(annot_c)
                annot_t = annot_c
            else:
                t_zero = [0] * (general_length)
                t_zero.append(annot_w)
                annot_t = annot_w
            tt.append(t_zero)

        if annot_c == annot_t and annot_c != annot_w:
            #print "first if"
            run_flag = True
            if not chest_temp:
                run_flag = False
            elif not waist:
                run_flag = False
            elif annot_w == chest_temp[0][general_length] or annot_w == thigh_temp[0][general_length] :
                run_flag = True
            else:
                run_flag = False

            print run_flag
            if run_flag:
                w_zero = []
                raw_w_zero = [0] * (general_length)
                raw_w_zero.append(annot_c)
                w_zero.append(raw_w_zero)
                temp_fin_array = combined_funct(ct, w_zero, tt)
                final_array.extend(temp_fin_array)
                ct = []
                tt = []
                if chest_temp:
                    annot_c = chest_temp[0][general_length]
                if thigh_temp:
                    annot_t = thigh_temp[0][general_length]
            else:
                c_zero = []
                raw_c_zero = [0] * (general_length)
                raw_c_zero.append(annot_w)
                c_zero.append(raw_c_zero)

                t_zero = []
                raw_t_zero = [0] * (general_length)
                raw_t_zero.append(annot_w)
                t_zero.append(raw_t_zero)

                temp_fin_array = combined_funct(c_zero, wt, t_zero)
                final_array.extend(temp_fin_array)
                wt = []
                if waist_temp:
                    annot_w = waist_temp[0][general_length]

        elif annot_w == annot_t and annot_c != annot_w:
            #print "second if"
            run_flag = True
            if not waist_temp:
                run_flag = False
            elif not thigh_temp:
                run_flag = False
            elif annot_c == thigh_temp[0][general_length] or annot_c == waist_temp[0][general_length]:
                run_flag = True
            else:
                run_flag = False
            #print run_flag
            if run_flag:
                c_zero = []
                raw_c_zero = [0] * (general_length)
                raw_c_zero.append(annot_w)
                c_zero.append(raw_c_zero)
                temp_fin_array = combined_funct(c_zero, wt, tt)
                final_array.extend(temp_fin_array)
                wt = []
                tt = []
                if waist_temp:
                    annot_w = waist_temp[0][general_length]
                if thigh_temp:
                    annot_t = thigh_temp[0][general_length]
            else:
                t_zero = []
                raw_t_zero = [0] * (general_length)
                raw_t_zero.append(annot_c)
                t_zero.append(raw_t_zero)

                w_zero = []
                raw_w_zero = [0] * (general_length)
                raw_w_zero.append(annot_c)
                w_zero.append(raw_w_zero)

                temp_fin_array = combined_funct(ct, w_zero, t_zero)
                final_array.extend(temp_fin_array)
                ct = []

                if chest_temp:
                    annot_c = chest_temp[0][general_length]

        elif annot_c != annot_t and annot_c == annot_w:
            #print "third if"
            run_flag = True
            if not chest_temp:
                run_flag = False
            elif not waist_temp:
                run_flag = False
            elif annot_t == waist_temp[0][general_length] or annot_t == chest_temp[0][general_length]:
                run_flag = True
            else:
                run_flag = False

            if run_flag:
                t_zero = []
                raw_t_zero = [0] * (general_length)
                raw_t_zero.append(annot_c)
                t_zero.append(raw_t_zero)
                temp_fin_array = combined_funct(ct, wt, t_zero)
                final_array.extend(temp_fin_array)
                ct = []
                wt = []
                if chest_temp:
                    annot_c = chest_temp[0][general_length]
                if waist_temp:
                    annot_w = waist_temp[0][general_length]
            else:
                w_zero = []
                raw_w_zero = [0] * (general_length)
                raw_w_zero.append(annot_t)
                w_zero.append(raw_w_zero)

                c_zero = []
                raw_c_zero = [0] * (general_length)
                raw_c_zero.append(annot_t)
                c_zero.append(raw_c_zero)
                temp_fin_array = combined_funct(c_zero, w_zero, tt)
                final_array.extend(temp_fin_array)
                tt = []
                if thigh_temp:
                    annot_t = thigh_temp[0][general_length]

        else:
            temp_fin_array = combined_funct(ct, wt, tt)
            final_array.extend(temp_fin_array)
            ct = []
            wt = []
            tt = []

            if chest_temp:
                annot_c = chest_temp[0][general_length]
            if waist_temp:
                annot_w = waist_temp[0][general_length]
            if thigh_temp:
                annot_t = thigh_temp[0][general_length]

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
    #print array
    while flag_count and len(array) > 0:
        temp_row = array[0]
        temp_annot = temp_row[len(temp_row)-1]
        #print temp_row
        if len(new_temp) == 0:
            #print "count is zero"
            if temp_annot != annot:
                #print "count is zero and annots are not the same"
                del array[0]
            else:
                #print "count is zero and annots are the same"
                new_temp.append(temp_row)
                del array[0]
        else:
            if temp_annot == annot :
                #print "count is not zero and annot is the same"
                temp_row = array[0]
                temp_annot = temp_row[len(temp_row)-1]
                new_temp.append(temp_row)
                del array[0]
            else:
                #print "flag"
                flag_count = False
        #print "this is len array: " + str(len(array))
    return new_temp, array
