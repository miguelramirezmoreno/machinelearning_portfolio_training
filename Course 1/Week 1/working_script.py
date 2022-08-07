#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is version 1.0 of my script for linear regression gradient descent.

Requires: numpy,

Data requirement:
    
    1-Place the script int the same folder than the data to be loaded

@author: Miguel Ramirez Moreno
"""
%reset
import numpy as np;
import matplotlib.pyplot as plt;
data= np.loadtxt("./ex1data1.txt", delimiter = ",");
#next: assign variables. First colum is city population, 
#and second column is profit of food trucks in those cities.

import pandas as pd
data3= pd.read_csv('./ex1data1.txt',delimiter = ",", names=('city_population', 'profit'))
plt.plot(x-train,y-train);
plt.xlabel('City Population');
plt.ylabel('Y-axis');
plt.title("Data");
plt.show()vv