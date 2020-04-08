import os
from os import walk
import csv
import xml.etree.ElementTree as ET

IMAGES_PATH = 'C:/Users/bitlg/PycharmProjects/object_detection/venv/main/images/'
TRAIN_IMAGES_PATH = 'C:/Users/bitlg/PycharmProjects/object_detection/venv/main/images/train'
TEST_IMAGES_PATH = 'C:/Users/bitlg/PycharmProjects/object_detection/venv/main/images/test'

train_images = {}
for (dirpath, dirnames, filenames) in walk(TRAIN_IMAGES_PATH):
    for filename in filenames:
        train_images[filename] = filename
    break

test_images = {}
for (dirpath, dirnames, filenames) in walk(TEST_IMAGES_PATH):
    for filename in filenames:
        test_images[filename] = filename
    break

with open('images.csv') as images:
    for row in csv.reader(images):
        image_name = row[0]
        xmin = row[1]
        ymin = row[2]
        width = row[3]
        height = row[4]
        xmax = int(xmin) + int(width)
        ymax = int(ymin) + int(height)
        if image_name in test_images:
            folder_name = 'test'
        else:
            folder_name = 'train'
        # create the file structure
        annotation = ET.Element('annotation')
        folder = ET.SubElement(annotation, 'folder')
        folder.text = folder_name
        filename = ET.SubElement(annotation, 'filename')
        filename.text = image_name
        path = ET.SubElement(annotation, 'path')
        path.text = IMAGES_PATH + folder_name + "/" + image_name
        source = ET.SubElement(annotation, 'source')
        database = ET.SubElement(source, 'database')
        database.text = 'Unknown'
        size = ET.SubElement(annotation, 'size')
        width = ET.SubElement(size, 'width')
        width.text = '1280'
        height = ET.SubElement(size, 'height')
        height.text = '720'
        depth = ET.SubElement(size, 'depth')
        depth.text = '3'
        segmented = ET.SubElement(annotation, 'segmented')
        segmented.text = '0'

        object = ET.SubElement(annotation, 'object')
        name = ET.SubElement(object, 'name')
        name.text = 'main road'
        pose = ET.SubElement(object, 'pose')
        pose.text = 'Unspecified'
        truncated = ET.SubElement(object, 'truncated')
        truncated.text = '0'
        difficult = ET.SubElement(object, 'difficult')
        difficult.text = '0'
        bndbox = ET.SubElement(object, 'bndbox')
        xminElem = ET.SubElement(bndbox, 'xmin')
        xminElem.text = str(xmin)
        ymimElem = ET.SubElement(bndbox, 'ymin')
        ymimElem.text = str(ymin)
        xmaxElem = ET.SubElement(bndbox, 'xmax')
        xmaxElem.text = str(xmax)
        ymaxElem = ET.SubElement(bndbox, 'ymax')
        ymaxElem.text = str(ymax)
        xmlData = ET.tostring(annotation, encoding='unicode')
        myfile = open(IMAGES_PATH + folder_name + '/' + image_name.rsplit('.jpg')[0] + '.xml', 'w')
        myfile.write(xmlData)
