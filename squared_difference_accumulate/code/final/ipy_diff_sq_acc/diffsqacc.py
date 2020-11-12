
# coding: utf-8

# In[29]:


import random
import math
import numpy as np

from __future__ import print_function

import sys

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/diffsqacc.bit")
    regIP = ol.diff_sq_acc_0
    
    N = 10
    a = allocate(shape=(N,), dtype=np.int64)
    b = allocate(shape=(N,), dtype=np.int64)
    
    cnt = 0
    for i in range(10):
        res_ref = 0
        for j in range(N):
            x = int(round(random.random()*16384,0))
            y = int(round(random.random()*16384,0))
            a[j] = x
            b[j] = y
            diff = a[j] - b[j]
            diff2 = diff**2
            res_ref += diff2

        for j in range(int(N/2)):
            regIP.write(0x20 + j*4, int(a[2*j]+a[2*j+1]*2**16))
            regIP.write(0x40 + j*4, int(b[2*j]+b[2*j+1]*2**16))
        regIP.write(0x00, 0x01)
        res = regIP.read(0x60)
        print("got " + str(res) + " expected " + str(res_ref) + "\n")
        if (res != res_ref):
            cnt += 1

    if (cnt > 0):
        print("TEST FAILED: " + str(cnt) + " errors\n")
    else:
        print("TEST SUCCESS!\n")
        

