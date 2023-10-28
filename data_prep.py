### Importing libraries
import pandas as pd
from tqdm import tqdm
from PIL import Image
import os

df = pd.read_csv('data/list_bbox_celeba.csv')

with open('paths.txt', 'r') as plik:
    data_path = plik.readline()

raw_folder = 'img_celeba'
finall_folder = 'img_celeba_extended'

if not os.path.exists(os.path.join(data_path, finall_folder)):
    os.makedirs(os.path.join(data_path, finall_folder))

for i in tqdm(range(len(df))):
    
    raw_path = os.path.join(data_path, raw_folder, df.iloc[i, 0])
    finall_path = os.path.join(data_path, finall_folder, df.iloc[i, 0])
    temp_img = Image.open(raw_path)
    width, height = temp_img.size

    if width < 512 and height < 512:

        padding = (0,0)
        expanded_image = Image.new('RGB', (512, 512), (0, 0, 0))
        expanded_image.paste(temp_img,padding)

        if not os.path.exists(os.path.join(data_path, finall_folder, df.iloc[i, 0])):
            expanded_image.save(os.path.join(data_path, finall_folder, df.iloc[i, 0]))

    else:
        pass
