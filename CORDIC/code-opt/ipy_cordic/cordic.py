
# coding: utf-8

# In[10]:


from __future__ import print_function

import sys
import numpy as np
from time import time
import matplotlib.pyplot as plt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate
import math

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/CORDIC.bit")
    ipCORDIC = ol.cordic_0

    s=0.0 # sine
    c=0.0 # cos
    radian=0.0 # radian versuin of degree

    # zs=sin, zc=cos using math.h in VivadoHLS
    zs=0.0 # sine and cos values calculated from math.
    zc=0.0 # sine and cos values calculated from math.

    # Error checking
    Total_Error_Sin=0.0
    Total_error_Cos=0.0
    error_sin=0.0
    error_cos=0.0

    M_PI=3.1415926536897932384626
    NUM_DEGREE=90

    for i in range(1, NUM_DEGREE):
        radian = i*M_PI/180
        radian = round(radian, 3)
        # print(radian)
        radian_I = int(radian)
        # print(radian_I)
        radian_B = (radian - radian_I) * 1000
        # print(radian_B)
        radian = radian_I*(2**10) + radian_B
        ipCORDIC.write(0x10, int(radian))
        ipCORDIC.write(0x00, 0x1)
        while (ipCORDIC.read(0x00) & 0x4) == 0x0:
            continue
        radian = ipCORDIC.read(0x18)
        radian_I = int(radian/1024)
        radian_B = (radian - radian_I*1024)/1000
        radian = radian_I + radian_B
        s = ipCORDIC.read(0x20)
        s_I = int(s/1024)
        s_B = (s - s_I*1024)/1000
        s = s_I + s_B
        c = ipCORDIC.read(0x28)
        c_I = int(c/1024)
        c_B = (c - c_I*1024)/1000
        c = c_I + c_B
        zs = math.sin(float(radian))
        zc = math.cos(float(radian))
        error_sin = (abs(float(s)-zs)/zs)*100.0
        error_cos = (abs(float(c)-zc)/zc)*100.0
        Total_Error_Sin += error_sin
        Total_error_Cos += error_cos

    print("Total_Error_Sin="+str(Total_Error_Sin)+", Total_error_Cos="+str(Total_error_Cos))
    print("============================")
    print("Exit process")

