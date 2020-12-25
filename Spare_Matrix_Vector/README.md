# MSoC-HLS-Sparse Matrix Vector



<br />
<p align="center">

  <h3 align="center">MSoC-HLS Sparse Matrix Vector</h3>
  
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
This is a Sparse Matrix Vector hls projects.

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
* Sparse matrix-vector multiplication (SpMV) of the form y=Ax is a widely used computational kernel existing in many scientific applications. The input matrix A is sparse. The input vector x and the output vector y are dense. In case of repeated y=Ax operation involving the same input matrix A but possibly changing numerical values of its elements, A can be preprocessed to reduce both the parallel and sequential run time of the SpMV kernel.

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



