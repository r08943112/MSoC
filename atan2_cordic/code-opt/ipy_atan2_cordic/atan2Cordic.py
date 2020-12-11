from __future__ import print_function

import sys
import numpy as np

sys.path.append('/home/xilinx')
from pynq import Overlay

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/atan2Cordic.bit")
    regIP = ol.top_atan2_0

    inp_y = np.array([-15,-15,-7,-7,-35,-35,-42,-42,-84,-84], dtype=int)
    inp_x = np.array([-14,-14,34,34,-42,-42,-32,-32,74,74], dtype=int)
    ref_res = np.array([-2.3217253685,-2.3217253685,-0.2030452192,-0.2030452192,-2.4468543530,-2.4468543530,-2.2218730450,-2.2218730450,-0.8486049771,-0.8486049771], dtype=np.float32)
    
    total_error = 0
    for i in range(10):
        regIP.write(0x10, int(inp_y[i]))
        regIP.write(0x18, int(inp_x[i]))
        while (regIP.read(0x24) != 1):
            pass
        Res = regIP.read(0x20)
        diff = Res - ref_res[i]
        if (diff < 0):
            diff = 0 - diff
        total_error += diff
    print("total    error = " + str(total_error))
    print("relative error = " + str(total_error / 10))

    print("Exit process")
