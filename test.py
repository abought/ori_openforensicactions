"""
Common actions related to loading and displaying image data
"""

__author__ = 'abought'

from scipy import misc
from matplotlib import pyplot as plt

IMAGE_SAMPLE = "sample/deposition/paper_fig1d_small.png"

img_data = misc.imread(IMAGE_SAMPLE, flatten=True)  # greyscale
plt.imshow(img_data, cmap=plt.cm.gray)
plt.axis('off')
plt.contour(img_data)
plt.show()
