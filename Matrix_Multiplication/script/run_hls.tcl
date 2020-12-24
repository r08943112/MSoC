
open_project hls_matrixmultiplication_prj -reset
add_files  "matrixmultiplication.cpp"
add_files -tb "matrixmultiplication-top.cpp"
add_files -tb "matrixmultiplication.gold.dat"
set_top matrixmul



open_solution "solution0"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
csim_design 
csynth_design 
cosim_design 
export_design -format ip_catalog
close_project

