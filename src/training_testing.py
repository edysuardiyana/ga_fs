from sklearn.linear_model import LogisticRegression
import statistics as stat
import source_reader as src
import csv

FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])


def accuracy_measure(list_name):
    features = []
    f_score = []
    total_training_set = []
    total_class_training = []
    clf = LogisticRegression(C = 1e8)

    for name in list_name:
        for sub_name in list_name:
            if name == sub_name:
                testing_set, new_annot_testing, real_annot_testing = read_file(sub_name)
            else:
                training_set, new_annot_training,_ = read_file(sub_name)
                for i in range(len(training_set)):
                    total_training_set.append(training_set[i])
                    total_class_training.append(new_annot_training[i])

        clf = clf.fit(total_training_set, total_class_training)
        prediction_val = clf.predict(testing_set)
        TP, FP, TN, FN = calc_metrics(prediction_val,new_annot_testing, real_annot_testing, name)

        Prec = float(TP)/(TP+FP) * 100
        Rec = float(TP)/(TP + FN) * 100
        F_val = float((2*TP))/((2*TP)+FP+FN) * 100

        total_training_set = []
        total_class_training = []

        f_score.append(F_val)
    write_fscore(list_name, f_score)
    mean_fscore = stat.mean(f_score)
    return mean_fscore

def read_file(name):
    path = src.combined_path(name)

    data = []
    class_flag = []
    annot = []

    with open(path) as accel:
        for line in accel:
            raw_data = line.split()
            ori_data = [float(i) for i in raw_data[:len(raw_data)]]
            #ori_data = [round(k,4) for k in ori_data_pre[:len(ori_data_pre)]]
            data.append(ori_data[0:len(ori_data)-1])
            if (ori_data[len(ori_data)-1]) in FALL_SET:
                class_flag.append(1) #last element , 1 for fall, 0 for non-fall
            else:
                class_flag.append(0)
            annot.append(ori_data[len(ori_data)-1])  # annot: 1 = standing, 2= fall forward, etc.. etc
    
    return data, class_flag, annot


def write_fscore(listname, f_list):
    path = src.read_temp_fscore()
    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')
    for i in range(len(listname)):
        write_line = [listname[i],f_list[i]]
        csv_writer.writerow(write_line)
    out_file.close()

def calc_metrics(prediction_val, class_testing, annot_testing, name):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    Prec = 0
    Rec = 0
    Fscore = 0
    Spec = 0
    temp_val = []
    temp_annot = 0
    for i in range(len(prediction_val)):
        if not temp_val:
            temp_annot = annot_testing[i]
            temp_val.append([prediction_val[i], class_testing[i]])
        else:
            if temp_annot == annot_testing[i]:
                temp_val.append([prediction_val[i], class_testing[i]])
            else:
                result = check_metrics(temp_val)
                if result == 1:
                    TP = TP + 1
                elif result == 2:
                    FP = FP + 1
                elif result == 3:
                    TN = TN + 1
                else:
                    FN = FN + 1

                del temp_val[:]
                temp_annot = annot_testing[i]
                temp_val.append([prediction_val[i], class_testing[i]])

    if temp_val:
        result = check_metrics(temp_val)
        if result == 1:
            TP = TP+1
        elif result == 2:
            FP = FP + 1
        elif result == 3:
            TN = TN + 1
        else:
            FN = FN + 1
    return TP, FP, TN, FN

def check_metrics(data_array):
    temp_val = []
    for i in range(len(data_array)):
        raw = data_array[i]
        val = accuracy_check(raw[0], raw[1])
        temp_val.append(val)
    final_result = min(temp_val)
    return final_result

def accuracy_check(final_detec_flag, annot):
    result = 0
    if annot == 1 and final_detec_flag == 1:
        #true positive
        result = 1
    elif annot == 0  and final_detec_flag == 1:
        #false positive
        result = 2
    elif annot == 0 and final_detec_flag == 0:
        #true negative
        result = 3
    else: #in Fall Set and not final_detec_flag
        #false negative
        result = 4
    return result
