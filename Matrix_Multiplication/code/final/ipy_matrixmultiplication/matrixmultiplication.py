
# coding: utf-8

# In[21]:


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

    ol = Overlay("/home/xilinx/IPBitFile/matrixmultiplication.bit")
    ipMatrixmul = ol.matrixmul_0

    N = 32
    M = 32
    P = 32

    A = np.zeros((N,M), dtype=int)
    B = np.zeros((N,M), dtype=int)
    AB = np.zeros((N,M), dtype=int)
    
    for i in range(N):
        for j in range (M):
            A[i][j] = i+j

    for i in range(M):
        for j in range(P):
            B[i][j] = i+j;

    for i in range(N):
        for j in range(M):
            ipMatrixmul.write(0x1000 + i*128 + j*4, int(A[i][j]))
    for i in range(N):
        for j in range(M):
            ipMatrixmul.write(0x2000 + i*128 + j*4, int(B[i][j]))        

    print("running Design Under Test\n")
    ipMatrixmul.write(0x00, 0x01)
    
    for i in range(N):
        for j in range(M):
            AB[i][j]=ipMatrixmul.read(0x3000 + i*128 + j*4)

    # Print output
    fp = open("matrixmultiplication.out.dat", "w")
    print("Output:")
    for i in range(N):
        print(str(i)+"\t ", end='')
        for j in range(P):
            print(str(AB[i][j])+" ", end='')
            fp.write("{:>4d}".format(i))
            fp.write("\t")
            fp.write("{:>4d}".format(j))
            fp.write("\t")
            fp.write("{:d}".format(AB[i][j]))
            fp.write("\t")
            fp.write("\n")
        print("\n")
    
    print("Comparing against output data")
    if (os.system('diff -w matrixmultiplication.out.dat matrixmultiplication.gold.dat')):
        print("*******************************************")
        print("FAIL: Output DOES NOT match the golden output")
        print("*******************************************")
    else:
        print("*******************************************")
        print("PASS: The output matches the golden output!")
        print("*******************************************")
    

