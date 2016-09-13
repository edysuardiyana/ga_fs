import ConfigParser

def configParser(section):

    Config = ConfigParser.ConfigParser()
    Config.read('/Users/ArseneLupin/Documents/edy/ga_fs/src/path.ini')
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

def read_num_pop():
    num_of_pop = int(configParser("DataPath")['pop_size'])
    return num_of_pop

def read_gen_size():
    num_of_gen = int(configParser("DataPath")['gen_size'])
    return num_of_gen

def read_p_mutate():
    mutation_rate = float(configParser("DataPath")['p_mutate'])
    return mutation_rate

def read_p_cover():
    cover_rate = float(configParser("DataPath")['p_cover'])
    return cover_rate

def read_num_position():
    pos = configParser("DataPath")['position']
    num_pos = pos.split(",")
    return len(num_pos)

def read_temp_fscore():
    path = configParser("DataPath")['result_temp']
    source_path = path + "result.csv"
    return source_path
