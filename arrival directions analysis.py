import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import pandas as pd
from astropy import coordinates as coord
from astropy import units as u
from scipy.stats import kde
import os

location=os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
filename_data="Arrival_directions_8EeV_Science_2017.dat"
filename_source="Arrival Directions Source Weights ICRC 2019"

texture=1
p=1


plt.figure()
plt.subplot(111, projection="aitoff")
plt.grid(True)

columns_to_keep = ['dec', 'RA']
data = pd.read_table(os.path.join(location, filename_data), sep="\s+", usecols=columns_to_keep)
d_dec=data['dec'].values
d_RA=data['RA'].values
plt.plot((2*np.pi*d_RA/360)-np.pi, -np.pi*d_dec/180, '.', markersize=30, alpha=0.010)


'''
columns_to_keep = ['dec', 'RA']
source = pd.read_table(os.path.join(location, filename_source), sep="\s+", usecols=columns_to_keep)
s_dec=source['dec'].values
s_RA=source['RA'].values
plt.plot((2*np.pi*s_RA/360)-np.pi, -np.pi*s_dec/180, 'x', markersize=1, alpha=0.1, color='red')
'''


plt.show()
