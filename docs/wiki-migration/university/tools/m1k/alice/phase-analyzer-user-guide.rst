Phase Analyzer Virtual Instrument for ADALM1000 in ALICE 1.3
============================================================

Objective:
----------

This document serves as the Phase Analyzer section of the User’s Guide in the ALICE 1.3 Desktop software interface written for use with the ADALM1000 active learning kit hardware.

Background
----------

There are many times where you are interested in measuring the phase angle and magnitude difference between two signals (sine waves). In most Circuits classes, students calculate phase difference using an oscilloscope by measuring the time difference between the zero crossings of two signals. This process can be tedious and prone to errors. Measuring phase is part of teaching phasor notation. Students have trouble going back and forth between phasor notation and time signals, at least in the beginning. Students are exposed to the same sort of gain / phase information from a Bode plot but in a different form.

There are specialized instruments for that, known as a Phase Analyzer. This is typically used in teaching power systems and power electronics circuits but general circuits classes can benefit as well. A virtual instrument has been included in the ADALM1000 tool kit in ALICE 1.3. A phase analyzer shows the phase relationships between two or more sinusoids in the complex plane, on a polar plot. Many professors teaching introductory circuits courses find a tool like this useful when students are first learning about phasors. The simultaneous current and voltage measurement functionality of the SMU in M1k makes adding this polar / vector display very inviting.

Phase Analyzer Virtual Instrument
---------------------------------

The ALICE Phase Analyzer virtual instrument display mode.

The corresponding time domain scope display is shown first in figure 1 for comparison.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Time domain scope display.


The Phase Analyzer uses the Time domain waveform data to calculate an FFT and extracts amplitude and phase information from that. The Time display must be actively running to display Phase information. The Phase display for the time waveforms in figure 1 is shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Phase Analyzer screen.


In the Phase Analyzer you choose one of the input signals to be the "reference." It is assigned 0 degrees and all other signals are measured with respect to this. The reference phase can be any of the four signals. The voltage and current vectors can be turned on or off. The scale for the voltage and current can each be adjusted. Other controls for the FFT work much like the impedance analyzer and spectrum analyzer.

Use Examples
~~~~~~~~~~~~

RC and RL Circuits
^^^^^^^^^^^^^^^^^^

In the circuit example shown in figure 2A, we have the CH-A output driving a series RL circuit (R=100 L=20 mH) and the CH-B output is driving a series RC circuit (R=120 C=2 uF). The CH-A voltage vector is used as the reference phase (set to 0). The sine wave amplitude for both channels is set to 1 Vrms (CH-A green vector, CH-B orange vector) and the current for channel CH-A in mArms is the blue vector. In the AWG controls the CH-B phase is set to 0 degrees relative to CH-A. The current for CH-B channel in mArms is the yellow vector. The two voltage vectors are both at 0 degrees and are plotted on top of each other.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig2a.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2A, Example Circuits


In the first example the two SMU channels are used independently to measure two separate circuits. In the second example SMU Channel A is connected to the same RL circuit but Channel B is now put in the Hi-Z mode and connected to measure the voltage seen across just the inductor. We also select the B voltage as the reference phase in order to measure the relative phase between the inductor current (cyan vector) and the inductor voltage (orange vector).

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Relative phase between inductor current and voltage.


Multiple Outputs Example
^^^^^^^^^^^^^^^^^^^^^^^^

While being able to plot the two voltage and two current measurements is helpful, there are use cases where these four signals are not enough to examine the operation of some circuits. ALICE 1.3 already has the ability to make use of an :doc:`external analog Multiplexer </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` (Mux) to expand the channel count to 5 voltages, plus the two currents (Three voltages if you use the LT1043 analog switch from :doc:`ADALP2000 parts kit. </wiki-migration/university/tools/adalp2000/parts-index>` parts kit). See this page on the :doc:`analog Mux M1k accessory board </wiki-migration/university/tools/adalm1000/accessory-boards-index>`.

The Phase Analyzer can also use this expanded number of channels. If the Analog Mux controls are opened first the Phase Analyzer controls will look like figure 4.

A very good use case example where the extra inputs is very helpful is looking at the standing wave pattern along an artificial lumped LC transmission line. This experiment board from the :git-education_tools:`education tools <experiment-boards>` on the ADI GitHub repository has 20 sections. The specific board tested is populated with 100 uH unit inductors and 47 nF unit capacitors.

Below in figure 4 we show the M1k with the mux board connected to one of the LC transmission line boards at 5 different taps more or less evenly spaced along the line.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, M1k plus Mux accessory board connected to lumped LC transmission line.


The screen shot in figure 5 shows the results. The green reference phase (always Ch A) is the first tap. The other four are more or less evenly spaced along the line with the last input, the yellow vector, on the final end tap. The line was terminated with a resistor = line impedance (no reflections). Frequency of the input set to about 6 Khz which seems to be about where 1/4 the wavelength = the line length (90 degree phase shift at the final tap).

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, M1k plus Mux accessory board connected to lumped LC transmission line.


It is also possible to plot the Channel A current vector at the same time which shows how "resistive" (or not) the input port of the line looks. In figure 6 the transmission line input current phase and amplitude with the end shorted is plotted along with the voltage amplitude and phase for the first 5 taps.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Plotting the transmission line input current phase and amplitude (end shorted).


One of the features in the Phase analyzer is the ability to save any or all of the amplitude and phase values to a comma separated values (csv) file. The Save Data button under the File menu will ask for a file name and then append the current selected data to the file if it exists or create a new file if not. If the Append option is checked the data will be appended to the last file name entered (without requesting a new file name). Once a list of vector values has been saved to a file the vectors can be plotted on the grid using the Plot From File button.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig6a.png
   :align: center
   :width: 400px

To gather data for the entire transmission line, the four Mux inputs were moved along the taps in groups of four. The values for three conditions, terminated, open and shorted, were saved to files. It is then possible to plot the values from the saved files back onto the grid. Figure 7 plots the amplitude and phase values for all 21 taps of the terminated line.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Phasor plot for all taps, terminated line.


The csv file was then loaded into Excel and after some minor editing a plot of the amplitude vs tap position was made as shown in figure 8.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Plot of amplitude vs tap position for Terminated line.


The same process was repeated for the open line case.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, Phasor plot for all taps, open line.


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, Plot of amplitude vs tap position for open line.


For the open line condition we can clearly see the standing wave pattern along the taps of the line with peaks at the beginning middle and end of the line as you would expect. The same process was repeated for the shorted line case.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, Phasor plot for all taps, shorted line.


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/phan-fig12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Plot of amplitude vs tap position for shorted line.


For the shorted line condition we can clearly see the different standing wave pattern along the taps of the line with nulls at the beginning middle and end of the line as you would expect.

**For Further Reading:**

**Return to the** :doc:`ALICE Main Page </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>`\ **.**
