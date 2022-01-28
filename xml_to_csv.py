import glob
import xml.etree.ElementTree as ET
import pandas as pd
import os


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            value = ('data/' + root.find('filename').text,
                     int(member[5][0].text),
                     int(member[5][2].text),
                     int(member[5][1].text),
                     int(member[5][3].text),
                     member[0].text,
                     )
            xml_list.append(value)
    column_name = ['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


image_path = os.path.join(os.getcwd(), 'data/')
dataset_df = xml_to_csv(image_path)

print('Completed')

import skimage.io as io
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.patches as patches

# DIVIDIR DATASET
train_df, test_df = train_test_split(dataset_df, test_size=0.2, random_state=2)

# CREAR ARCHIVOS CSV
train_df.to_csv('annotations.csv', index=False, header=None)
test_df.to_csv('annotations_test.csv', index=False, header=None)

classes = set(['cell'])

with open('classes.csv', 'w') as f:
    for i, line in enumerate(sorted(classes)):
        f.write('{},{}\n'.format(line, i))
