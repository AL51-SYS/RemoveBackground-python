# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt


################################################################
import sys 
imread_ = str(sys.argv[1])
print(imread_)
################################################################

image_bgr = cv2.imread(imread_)

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# get dimensions of image
dimensions = image_bgr.shape
 
# height, width, number of channels in image
height = image_bgr.shape[0]
width = image_bgr.shape[1]

# Rectange values: start x, start y, width, height
rectangle = (0, 0, height, width)


# Create initial mask
mask = np.zeros(image_rgb.shape[:2], np.uint8)

# Create temporary arrays used by grabCut
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Run grabCut
cv2.grabCut(image_rgb, # Our image
            mask, # The Mask 
            rectangle,# Our rectangle
            bgdModel, # Temporary array for background
            fgdModel, # Temporary array for background
            5, # Number of iterations
            cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle

# Create mask where sure and likely backgrounds set to 0, otherwise 1
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

# Multiply image with new mask to subtract background
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]

# Show image
plt.imshow(image_rgb_nobg), plt.axis("off")
plt.show()