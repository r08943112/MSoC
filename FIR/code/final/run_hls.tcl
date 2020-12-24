
open_project hls_fir_prj
add_files  "fir.c"
add_files -tb "fir-top.c"
set_top fir

#open_solution "solution0"
#set_part {xc7z020clg484-1}
#create_clock -period 5 -name default
#csim_design 
#csynth_design 
#cosim_design 
#export_design -format ip_catalog
#close_project
#

open_solution "solution1"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
csim_design 
csynth_design 
cosim_design 
export_design -format ip_catalog
close_project

