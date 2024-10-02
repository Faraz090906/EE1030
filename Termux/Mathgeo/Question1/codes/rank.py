#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Rank


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/faraz090906/Python/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


#if using termux
import subprocess
import shlex
#end if

# Load the points from the text file
points = np.loadtxt("points.dat", delimiter=',',max_rows=len(list(open("./points.dat")))-1)

# Extract the x and y coordinates
x = points[:, 0]
y = points[:, 1]

A = np.array([points[0,0],points[0,1]])
B = np.array([points[20,0],points[20,1]])
C = np.array([points[41,0],points[41,1]])  

# Print rank 
rank = LA.matrix_rank(np.block([B-A, C-A]))
print(f"Rank is {rank}, which means it has a zero row")



