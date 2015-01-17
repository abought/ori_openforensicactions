"""
Auto-generated file: low-cycle gradients for recoloring image data

Adapted from http://ori.hhs.gov/advanced-forensic-actions
"""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

BlackWhite_data = {'blue': [(0.0, 0.032, 0.032), (1.0, 1.0, 1.0)],
                   'green': [(0.0, 0.031, 0.031), (1.0, 1.0, 1.0)],
                   'red': [(0.0, 0.025, 0.025), (1.0, 1.0, 1.0)]}
BlackWhite = LinearSegmentedColormap('BlackWhite', BlackWhite_data)
plt.register_cmap(cmap=BlackWhite)

low_2_data = {'blue': [(0.0, 1.0, 1.0),
                          (1.0, 0.0, 0.0)],
                 'green': [(0.0, 1.0, 1.0),
                           (1.0, 0.0, 0.0)],
                 'red': [(0.0, 0.0, 0.0),
                         (1.0, 0.0, 0.0)]}
low_2 = LinearSegmentedColormap('low_2', low_2_data)
plt.register_cmap(cmap=low_2)

low_3_data = {'blue': [(0.0, 0.0, 0.0),
                          (1.0, 0.0, 0.0)],
                 'green': [(0.0, 0.996, 0.996),
                           (1.0, 0.0, 0.0)],
                 'red': [(0.0, 0.0, 0.0),
                         (1.0, 0.0, 0.0)]}
low_3 = LinearSegmentedColormap('low_3', low_3_data)
plt.register_cmap(cmap=low_3)

ForegroundtoBackground_data = {'blue': [(0.0, 0.0, 0.0),
                                        (1.0, 0.0, 0.0)],
                               'green': [(0.0, 0.0, 0.0),
                                         (1.0, 0.0, 0.0)],
                               'red': [(0.0, 1.0, 1.0),
                                       (1.0, 0.012, 0.012)]}
ForegroundtoBackground = LinearSegmentedColormap('ForegroundtoBackground',
                                                 ForegroundtoBackground_data)
plt.register_cmap(cmap=ForegroundtoBackground)

low_5_data = {'blue': [(0.0, 1.0, 1.0),
                          (1.0, 1.0, 1.0)],
                 'green': [(0.0, 1.0, 1.0),
                           (1.0, 1.0, 1.0)],
                 'red': [(0.0, 0.0, 0.0),
                         (1.0, 1.0, 1.0)]}
low_5 = LinearSegmentedColormap('low_5', low_5_data)
plt.register_cmap(cmap=low_5)

low_6_data = {'blue': [(0.0, 1.0, 1.0),
                          (1.0, 1.0, 1.0)],
                 'green': [(0.0, 0.0, 0.0),
                           (1.0, 1.0, 1.0)],
                 'red': [(0.0, 0.0, 0.0),
                         (1.0, 1.0, 1.0)]}
low_6 = LinearSegmentedColormap('low_6', low_6_data)
plt.register_cmap(cmap=low_6)

low_7_data = {'blue': [(0.0, 0.0, 0.0),
                          (1.0, 0.0, 0.0)],
                 'green': [(0.0, 0.937, 0.937),
                           (1.0, 0.0, 0.0)],
                 'red': [(0.0, 0.996, 0.996),
                         (1.0, 0.0, 0.0)]}
low_7 = LinearSegmentedColormap('low_7', low_7_data)
plt.register_cmap(cmap=low_7)

low_8_data = {'blue': [(0.0, 0.0, 0.0),
                          (1.0, 1.0, 1.0)],
                 'green': [(0.0, 0.729, 0.729),
                           (1.0, 0.345, 0.345)],
                 'red': [(0.0, 1.0, 1.0),
                         (1.0, 0.0, 0.0)]}
low_8 = LinearSegmentedColormap('low_8', low_8_data)
plt.register_cmap(cmap=low_8)

OrangeBlue_data = {'blue': [(0.0, 0.0, 0.0),
                            (1.0, 0.455, 0.455)],
                   'green': [(0.0, 0.486, 0.486),
                             (1.0, 0.157, 0.157)],
                   'red': [(0.0, 0.992, 0.992),
                           (1.0, 0.0, 0.0)]}
OrangeBlue = LinearSegmentedColormap('OrangeBlue', OrangeBlue_data)
plt.register_cmap(cmap=OrangeBlue)

low_10_data = {'blue': [(0.0, 0.0, 0.0),
                           (1.0, 0.359, 0.359)],
                  'green': [(0.0, 0.902, 0.902),
                            (1.0, 0.463, 0.463)],
                  'red': [(0.0, 0.976, 0.976),
                          (1.0, 0.0, 0.0)]}
low_10 = LinearSegmentedColormap('low_10', low_10_data)
plt.register_cmap(cmap=low_10)

low_11_data = {'blue': [(0.0, 0.0, 0.0),
                           (1.0, 0.424, 0.424)],
                  'green': [(0.0, 0.988, 0.988),
                            (1.0, 0.082, 0.082)],
                  'red': [(0.0, 0.953, 0.953),
                          (1.0, 0.435, 0.435)]}
low_11 = LinearSegmentedColormap('low_11', low_11_data)
plt.register_cmap(cmap=low_11)

BlueVioletYellowOrange_data = {'blue': [(0.0, 0.349, 0.349),
                                        (1.0, 0.0, 0.0)],
                               'green': [(0.0, 0.039, 0.039),
                                         (1.0, 0.486, 0.486)],
                               'red': [(0.0, 0.161, 0.161),
                                       (1.0, 1.0, 1.0)]}
BlueVioletYellowOrange = LinearSegmentedColormap('BlueVioletYellowOrange',
                                                 BlueVioletYellowOrange_data)
plt.register_cmap(cmap=BlueVioletYellowOrange)

RedGreen_data = {'blue': [(0.0, 0.098, 0.098),
                          (1.0, 0.106, 0.106)],
                 'green': [(0.0, 0.0, 0.0),
                           (1.0, 0.376, 0.376)],
                 'red': [(0.0, 0.882, 0.882),
                         (1.0, 0.0, 0.0)]}
RedGreen = LinearSegmentedColormap('RedGreen', RedGreen_data)
plt.register_cmap(cmap=RedGreen)

low_15_data = {'blue':
                      [(0.0, 0.0, 0.0),
                       (0.484, 0.0, 0.0),
                       (1.0, 0.424, 0.424)],
                  'green': [(0.0, 0.0, 0.0),
                            (0.484, 0.988, 0.988),
                            (1.0, 0.082, 0.082)],
                  'red': [(0.0, 0.988, 0.988),
                          (0.484, 0.953, 0.953),
                          (1.0, 0.435, 0.435)]}
low_15 = LinearSegmentedColormap('low_15', low_15_data)
plt.register_cmap(cmap=low_15)

ALL_GRADIENTS = ['BlackWhite',
                 'low_2',
                 'low_3',
                 'ForegroundtoBackground',
                 'low_5',
                 'low_6',
                 'low_7',
                 'low_8',
                 'OrangeBlue',
                 'low_10',
                 'low_11',
                 'BlueVioletYellowOrange',
                 'RedGreen',
                 'low_15']

