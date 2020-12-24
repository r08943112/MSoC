
# coding: utf-8

# In[1]:


from __future__ import print_function

import sys
import numpy as np
from time import time
import matplotlib.pyplot as plt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/FIR.bit")
    ipFIRN = ol.fir_0

    SIZE = 256

    numTaps = 16
    taps = [1, 2, 0, -3, 0, 4, -5, 0, 1, -2, 0, -3, 0, 4, -5, 0]
    taps0 = allocate(shape=(numTaps,), dtype=np.int32)
    out = allocate(shape=(1,), dtype=np.int32)
    for i in range(numTaps):
        taps0[i] = taps[i]

#     out = 0
    for i in range(SIZE):
        ipFIRN.write(0x10, i)
        for j in range(numTaps):
            ipFIRN.write(0x40+j*4, int(taps0[j]))
        ipFIRN.write(0x00, 0x1)
    while ((ipFIRN.read(0x00)&0x02) != 0x02):
        continue
    out = ipFIRN.read(0x18)
#    print(out)
    
    if out == 4294965844:#2's complement value of -1452 = 1111111111111111111111111111111111111111111111111111_1010_0101_0100 = 4294965844
        print("TEST PASS!")
    else:
        print("TEST FAIL!")

    print("============================")
    print("Exit process")

