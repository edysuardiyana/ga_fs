import eves
import source_reader as src

def main_detection(listname):

    for name in listname:
        #chest
        #read data
        x_c, y_c, z_c, ann_c = read_seq(name,"chest")


        #waist
        x_w, y_w, z_w, ann_w = read_seq(name,"waist")


        #thigh






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
