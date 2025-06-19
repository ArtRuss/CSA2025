import ast
import xml.etree.ElementTree as ET

def label_name(label_id):
    '''This function uses the id to get the text name of the image from the txt file'''
    with open("codes/imagenet_label_to_wordnet_synset.txt") as file_name:
        labels_str = file_name.read() # extract the data from txt into a string
        labels_dict = ast.literal_eval(labels_str) # convert the string into a dictionary

    id = label_id
    clean_id = id.text.replace("n", "")

    # go through the dictionary to look for the specific lable
    for item in labels_dict.values():
        if clean_id in item["id"]:
            animal_name = item["label"]
            print("The animal is a(n):", item["label"], "\n")

    return animal_name

def label_id(file):
    '''This image gets the id and the points from the xml file'''
    
    # load the XML file
    xml_file = file
    tree = ET.parse(xml_file)  

    # get the root element
    root = tree.getroot()

    # find the <name> element in the root's tree for the ID of the object
    id = root.find(".//name")
    print("The ID is:", id.text)

    # find the xmin, xmax, ymin, ymax to get the points of the rectangle
    xmin = int(root.find(".//xmin").text)
    ymin = int(root.find(".//ymin").text)
    xmax = int(root.find(".//xmax").text)
    ymax = int(root.find(".//ymax").text)

    return(id, xmin, ymin, xmax, ymax)








