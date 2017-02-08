import ConfigParser
import os

def configParser(section):
    script_dir = os.path.dirname(__file__)
    real_path = os.path.join(script_dir,'path.ini')
    Config = ConfigParser.ConfigParser()
    Config.read(real_path)
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def listname_path():
    path = configParser("DataPath")['list_name']
    return path

def raw_source(name,position):
    config_address = position+"_data"
    path = configParser("DataPath")[config_address]
    source_path = path + str(name) + ".csv"
    return source_path

def runtime_path(name,position):
    address = position + "_time"
    path = configParser("DataPath")[address]
    source_path = path + name + ".csv"
    return source_path

def feat_path(name, position):
    address = position + "_feat"
    path = configParser("DataPath")[address]
    source_path = path + name + ".csv"
    return source_path

def combined_path(name):
    path = configParser("DataPath")['combined_feat']
    source_path = path + str(name) + ".csv"
    return source_path

def read_init_size():
    path = configParser("DataPath")['init_pop_size']
    init_array = path.split(",")
    fin_array = [int(i) for i in init_array[:len(init_array)]]
    return fin_array

def read_gen_size():
    num_of_gen = int(configParser("DataPath")['individual_size'])
    return num_of_gen

def read_tot_gen():
    tot_gen = configParser("DataPath")['tot_gen']
    new_tot = tot_gen.split(",")
    fin_array = [int(i) for i in new_tot[:len(new_tot)]]
    return fin_array

def read_p_mutate():
    mutation_rate = float(configParser("DataPath")['p_mutate'])
    return mutation_rate

def read_p_cover():
    cover_rate = float(configParser("DataPath")['p_cover'])
    return cover_rate

def read_num_position():
    pos = configParser("DataPath")['position']
    num_pos = pos.split(",")
    return num_pos

def read_temp_fscore(exp,init):
    path = configParser("DataPath")['result_temp']
    source_path = path +"init" + str(init)+ "_" + "result_gen_" + str(exp) +".csv"
    return source_path

def read_num_of_exp():
    num = int(configParser("DataPath")["num_of_exp"])
    return num
