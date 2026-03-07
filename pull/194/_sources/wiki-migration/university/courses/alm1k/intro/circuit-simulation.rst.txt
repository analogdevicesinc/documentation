Activity: Circuit Simulation with LTspice - ADALM1000
=====================================================

Objective:
----------

The objective of this activity is to gain experience with the tools electrical engineers use (i.e. electronic test and measuring equipment and the analysis software) and to gain some fundamental understanding of voltage dividers.

Background:
-----------

| Before doing this experiment, students should be able to
| - Determine the values of resistors connected in series and parallel
| - Identify the audible frequency range in humans
| - Identify the value of standard resistors from the ALP2000 kit by color code
| - Download and install ALICE desktop software on a Windows machine
| - Download and install LTspice software on a Windows machine

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless Breadboard
| Jumper wires
| 3.5mm headphone jack adapter
| Headphone or ear bubs (loudspeaker as option)

Sine Waves and Hearing
----------------------

In this part of the activity, the ADALM1000 waveform generator will be used to produce electrical signals with various shapes, including sine waves. The objective is to learn about the basic properties of sine waves and related signals by visualizing them vs time with the oscilloscope tool and hearing them by connecting the generator output signal to headphones / ear buds. You will need a set of ear buds or something similar such as the loudspeaker from the ALP2000 part kit to hear the audio.

We will also demonstrate some interesting facts about human hearing.

Equipment:
~~~~~~~~~~

What formerly would require the use of an entire benchtop of instruments can now be accomplished using the ADALM1000 (see figure 1) and a laptop computer. This hardware module, coupled with the ALICE Desktop software, can produce the same functionality as each of the following pieces of equipment (and more): a two channel oscilloscope (scope), a digital voltmeter (DVM), two DC power supplies and a two channel waveform generator. The digital voltmeter (DVM) has 2 channels. The oscilloscope is a measuring device that lets you view a graph of a voltage or current signal vs time. The DC power supplies generate constant DC voltage signals (like a battery). The waveform generator creates a voltage signal that varies with time. The computer is an integral part of the equipment setup. You use it to simulate many of the circuits you will build (using the LTspice program), as well as to control the ADALM1000 hardware.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, ADALM1000 hardware


The waveform generator can be programmed to generate signals with specified amplitude and frequency. Ear buds (headphones) or loud speakers convert an electrical signal to sound that can heard. The oscilloscope displays a graph of an electrical signal and further analysis can be performed. The combination of the oscilloscope and audio output allows us to see what we are hearing. The two waveform generators are labeled as CH A and CH B. Only one of the waveform generators will be used in this activity to start. See

The sine wave equation:
~~~~~~~~~~~~~~~~~~~~~~~

Everyone should have studied the sine and cosine trigonometric functions in math and physics classes. A sine wave is described by an equation of the form v(t) = A sin(2πft) = A sin(ωt), where the variable t represents time. We use the term "wave'" because the up and down shape is similar to a water wave that you might see in a body of water. Shown in figure 2, a sine wave is characterized by two parameters, called amplitude (A) and frequency (f). The amplitude A determines the maximum value that the sine wave achieves along the vertical axis. The sine wave takes on values between +A and -A at various times. In electronics the value might be the voltage or current in a circuit.

The frequency f of a sine wave can be understood like this. The sine wave reaches its peak value of +A at regular intervals in time. The time between peaks is called the period of the sine wave. The letter T is used to denote the period and it is measured in seconds (Sec). The frequency is defined as the number of times that the sine wave reaches the peak value per second. Since adjacent peaks are separated by T sec, the wave has 1/T peaks per second. The frequency f is then equal to 1/T. The units of frequency are sec\ :sup:`-1`. Another name for the unit sec\ :sup:`-1` is Hertz, or abbreviated as Hz. Another way to denote the frequency of a wave is the product 2πf or ω, where ω is called the angular frequency in electronics. (In physics, ω is the rate of change of the angle in a rotating system, called angular velocity.) Note that one of the most common mistakes made is confusing frequency f and angular frequency ω.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2. Sine wave with amplitude A, frequency f, and period T.


Including a DC offset:
~~~~~~~~~~~~~~~~~~~~~~

If a DC offset voltage is added to the sine wave signal it moves the entire wave up or down such that it is no longer centered around 0 but is instead centered on the DC voltage, V\ :sub:`DC`. The equation becomes v(t) = A sin(2πft) + V\ :sub:`DC`. In electronics, the AC and DC parts of a signal can be treated as two separate and distinct parts of the waveform.

Scalar measurement of sine waves:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Measurement devices may not give us the amplitude, A, directly. It is relatively easy to read off the maximum and minimum values of a waveform on an oscilloscope screen. This will likely include any DC offset. The DC offset is generally taken as the average voltage over one (or more) whole cycles. The difference between the maximum and minimum values is V\ :sub:`P-P` (the peak-to-peak voltage) so it should be nearly equal to A - (-A) = 2A. The RMS voltage, V\ :sub:`RMS`, is determined by taking the square root of the sum of the voltage squared over one cycle. If the voltage waveform is a sinusoid this reduces to:

:math:`V_RMS = V/sqrt(2) = V/1.414`

Impedance and resistance:
~~~~~~~~~~~~~~~~~~~~~~~~~

Everyone should be familiar with the term resistance at this point. It is a measure of the degree to which a circuit component like a resistor resists the flow of current. Circuits that have a combination of components (some of which are not simple resistors) also affect the current. The behavior of such circuits is more complicated because it changes with the frequency of the signal. We call this complicated response “impedance.” Both resistance and impedance are measured in Ohms (Ω) and the terms are often used interchangeably.

Human hearing:
~~~~~~~~~~~~~~

We are exposed to a wide variety of sounds every day. We hear a sound after our brain processes the sensations detected by our ears. Two attributes that are commonly used to characterize sounds are loudness (amplitude) and pitch (frequency). Loudness, of course, refers to how loud or intense we perceive the sound to be. Pitch refers to whether we perceive the sound to be high or low. For example, the sound produced by a piano key to the right side has a higher pitch than the sound produced by a key on the left. Keep in mind that the human ear is a biological system. It is designed to hear certain pitches better than others even though, technically, they have the same loudness.

Experiment
----------

Setting up a Sine Wave on the waveform generator:

For the first step, we need to set up a sinusoidal voltage. Set up the ALM1000 to generate a signal from waveform generator A and measure it with scope trace CA-V. The output of the generator and input of the scope are by default connected internally on the same ALM1000 pin (CH A in figure 1) so no external connections are needed.

After correctly installing the ALICE Desktop software and connecting the ALM1000 to a USB port, open the software. You should see the windows similar to that shown in Figure 4 for the waveform generator controls and the oscilloscope. The values for various parameter settings shown in both windows will likely be different. You will adjust those now.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-3.png
   :align: center
   :width: 800px

.. container:: centeralign

   Figure 4 ALICE Screen.


Waveform Generator:
~~~~~~~~~~~~~~~~~~~

We only need one waveform generator in this experiment. Note that we will use the term waveform generator and AWG (Arbitrary Waveform Generator) pretty much interchangeably. The AWG can produce any time-varying signal, so the term arbitrary, but we mostly use it to produce sine, triangular and square waves like a function generator.

First the frequency is set. The frequency of the function generator is adjusted as follows:

Set the Freq Ch A entry to display 1000.

Set the Max Ch A entry to 2.7. Set the Min voltage Ch A entry to 2.3. This will produce a waveform with a 0.2 V amplitude centered on 2.5 V. The AWG has three modes, SVMI (source voltage, measure current), SIMV (source current, measure voltage) and Hi-Z. For this step select the SVMI mode. Under the Shape menu the Sine shape should be checked.

Your AWG window should look like Figure 5. Only the Min, Max, and Freq settings for AWG CH A matter at this point. The settings under AWG B can be anything at this point.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-5.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 5, AWG settings.


Scope:
~~~~~~

Make sure trace CA-V is selected under the curves drop down menu. Uncheck CB-V, since we will not be using channel B.

First we set up the vertical and horizontal scales for the display. On scope channel CA, select the Volts/div to 0.5, the offset to 2.5. The CA V Pos should be set to 2.5 (center of grid). The Time/div should be set at 0.2 ms/div. The vertical (voltage and current) scale settings are found at the bottom and the horizontal time scale settings are found at the top of the scope window.

When you are ready, press the green “Run” button on the Scope screen.

It is useful to know how to copy plots and paste them into a word processor. In the upper right hand corner, under the Files menu, select save screen and you can save the Oscilloscope screen to an encapsulated postscript file. Or you can use a screen snap shot tool such as the Windows Snipping tool to grab the scope screen image and paste it directly into your laboratory report. Save a copy of the Oscilloscope plot for your report.

Change the frequency setting up or down as desired. The mouse wheel is useful for doing this when hovering inside the Freq entry spot. How does this change the signal trace displayed on the scope? The purpose of this step is to see what kind of signals this setup can produce. You should play around a little with different frequencies, voltage amplitudes, signal shapes, etc.

Set the AWG again so the Freq display reads 1000 and the amplitude is 0.2 V (centered on the 2.5 V DC offset). Copy screen as an image and paste it in your report document. Clearly label both the amplitude and period as well as the DC offset of the signal you have measured.

Connecting the Output from AWG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now wish to connect the waveform generator, scope and earphones to perform some simple experiments.

The ADALP2000 Analog Parts Kit includes a 3.5 mm audio connector break-out-board, figure 6, that can be inserted in a solderless breadboard. The board pins are numbered 1-5. Pin 4 is the sleeve (ground), Pin 2 is the tip (left audio) and Pin 3 is the ring (right audio).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-6.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 6, stereo audio connector break-out-board


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, connecting an audio connector to AWG


There are typically two types of connectors used for earbuds, depending on whether or not a microphone is included. Both are shown in figure 7. If you have the three connection style plug then adapter pins 1 and 4 will be shorted together.

Start by measuring the resistance of each channel for your ear buds or earphones (from left or right to common) using a handheld DMM or the ALICE ohmmeter tool. We only need an approximate value for the resistance, so any meter can be used for this purpose.

To use the ALICE ohmmeter, open the Ohmmeter tool on the right side of the Scope main screen.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-8.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 8, ALICE Ohmmeter


Connect either the right or left pin of the headphone jack and the common pin of the headphone jack to CH A and CH B respectively on the ALM1000 connector. In the ohmmeter controls make sure the Int option is selected for the Known Res and the Known Res value is set to 50 (the value of the internal resistor). Set the test voltage to about 2 or 3 volts so as to not send too much DC current through the headphone element. After you double check the connections and settings click on Run. You should see an Ohms reading somewhere between 15 and 45 ohms depending on your headphones. Be sure to Dismiss the Ohmmeter controls after you are finished measuring the resistance of your headphones.

Connect the adapter jack to the ALM1000 connector as shown in figure 7. Double check to make sure the AWG settings are set as earlier in Figure 5 (Sync AWG box not checked). Run the Oscilloscope and confirm you are seeing the 200 mV amplitude sine wave.

Plug your ear buds into the headphone adapter jack. Do not do this with the ear buds in your ears. The volume may be too high. It is best to turn on the (enable) the generator with the ear buds away from your ears and bring them closer until you are sure the volume level is comfortable. You should hear only one channel. If you use both AWG sources you will hear both channels.

Adjust the volume of the signal to a comfortable level by changing the Min and Max values of the signal. Be sure the keep the values centered around 2.5 as best you can. By comfortable level, we mean the lowest amplitude that allows you to hear a distinct sound. What is the value of the voltage amplitude that you have selected?

You can also display the current flowing in your headphones by selecting the CA-I trace from the Curves drop down menu. You can adjust the vertical range for the current trace as needed. Compare the maximum current you measure with what you would calculate using Ohm's Law and the voltage amplitude and headphone resistance you measured earlier.

Let's investigate how our perception of loudness changes as the frequency of the sine wave is varied. With the sine wave amplitude fixed at your comfortable level, vary the frequency over the range from 100Hz to 10,000Hz. Try cycling through the following frequencies, without changing the signal amplitude: 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, and 10,000Hz. Does the maximum (peak) current change with frequency?

Which frequency do you hear the loudest? Is there any variation among other class members? If you have problems discerning significant differences in loudness, try a different set of ear buds.

Experiment with the Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this point, you will have put the waveform generator and scope through some basic tasks. Experiment with the other features of the AWG and see what happens. Some very interesting and annoying sound waves can be produced. Play around a little and then find a particular set of operating conditions that you find the most interesting. Under what circumstances might you experience the sounds you have produced or generally when might you encounter a waveform like the one you have displayed on your scope?

Summary
~~~~~~~

You should now know how to set up voltage signals with the waveform generator controls and display them using the oscilloscope. Connect the generator output to a headphone jack and headphone. You should understand the pitch/frequency and amplitude/volume relationships, and know how these relate to human hearing.

Introduction to LTspice
-----------------------

In this section we will learn about the circuit analysis software we will use as our primary simulation tool. You should download and install this software on your laptop. It is recommended that you install the latest version. LTspice may be downloaded from the :adi:`LTspice Home Page <ltspice>`. This page includes additional information about LTspice, documentation, articles,etc.

Learning more about LTspice
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the material on the LTspice home page, the following slide deck is available for either self-guided learning or presentation in a classroom setting.

A slide deck is provided as a companion to this exercise, and can be used to help in presenting this material in classroom, lab setting, or in hands-on workshops.

.. admonition:: Download
   :class: download

   `LTspice Basic Lab Class Slide Deck <https://wiki.analog.com/_media/university/courses/electronics/ltspice/ltspice_basic_lab_class_03-18-19.pptx>`_


.. _background-1:

Background
~~~~~~~~~~

The software we will be using to simulate the operation of circuits in this lab activity is called LTspice which uses information on a circuit in the form of a schematic and analyzes how it will behave. When placing parts in the circuit, resistors, capacitors, inductors, diodes and wires all have their own symbols in the menu. All other parts are accessed through the “Place Components” button. See figure 9. Once the parts are placed, their values must be specified. This is usually done by right clicking your mouse on the circuit element or one of its parameters. Once the circuit is complete, the simulation must be setup. This is done through the 'Simulate' drop down menu. The example below shows a transient simulation that runs from 0 to 5ms with a maximum step size of 1µs. Once the simulation is run, it displays an output similar to what you would see if you hooked the circuit to an oscilloscope. Figure 10 contains a sample waveform diagram.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-9.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 9. Example Schematic main page


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-10.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 10. Simulation result


Experiment (Simulation)
~~~~~~~~~~~~~~~~~~~~~~~

\**Opening a New Simulation \*\*

In this part of the experiment, we will draw the simple circuit we have been studying, a combination of resistors and a sinusoidal voltage source representing a resistive divider.

\**Run the “LTspice” program \*\*

It will open with no schematic or simulation loaded. Click on the File pull-down menu and select New Schematic. You will name your project when you save it. You should also decide where you want to save schematics. You will have to choose a directory when you save your work.

\**Drawing a Circuit \*\*

Figure 11 is the LTspice main screen with the circuit we will be drawing. Note that this is the circuit used in the resistor divider activity including the input resistance of one channel of the ADALM1000 as R3.

In the circuit shown in figure 11, we have some resistors, a sinusoidal voltage source, a ground and some wires. To create this diagram, we will use the command buttons. For the resistors we will click on the button that looks like a resistor. You can also do this by using the Edit menu or by hitting the R key. You should see a resistor symbol that you are free to place anywhere in the schematic. The Edit menu also shows you what name goes with every symbol. For the ground, select the ground button, use the Edit menu or hit the G key. For the voltage source and most other components, you have to use the component button (which can also be selected from the Edit menu) and then pick Voltage from the many options offered.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-11.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 11.


When you have finished placing resistors or doing just about anything else, hit the Esc key to get back to the basic diagram.

When you have placed all resistors, the voltage source and the ground, connect everything with wires. Access wires by clicking on the symbol that looks like a pencil, next to the ground button.

To complete the schematic, we have to change the component values. Each resistor was given a name in the order it was placed on the diagram. Thus, your resistors may not have the same names as shown in the figure. For simplicity, they will be referred to by the name shown here and you can change the names if you wish the same way their parameter values are changed.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-12.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 12. Change resistor value


To change R3 to 1Meg Ohm, right click on the bottom R and you should get the window shown in Figure 12. Change the R to 1MEG. If you find that the number or anything else is in a hard to read position on the circuit diagram, move it with the mouse by first clicking on the Move button that looks like an open hand. When you type the value of the resistance, you must type 1Meg with no spaces. Note that you have to type Meg since SPICE uses M to mean 10\ :sup:`-3` (milli) and Meg for 10\ :sup:`6`. It is not case sensitive. Note that in the schematic pictured, R1 and R2 are the resistors in your voltage divider and R3 represents the impedance of the scope input. Since the scope impedance is 1 MΩ, R3 should be 1Meg. R1 and R2 should be 1k Ω.

After you have changed all the resistor values and moved them to neat and readable positions, you must set up the voltage source. In LTspice, voltage sources are DC by default. To specify the source as sinusoidal, right click on the voltage source symbol and select the Advanced button. The window in figure 13 will appear. Select SINE and then set the values shown for offset, amplitude and frequency. Once the symbol is labeled as SINE, these parameters can be changed by right clicking on the symbol. The values are used to label the voltage source as shown in figure 11.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 13.


\**Setting Up the Analysis \*\*

After all the components are defined, wired up and their values are set appropriately, you are ready to run a simulation.

Find the Simulation drop-down menu and click and select Edit Simulation Cmd. You will get the window shown in Figure 14. Select the tab for the type of analysis you wish to perform. In this case it is Transient since we are interested in output that is vs time like a scope. The simulation will begin at time t = 0, but we can choose to start saving data after that. Thus, we specify the Stop Time (the end time of the simulation), the Time to Start Saving Data, and the Maximum Timestep (the resolution of our simulation). Here we choose, 5ms, 0 and 1µs, respectively. Note that there is no µ so we have to use the letter u.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-14.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 14.


The final time (Stop Time:) has been set at 5ms because the period of a 1 kHz sine wave is 1 mSec. This allows us to simulate five periods of the sine wave. The Maximum Timestep needs to be set so that you get a reasonable representation of the output. A step size that is too small will take a long time to run, a step size that is too big will give you an under-sampled representation of the output. A step size between 1/100 to 1/1000 of the run time is reasonable. The analysis will begin saving data at 0 seconds. Note again that there should never be any spaces between the number and its units. Click on the OK button when you are finished putting in the numbers. You will be able to place the information on the simulation anywhere on your circuit. Choose a space where it is easy to read and does not block anything else.

When you have finished, you can run the simulation either by clicking the button that looks like a little person running or select Run from the Simulation drop-down menu.

\**Transient Analysis \*\*

You are now ready to run the simulation.

Click on the Run button. A set of axes with no signals shown will appear. You can now add voltages where ever you wish by left-clicking with your mouse. You will see that whenever you hover over a wire in the schematic with your mouse, a symbol like a voltage probe will appear. Click on the wire you want to know the voltage. If you want to plot current, hover over a device symbol and your mouse symbol will change to a current probe. If you click on a device, the current through it will appear on the plot. In the plot shown in Figure 15, the input and output voltages for the voltage divider are displayed. Note that the ratio between the two is what you should expect for this simple circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-15.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 15.


You should get something like (but maybe not identical to) the window shown in figure 15. The voltage divider expression we used in the voltage division activity can be applied to sinusoidal signals as well. For sinusoidal signals, the amplitude of the sine wave changes based on the voltage divider ratio. We can then perform the same comparison between source voltage amplitude and resistor voltage amplitude as we did where we compared the source DC voltage and the resistor DC voltage. For the 1 kΩ voltage divider circuit, do we see the same ratio of voltage amplitudes as seen for DC voltages?

It is also useful to know how to copy plots and paste them into a word processor. Under the Tools menu, click on “Write image to .emf file”. Now there is a .emf file saved that you can insert into a word processor. Open your word processor and paste the image somewhere. Save this file or print the output plot for the 1k voltage divider directly. You should see a plot like the one shown in figure 16. If you get the schematic instead, click your mouse on the voltage plot window to select it and try again.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro-simulation-fig-16.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 16.


The "Copy bitmap to clipboard" and "Write image to .emf file" options under the Tools menu can be used to capture either the schematic drawing or waveform plots. By default the waveform lines on the plot can be a bit thin and hard to read. You can change the data display on the plots generated by selecting Control Panel from the Tools menu and then selecting Waveforms. Select Plot data with thick lines. They will be much easier to see.

Change the values of the resistors in the voltage divider to 1 Meg and rerun the simulation. Save or print this plot as well. Both plots should have two traces: the source voltage, and the voltage across the resistor closest to ground. For the 1 MegΩ voltage divider circuit with the 1 MegΩ probe resistor, do we see the same ratio of voltage amplitudes as seen for DC voltages? Try varying the frequency, amplitude and offset of the V1 SINE source one at a time and rerun the analysis. What happens to your signal? Is the amplitude ratio still the same? Does it make sense based on your knowledge of sine waves and voltage dividers?

Show your results for the 1 Meg simulation to a TA or instructor and have them check-off on your hand-drawn circuit diagram for this simulation.

| For this and other activities in this course, you must explain:
| - the purpose of the data (using your hand-drawn circuit diagram),
| - what information is contained in the plot and
| - why you believe that the plot is correct.

.. _summary-1:

Summary
~~~~~~~

LTspice is a very powerful simulation tool meant to address the circuit simulation needs of all engineers who must do circuit design and analysis. Thus, there are many, many opportunities to make what seem like silly mistakes that prevent the analysis from working properly. In your first attempt at using these tools, it is likely that you have already made some of these mistakes. You should also have heard about some of them in class. What mistakes did you make?

\**For Further Reading: \*\*

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
