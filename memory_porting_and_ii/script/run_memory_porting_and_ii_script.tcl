#// SOLUTION 1
open_project proj_memory_porting_and_ii
set_top matrixmul
add_files matrixmul.cpp
add_files -tb  matrixmul_test.cpp -cflags "-DHW_COSIM"
open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
csim_design
csynth_design
cosim_design
#export_design -rtl verilog -format ip_catalog
close_project

#// SOLUTION 2
open_project proj_memory_porting_and_ii
set_top matrixmul
add_files matrixmul.cpp
add_files -tb  matrixmul_test.cpp -cflags "-DHW_COSIM"
open_solution "solution2"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
set_directive_pipeline "matrixmul/J_LOOP"
set_directive_array_reshape -type complete -dim 2 "matrixmul" a
set_directive_array_partition -type complete -dim 1 "matrixmul" b
csim_design
csynth_design
cosim_design
#export_design -rtl verilog -format ip_catalog
close_project

#// SOLUTION 3
open_project proj_memory_porting_and_ii
set_top matrixmul
add_files matrixmul.cpp
add_files -tb  matrixmul_test.cpp -cflags "-DHW_COSIM"
open_solution "solution3"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
set_directive_pipeline matrixmul
set_directive_unroll matrixmul/K_LOOP
set_directive_unroll matrixmul/J_LOOP
set_directive_unroll matrixmul/I_LOOP
set_directive_array_partition -type complete -dim 0 "matrixmul" a
set_directive_array_partition -type complete -dim 0 "matrixmul" b
set_directive_array_partition -type complete -dim 0 "matrixmul" res
set_directive_interface -mode ap_ctrl_none "matrixmul"
set_directive_interface -mode s_axilite "matrixmul" a
set_directive_interface -mode s_axilite "matrixmul" b
set_directive_interface -mode s_axilite "matrixmul" res
csim_design
csynth_design
# cosim_design
export_design -rtl verilog -format ip_catalog
close_project


exit