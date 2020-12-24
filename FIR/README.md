# MSoC-HLS-FIR



<br />
<p align="center">

  <h3 align="center">MSoC-HLS FIR</h3>
  
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
* vivado_hls run_hls.tcl

## Algorithm
* In signal processing, a finite impulse response (FIR) filter is a filter whose impulse response (or response to any finite length input) is of finite duration, because it settles to zero in finite time. This is in contrast to infinite impulse response (IIR) filters, which may have internal feedback and may continue to respond indefinitely (usually decaying).

* The impulse response (that is, the output in response to a Kronecker delta input) of an Nth-order discrete-time FIR filter lasts exactly N + 1 samples (from first nonzero element through last nonzero element) before it then settles to zero.

* FIR filters can be discrete-time or continuous-time, and digital or analog.

## References
* https://github.com/KastnerRG/pp4fpgas/tree/master/examples
<!-- CONTRIBUTING -->
## Contributing
* Zuo-Yu Wang


<!-- LICENSE -->
## License
* https://github.com/KastnerRG/pp4fpgas/tree/master/examples


<!-- CONTACT -->
## Contact
* r08943112@ntu.edu.tw



