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

    ol = Overlay("/home/xilinx/IPBitFile/dataflow_stable_content.bit")
    ipFilter = ol.example_0
    ipDMAIn1 = ol.axi_dma_0
    ipDMAIn2 = ol.axi_dma_1
    ipDMAOut = ol.axi_dma_2

    numSamples = 32
    inBuffer0 = allocate(shape=(numSamples,), dtype=np.int32)
    inBuffer1 = allocate(shape=(numSamples,), dtype=np.int32)
    outBuffer0 = allocate(shape=(numSamples,), dtype=np.int32)

    # a = 1, b = 7
    # a = 4, b = 0
    # a = 9, b = 4
    # a = 8, b = 8
    # a = 2, b = 4
    # a = 5, b = 5
    # a = 1, b = 7
    # a = 1, b = 1
    # a = 5, b = 2
    # a = 7, b = 6
    # sum = 30
    inBuffer0[0] = 1 
    inBuffer0[1] = 4
    inBuffer0[2] = 9
    inBuffer0[3] = 8
    inBuffer0[4] = 2
    inBuffer0[5] = 5
    inBuffer0[6] = 1
    inBuffer0[7] = 1
    inBuffer0[8] = 5
    inBuffer0[9] = 7
    inBuffer1[0] = 7
    inBuffer1[1] = 0
    inBuffer1[2] = 4
    inBuffer1[3] = 8
    inBuffer1[4] = 4
    inBuffer1[5] = 5
    inBuffer1[6] = 7
    inBuffer1[7] = 1
    inBuffer1[8] = 2
    inBuffer1[9] = 6

    ipFilter.write(0x00, 0x01)
    ipDMAIn1.sendchannel.transfer(inBuffer0)
    ipDMAIn2.sendchannel.transfer(inBuffer1)
    ipDMAOut.recvchannel.transfer(outBuffer0)
    ipDMAIn1.sendchannel.wait()
    ipDMAIn2.sendchannel.wait()
    ipDMAOut.recvchannel.wait()
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    
    # Check DUT vs reference result
    if (outBuffer0[0] == 30):
        print("*** TEST PASSED ***")
    else:
        print("!!! TEST FAILED - mismatches detected !!!")

    print("============================")
    print("Exit process")
