Overview
========

| ADIsim is a behavioral modeling simulator developed by Analog Devices. It is a discrete time simulator that is not limited to digital simulation. Because it is behavioral, it can support mixed signal or pure analog devices. The simulator is compiled into one Windows DLL: ADIsim.dll.
| Behavioral modeling has many advantages over more traditional types of simulation but be aware that it is not meant to replace them. As with any engineering practice, the benefits must be weighed against the disadvantages. In this case, you exchange simulation time for overall accuracy. However, as with many simulation environments, this tradeoff is deemed acceptable. The goal of Analog Devices, Inc., is to enable engineers to better do their jobs through the use of this simulator tool, whether it be through product selection, training, system design, or algorithm development.

Resources
=========

| `API Definition <https://wiki.analog.com/adisimapi>`_
| For a detailed description of how to interface to the DLL, see this section.
| `Online ADC Analysis <http://designtools.analog.com/dtSimADCWeb/dtSimADCMain.aspx>`_
| For simple product selection, a simple web-based application is accessible from the product pages of devices that are supported by ADIsimADC. This tool requires no downloads and allows control of the test conditions and design specific performance plots. Results are graphed, which greatly reduces the uncertainty of how a part can be expected to perform in an application. The tool also allows input of desired operating conditions and required performance levels and then it recommends suitable devices to the user. The following functions are available with the ADIsimADC:

-  Advanced online product selection
-  Vary input amplitude and frequency
-  Single tone or two tone FFT analysis
-  Amplitude and frequency sweeps
-  Generate a list of ADCs that meet your signal processing requirements

| 
| :adi:`AN_737`
| AN-737 Application Note, *How ADIsimADC Models an ADC*, provides a description of how behavioral simulation is used to model an ADC.
