# Qualisys PAF – Python example

## Getting started
To download this example project to your computer, you can either:

* [Click here](https://github.com/qualisys/paf-python-example/archive/refs/heads/main.zip) to download it as a zip file.
<br>_— or —_
* Clone this repository to your computer.

## Preparing Qualisys data for Python processing

1. Install Miniconda installer for Windows and Python 3.9: https://docs.conda.io/en/latest/miniconda.html
2. Run the installer and when prompted add Anaconda to your PATH environment variable
3. Open a command line prompt and enter the following:
    1. `conda create -n python-example python=3.9`
    2. `conda activate python-example`
    3. `conda install -c conda-forge ezc3d` (c3d parsing library, see https://github.com/pyomeca/ezc3d)
    4. `conda install -c anaconda lxml` (xml parsing library)
4. Open QTM and make sure that the path to `Command Prompt` is set in Project Options/Miscellaneous/Folder Options (the path is usually C:\Windows\System32\cmd.exe)   
5. Click on `Start Processing` to automatically export c3d files, read the c3d files content and export some data into an xml file. 

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
