.. _cn0566_software:

CN0566 Software User Guide
==========================

There are several pieces of software used with the CN0566 Phaser, including a
user-friendly Graphical User Interface (GUI) and a number of command-line
utilities. These are located in the pyadi-iio examples folder. Assuming the
pyadi-iio repository has been cloned to user analog’s home directory, the path
to the cn0566 examples is:

::

   analog@phaser:~/pyadi-iio/examples/cn0566 $

Configuration and Calibration files
-----------------------------------

There are several calibration and configuration files that the software uses.
Calibration files are generated as described in `CN0566
Calibration </resources/eval/user-guides/circuits-from-the-lab/cn0566/calibration>`__,
and are as follows:

::

   hb100_freq_val.pkl - Measured frequency of microwave source
   gain_cal_val.pkl   - Gain calibration coefficients
   phase_cal_val.pkl  - Phase calibration offsets

While these are intended to be generated once and re-used each time a program is
run, they are easy to recreate as the physical surroundings change - microwave
reflective surfaces, distance between the phaser array and source, changing
between the onboard transmitter or independent microwave source, etc. If these
files are deleted (or not present in the first place), default values will be
used.

The **config.py** file contains parameters for the operation of the phaser,
including signal frequencies, sample rates, bandwidths, etc. This file can be
edited directly, after which any software using it must be restarted.

As a convenience for staying consistent with the Pyadi-iio Git repository, the
config.py file can be copied to **config_custom.py**. If present, software
will use config_custom.py - this file can be edited without affecting the Git
repository.

GUI operation
-------------

The GUI can be launched either from the command line or from the Thonny IDE.
From the command line, run the following command:

::

   python3 cn0566_gui.py

which will print debug information to the console as shown below. In this
case, gain and phase calibration files were not present, but a frequency
measurement file for an HB100 was found.

**Typical console output:**

::

   analog@phaser:~/pyadi-iio/examples/cn0566 $ python3 cn0566_gui.py 
   file not found, loading default (all gain at maximum)
   file not found, loading default (no phase shift)
   Gain cal:  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
   Phase cal:  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
   Didn't find custom config, looking for default.
   Found signal freq file,  10495859375.0
   Running on Linux, connecting to  ip:localhost  and  ip:192.168.2.1

The GUI will launch and display an FFT of the incoming signal, with the beam set
to maximum gain, steering angle of zero.

.. figure:: phaser_gui_overview.png

   GUI overview (FFT plot)

If no signal is present, this indicates that the frequency is not set
properly, or if you are using an antenna connected to J1, the “Transmit
Disabled” is selected. If using an HB100, run the cn0566_find_hb100.py script
again.

Switch to the Rectangular Plot and select ``Enable All`` in the drop-down menu.
An uncalibrated beam pattern will be displayed, which typically appears as a
distorted SINC1 pattern.

.. figure:: phaser_gui_uncalibrated.png

   Uncalibrated Beam Pattern

Close the GUI, Run the calibration routine to generate calibration files:

::

   python3 cn0566_examples.py cal

Then re-start the GUI. The beam should be much closer to ideal, with first side
lobes approximately 13dB below the main lobe.

.. figure:: phaser_gui_beam_pattern.png
   
   Beam Pattern After Calibration

Much more detail on each control panel, walk through each experiment.

CLI example operation
---------------------

A command line example is also provided. The main purpose for this script is to
provide a template for developing additional custom programs (CLI, GUI, or
other), as well as interacting directly with the CN0566 from the Python console.
Run:

::

   python3 cn0566_examples.py

The script will continuously take beam pattern measurements, and plot a
representative time-domain and frequency-domain plot at mechnical boresight.

.. figure:: cli_plots.png

   CLI Plots

Detail on CL options, interactive operation from the
Python console, calibration, etc.
