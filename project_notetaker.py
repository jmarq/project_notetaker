

def parseConfigFile(config_filename):
    fi = open(config_filename)
    lines = fi.read().strip().split("\n")
    lines = filter(lambda(d):d and d[0]!="#",lines)
    results = {}
    for line in lines:
        file_path = description = ""
        split_line = line.split(";")
        #file_path = split_line[0]
        #description = split_line[1]
        file_path, description = split_line
        results[file_path] = description
    return results

print parseConfigFile("possible_conf_file.conf")

        
