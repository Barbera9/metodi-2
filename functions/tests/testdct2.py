import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dd2 import dct_2D,compute_D

f=np.array([[231, 32, 233, 161, 24, 71, 140, 245],
    [247, 40, 248, 245, 124, 204, 36, 107],
    [234, 202, 245, 167, 9, 217, 239, 173],
    [193, 190, 100, 167, 43, 180, 8, 70],
    [11, 24, 210, 177, 81, 243, 8, 112],
    [97, 195, 203, 47, 125, 114, 165, 181],
    [193, 70, 174, 167, 41, 30, 127, 245],
    [87, 149, 57, 192, 65, 129, 178, 228]], dtype=float)


c= dct_2D(f)

print( "DCT2 :")
#np.set_printoptions(precision=2, suppress=True)
np.set_printoptions(formatter={'float_kind':lambda x:f"{x:.2e}"})
print(c)
print("----------------------------------------------------")
print("----------------------------------------------------")
print("")

#Dct1d sulla prima riga
D=compute_D(8)
dct1_row1= D @ f[0,:]
print("DCT1 (1°riga): ")
print(dct1_row1)
