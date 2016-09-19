import eves
#import ga_fs.src.source_reader as src
import source_reader as src
import csv
import combined_features as cf
import training_testing as tt
import statistics as stat


FREQ_RATE = 100

def main_detection(listname, elem_pop): #elem pop is an individual

    print "individual: "
    print elem_pop
    f_score_val = 0
    avg_run_time = 0
    tot_num_sens = 0
    tot_chest_time = []
    tot_waist_time = []
    tot_thigh_time = []

    for name in listname:
        print "extracting features from : " + name

        #chest
        #read data
        x_c, y_c, z_c, a_c = read_seq(name,"chest")
        ins_c, runt_c = eves.eves_window(x_c, y_c, z_c, a_c, FREQ_RATE, elem_pop, "chest")
        write_result(name,"chest","instance",ins_c) #writing instances
        write_result(name,"chest", "runtime", runt_c) #writing run time
        for line_c in runt_c:
            tot_chest_time.append(line_c[1])


        #waist
        x_w, y_w, z_w, a_w = read_seq(name,"waist")
        ins_w, runt_w = eves.eves_window(x_w, y_w, z_w, a_w, FREQ_RATE, elem_pop, "waist")
        write_result(name,"waist","instance",ins_w) #writing instances
        write_result(name,"waist", "runtime", runt_w) #writing run time
        for line_w in runt_w:
            tot_waist_time.append(line_w[1])


        #thigh
        x_t, y_t, z_t, a_t = read_seq(name, "thigh")
        ins_t, runt_t = eves.eves_window(x_t, y_t, z_t, a_t, FREQ_RATE, elem_pop, "thigh")
        write_result(name,"thigh","instance",ins_t) #writing instances
        write_result(name,"thigh", "runtime", runt_t) #writing run time
        for line_t in runt_t:
            tot_thigh_time.append(line_t[1])

    cf.combined_features(listname)

    temp_c_runtime = stat.mean(tot_chest_time)
    temp_w_runtime = stat.mean(tot_waist_time)
    temp_t_runtime = stat.mean(tot_thigh_time)

    tot_run_time = temp_c_runtime + temp_w_runtime + temp_t_runtime #total run time
    prec_val, rec_val, f_score_val = tt.accuracy_measure(listname) # average f_score
    sensor_place = num_of_sens(elem_pop)

    return prec_val, rec_val, f_score_val, tot_run_time, sensor_place


def read_seq(name, position):
    path = src.raw_source(name,position)
    x = []
    y = []
    z = []
    annot = []
    with open(path) as obj:
        for line in obj:
            raw_splitted = line.split()
            f_split = [float(i) for i in raw_splitted]
            x.append(f_split[0])
            y.append(f_split[1])
            z.append(f_split[2])
            annot.append(f_split[3])

    return x,y,z,annot

def num_of_sens(elem):
    len_part = len(elem)/3
    chest_part = elem[:len_part]
    waist_part = elem[len_part:len_part * 2]
    thigh_part = elem[len_part * 2:len_part * 3]

    flag_chest = 0
    flag_waist = 0
    flag_thigh = 0

    tot_num_sens = 0
    for i in range(len_part):
        if chest_part[i] > 0:
            flag_chest = 1

        if waist_part[i] > 0:
            flag_waist = 1

        if thigh_part[i] > 0:
            flag_thigh = 1

    tot_num_sens = flag_chest + flag_waist + flag_thigh

    return tot_num_sens


def write_result(name,position,indicator, data):
    if indicator == "instance":
        path = src.feat_path(name,position)
    else:
        path = src.runtime_path(name,position)

    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')
    for line in data:
        csv_writer.writerow(line)
    out_file.close()




def main():
    listname = ['kao','bimo']
    elem = [0] * 81
    elem[20] = 1
    elem[25] = 1
    elem[40] = 1
    elem[60] = 1

    main_detection(listname, elem)


if __name__ == '__main__':
    main()
