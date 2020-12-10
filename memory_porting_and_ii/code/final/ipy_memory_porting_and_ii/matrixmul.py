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

    ol = Overlay("/home/xilinx/IPBitFile/matrixmul.bit")
    regIP = ol.matrixmul_0
    
    in_mat_a = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=int)
    in_mat_b = np.array([[1, 1, 1], [0, 1, 1], [0, 0, 1]], dtype=int)
    hw_result = np.zeros((3,3), dtype=int)
    sw_result = np.zeros((3,3), dtype=int)
    err_cnt = 0

    MAT_A_ROWS = 3
    MAT_A_COLS = 3
    MAT_B_ROWS = 3
    MAT_B_COLS = 3
    for i in range(MAT_A_ROWS):
        for j in range(MAT_B_COLS):
            for k in range(MAT_B_ROWS):
                sw_result[i][j] += in_mat_a[i][k] * in_mat_b[k][j]

    for i in range(MAT_A_ROWS):
        for j in range(MAT_B_COLS):
            regIP.write(0x10 + (i*3+j)*8, int(in_mat_a[i][j]))
            regIP.write(0x58 + (i*3+j)*8, int(in_mat_b[i][j]))
    
    regIP.write(0x00, 0x01)
    for i in range(MAT_A_ROWS):
        for j in range(MAT_B_COLS):
            hw_result[i][j] = regIP.read(0xa0 + (i*3+j)*8)
    
    print("{\n")
    for i in range(MAT_A_ROWS):
        print("{\n")
        for j in range(MAT_B_COLS):
            printf(str(hw_result[i][j]))
            if (hw_result[i][j] != sw_result[i][j]):
                err_cnt += 1
                print("*")
            if (j == MAT_B_COLS-1):
                print("}\n")
            else:
                print(",")
    print("}\n")

    if (err_cnt > 0):
        print("ERROR: " + str(err_cnt) + " mismatches detected!\n")
    else:
        print("Test passes.\n")
