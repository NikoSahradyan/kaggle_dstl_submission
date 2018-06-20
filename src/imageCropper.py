import os
import cv2
import csv
import numpy as np
import sys
from PIL import Image
#import Image
#img = cv2.imread("test.jpg")

gridSizesFile = "/Users/new/Desktop/TestAugment/AugmentationTool/grid_sizes.csv"
with open(gridSizesFile , 'a') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE)
    writer.writerow(["ImageId Xmax Ymin"])

train_wkt_v4 = "/Users/new/Desktop/TestAugment/AugmentationTool/train_wkt_v4.csv"
with open(train_wkt_v4 , 'a') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE)
    writer.writerow(["ImageId Data"])

img = Image.open('justSave.tiff')
#height, width, channels = img.shape
width, height = img.size
sample_width = 112
sample_height = 112
croppedX = 0
croppedY = 0
print(height)
print(width)
currentImage = 1
while height > croppedY + sample_height:
    while width > croppedX + sample_width:
        ImageName = "cropped" + str(croppedX+sample_width) + "_" + str(croppedY)
        currentImage += 1
        with open(gridSizesFile, 'a') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONE)
            temp = [ImageName + " " + str(croppedX + sample_width) + " " + str(croppedY)]
            writer.writerow(temp)
        crop_img = img.crop((croppedX, croppedY, croppedX+sample_width, croppedY+sample_height))
        #crop_img = img[croppedY:croppedY+32, croppedX:croppedX+32]
        name = os.path.join("/Users/new/Desktop/TestAugment/AugmentationTool/cropped/") + ImageName + ".jpg"
        #print(name)
        #crop_img.save(name)
        #cv2.imwrite(name, crop_img)

        #img_file = Image.open(name)
        format = crop_img.format
        mode = crop_img.mode
        
        # Make image Greyscale
        
        img_grey = crop_img.convert('L')
        # Save Greyscale values
        value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        with open(train_wkt_v4 , 'a') as f:
            writer = csv.writer(f)
            writerTemp = csv.writer(f, quoting=csv.QUOTE_NONE)
            writerTemp.writerow([ImageName])
            writer.writerow(value)
        croppedX+=sample_width
        
    croppedX = 0
    croppedY += sample_height
