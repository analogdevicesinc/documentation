Active Learning Interface (for) Circuits (and) Electronics M1K:
===============================================================

Objective:
----------

This document serves as a User’s Guide for the ALICE Desktop software interface written for use with the ADALM1000 active learning kit hardware. If you are looking for ALICE for the ADALM2000 (M2K) :doc:`look here </wiki-migration/university/tools/m2k/alice/users-guide-m2k>`.

Background:
-----------

Although the word ALICE can be spelled out from the title of this users guide, it is actually an allusion to the fantasy works of Lewis Carroll: 1865’s Alice’s Adventures in Wonderland and its 1871 sequel Through the Looking-Glass, and What Alice Found There. In these stories Alice explores a strange and wondrous world down a rabbit hole and on the other side of a mirror ( looking glass ).


|image1|

.. container:: centeralign

   Alice Meets the Caterpillar, John Tenniel illustration from Alice in Wonderland by Lewis Carroll


Hopefully, through the use of this software along with the ADALM1000 active learning kit hardware, Students can explore the strange and wondrous world of Circuits, Electronics and Electrical Engineering.

Functions:
----------

The ALICE Desktop software provides the following functions:

-  :doc:`Two Channel Oscilloscope </wiki-migration/university/tools/m1k/alice/oscilloscope-x-y-user-guide>` for time domain display and analysis of voltage and current waveforms.
-  :doc:`Two Channel Arbitrary Waveform Generator </wiki-migration/university/tools/m1k/alice/desk-top-awg-users-guide>` (AWG) controls.
-  :doc:`X-Y display </wiki-migration/university/tools/m1k/alice/oscilloscope-x-y-user-guide>` for plotting captured voltage and current vs voltage and current data as well as voltage waveform histograms.
-  :doc:`Phase Analyzer </wiki-migration/university/tools/m1k/alice/phase-analyzer-user-guide>`, Polar plotting of voltage and current waveform amplitude and phase
-  :doc:`Two Channel Spectrum Analyzer </wiki-migration/university/tools/m1k/alice/desktop-sa-ba-ia-users-guide>` for frequency domain display and analysis of voltage waveforms.
-  :doc:`Bode plotter and network analyzer </wiki-migration/university/tools/m1k/alice/desktop-sa-ba-ia-users-guide>` with built-in sweep generator.
-  :doc:`Impedance Analyzer </wiki-migration/university/tools/m1k/alice/desktop-sa-ba-ia-users-guide>` for analyzing complex RLC networks and as a RLC meter and Vector Voltmeter.
-  :doc:`DC Ohmmeter </wiki-migration/university/tools/m1k/alice/dc-ohmmeter-user-guide>`, measures unknown resistance with respect to known external resistor or known internal 50 ohms.
-  :doc:`Board Self-Calibration </wiki-migration/university/tools/m1k/alice/self-calibration-user-guide>` using the AD584 precision 2.5V reference from the ADALP2000 Analog Parts Kit

Required files:
---------------

The ALICE Desktop program is written in Python and the source code is compatible with either 2.7 or 3.7 versions of Python installed on the user’s computer. The program only imports modules generally included with standard Python installation packages.

Windows:
~~~~~~~~

Windows users who do not wish to install Python and the other required software packages can install the standalone executable from here. This is a link to a set by step `guide for installing ALICE on Windows <https://wiki.analog.com/_media/university/tools/m1k/alice/alice-install-procedure.pdf>`_.

.. admonition:: Download
   :class: download

   Download Windows installer here:

   
   -  Version 1.3 :git-alice:`Windows executable <releases>` always use the latest release.
   
   Download Windows Libsmu installer here:
   
   -  Version 1.0.4 for 64 bit systems :git-libsmu:`64 bit Libsmu installer <releases/download/v1.0.4/libsmu-1.0.4-setup-x64.exe>`
   -  Version 1.0.4 for 32 bit systems :git-libsmu:`32 bit Libsmu installer <releases/download/v1.0.4/libsmu-1.0.4-setup-x86.exe>`
   
   The installer should include all required (python) packages but not the USB device drivers or low level interface library libsmu for the ADALM1000. The drivers can be installed by installing the Libsmu library and clicking on the install WinUSB driver box when prompted.


Before connecting your ADALM1000 to your computer you need to install the WinUSB device drivers. On 64 bit computers (most common), run the libsmu-1.0.4-setup-x64.exe installer program. Click on the box to install the WinUSB device drivers.

For 32 bit systems, run the libsmu-1.0.4-setup-x86.exe installer program. Do not click on the box to install the WinUSB device drivers, that was already done by first step. If you do happen to have a version of Python and wish to write your own scripts to control the ADALM1000 then optionally install the appropriate Python bindings as well.

Run the alice-desktop-1.3-x64-setup.exe installer program. For 32 bit systems, run alice-desktop-1.3-x32-setup.exe installer program. ALICE desktop opens and saves info and data to various files in the installation directory. Because of user permission issues with some installations of Windows you may need to install the software in a directory other than the usual default “Program Files”. C:\\ALM Software\\ would be a good second choice or further down in the Documents folder. The installer adds desktop icons for each tool in the suite. Alternatively, under the properties for the icons, you can change the directory the program(s) start in.

Using the Widows executable is highly recommended but the ALICE Desktop can also be run from the Python 2.X/3.X compatible source code with the following packages installed:

| **Python 2.7 or Python 3.7**
| tKinter
| numpy numerical package extension
| matplotlib plotting package extension
| libsmu/pysmu

Python for Linux and OSX:
~~~~~~~~~~~~~~~~~~~~~~~~~

Most releases of the Linux operating system have Python included and many also include the tKinter and numpy numerical packages as well. Linux ( including Raspberry Pi ) and OSX users must manually compile libsmu/pysmu. For Python on Linux systems that do not come with pre-installed packages here are the commands that might be needed:

-  sudo apt-get install python3-pip
-  sudo python3 -m pip install numpy
-  sudo apt-get install tk

Manually installing libsmu / pysmu required by the ALICE Desktop Python source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   **For all Non-Windows Operating Systems**

   
   If you are going to be using the ALICE Desktop software on a computer with an operating system other than Windows you will need to run the program from the Python source code (compatible with either Python 2 or 3). **DO NOT** proceed beyond this point without first installing the pysmu library (and the underlying libsmu package) following the instructions found in the readme file on the `Libsmu GitHub Repository <https://github.com/analogdevicesinc/libsmu>`_.
   
   \*\* The Recommended Method for all non-Windows operating systems is to use Anaconda (Python) and the Conda installation packages as outlined here: :doc:`Conda Packages </wiki-migration/university/tools/conda>`\ \*\*


There are Python :git-libsmu:`test examples that can be found here <bindings/python/examples>` to assist in testing and confirming that you have a working version of pysmu installed.

Once you have a verified working version of pysmu installed then the Version 1.3 ALICE Python source code can be downloaded from the :git-alice:`alice GitHub Repository <tree/Version-1.3>`

The following file also outlines the `steps used to install libsmu <https://wiki.analog.com/_media/university/tools/m1k/alice/linux-install-steps-v1.3.pdf>`_ with Python bindings and ALICE desktop source code on Ubuntu version 18.04 of Linux using the above packages from the libsmu repository. For operating systems other than Windows the use of the :doc:`Conda packages </wiki-migration/university/tools/conda>` is the recommended method for installing libsmu and the pysmu bindings in Python.

Manually installing numpy Python extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Linux users, numpy might already be part of your Python 2.7 distribution. Otherwise you can download and install numpy through the software / package manager on your particular version of Linux.

For Windows users, there are Windows binary installers that can be downloaded from `SourceForge <https://sourceforge.net/projects/numpy/files/NumPy/1.10.2/>`_. The latest version may or may not have a Windows binary so you may need to look back one or two version releases to find a Windows binary. As of this writing the newest version with a binary is numpy-1.10.2-win32-superpack-python2.7.exe 2015-12-14. Be sure to download the version for Python 2.7! Note that the developers have only created a Windows binary for 32 bit Python 2.7. Users more familiar with building from source code can download the source archive and use the setup scripts to install ( build ) numpy for their 64 bit version of Python.

Directions:
-----------

It is assumed that the reader is somewhat familiar with the functionality and capabilities of the ADALM1000 hardware. For more on the ADALM1000 hardware please refer to the following documents:

| :doc:`ADALM1000 Overview </wiki-migration/university/tools/m1k>`
| :doc:`ADALM1000 Hardware </wiki-migration/university/tools/m1k/hw>`
| :doc:`ADALM1000 Design Document </wiki-migration/university/tools/m1k/design>`
| `What is a Source Measurement Unit or SMU? <https://wiki.analog.com/_media/university/tools/m1k/alice/alice_whats-a-smu.pdf>`_
| `What is a Curve Tracer vs an Analog Signature Analyzer vs a SMU? <https://wiki.analog.com/_media/university/tools/m1k/alice/alice_curve-tracing_what-is-analog_signature_analysis.pdf>`_
| `Measuring current with the ADALM1000 <https://wiki.analog.com/_media/university/tools/m1k/alice/alice_measuring-current.pdf>`_
| :doc:`ADALM1000 Accessory Boards </wiki-migration/university/tools/adalm1000/accessory-boards-index>`
| :doc:`ADALM1000 Analog Inputs </wiki-migration/university/tools/m1k/analog-inputs>`
| :doc:`ADALM1000 Analog Multiplexers </wiki-migration/university/tools/m1k/analog-mux>`
| :doc:`ADALM1000 Digital Outputs </wiki-migration/university/tools/m1k/digital-outputs>`
| :doc:`ADALM1000 Low Capacitance FET Input Buffers </wiki-migration/university/tools/m1k/fet-probes>`

The Windows executable installer, in addition to the main ALICE Desktop program, includes the following DC measurement tools:

-  DC Voltmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/voltmeter_lab-0.pdf>`_ (volt-meter-tool-1.2.exe)
-  DC Ohmmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/ohmmeter_lab-0.pdf>`_ (ohm-meter-vdiv-1.2.exe)
-  DC Meter-Source `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/meter-source-lab0.pdf>`_ (dc-meter-source-tool-1.3.exe)
-  :doc:`DC Power Profiler Tool </wiki-migration/university/courses/tutorials/alm-power-profiler>` (`Python source <https://raw.githubusercontent.com/analogdevicesinc/alice/Version-1.3/power-profiler-1.3.pyw>`_)
-  DC Strip Chart Tool (`Python source <https://raw.githubusercontent.com/analogdevicesinc/alice/Version-1.3/strip-chart-tool-1.3.pyw>`_)
-  DC Data-Logger Tool (`Python source <https://raw.githubusercontent.com/analogdevicesinc/alice/Version-1.3/data-logger-tool-1.3.pyw>`_)

| A few notes on nomenclature used in this document:
| CA-V refers to the Channel A voltage signal
| CA-I refers to the Channel A current signal
| CB-V refers to the Channel B voltage signal
| CB-I refers to the Channel B current signal

Customizing ALICE Desktop
-------------------------

There are many aspects of ALICE that can be customized and advanced features that can be enabled by making changes in the alice_init.ini file. Things that can be customized / changed are outlined in the :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>`.

Using the numpy library
-----------------------

Alice includes the Python nunpy numerical library and there are many more functions that can be used manually. How to do that is outlined in the :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>`.

Using Equivalent Time Sampling with the ADALM1000
-------------------------------------------------

One of the advanced features that can be enabled in ALICE is Equivalent Time Sampling which, for certain classes of periodic waveforms, can increase the apparent sampling to MSPS rates. How to use ETS is outlined in the :doc:`ALICE Equivalent Time Sampling User’s Guide </wiki-migration/university/tools/m1k/alice/advanced-equivalent-time-sampling-guide>`

Oscilloscope / Main Window:
---------------------------

Be sure that the ALM1000 board is plugged into a USB port before starting the program. Once the program is running the main window, as shown in figure 1, should appear. This is the main desktop window and serves as the Oscilloscope Tool Window as well as controls for opening the other display windows and certain common control functions. It is sub divided into 4 sections.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/main-window-1.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 1, ALICE Desktop main window


Full Details can be found in the :doc:`Oscilloscope Users Guide </wiki-migration/university/tools/m1k/alice/oscilloscope-x-y-user-guide>`.

AWG Controls Window:
--------------------

The :doc:`AWG section Guide </wiki-migration/university/tools/m1k/alice/desk-top-awg-users-guide>`.

The X-Y Plotting Tool:
----------------------

When the :doc:`X-Y Plot Window </wiki-migration/university/tools/m1k/alice/oscilloscope-x-y-user-guide>` button is clicked in the Main Window the X-Y display Window will appear.

The Spectrum Analyzer / Bode Plotter:
-------------------------------------

The :doc:`Spectrum Analyzer / Bode Plotting / Impedance Analyzer </wiki-migration/university/tools/m1k/alice/desktop-sa-ba-ia-users-guide>` section Guide.

DC Ohmmeter Window:
-------------------

The :doc:`DC Ohmmeter </wiki-migration/university/tools/m1k/alice/dc-ohmmeter-user-guide>` Virtual instrument is used to measure an unknown resistance.

Digital I/O controls Windows:
-----------------------------

The ALM1000 hardware provides four 3.3V CMOS digital input / output pins. The four general purpose input/output pins along with ground and the 3.3V power supply are provided on the digital port connector as shown in figure 27.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 27 Digital I/O connector


Part of the ALM1000 rev D schematic is shown in figure 28D and the rev F schematic is shown in figure 28F. As can be seen each of the four general purpose PIO pins ( connector P3 ) is connected to a 220 Ω and a 470 Ω resistor in rev D and in rev F 4.7K resistors in place of the 470 Ω resistors. The 220 Ω resistors connect to Port A pins 0-3 and the 470 Ω / 4.7k resistors connect to Port A pins 4-7. This configuration with two digital port pins connected though two different series resistors is unique and not generally typical of digital pins in other small portable USB based hardware such as the Analog Discovery module.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 28D ALM1000 rev D digital interface input/output diagram


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/m1k-f-digital-outputs_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 28F ALM1000 rev F digital interface input/output diagram


The state of the Port A pins can be controlled using the simple digital control interface shown in figure 29. At this time only static hi / low functionality is supported. Eight rows of selectors are provided, one for each microcontroller pin for Port A ( PA0-PA7). Each port pin can be set to either a logic low, 0, a high-impedance or floating state, Z or a logic high, 1. When in the high-impedance or floating state that pin can be used as a logic input.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/digital-pio-window.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 29, Digital I/O control window


**Using these pins for purposes other than digital**

This configuration with two digital output drivers connected to a single connector pin through two different series resistors could be viewed in a different light. We might consider the CMOS output diver of the microcontroller pin as a three position single pole switch that can connect to ground or the 3.3 V supply or open circuit as shown in figure 30. This is more of an analog representation of the circuit. Looking at the circuit in this way it can perhaps be used in part to teach and learn concepts in DC resistor networks such as Thevenin and Norton equivalent circuits, series/parallel resistors, KVL, KCL, voltage dividers and nodal analysis etc.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 30, Switch based analog representation of the circuit


There are nine possible combinations of the switches which give rise to the 8 Thevenin equivalent circuits shown in figure 31, with the ninth being of course an open circuit. It is important to note here that the resistance and voltage values given are for ideal nominal conditions and actual values may be noticeably different. It also assumes that the ON resistance of the MOS FET switches is zero which is actually never the case.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-digital-outputs_f4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 31, 8 Equivalent circuits


The first four cases are obvious. The next two are for the case where the 220 Ω resistor is connected in parallel with the 470 Ω resistor. The last two are for the case where the 220 Ω resistor is connected to ground and the 470 Ω resistor is connected to 3.3 V and the reverse.

A 9 level DAC can be created on each output pin by connecting an external resistor divider, R1, R2, as shown in figure 32. Using two 1 KΩ resistors as shown presents effectively a 500 Ω resistance to 3.3/2 (1.65) volts on one of the PIO connector outputs. This effective resistance to 1.65 V and the switchable equivalent circuits from figure 31 results in the 9 different output voltages shown in figure 32. Other values for R1 and R2 of course can be used to produce different ranges of output voltage.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/dio-dac-window.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 32, Nine level "DAC" interface window


Simply shorting two of the PIO pins together results in 9 X 9 or 81 total possible combinations. Many are redundant and some give the same voltage but with different source resistance values. Shorting all four pins together results in 6561 possible combinations using no external resistors. Limited only by your imagination and far more than can be listed in this document.

In addition when one or the other digital window is open the state of PIO 0, PIO 1, PIO, 2 and PIO 3 from left to right and are displayed in the Oscilloscope graphics area and are updated once each time the analog scope display is refreshed.

Steps performed by ALICE Desktop Self Calibration:
--------------------------------------------------

ALICE Desktop can perform a :doc:`self-calibration </wiki-migration/university/tools/m1k/alice/self-calibration-user-guide>` sequence.

Optional Features and Support for Plug-In Boards
------------------------------------------------

ALICE Desk-Top provides software interfaces advanced features and external plug-in boards which extend the functionality of the basic software and hardware. There are many types of :doc:`external boards </wiki-migration/university/tools/adalm1000/accessory-boards-index>` currently supported. External analog multiplexers to increase the number of analog input channels. External DDS based function generators such as the AD9837 based MiniGen from SparkFun. AD5626 serial 12 bit DAC from the :doc:`ADALP2000 parts kit. </wiki-migration/university/tools/adalp2000/parts-index>` External serial 8 bit DACs such as the AD7303 based `PmodDA1 from Digilent <http://store.digilentinc.com/pmodda1-four-8-bit-d-a-outputs/>`_. External digital potentiometers such as the AD840X single, dual, quad family or the AD5160 based `PmodDPOT from Digilent <http://store.digilentinc.com/pmoddpot-digital-potentiometer/>`_. A generic 3 wire SPI serial output interface.

The software interfaces for these can be enabled or disabled by setting the following variables to either 1 or 0 in the alice_init.ini file, see :doc:`ALICE Advanced User’s Guide </wiki-migration/university/tools/m1k/alice/desk-top-advanced-guide>` for more details.

| global EnableCommandInterface; EnableCommandInterface = 0
| global EnableMuxMode; EnableMuxMode = 0
| global EnableMinigenMode; EnableMinigenMode = 0
| global EnablePIODACMode; EnablePIODACMode = 0
| global EnablePmodDA1Mode; EnablePmodDA1Mode = 0
| global EnableDigPotMode; EnableDigPotMode = 0 global EnableGenericSerialMode; EnableGenericSerialMode = 0
| global EnableAD5626SerialMode; EnableAD5626SerialMode = 0
| global EnableDigitalFilter; EnableDigitalFilter = 0
| global EnableMeasureScreen; EnableMeasureScreen = 0
| global EnableETSScreen; EnableETSScreen = 0
| All of these optional add-on functions are set to 0 by default in the alice_init.ini file supplied with the Windows installer. When these variables are set to a 1 a button to open their respective control window will appear in the right side of the main ALICE window.

Multichannel analog interface for the ADALM1000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two analog input channels of the ADALM1000 provide a high input impedance and wide dynamic range which is very helpful for many of the measurements that a user would be making during laboratory activities. However, there are only the two analog inputs. Often, there are many more than two signals in the circuit under investigation that the user would like to monitor. Or there could be a number of low bandwidth sensors, such as ambient temperature or light levels around a room, that need to be measured or monitored over a long duration of time when gathering experimental data. As a solution to this need ALICE desktop provides the necessary software interface to control an external multi-channel analog multiplexer.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/analog-mux-curcuit.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 35, Generic Analog multiplexer


These two breakout boards from SparkFun based on `the 74HC4067 16:1 MUX <https://www.sparkfun.com/products/9056>`_ and `the 74HC4051 8:1 MUX <https://www.sparkfun.com/products/13906>`_ provide ready built off the shelf hardware. Design files for other M1k compatable multiplexer boards can be found in the :doc:`M1k Accessory Board </wiki-migration/university/tools/adalm1000/accessory-boards-index>` list.

**Hook-Up Guides**

-  For the :doc:`LTC1043 Switch Block </wiki-migration/university/tools/m1k/alice-ltc1043-analog-mux-ug>`
-  For the :doc:`CD4051 8:1 analog mux </wiki-migration/university/tools/m1k/alice-cd4051-analog-mux-ug>`
-  For the :doc:`CD4052 dual 4:1 analog mux </wiki-migration/university/tools/m1k/alice-cd4052-analog-mux-ug>`
-  For the :doc:`CD4053 triple 2:1 analog mux </wiki-migration/university/tools/m1k/alice-cd4053-analog-mux-ug>`

|image2| |image3|

.. container:: centeralign

   Analog multiplexer example schematics


**To access the external analog multiplexer controls in ALICE configure this line in the alice_init.ini file:**

global EnableMuxMode; EnableMuxMode = 1

The analog Mux control window is shown in figure 36. The CB voltage and current controls on the main scope window no longer function when this window is open and are replaced by the four new sets of voltage controls. The check boxes select which of the four Mux input channels will be displayed. The Mux-Enb checkbox sets PIO-2 either low ( when not checked ) or high ( when checked ) for Muxes like the CD4052 with enable low inputs or the ADG609 with enable high inputs.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/analog-mux-controls.png
   :align: center
   :width: 260px

.. container:: centeralign

   Figure 36, Analog Mux Control window


**Alternating Sweep Mode**

The analog Mux interface in ALICE desktop uses a technique common in analog CRT oscilloscopes ( with a single electron beam ) where multiple input channels are switched to the beam deflection circuits on alternating sweeps. This trick requires periodic signals and that each sweep be “triggered” or synced from the same input signal. In this case the triggering signal will be channel A which is not multiplexed. This could be either the AWG generator output of channel A or an external signal input to channel A in Hi-Z mode. Because it is assumed that a MUX is connected to channel B the AWG output function for that channel is set to Hi-Z mode and also since channel B is always a voltage input the current waveform display for that channel has also been disabled. As an example note the screen shot in figure 37.

**Chopping Mode**

A second Mux interface mode in the ALICE desktop uses another technique common in analog CRT oscilloscopes where two input signal are switched or chopped very quickly to the beam deflection circuits. In the case of the M1k we have a sampling system at 100 KSPS and we can use a square wave from the AWG channel A output to drive the Mux control input at 1/4 the system sample rate, or 25 KSPS. Thus each Mux input “gets” two samples. The software ignores the first of the two samples to allow for settling time and uses the second sample as the data. The software also up-samples the 25 KSPS data back to 100 KSPS using a 4X digital interpolation filter. The software automatically configures the channel A AWG settings. Once set these should not be changed while using the Chop Sweep mode.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/analog-mux-window.png
   :align: center
   :width: 720px

.. container:: centeralign

   Figure 37, Four channel Mux display of ALICE desktop


One important feature of the program is that a sync or sweep start pulse is output on the PIO 3 digital output pin just before each analog sweep starts. The sync pulse can be set to either a high going or low going pulse with the selector next to the pulse shaped icon. Using this “reset” pulse would be necessary whenever the alternating sweep function is used to observe a circuit that contains “state” for example a digital counter or state machine.

External DDS based function generators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ALM1000 has 4 general purpose digital input/output pins which can be used as a serial port (SPI). These pins are used to interface to direct digital synthesis (DDS) waveform generators such as the AD9837 and AD9833. These DDS generators are capable of producing sine, triangular, and square wave outputs. SparkFun offer a breakout board based around the AD9837 DDS called the MiniGen ($29.95).

In figure 33 we see that it is a relatively simple matter to connect the MiniGen board to the digital connector on the ALM1000. If a 6 pin right angle male header is installed as shown, the FSYNC, SDATA, and SCLK pins connect to PIO 0, PIO 1, and PIO 3 respectively. The other three header pins are open connections on the MiniGen board and the ground and power GND, The VIN pin can be wired to 3.3V and GND to GND with jumper wires. The solder bridge jumper, which shorts out the on board LDO, for powering the board directly from 3.3V will also need to be soldered in as shown. Installing a two pin female right angle connector to the analog output connection points is needed as well.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/mini-gen-connections.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 33 Adapting AD9837 MiniGen to ALM1000


The MiniGen control window, figure 34, allows the four possible waveform shapes to be selected. The master clock frequency can be set, the board comes populated with a 16 MHz crystal oscillator. And of course the output frequency can be set.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f21.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 34, AD983X DDS function generator controls


The MiniGen board produces a fixed 1 V p-p amplitude signal centered on the supply / 2 which is about 1.65 V in this case.

The AD9833 is a DDS waveform generator chip similar to the AD9837. The datasheet for the AD9833 indicates that the serial interface waveforms are the same as for the AD9837 and the configuration of the control, frequency and phase registers are the same as well so the ALICE Desktop interface will work for both devices by connecting which I/O pins map to FSYNC, SDATA and SCLK as needed.

**Using MiniGen with Bode Plotter**

As of the 6-19-2017 version of ALICE 1.1 Desktop it is possible to use the MiniGen as the sweep signal source for the Bode Plotter. If the MiniGen controls are opened before opening the Bode Plot window a third option will appear under Sweep Generator. The MiniGen has a fixed amplitude or 1 V p-p centered on one half the power supply, which is typically 3.3 V. The MiniGen is capable of generating much higher frequencies than the built in AWG sources. This allows sweeps all the way to just below the 50 KHz limit of the 100 KSPS.

External serial 8 bit DAC Pmods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital input/output pins can interface to the PmodDA1 4 channel DAC module sold through `Digilent <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,401,501&Prod=PMOD-DA1>`_ and other distributors such as `Mouser <http://www.mouser.com/ProductDetail/Digilent/410-063P/?qs=sGAEpiMZZMtWZAo%2fKf1JUOZxRUX4AaOJSE8oCSC4CQo%3d>`_.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmodda1-obl-400.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 35, PmodDA1


The PmodDA1 has two AD7303 8 bit dual voltage output DACs as shown in the block diagram in figure 36.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmodda1-block-336.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 36, PmodDA1 block diagram.


The module has a 6 pin male connector which plugs directly into the digital port on the ADALM1000. Because of the “Top” component side of the ALM1000 actually faces down the PmodDA1 also needs to be plugged in with the “Top” component side facing down. Carefully note the pin labels on both boards before plugging in the Pmod. The 6 pin header on the module lines up with the pins on the ALM1000 digital connector and all four of the general purpose I/O pins are used as follows. PIO 0 connects to the SYNC input on both DACs. PIO 1 connects to the data input on the first AD7303. PIO 2 connects to the data input on the second AD7303 and PIO 3 connects to the SCLK serial clock input on both DACs.

There is no external access to the reference input voltage on the DACs so they must generally be configured to use VDD/2 as the reference. In this case VDD is wired to the 3.3 Volt suppled on the digital port connector. The voltage output range for all four output channels will be 0 to 3.3 V.

The AD7303 DACs are also available in 8 pin PDIP packages and could be used plugged into solder-less breadboards with other components of a circuit project.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmod-da1-controls.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 37, PmodDA1 control window


Controls for the four DAC channels of the PmodDA1 are shown in figure 37. Enter the desired DC voltage(s) from 0 to 3.3 V ( less one LSB ) and click UpDate to send the new values to the DACs.

External digital potentiometers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD8402 dual 10 KΩ and AD8403 quad 10 KΩ digital potentiometer have 8 bit resolution and are available in PDIP packages that work well in solder-less breadboards. How to connect the AD8402 to the ALM1000 is shown in figure 39. The single 8 bit 10 KΩ digital potentiometer, AD5160, based PmodDPOT, figure 38, is also compatible with the same 6 pin male connector which plugs directly into the digital port on the ADALM1000. Because of the “Top” component side of the ALM1000 actually facing down the PmodDPOT also needs to be plugged in with the “Top” component side facing down. Carefully note the pin labels on both boards before plugging in the Pmod.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/pmod_dpot_top.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 38, PmodDPOT


Connections for the AD8402 dual pot are shown in figure 39. Connections for the AD8400 single and AD8403 quad are similar.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/ad8402-connections.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 39, AD8402 connections


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/dig-pot-controls.png
   :align: center
   :width: 290px

.. container:: centeralign

   Figure 40, Digital Pot control window


The digital potentiometer controls window has check boxes to select which of the up to four pots of the AD8403 are sent data. Each pot has a slider to control its value from 0 to 255. The radio button selects between the AD840X family which sends 10 bit data ( 8 bit value + 2 bit address ) and the AD5160 single pot which sends 8 bit data.

Generic 3 wire SPI output:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital input/output pins can output serial data to generic 3 wire SPI serial input devices. The provided interface allows the user to configure any of the 4 PI/O digital pins ( 0 – 3 ) as either the SCLK, SData, or Latch ( sometimes called CS or SYNC ) outputs. The user can set the number of bits to be sent in each digital write. The data word to be sent can be entered in either decimal ( integer ) form or Hex by using the 0x00 format. The “resting” sense, i.e. the level between writes, of the latch output can be set as well ( Latch Phase selector ). Some serial devices operate on the rising edge of the Latch (CS, SYNC) signal or on the falling edge. It is possible to select order in which the serial bits are sent, either LSB first or MSB first. The current data value is sent or written each time the Send button is clicked.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/serial-out-controls.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 41, Generic Serial Interface screen


Command Line Interface:
-----------------------

ALICE Desktop provides a simple command line interface for more advanced users who would like full access to the captured data and the inner working of the program and especially the Numpy library of array math functions. By default the button to activate this interface is not included in the Main ALICE window. To include the activate button, add the following line to the alice_init.inc file:

global EnableCommandInterface; EnableCommandInterface = 1

The interface is not complex to use if you are relatively familiar with Python syntax and the variable structure of ALICE. To execute more than function per line use a ; to separate commands on the single line. To execute the command line either hit the <enter> or <return> key or click on the Execute button. The last line successfully executed is displayed just below where it says Last command. A sequence of commands can be entered in a plain text file and run as a script by clicking on the Run Script button.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/command-line-window.png
   :align: center
   :width: 370px

.. container:: centeralign

   Figure 43 ALICE Command Interface


More advance information on the inner working of ALICE, variable and array names and the Numpy function library can be found in the ALICE Advanced User’s Guide.

One useful function that might come in handy is the Numpy function to write the contents of an array to a text file. For example, to save the VBuffA ( channel A voltage waveform buffer ) to a .csv file you would type:

numpy.savetxt(“my_data.csv”, VBuffA, delimiter=",", fmt='%2.4f')

Where “my_data.csv” is the name of the destination file, VBuffA is of course the data array to save, delimiter="," tells the function to use a , to separate the columns ( there won’t be multiple columns since most ALICE arrays are one dimensional ) and fmt='%2.4f' sets the format to 4 decimal places.

**For Further Reading:**

**Return to the** :doc:`Table of Contents </wiki-migration/university/tools/m1k>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/hookah-smoking_caterpillar.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/cd4052-analog-mux.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m1k/alice/adg609-analog-mux.png
   :width: 500px
