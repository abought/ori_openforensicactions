"""
Code adapted from:
 http://matplotlib.org/examples/color/colormaps_reference.html
Copyright (c) 2012-2013 Matplotlib Development Team; All Rights Reserved

Reference for colormaps included with Matplotlib.

This renders a figure showing all colormaps made available in this package.
"""
__author__ = 'abought'

from matplotlib import pyplot as plt
import numpy as np

from ori_gradients import low_cycle, mid_cycle, high_cycle


cmaps = [("low_cycle", low_cycle.ALL_GRADIENTS),
         ("mid_cycle", mid_cycle.ALL_GRADIENTS),
         ("high_cycle", high_cycle.ALL_GRADIENTS)]

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)


def plot_color_gradients(plot_title, cmap_names_list):
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(plot_title + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_names_list):
        print "now plotting: ", name
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

for cmap_category, cmap_list in cmaps:
    plot_color_gradients(cmap_category, cmap_list)

plt.show()
