
# coding: utf-8

# In[34]:


from __future__ import print_function

import os
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

    ol = Overlay("/home/xilinx/IPBitFile/matrixVector.bit")
    ipMatrixVector = ol.matrix_vector_0
    
    SIZE=8
    
    M = np.zeros((SIZE,SIZE), dtype=int)
    V_In = np.zeros(SIZE, dtype=int)
    V_Out = np.zeros(SIZE, dtype=int)
    
    for i in range(SIZE):
        V_In[i] = i;
        for j in range(SIZE):
            M[i][j] = i+j;
    

        
    for i in range(SIZE):
        for j in range(SIZE):
            ipMatrixVector.write(0x100 + (i*8+j)*4, int(M[i][j]))
            # print(str(i)+"\t"+str(j)+"\t"+str(int(M[i][j]))+"\t"+str(ipMatrixVector.read(0x100 + (i*8+j)*4)))
    for i in range(SIZE):
        ipMatrixVector.write(0x200 + i*4, int(V_In[i]))
        # print(str(V_In[i])+"\t"+str(ipMatrixVector.read(0x200 + i*4)))
        


    print("running Design Under Test\n")
    ipMatrixVector.write(0x000, 0x1)
    while (ipMatrixVector.read(0x000) & 0x4) == 0x0:
        continue
    
    for i in range(SIZE):
        V_Out[i]=ipMatrixVector.read(0x220 + i*4)

    # Print output
    fp = open("matrix_vector_base.out.dat", "w")
    print("Printing DFT Output:")
    for i in range(SIZE):
        print("{:>4d}".format(i),end='')
        print("\t",end='')
        print("{:d}".format(V_Out[i]), end='')
        print("\n")
        fp.write("{:>4d}".format(i))
        fp.write("\t")
        fp.write("{:d}".format(V_Out[i]))
        fp.write("\n")
    
    print("Comparing against output data")
    if (os.system('diff -w matrix_vector_base.out.dat out.matrix_vector.gold.dat')):
        print("*******************************************")
        print("FAIL: Output DOES NOT match the golden output")
        print("*******************************************")
    else:
        print("*******************************************")
        print("PASS: The output matches the golden output!")
        print("*******************************************")
    

