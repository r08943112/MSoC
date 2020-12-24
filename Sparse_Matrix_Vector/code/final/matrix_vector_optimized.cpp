#define SIZE 8
typedef int BaseType;

void matrix_vector(BaseType M[SIZE][SIZE], BaseType V_In[SIZE], BaseType V_Out[SIZE]) {
//#pragma HLS array_partition variable=M dim=2 complete
//#pragma HLS array_partition variable=V_In complete
#pragma HLS resource variable=M core=RAM_1P_BRAM
#pragma HLS resource variable=V_In core=RAM_1P_BRAM
#pragma HLS array_map variable=M instance=combine horizontal
#pragma HLS array_map variable=V_In instance=combine horizontal
	BaseType i, j;
data_loop:
	for (i = 0; i < SIZE; i++) {
#pragma HLS pipeline II=1
		BaseType sum = 0;
	dot_product_loop:
		for (j = 0; j < SIZE; j++) {
			sum += V_In[j] * M[i][j];
		}
		V_Out[i] = sum;
	}
}
