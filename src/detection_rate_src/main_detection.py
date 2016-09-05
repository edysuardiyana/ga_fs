import eves
import source_reader as src


FREQ_RATE = 100

def main_detection(listname, elem_pop):

    for name in listname:
        #chest
        #read data
        x_c, y_c, z_c, a_c = read_seq(name,"chest")
        ins_c, runt_c = eves.eves_window(x_c, y_c, z_c, a_c, FREQ_RATE, elem_pop, "chest")


        #waist
        x_w, y_w, z_w, a_w = read_seq(name,"waist")
        ins_w, runt_w = eves.eves_window(x_w, y_w, z_w, a_w, FREQ_RATE, elem_pop, "waist")


        #thigh
        x_t, y_t, z_t, a_t = read_seq(name, "thigh")
        ins_t, runt_t = eves.eves_window(x_t, y_t, z_t, a_t, FREQ_RATE, elem_pop, "thigh")





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


def write_feat(name,position)
