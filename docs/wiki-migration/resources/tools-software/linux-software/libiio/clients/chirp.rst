Generating and Downloading a Baseband Signal using the IIO System Object
========================================================================

This example is inspired by the MathWorks example "`Generating and Downloading a Baseband Signal to an RF Signal Generator <https://www.mathworks.com/help/instrument/generating-and-downloading-a-baseband-signal.html>`__".

This example shows the creation of a complex baseband (I & Q) signal with MATLAB, how to download this signal to a AD9361 based platform, which up converters the signal to an RF carrier. The download of the signal and control of the AD9361 uses the Analog Devices' `IIO System Object <https://wiki.analog.com/matlab_simulink>`__, which supports communication the AD9361 through ethernet.

Introduction
------------

In this example we create a baseband signal and download it over a TCP/IP interface to the FMCOMMS3 and FMCOMMS5. We then control the AD9361 on the platform to upconvert the signal to RF and play it out the Tx side, and record the results on the receive side.

Requirements
~~~~~~~~~~~~

This example was tested with an FMCOMMS3 connected to a ZedBoard. The example uses the `Signal Processing Toolbox <https://www.mathworks.com/products/signal/>`__ to create the waveforms and the IIO System Object to interface with the hardware. The example requires the Zedboard to be on the same network as the PC running MATLAB.

Create the Complex Baseband Signal
----------------------------------

In this example we will create a `chirped waveform <https://en.wikipedia.org/wiki/Pulse_compression#Pulse_compression_by_linear_frequency_modulation_.28or_chirping.29>`__, or linear frequency modulated (LFM) pulse. Such wave forms may be used to simulate the output of the transmitter module of a pulse-doppler RADAR.

Additional Information
----------------------

This example shows the generation of simple LFM pulsed waveforms, and download and playback using an RF Signal Generator. `MATLAB <https://www.mathworks.com/products/matlab/>`__ can be used to define a wide variety of standard and arbitrary signals using the rich library of functions in the `Signal Processing Toolbox <https://www.mathworks.com/products/signal/>`__ and [[mw>products/communications.html|Communications Toolbox]™. Additionally, using Analog Device's IIO System Object, it is possible to download these signals to RF devices, like the FMCOMMS2/3/4/5 so they can function as Function Generators, Arbitrary Waveform Generators and RF Signal Generators, and to automate the control of these devices.
