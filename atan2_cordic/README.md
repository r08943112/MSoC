# MSoC-HLS-atan2_cordic



<br />
<p align="center">

  <h3 align="center">MSoC-HLS atan2_cordic</h3>
  
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Usage](#usage)
* [Algorithm](#Algorithm)
* [References](#References)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
This is a atan2_cordic hls projects.

**Directory structure**
* **README.md** - introduce the project, algorithm, reference ....
* **code/**
  * original - original code from open source
  * final (use inline pragma) - include both host and kernel code
* **code-opt/** - include both host and kernel code
* **script/** - vivado_hls run.tcl
* **impl/** - result of the implementation, HLS csynth report
      


<!-- USAGE EXAMPLES -->
## Usage
* vivado_hls run_atan2_hls_script.tcl

## Algorithm
* The function to be achieved by this project is to use CORDIC to calculate Atan2(), give a coordinate file as input data, output the result as the answer, and compare the answer with the simulation result of matlab. In this project, the original author mainly discusses four methods. The first is to use 64-bit floating point numbers for calculation, the second is to use 32-bit floating point numbers for calculation, and the third is Use the CORDIC algorithm to do the calculation, and the fourth is to use the simplified CORDIC algorithm to calculate.

## References
* https://github.com/Xilinx/HLx_Examples
<!-- CONTRIBUTING -->
## Contributing
* Zuo-Yu Wang


<!-- LICENSE -->
## License
* Xilinx/Vivado/2019.2/examples/design


<!-- CONTACT -->
## Contact
* r08943112@ntu.edu.tw



