import ConfigParser

def configParser(section):

    Config = ConfigParser.ConfigParser()
    Config.read('/home/edysuardiyana/edy/git/ga_fs/src/path.ini')
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

def chest_path(name):
    path = configParser("DataPath")['chest_feat']
    source_path = path + str(name) + ".csv"
    return source_path

def waist_path(name):
    path = configParser("DataPath")['waist_feat']
    source_path = path + str(name) + ".csv"
    return source_path

def thigh_path(name):
    path = configParser("DataPath")['thigh_feat']
    source_path = path + str(name) + ".csv"
    return source_path

def combined_path(name):
    path = configParser("DataPath")['combined_feat']
    source_path = path + str(name) + ".csv"
    return source_path
