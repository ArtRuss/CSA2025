import cv2
import sys
from labeling import labeling
import os

# get a list of all the file names from the imagenet folder
files_ = os.listdir("/Users/alliebritton/Desktop/csa summer/class challenges/image challenges/imagenet")

# get only the file names of the jpeg files
images_path = []
for file_ in files_:
    if file_[-4:] == "JPEG":
        images_path.append(file_)
print()
print(images_path)

for i in range(len(images_path)):
    image_name = images_path[i]

# load the image
image = cv2.imread("ILSVRC2012_val_00000001.JPEG")

# draw rectangle
cv2.rectangle(image, (111,108), (441, 193), (0, 0, 255), 3)

# add the text
font = cv2.FONT_HERSHEY_SIMPLEX

# call the function to get the name of the animal
animal_id = input("What's the animal ID: ")
animal_name = labeling(animal_id)

# add the text to the image (label)
cv2.putText(image, animal_name,(111, 100), font, 1.2,(255,255,255),2)

# show image
cv2.imshow("snake", image)
cv2.waitKey(5000)
cv2.destroyAllWindows()


