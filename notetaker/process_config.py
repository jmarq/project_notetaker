import os

def map_lines(line):
    """ used while parsing config file, splits each line and does a little formatting """
    result = line.split(";")
    result[0] = os.path.expanduser(result[0])
    result[1] = result[1].strip()
    return result

def parseConfigFile(config_filename):
    """ returns a list of file_path/project description pairs, based on what is found in the config_filename file """
    fi = open(config_filename)
    lines = fi.read().strip().split("\n")
    lines = filter(lambda(d):d and d[0]!="#",lines)
    results = map(map_lines, lines)
    return results

