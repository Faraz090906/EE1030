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

#Given points
A = np.array(([3, 4])).reshape(-1,1) 
B = np.array(([6, 7])).reshape(-1,1)  
C = np.array(([9, 10])).reshape(-1,1)  

# Print rank 
rank = LA.matrix_rank(np.block([B-A, C-A]))
print(f"Rank is {rank}, which means it has a zero row")



