# drawing bounding boxes to visualize labeled imagenet images

import ast

from bs4 import BeautifulSoup
from PIL import Image, ImageDraw

with open("imagenet_label_to_wordnet_synset.txt", "r") as f:
    data = ast.literal_eval(f.read())
    id_to_label = {v["id"]: v["label"] for v in data.values()}

for img_name in ["baby", "dog", "skiers", "snake", "soup"]:

    with open(f"imagenet_sample/{img_name}.xml" ) as xml:
        contents = xml.read()
    soup = BeautifulSoup(contents, "xml")
    objects = soup.find_all("object")

    with Image.open(f"imagenet_sample/{img_name}.JPEG") as img:
        draw = ImageDraw.Draw(img)
        for obj in objects:
            xmin = int(obj.find("xmin").text)
            ymin = int(obj.find("ymin").text)
            xmax = int(obj.find("xmax").text)
            ymax = int(obj.find("ymax").text)

            label_id = obj.find("name").text[1:] + "-n"
            label = id_to_label.get(label_id, "unknown")

            print(xmin, ymin, xmax, ymax, label_id, label)

            draw.rectangle([(xmin,ymin), (xmax,ymax)], fill=None, outline="red", width=2)
            draw.text((xmin+5,ymin+5), label, fill="red", font_size=16)

        img.save(f"labeled_imgs/{img_name}.JPEG")
        img.show()
