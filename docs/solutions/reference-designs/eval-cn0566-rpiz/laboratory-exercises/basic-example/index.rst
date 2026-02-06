.. _cn0566_basic_example:

Controlling CN0566 (Phaser) from Python
=======================================

The purpose of this lab is to get acquainted with how the software controls
and captures data from the Phaser hardware. You COULD skip forward to the
calibration section in this lab, which is prerequisite for the subsequent
labs, but eventually you may want to write your own custom software, or at
least modify the provided example scripts. Rest assured, very little software
knowledge is required to understand this lab; it is intended to be the Phaser
equivalent of “Hello, World!”

Make sure that the Phaser hardware and software is set up according to 
:ref:`Phaser Overview and Setup <eval-cn0566-rpiz>`.

Finding the Source Frequency
----------------------------

There are two distinct ways to use the Phaser setup:

- With a source of unknown frequency, such as an HB100 microwave motion sensor,
  or more generally, receiving communications from one or more transmitters that
  are not locked to the receiver. This tends to give the sharpest nulls in the
  measured pattern.
- With the CN0566 itself providing the signal on one of the TX outputs, fed to
  an antenna. This is required for FMCW RADAR applications, but is also
  convenient for pattern measurements. The drawback is local leakage limits the
  depth of the nulls in the pattern.

Most of the scripts only examine a few MHz worth of bandwidth at a time, while
the HB100 frequency can vary by several tens of MHz. Thus it is essential to
know the frequency of the source. The cn0566_find_hb100.py script sweeps
several 10 MHz wide bands and attempts to locate the peak frequency. Open the
script in Thonny and run it. (The script can also be run from the command line
if preferred). Typical results are shown in Figure 1.

.. figure:: find_hb100_step_1.png
  
  Find HB100 script

Ideally, there should be a single, sharp peak. If there are several peaks or no
visible peak, close the plot and enter ‘n’ at the prompt. Reposition the HB100
(and make sure there are no other sources nearby), then re-run the script.
Another method to ensure that the correct source is being identified is to run
the script several times, moving the HB100 toward or away from the antenna. The
peak should increase and decrease accordingly. Once the correct peak has been
identified, enter ‘y’ at the prompt as shown in Figure 2. This will save the
frequency to a calibration file that other scripts and GUIs will read in.

.. figure:: find_hb100_step_2.png
  
  Saving Frequency Calibration File

Running the Minimal Example
---------------------------

- Aim the HB100 at the Phaser.
- Open the cn0566_minimal_example.py script, either in Thonny, or run from the
  command line.
- Observe the output, which should look similar to the figure below:

.. figure:: minimal_example_output.png
  
Here’s what we’ve done:

- Received the 10.525 GHz signal
- Downconverted it to 2.2 GHz
- Received the 2.2 GHz IF with the Pluto SDR
- Set the Pluto’s internal PLLs to 2.2 GHz minus a small offset
- Set the Pluto’s ADC sample rate to 30 Msps
- Loaded a 20 MHz wide digital filter into the Pluto
- Capture a buffer of 1024 samples
- Plot the time domain samples
- Take the FFT of the samples, then plot.

So what does that Python script do?? The python script,
“cn0566_minimal_example.py” first takes care of some housekeeping operations -
set the antenna to zero phase, equal gain on all elements, and set a few
parameters in the Pluto SDR. Then we are simply plotting the buffers of data
from Pluto.

Next, change the “offset” variable (line 176) to something between -10e6 and
+10e6 (your choice!). Re-run the script and verify that the tone moves along
the horizontal axis accordingly.

Calibrating Element Gain and Phase
----------------------------------

The phaser board is initially uncalibrated; each element will have a slightly
different gain and slight phase error due to numerous factors. This was fine
for finding the HB100 frequency and the minimal example, but the performance
of the subsequent labs requires that each element have a predictably
controllable gain and phase, with respect to other elements in the array.
Since there will always be both gain and phase mismatch due to manufacturing
tolerances, we’ll compensate for this in software.

For the gain calibration, we’ll illuminate the array with the HB100 held far
away, and at mechanical boresight (zero degrees). One element at a time will
be set to its maximum gain, which is done by setting the ADAR1000 gain for the
associated channel. All other elements are set to zero. The resulting signal
level for each element is measured, and the element with the minimum gain is
chosen as a reference. A factor is then calculated for the other elements,
which are used to equalize their gains to that of the lowest gain element.

For the phase calibration, two adjacent elements are set to the maximum
calibrated gain. The phase of one of the elements is then swept from 0 to 360
degrees. The phase that produces the minimum null is 180 degrees away from the
phase that will match the two elements (nulls are much sharper than peaks, and
can be measured more accurately.) Each adjacent pair is measured, and an array
of phase compensation values is generated.

The cn0566_examples.py script provides a calibration utility that will
generate calibration files. Place an HB100 (or antenna connected to J1) facing
straight at the antenna array from approximately 1.5m away. Then run:

::

   python3 cn0566_examples.py cal

The script provides debug information and plots as it is running, you may have
to close out of each plot for the script to proceed. Calibration is not an exact
science, and is subject to noise, interfering signals, reflections from nearby
objects, and other impairments. But in general, plots from an acceptable
calibration run will have the following features:

- Gain plots will show eight impulses near the middle of the horizontal axis.
  The lowest impulse should be no lower than about 70% of the higherst impulse.
  Note that impulse may tend to be grouped into two groups of four, with each
  group representing one ADAR1000.
- Phase plots will show seven arcs centered around zero degrees, with nulls
  between -180° and -135° or between 135° and 180°.

  Typical plots are shown in Figure 3.

  .. figure:: gain_phase_cal_plots.png
    
    Gain and Phase Calibration Plots

After running this script, files gain_cal_val.pkl and phase_cal_val.pkl will
be placed in the working directory. The GUI program will also load these files
automatically.

If plots differ greatly from Figure 3, examine the physical setup, reposition
the source or antenna, remove interfering objects, and re-run the script.
