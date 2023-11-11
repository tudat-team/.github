## Welcome <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge)](CODE_OF_CONDUCT.md)

This is the Github landing page for the TU Delft Astrodynamics Toolkit - or Tudat - project. Tudat is a powerfull toolbox for research and education in numerical orbit propagation, state and parameter estimation, and mission design. The project originated at, and is managed by, staff and students at TU Delft, with an ever growing network of users, developers and alumni. The bulk of the functionality is written in C++ (Tudat), but the typical user interface is in Python (Tudatpy), which links to the Tudat core code.

Below you'll find a list of all the repositories relevant to our project. However, our main documentation pages are:
- [The Tudat website](https://docs.tudat.space/en/latest/) where you can find installation instructions, examples, overview of functionalities, and more!
- [The Tudat API reference](https://py.api.tudat.space/en/latest/), where a comprehensive overview of the user interfaces can be found.
- [The Tudat developer documentation](https://tudat-developer.readthedocs.io/en/latest/), where details on how Tudat and the ecosystem around it is put together.

## Our repositories

You can find the following repositories below:

- [tudat](https://github.com/tudat-team/tudat) The repository with the code code of our project (in C++), where much of our functionality and unit tests are implemented.
- [tudatpy](https://github.com/tudat-team/tudatpy) The repository with the code to generate the Python exposure of our C++ core (using [pybind11](https://github.com/pybind/pybind11)), as well as a limited set of Python native code. 
- [tudatpy-examples](https://github.com/tudat-team/tudatpy-examples) The repository with an ever-growing list of example applications using Tudatpy (in both .py and .ipynb).
- [tudat-bundle](https://github.com/tudat-team/tudat-bundle) The repository that one would typically use to build a local version of Tudat and Tudatpy (including build instructions)
- [tudat-resources](https://github.com/tudat-team/tudat-resources) The repository with the default set of data files which is automatically downloaded when installing tudat
- [tudat-multidoc](https://github.com/tudat-team/tudat-multidoc) The repository with the entries from which our [API reference documentation](https://py.api.tudat.space/en/latest/) is generated.
- [tudat-space](https://github.com/tudat-team/tudat-space) The repository from which our [website](https://docs.tudat.space/en/latest/) is generated.
- [tudat-developer-docs](https://github.com/tudat-team/tudat-developer-docs) The repository from which our [developer docs website](https://tudat-developer.readthedocs.io/en/latest/) is generated.
- [cspice-cmake](https://github.com/tudat-team/cspice-cmake) Our clone of the [cspice](https://naif.jpl.nasa.gov/naif/) software, built using CMake
- [sofa-cmake](https://github.com/tudat-team/sofa-cmake) Our clone of the [sofa](http://www.iausofa.org/) software, built using CMake
- [nrlmsise-00-cmake](https://github.com/tudat-team/nrlmsise-00-cmake) Our clone of the [nrlmsise-00](https://www.brodo.de/space/nrlmsise/) software, built using CMake
- Feedstocks for [tudat](https://github.com/tudat-team/tudat-feedstock), [tudatpy](https://github.com/tudat-team/tudatpy-feedstock), [tudat-resources](https://github.com/tudat-team/tudat-resources-feedstock), [cspice-cmake](https://github.com/tudat-team/cspice-cmake-feedstock), [sofa-cmake](https://github.com/tudat-team/sofa-cmake-feedstock), [nrlmsise-00-cmake](https://github.com/tudat-team/nrlmsise-00-cmake-feedstock)

In addition, there are a number of repositories related to education at TU Delft

## Our conda packages

The feedstock repositories listed above are used to build conda packages on [Azure](https://dev.azure.com/tudat-team/feedstock-builds/_build), from which ``conda`` packages are created and stored on our [Anaconda tudat-team channel](https://anaconda.org/tudat-team/). For tudat and tudatpy, we regualrly release new ``dev`` packages, to allow users to make immediate use of new functionality that has been pushed to our repositories. See [installation instructions](https://docs.tudat.space/en/latest/_src_getting_started/installation.html) on our website for more details. 


