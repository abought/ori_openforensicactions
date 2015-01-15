"""
Apply an ORI gradient to the provided image
"""
__author__ = 'abought'

import argparse

from matplotlib import pyplot as plt
from scipy import misc

from ori_gradients import low_cycle, mid_cycle, high_cycle


def command_line():
    known_gradients = set(low_cycle.ALL_GRADIENTS +
                          mid_cycle.ALL_GRADIENTS +
                          high_cycle.ALL_GRADIENTS)

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to the file of interest")
    parser.add_argument("--lut",
                        default="Custom_21",
                        choices=known_gradients)
    return parser.parse_args()


def main(img_fn, lut_name):
    img_data = misc.imread(img_fn, flatten=True)  # greyscale
    plt.imshow(img_data, cmap=plt.get_cmap(lut_name))
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    parsed_args = command_line()
    main(parsed_args.filename, parsed_args.lut)

