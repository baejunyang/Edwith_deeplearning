import numpy as np
import os
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

cwd = os.getcwd()
print (cwd)

def print_typeshape(img):
    print ("Type is %s" % (type(img)))
    print ("Shape is %s" % (img.shape,))

# Load
cat = imread(cwd + '/data/cat1.jpg')
print_typeshape(cat)

# Plot
plt.figure(0)
plt.imshow(cat)
plt.title("My favorite")
plt.show()

# Load
cat2 = imread(cwd + '/data/cat1.jpg').astype(np.float)
print_typeshape(cat2)