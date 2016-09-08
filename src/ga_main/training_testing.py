from sklearn.linear_model import LogisticRegression
import statistics as stat
import source_reader as src


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

#def running_time_measure(elem,):

def accuracy_measure(elem, list_name):
    features = []
    f_score = []
    total_training_set = []
    total_class_training = []
    clf = LogisticRegression(C = 1e8)

    for name in list_name:
        for sub_name in list_name:
            if name == sub_name:
                testing_set, new_annot_testing, real_annot_testing = read_file(sub_name,elem)
            else:
                training_set, new_annot_training,_ = read_file(sub_name,elem)
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

    mean_fscore = stat.mean(f_score)
    return mean_fscore

def read_features(name,elem):
    path = src.combined_path(name)
    temp_data = [] #contains data
    new_annot = [] #contains new annotation, 1 for fall, and 0 for non -fall
    annot = [] #contains the original annotation, 2 for fall forward, 6 for fall backward, dll.
    with open(path) as obj:
        for line in obj:
            raw_split = line.split()
            converted_data = [float(i) for i in raw_split[:len(raw_split)]]
            selected = select_feature(converted_data[:len(converted_data)-1],elem)

            temp_data.append(selected)

            annot.append(converted_data[len(converted_data)-1])

            if converted_data[len(converted_data)-1] in FALL_SET:
                new_annot.append(1)
            else:
                new_annot.append(0)

    return temp_data


def select_feature(array, elem): #array is the collection of features, elem is individual
    temp_row = []
    for i in range(len(elem)):
        if elem[i] == 1:
            temp_row.append(array[i])

    return temp_row

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
