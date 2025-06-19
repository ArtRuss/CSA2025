import cv2
import sys
from labeling import label_name, label_id
import os

# get a list of all the file names from the imagenet folder
files_ = os.listdir("/Users/alliebritton/Desktop/csa summer/class challenges/image challenges/imagenet")

# make a list only wiht the XML files
xml_path = []
for file_ in files_:
    if file_[-3:] == "xml":
        xml_path.append(file_)
xml_path = sorted(xml_path)
#print(xml_path)

# make a list only with the JPEG files
images_path = []
for file_ in files_:
    if file_[-4:] == "JPEG":
        images_path.append(file_)
images_path = sorted(images_path)
#print(images_path)

# display all of the images with the labels as a loop
for i in range(len(images_path)):
    image_name = images_path[i]
    xml_name = xml_path[i]

    # load the image
    image = cv2.imread(image_name)

    # add the text
    font = cv2.FONT_HERSHEY_SIMPLEX

    # call the function to get the name of the animal
    animal_id, xmin, ymin, xmax, ymax = label_id(xml_name)
    animal_name = label_name(animal_id)

    # draw rectangle
    cv2.rectangle(image, (xmin,ymin), (xmax, ymax), (0, 0, 255), 3)

    # add the text to the image (label)
    cv2.putText(image, animal_name,(111, ymin-10), font, 1.2,(255,255,255),2)

    # show image
    cv2.imshow("snake", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


