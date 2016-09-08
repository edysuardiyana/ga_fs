import eves
#import ga_fs.src.source_reader as src
import source_reader as src
import csv


FREQ_RATE = 100

def main_detection(listname, elem_pop): #elem pop is an individual

    for name in listname:
        #chest
        #read data
        x_c, y_c, z_c, a_c = read_seq(name,"chest")
        ins_c, runt_c = eves.eves_window(x_c, y_c, z_c, a_c, FREQ_RATE, elem_pop, "chest")
        write_result(name,"chest","instance",ins_c) #writing instances
        write_result(name,"chest", "runtime", runt_c) #writing run time


        #waist
        x_w, y_w, z_w, a_w = read_seq(name,"waist")
        ins_w, runt_w = eves.eves_window(x_w, y_w, z_w, a_w, FREQ_RATE, elem_pop, "waist")
        write_result(name,"waist","instance",ins_w) #writing instances
        write_result(name,"waist", "runtime", runt_w) #writing run time

        #thigh
        x_t, y_t, z_t, a_t = read_seq(name, "thigh")
        ins_t, runt_t = eves.eves_window(x_t, y_t, z_t, a_t, FREQ_RATE, elem_pop, "thigh")
        write_result(name,"thigh","instance",ins_t) #writing instances
        write_result(name,"thigh", "runtime", runt_t) #writing run time






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
    elem[25] = 1
    elem[40] = 1
    main_detection(listname, elem)


if __name__ == '__main__':
    main()
