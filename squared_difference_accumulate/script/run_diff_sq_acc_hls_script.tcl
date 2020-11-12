#// SOLUTION 0
open_project hls_diff_sq_acc
set_top diff_sq_acc
add_files src/diff_sq_acc.cpp
add_files -tb  tb/diff_sq_acc_tb.cpp
open_solution "solution0"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
csim_design
csynth_design
cosim_design
#export_design -rtl verilog -format ip_catalog
close_project

#// SOLUTION 1
open_project hls_diff_sq_acc
set_top diff_sq_acc
add_files src/diff_sq_acc.cpp
add_files -tb  tb/diff_sq_acc_tb.cpp
open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
set_directive_pipeline "diff_sq_acc"
csim_design
csynth_design
cosim_design
#export_design -rtl verilog -format ip_catalog
close_project
