# MSoC-HLS-reed_solomon_erasure(xapp1273)



<br />
<p align="center">

  <h3 align="center">MSoC-HLS reed_solomon_erasure(xapp1273)</h3>
  
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
This is a reed_solomon_erasure(xapp1273) hls projects.

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
* vivado_hls run_reed_solomon_erasure.tcl

## Algorithm
* Reed–Solomon codes operate on a block of data treated as a set of finite-field elements called symbols. Reed–Solomon codes are able to detect and correct multiple symbol errors. By adding t = n − k check symbols to the data, a Reed–Solomon code can detect (but not correct) any combination of up to and including t erroneous symbols, or locate and correct up to and including ⌊t/2⌋ erroneous symbols at unknown locations. As an erasure code, it can correct up to and including t erasures at locations that are known and provided to the algorithm, or it can detect and correct combinations of errors and erasures. Reed–Solomon codes are also suitable as multiple-burst bit-error correcting codes, since a sequence of b + 1 consecutive bit errors can affect at most two symbols of size b. The choice of t is up to the designer of the code and may be selected within wide limits.

## References
* https://github.com/Xilinx/HLx_Examples/tree/master/DSP/reed_solomon_erasure
<!-- CONTRIBUTING -->
## Contributing
* Zuo-Yu Wang


<!-- LICENSE -->
## License
* https://github.com/Xilinx/HLx_Examples/blob/master/DSP/reed_solomon_erasure/LICENSE.md


<!-- CONTACT -->
## Contact
* r08943112@ntu.edu.tw



