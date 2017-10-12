import os
import sys
import xml.etree.ElementTree as ET

def stat_xmls(dire):
    '''
    This function stat xml files
    '''
    pathlist = search_xml(dire)
    all_num_benign = 0
    all_num_malignant = 0
    num_benign_file = 0
    num_malignant_file = 0
    for path, name in pathlist:
        num_benign, num_malignant = parse_xml(path, name)
        print("\t\t%s\tbenign: %d, malignant: %d" % (name, num_benign, num_malignant))
        if num_benign != 0 and num_malignant == 0:
            num_benign_file += 1
        elif num_benign == 0 and num_malignant != 0:
            num_malignant_file += 1
                   
        all_num_benign += num_benign
        all_num_malignant += num_malignant

    print('Number of Files          benign: %d, malignant: %d, total: %d' % (num_benign_file, num_malignant_file, num_benign_file + num_malignant_file))
    print('All Number of Objects    benign: %d, malignant: %d, total: %d' % (all_num_benign, all_num_malignant, all_num_benign + all_num_malignant))


def search_xml(dirname):
    '''
    This function finds xml files within input directory.
    '''
    pathlist = list()

    for (path, _, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.xml':
                path = path.replace("\\", "/")
                pathlist.append((path, filename))

    return pathlist


def parse_xml(path, name):
    xml = ET.parse(path+"/"+name)
    num_benign = 0
    num_malignant = 0
    for obj in xml.findall(".//object"):
        if obj.find("name").text == "Benign":
            num_benign += 1
        elif obj.find("name").text == "Malignant":
            num_malignant += 1

    return (num_benign, num_malignant)


if __name__ == '__main__':
    DIR_OF_XMLS = sys.argv[1]
    stat_xmls(DIR_OF_XMLS)
