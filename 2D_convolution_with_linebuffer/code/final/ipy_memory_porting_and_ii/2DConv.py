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

    ol = Overlay("/home/xilinx/IPBitFile/2DConv.bit")
    ipFilter = ol.filter11x11_strm_0
    ipDMAIn = ol.axi_dma_0
    ipDMAOut = ol.axi_dma_1

    TEST_IMG_ROWS = 135
    TEST_IMG_COLS = 240
    TEST_IMG_SIZE = TEST_IMG_ROWS * TEST_IMG_COLS

    src_img_strm = allocate(shape=(TEST_IMG_SIZE,), dtype=np.int32)
    dut_img_strm = allocate(shape=(TEST_IMG_SIZE,), dtype=np.int32)

    src_img = np.zeros(TEST_IMG_ROWS*TEST_IMG_COLS, dtype=np.int32)
    ref_img = np.zeros(TEST_IMG_ROWS*TEST_IMG_COLS, dtype=np.int32)
    chkr_size = 5
    max_pix_val = 255
    min_pix_val = 0
    err_cnt = 0
    ret_val = 20
    for i in range(TEST_IMG_ROWS):
        chkr_pair_val = np.zeros(2, dtype=np.int32)
        if (((i/chkr_size)%2)==0):
            chkr_pair_val[0] = max_pix_val
            chkr_pair_val[1] = min_pix_val
        else:
            chkr_pair_val[0] = min_pix_val
            chkr_pair_val[1] = max_pix_val
        for j in range(TEST_IMG_COLS):
            pix_val = chkr_pair_val[int(j/chkr_size)%2]
            src_img[i*TEST_IMG_COLS+j] = pix_val
            src_img_strm[i*TEST_IMG_COLS+j] = pix_val

    filt11_coeff = np.array([36, 111, 266, 498, 724, 821, 724, 498, 266, 111, 36])
    K = 11
    conv_size = K
    border_width = int(conv_size / 2);
    local = np.zeros(TEST_IMG_ROWS*TEST_IMG_COLS, dtype=np.int32)
    # width = COL =, height = ROW
    for i in range(TEST_IMG_ROWS*TEST_IMG_COLS):
        local[i] = 0
    for col in range(0, TEST_IMG_ROWS):
        for row in range(border_width, TEST_IMG_COLS - border_width):
            pixel = col*TEST_IMG_COLS + row
            for i in range(-border_width, border_width + 1):
                local[pixel] += src_img[pixel+i]*filt11_coeff[i+border_width]

    # width = COL =, height = ROW
    for i in range(TEST_IMG_ROWS*TEST_IMG_COLS):
        ref_img[i] = 0
    for col in range(border_width, TEST_IMG_ROWS - border_width):
        for row in range(0, TEST_IMG_COLS):
            pixel = col*TEST_IMG_COLS + row
            for i in range(-border_width, border_width + 1):
                offset = i * TEST_IMG_COLS
                ref_img[pixel] += local[pixel+offset]*filt11_coeff[i+border_width]

    border_width_offset = border_width * TEST_IMG_COLS
    border_height_offset = (TEST_IMG_ROWS - border_width - 1) * TEST_IMG_COLS
    for col in range(border_width):
        offset = col*TEST_IMG_COLS
        for row in range(border_width):
            pixel = offset + row
            ref_img[pixel] = ref_img[border_width_offset+border_width]
        for row in range(border_width, TEST_IMG_COLS-border_width):
            pixel = offset + row
            ref_img[pixel] = ref_img[border_width_offset+row]
        for row in range(TEST_IMG_COLS-border_width, TEST_IMG_COLS):
            pixel = offset + row
            ref_img[pixel] = ref_img[border_width_offset+TEST_IMG_COLS-border_width-1]
    for col in range(border_width, TEST_IMG_ROWS-border_width):
        offset = col*TEST_IMG_COLS
        for row in range(border_width):
            pixel = offset + row
            ref_img[pixel] = ref_img[offset+border_width]
        for row in range(TEST_IMG_COLS-border_width, TEST_IMG_COLS):
            pixel = offset + row
            ref_img[pixel] = ref_img[offset+TEST_IMG_COLS-border_width-1]
    for col in range(TEST_IMG_ROWS-border_width, TEST_IMG_ROWS):
        offset = col*TEST_IMG_COLS
        for row in range(border_width):
            pixel = offset + row
            ref_img[pixel] = ref_img[border_height_offset+border_width]
        for row in range(border_width, TEST_IMG_COLS-border_width):
            pixel = offset + row
            ref_img[pixel] = ref_img[border_height_offset+row]
        for row in range(TEST_IMG_COLS-border_width, TEST_IMG_COLS):
            pixel = offset + row
            ref_img[pixel] = ref_img[border_height_offset+TEST_IMG_COLS-border_width-1]


    ipFilter.write(0x10, TEST_IMG_COLS)
    ipFilter.write(0x18, TEST_IMG_ROWS)
    ipFilter.write(0x00, 0x01)
    ipDMAIn.sendchannel.transfer(src_img_strm)
    ipDMAOut.recvchannel.transfer(dut_img_strm)
    ipDMAIn.sendchannel.wait()
    ipDMAOut.recvchannel.wait()
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    
    # Check DUT vs reference result
    for i in range(0, TEST_IMG_ROWS):
        for j in range(0, TEST_IMG_COLS):
            dut_val = dut_img_strm[i * TEST_IMG_COLS + j]
            ref_val = ref_img[i * TEST_IMG_COLS + j]
            if (dut_val != ref_val):
                err_cnt += 1


    if (err_cnt == 0):
        print("*** TEST PASSED ***")
        ret_val = 0
    else:
        print("!!! TEST FAILED - " + err_cnt + " mismatches detected !!!")
        ret_val = -1

    print("============================")
    print("Exit process")
