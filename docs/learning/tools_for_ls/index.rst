Tools for Low Speed Mixed Signal System Design
----------------------------------------------

**Note:** This is a work in progress.

Introduction
~~~~~~~~~~~~

The goal of this tutorial is to equip the reader with a collection of hardware and software tools for developing low-speed mixed-signal applications.
Content Guide: This tutorial includes complete written instructions, a video guide, and a slide deck that can be used for delivering as a hands-on workshop.


What exactly does “Low Speed” mean? In the context of this tutorial, it means that timing is not very critical. Signals are either completely static or moving slowly such that it doesn't matter if the instant that an ADC samples the signal wiggles around a bit relative to the previous sampling. While clock jitter is one source of this uncertainty, software delays (such as the time between a timer interrupt and the assertion of a “convert” edge) will likely be dominant. Important parameters in low-speed applications are offset, gain error, linearity, and temperature drift. “Noise” in a low-speed application is typically synonymous with resolution, and is typically measured by applying a noiseless input signal and taking a histogram of the output readings. AC performance metrics such as signal to noise ratio and total harmonic distortion extracted from a Fourier transform of the data will not be considered.
In contrast - sample jitter is important in a “high speed” application. If you are measuring signal to noise ratio, the Signal to Noise ratio (SNR) can be no greater than:

:math:`SNR <= -20 * log(2*pi*f\_{IN}*t\_{j})`

where:

- :math:`f\_{IN}` is the analog input frequency in Hz

- :math:`t\_{j}` is the RMS jitter in seconds RMS

where:
:math:`f_{IN}` is the analog input frequency in Hz
:math:`t_{j}` is the RMS jitter in seconds RMS

So that's it. In this tutorial, we will set voltages and currents, read voltages and currents, do some basic math, but each reading will be treated independently, no correlation to previous or future readings. We will NOT be measuring AC Signal to Noise Ratio (SNR), Total Harmonic Distortion (THD), nor measuring steps, wiggles, or any other situation where precise timing is required. (Rest assured, there are lots of very interesting applications in this category.)
Throughout the exercises we'll be writing simple Python code to capture and analyze data, using the industry standard Industrial I/O (IIO) framework to interact with the ADC, and the popular NumPy and Matplotlib Python libraries. Thus this exercise also serves as a mini-tutorial on Python.
==== Materials

-  Raspberry Pi 4; 2G, 4G, or 8G version. (3B, 3B Plus will work, but
   you will want the 4 :-) )
-  5V USB-C wall adapter for Raspberry Pi (micro USB for model 3)
-  :adi:`EVAL-AD5592R-PMDZ<eval-ad5592r-pmdz>`
-  Electrical connection hardware (choose one):

   -  :adi:`Raspberry Pi to PMOD/QuikEval™/LTpowerPlay® Adaptor HAT<pmd-rpi-intz>`

   - 12x 15cm socket-to-socket jumpers such as **[[https://schmartboard.com/wire-jumpers/female-jumpers/5-inch/|these from Schmartboard]]**
- 16GB (or larger) Class 10 (or faster) micro-SD card, with **[[resources:tools-software:linux-software:kuiper-linux|Analog Devices Kuiper Linux]]** installed
- User interface setup (choose one):
   - HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
   - Host Windows/Linux/Mac computer on same network as Raspberry Pi
- [[adi>en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm2000.html|ADALM2000]] (Not required for all experiments.)
- 2N3904 NPN Transistor
- 47Ω resistor
- 47kΩ resistor
- Breadboard or prototyping board, hookup wire
- Clone or download zip of the Python code for this tutorial
- Python files: **[[downgit>pyadi-iio/tree/master/examples/ad5592r_examples|AD5592r Pyadi-IIO examples]]**
   - (Note that these are included in the pyadi-iio repo, consider cloning the entire thing:

::

   git clone https://github.com/analogdevicesinc/pyadi-iio.git

-  AD5592R Device Tree Overlay for alternate configuration with GPIO
   pins

.. ADMONITION:: Download

   :download:`rpi-ad5592r-with_gpios-overlay source and compiled overlay <rpi-ad5592r-with_gpios-overlay.zip>`

Background
~~~~~~~~~~

| This tutorial builds on the concepts covered in:
| `Converter Connectivity
  Tutorial </university/labs/software/iio_intro_toolbox>`__
| It also serves as a preview to this tutorial that starts to deal with
  analyzing time series data:
| `Precision ADC
  Tutorial </university/labs/software/precision_adc_toolbox>`__

Slide Deck and Video
~~~~~~~~~~~~~~~~~~~~

Since this tutorial is also designed to be presented as a live, hands-on workshop, a slide deck is provided here:

.. ADMONITION:: Download

   :download:`Tools for Low-Speed Mixed Signal System Design Slide Deck <Tools_for_low_speed_ms_workshop.pptx>`

A complete video run-through is also provided, either as a companion to
following the tutorial yourself, or to practice before presenting as a
hands-on workshop: <WRAP todo> This video is accurate, but will be
re-done at some point:


.. video:: https://www.youtube.com/watch?v=tJtzUrt9_1U


| <WRAP todo> Finish Me
| (Translate slide deck and video into complete written instructions
  with photos, diagrams, etc.) </WRAP>

Preparation - a few resources for learning Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What does “Just Enough Software” look like?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Stack Background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introducing an exciting new product that we'll apply our skills
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Component selection based on software support (rather than pure analog performance)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware Setup
~~~~~~~~~~~~~~~~

Booting the system
~~~~~~~~~~~~~~~~~~~~~~~~

Post-boot housekeeping
~~~~~~~~~~~~~~~~~~~~~~~~

The Raspberry Pi-based hardware and Linux setup mirrors that of the ADXL345 used in the `Converter
Connectivity Toolbox and
Tutorial </university/labs/software/iio_intro_toolbox>`__, including bringing up the pyadi-iio example. Follow the instructions for downloading and installing ADI Kuiper Linux, and editing config.txt. The only difference is the interrupt connection and device tree overlay to be added to config.txt. For this exercise, add the following line to config.txt:

::

   dtoverlay=rpi-ad5592r

Configuring the System (and rebooting!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command Line Tools (Hello, AD5592r!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Device Trees: Telling Linux what's connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pyadi-iio And examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hands-On!** Working through a simple, but complete case study
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
Next Steps: Developing on a remote host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next Steps: Other languages (C++, C#, MATLAB, etc.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next Steps: No-OS development on Linux? You bet!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
...but I'm Confused... No-OS means no Operating System, but we're using Kuiper
Linux, and that's an Operating System. What gives?

Unlike the IIO drivers used in the previous tutorial , which
**require** the Linux kernel and operating system to function, No-OS
provides a portable software stack which can run on any platform that
supports a C compiler. This could be bare metal microcontrollers,
truly running without an operating system, up through full systems
like our Kuiper Linux running on a Raspberry Pi. The No-OS repository
includes existing support for the Linux OS, Real-Time Operating
Systems Chibios, and mbed, Raspberry Pico, as well as hardware support
for Maxim/ADI, STM32, Xilinx and Altera.
But why? Well, bringing up a toolchain for a particular embedded
processor has its own set of challenges - particularly if development
will begin on a standard development platform, then be ported to a
custom board. Runnin no-OS code on Linux provides a way to get started
on the embedded code development, before actually embedding.
A full treatment of this flow is beyond the scope of this tutorial,
but will be documented in a future tutorial. <WRAP todo> Port the Fred
in the Shed curve tracer to no-OS on Linux. </WRAP>

Next Steps: Porting to a fully embedded system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More “Just Enough Software” examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Drawing parallels to other software flows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wrapup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additional References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 4