open_project hls_reed_solomon_erasure_prj -reset 
add_files src/rs_erasure.c
add_files -tb  tb/tb_rs_erasure.c
add_files -tb  tv/tv_rs_erasure_in.txt
add_files -tb  tv/tv_rs_erasure_mout.txt

set_top rs_erasure
open_solution "solution0" -reset
set_part  {xc7z020clg484-1}
create_clock -period 5 -name default
csim_design 
csynth_design 
cosim_design 
export_design -format ip_catalog

open_solution "solution1" -reset
set_part  {xc7z020clg484-1}
create_clock -period 5 -name default
set_directive_array_partition -type complete rs_erasure c
set_directive_array_partition -type complete rs_erasure d
set_directive_interface -mode ap_none rs_erasure d
set_directive_interface -mode ap_vld rs_erasure codeidx
set_directive_pipeline -II 1  rs_erasure
csim_design 
csynth_design 
cosim_design 
export_design -format ip_catalog

exit