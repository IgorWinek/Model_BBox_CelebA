# Model_BBox_CelebA

This is a model based on CNN and more specifically VGG16 which is designed to show the bounding box of the face

Below is a brief description of how to go step-by-step through the entire script I created 

## 1. Data preparation
The data is too large to upload to the github repository so you have to prepare it individually on your own. Below are instuctions on how to do it

1.1. Prepare the Data folder on your computer

1.2. Download the data located at the given address https://drive.google.com/drive/folders/0B7EVK8r0v71pTUZsaXdaSnZBZzg?resourcekey=0-rJlzl934LzC-Xp28GeIBzQ. Download the exact data called img_celeba.7z

1.3. Unzip the data as shown in the instuction on google drive

1.4. Move the img_celeba folder to the previously created Data folder

1.5. Put the path to the images folder into a path.txt file, for example, like this C:Users\Desktop\Data\CelebA

1.6. Run the script data_prep.py which will create the folder img_celeba_extended in the Data folder. This will ensure that too much data will not be used for training and, in addition, images will be standardized to 512px / 512px

