#define NUM_TAPS 16

void fir(int input, int *output, int taps[NUM_TAPS])
{
#pragma HLS INTERFACE s_axilite port=input
#pragma HLS INTERFACE s_axilite port=output
#pragma HLS INTERFACE s_axilite port=taps
#pragma HLS INTERFACE s_axilite port=return

	#pragma HLS PIPELINE

	static int delay_line[NUM_TAPS] = {};
	#pragma HLS RESOURCE variable=delay_line core=RAM_2P_BRAM
	int result = 0;
	int i;

	for (i = NUM_TAPS - 1; i > 0; i--) {
	//#pragma HLS UNROLL
	//#pragma dataflow
		delay_line[i] = delay_line[i - 1];
	}
	delay_line[0] = input;

	for (i = 0; i < NUM_TAPS; i++) {
	int temp = delay_line[i] * taps[i];
	//#pragma dataflow

		result += temp;
		// printf("result = %d\n", result);
	}
	

	*output = result;
}
