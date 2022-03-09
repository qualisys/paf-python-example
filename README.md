# Qualisys PAF – Python example

## Getting started
To download this example project to your computer, you can either:

* [Click here](https://github.com/qualisys/paf-python-example/archive/refs/heads/main.zip) to download it as a zip file.
<br>_— or —_
* Clone this repository to your computer.

## Preparing Qualisys data for Python processing

1. Install Python, two options:
    1. Install a Python distribution like Anaconda that includes all common dependencies, see https://www.anaconda.com/download/
    2. Alternatively:
         - Install Python only (see https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi)
         - Add numpy and lxml packages (for example using PIP, see https://packaging.python.org/tutorials/installing-packages/)
2. Install BTK, btk-0.3.0_win32.exe (see https://pypi.python.org/pypi/btk)

Example tested with Anaconda (for Python 2.7, 32bit), alternatively Python 2.7.14 (32bit) with numpy and lxml package.

## Resources for using the Qualisys Project Automation Framework (PAF)

The purpose of the ***Project Automation Framework*** (PAF) is to streamline the motion capture process from data collection to the final report. This repository contains an example project that illustrate how PAF can be used to implement custom automated data collection in [Qualisys Track Manager (QTM)](http://www.qualisys.com/software/qualisys-track-manager/), and how QTM can be connected to a processing engine. 

### PAF Documentation

The full documentation for PAF development is available here: [PAF Documentation](https://github.com/qualisys/paf-documentation).


### PAF Examples

Our official examples for various processing engines:

- [Excel](https://github.com/qualisys/paf-excel-example)
- [Matlab](https://github.com/qualisys/paf-matlab-example)
- [OpenSim](https://github.com/qualisys/paf-opensim-example)
- [Python](https://github.com/qualisys/paf-python-example)
- [Theia Markerless](https://github.com/qualisys/paf-theia-markerless-example)
- [Visual3D](https://github.com/qualisys/paf-visual3d-example)

_As of QTM version 2.17, the official Qualisys PAF examples can be used without any additional license. Note that some more advanced analysis types require a license for the "PAF Framework Developer kit" (Article number 150300)._
