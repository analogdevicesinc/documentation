MOTIF Wrapper in MATLAB and Simulink
====================================

The goal of this library is to provide example code and the necessary infrastructure code to call MOTIF from MathWorks tools. With this library, you can simulate larger systems including behavioral models developed by Analog Devices.

Downloads
=========

.. note::

   In order to use the MATLAB/Simulink MOTIF, your `MATLAB <https://www.mathworks.com/products/matlab/>`__ license needs to include the following components:

   
   -  MATLAB (R2014b or higher version is required)
   -  Simulink
   


The MOTIF infrastructure code and examples can be found here on GitHub:

.. admonition:: Download
   :class: download

   
   -  :git-MOTIF_MathWorks:`MOTIF_MathWorks <tree/master>`
   


Each folder in this repository corresponds to a supported component.

Install MOTIF
=============

In order to run any of the models, it is first necessary to install MOTIF within MATLAB. To install MOTIF, under the root \\MOTIF directory, run the file ``InstallMe.m`` This sets up the proper paths.

Setup Compiler
==============

If it is the first time running Simulink, then it will need to be configured to use a compiler. To do this, type the command ``mex -setup`` This brings up the following window where a compiler can be selected:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/mex.png
   :width: 600px

AD9625 Example
==============

AD9625 is a 12-Bit, 2.5 GSPS/2.0 GSPS, 1.3 V/2.5 V Analog-to-Digital Converter. Its data sheet can be found :adi:`here <AD9625>`.

To use the AD9625 model, go to \\AD9625\\MOTIF directory, and double click on ``Main.m`` to open the main function.

There are several performance characteristics of AD9625 we can get from this model by setting up the simulation parameters. For example, we can change the setting of input tone frequency and get an FFT plot. The figure below shows the FFT with Fin = 730.3 MHz.

|image1| |image2|

Given a fixed input tone frequency Fin = 241 MHz, we can sweep the analog input amplitude from -90 dB to 0 dB, and get SFDR.

Generated from file: :git-MOTIF_MathWorks:`AD9625/MOTIF/PlotSFDR.m`.

|image3| |image4|

.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/motif/ad9625_matlab_figure7.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/technical-guides/motif/ad9625_data_sheet_figure7.png
   :width: 450px
.. |image3| image:: https://wiki.analog.com/_media/resources/technical-guides/motif/ad9625_matlab_figure20.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/technical-guides/motif/ad9625_data_sheet_figure20.png
   :width: 450px
