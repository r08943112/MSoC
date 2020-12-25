
open_project hls_spare_matrix_vector_prj
add_files "matrix_vector_base.c"
add_files -tb "matrix_vector_base-top.c"
add_files -tb "out.matrix_vector.gold.dat"

set_top matrix_vector

open_solution "solution0"
set_part {xc7z020clg484-1}
create_clock -period 5 -name default
csim_design 
csynth_design 
cosim_design 
export_design -format ip_catalog
close_project



