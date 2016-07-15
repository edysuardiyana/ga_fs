import csv
import source_reader as sc

def combined_features(list_name):
    combined_path = src.combined_path()
    combined_data = []
    chest_temp = []
    waist_temp = []
    thigh_temp = []
    com_temp = []
    count_chest = 0
    count_waist = 0
    count_thigh = 0

    ct_t = []
    wt_t = []
    tt_t = []
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

        while count_chest < chest_temp:
            if count_chest == 0:
                annot_ct = chest_temp[len(chest_temp)-1]
                annot_wt = waist_temp[len(waist_temp)-1]
                annot_tt = thigh_temp[len(thigh_temp)-1]
                count_chest += 1



            elif
