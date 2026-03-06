Activity: Data Analysis, For ADALM1000
======================================

Objective:
----------

The objective of this activity is to add to our data analysis skill set so that measurements made on the lab bench can be easily plotted and analyzed with simple software tools.

Learning Outcomes: Students will be able to

-  Plot experimental or simulated data with ALICE and LTspice
-  Generate diode I-V plots for signal diodes and LEDs
-  Plot load lines on diode I-V plots and solve for the operating point

Resources Required:

-  LTspice simulation software
-  ALICE desktop software
-  gnuplot plotting software
-  ADALM1000 learning module
-  ADAML2000 Parts Kit

Basics:
-------

Before beginning this activity, review your work on diodes. In experiments Diodes Part 1 and 2, you measured the voltage and current characteristics of the series combination of a resistor and a diode driven by the ADALM1000 function generator. In the first part on diodes, you should have saved a csv file containing data on diode voltage and current near the end of Part A. In Exp 9, the data was also saved near the end of Part A. Be sure to complete all steps below first for the signal diode 1N914 and then an LED. If you did not save this data, you will have to obtain it again.

Combining LTspice Simulations with ALICE Scope traces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Circuit simulators like LTspice, and others, are useful tools for testing out electronic circuit experiments before actually constructing the circuit. The ADALM1000 and ALICE Desktop is a multi-purpose and incredibly useful set of measurement tools for testing electronic circuits. In this Blog entry we are going to go over a simple example showing how to run a simulation in LTspice, export the simulated voltage waveforms and then load them into ALICE so they can be compared to the measured voltage waveform you get on the actual circuit. By comparing simulated and actual results you can get the most out of this powerful combination of software and hardware.

The first thing to do is enter the following simple RC circuit, shown in figure 1, into LTspice. The resistor, R1, we are using is 10K ohms and the capacitor, C1, is 0.22 uF. A PULSE source is used to simulate the CHA output of the ADALM1000 and a 2.5 V DC source is used to simulate the fixed 2.5 V rail. We will name the output of the pulse as CHA and the voltage on the capacitor as CHB to match the ADALM1000 connections.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-schematic-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1,


The transient simulation will be run from 0 to 20 mSec. Which will be exactly 2 cycles at 100 Hz (10 mSec period).

We use the .wave directive to output the two node voltages of interest. The sample rate is set to 100KSPS to match the sample rate of the ADALM1000. The data values saved in the wave output will be 16 bit integers scaled from -1 to 1 volt. So the pulse high and low values are set to -0.8 and 0.8. When ALICE imports these integers it offsets and scales the values to 0 to 5 V to fit exactly in the ADALM1000 voltage range. So -0.8 V becomes 0.5 V. 0.0V becomes 2.5 V and +0.8 V becomes 4.5 V.

After running the simulation the results should look like the following plot.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, RC simulation plot


There should also be the saved output.wav file that now contains the two simulated waveforms.

Now we can open ALICE and measure the actual circuit. With a 10 KΩ resistor and 0.22uF capacitor connected to the ADALM1000 as shown in the schematic. We can setup CHA to output the 100 Hz square wave. In CHA, set the Min value to 0.5 and the Max value to 4.5 with the Mode set to SVMI and the shape to Square. For right now we can set CHB mode to Hi-Z.

With the Horz time scale set to 2 mSec/Div we can run ALICE and see the measure results of the circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Measured RC plot


This plot looks a lot like the simulation but just how close are the two? To compare the two we next save snap-shots of the live waveforms and turn them on. The saved reference traces are drawn in a darker color so the plots will look like this.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4,


We can load in the output.wav file from the LTspice simulation and play the data back through the arbitrary waveform generators of the ADALM1000. Under the AWG CH A Shape drop down menu we can click on Read WAV File. It will prompt you for the file to load. Navigate to where output.wav was saved and click on it. The wave file contains two signals so the program puts the first one (the node named CHA) in the AWGAwaveform buffer and the second one (the node named CHB) in the AWGBwaveform buffer. The buffer lengths should be at least 2000 points.

If we now set the CH B mode to SVMI and temporarily disconnect it from the capacitor and hit Run we should see something like this.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5,


The brighter green and orange traces will now be the simulation results and the darker traces will be the actual measured results we just saved. As we can see the two results align closely but not exactly. This is most likely because the actual resistor and capacitor are not exactly 10 K ohms and 0.22uF.

There are other ways to display the waveform buffers loaded from the file and you can explore how to do that by reading through the ALICE Desktop Users Guide.

:doc:`/wiki-migration/university/tools/m1k/alice/desk-top-users-guide`

Combining ALICE Scope traces in LTSpice Simulations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes we might need to use the output generated from an actual circuit as the input stimulus for part of the overall design that might not be built yet. In this part of the activity we are going to go over a simple example showing how to save the output waveforms from ALICE desktop in a format that LTspice can use. We can then use them as PWL sources within a simulation so they can be used as either inputs to the simulated part of the circuit or compared to the simulated output voltage waveform.

Still using the simple RC circuit example. If we now set the CH B mode back to Hi_Z and reconnect it to the capacitor and hit Run we should again see something like figure .

For the next step save the waveform data in a form that LTspice can read in as points for a PWL source. Under the File drop down there is an option to Save PWL Data. The program prompts for which channel's data you want to save. Each PWL data file can contain data for just one source.

For this example we will use this function twice to save the channel A voltage trace data into a file named cha-out.txt and the channel B voltage trace data into a file named chb-out.txt.

Now we are all set to enter the example circuit in LTspice. We have one PWL source, named CHA-Meas, that will be the input to the RC circuit. We need a second PWL source, named CHB-Meas, that will simply play back the measured CH-B voltage data for comparison to the simulated voltage waveform on node CHB. Note that all you have to do is specify the name of the file to use in each of the PWL sources.

Now we can run the simulation for 20 mSec and we should get a plot much like we got in ALICE of the actual circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-6.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 6, Simulation results


The green plot is the voltage on the CHA source. The blue trace is the simulated voltage on the capacitor, node CHB, which is mostly behind the red voltage plot of the CHB-Meas source. Of course we are getting a very close match between simulated and actual measurements as we would expect in the simple example.

Curve Fitting
~~~~~~~~~~~~~

As an example use case the following simple resistor and diode circuit shown in figure 1 is offered. First construct the simple resistor and diode circuit as shown.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/poly-fit-0.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Diode test circuit


Set Channel A AWG Min value to 0V and Max value to 5V. Set the Mode to SVMI and the Shape to triangle. Set the Freq to 100 Hz. Set Channel B mode to Hi-Z to measure the voltage across the diode.

Set the Horz Time scale to 0.5mSec/Div. Turn on trace averaging. Hit Run, wait for a few seconds to capture some data then hit Stop. This should display the rising half of the triangle wave on Channel A from 0 to 5 V ( green trace ). The width of the grid will be 500 sample points (5 mSec at 10 uSec/sample). Channel B should display the voltage across the diode going from 0 to about 0.8 V (orange trace). You may want to change the vertical scale to 0.1 V/div and position to 0.5 for CH-B to display the waveform from 0 to 1 V. You should now have something like shown in figure 2.

The voltage across the diode is measured using scope channel B and the diode current is measured using the AWG A channel current as the channel A voltage is swept using a triangle wave. The data samples in the VBuffB and IBuffA arrays is used to fit an exponential. The following exponential curve fitting function included here for reference, is contained in ALICE.

::

   # Fit the function y = A * exp(B * x) to the data arrays xs and ys
   # returns (A, B)
   # From: https://mathworld.wolfram.com/LeastSquaresFittingExponential.html
   def fit_exp(xs, ys):
       S_x2_y = 0.0
       S_y_lny = 0.0
       S_x_y = 0.0
       S_x_y_lny = 0.0
       S_y = 0.0
       for (x,y) in zip(xs, ys):
           S_x2_y += x * x * y
           S_y_lny += y * numpy.log(y)
           S_x_y += x * y
           S_x_y_lny += x * y * numpy.log(y)
           S_y += y
       #end
       a = (S_x2_y * S_y_lny - S_x_y * S_x_y_lny) / (S_y * S_x2_y - S_x_y * S_x_y)
       b = (S_y * S_x_y_lny - S_x_y * S_y_lny) / (S_y * S_x2_y - S_x_y * S_x_y)
       return (numpy.exp(a), b)
   #

In the following ALICE script, the measured diode voltage and current data is analyzed and (fit) then plotted using the built-in pyplot functions from the Matplotlib library.

.. important::

   Note that this script uses the User Entry Widgets on the X-Y plotting screen to display the fit values for I\ :sub:`S` and N. You will need to have the User Entries enabled in the alice_init.ini file: EnableUserEntries = 1

   
   Alternatively these lines can be commented out and the values simply printed to the Console screen.


::

   xs = VBuffB[50:500] # diode voltage
   ys = IBuffA[50:500] # diode current
   ys = ys / 1000.0 # convert mA to Amps
   ys = numpy.absolute(ys) # make all y values positive for taking ln
   ys = ys - numpy.amin(ys) + 2.2e-9 # add offset and Is guess

   # Function to fit data I_d(x) + I_s = I_s * exp(x/(n*Vt))
   # note that I_d + I_s is approx I_d since I_s is small

   (A, B) = fit_exp(xs, ys)

   # some constants
   # Saturation current I_s = 1.0e-9
   # Ideality factor n < 2
   # Thermal voltage, KT/q
   Vt = 0.0259
   # guess values for Is and n
   # Iguess(x) = 5.0e-9*(exp(x/(2*Vt))-1.0)
   #print( "{Is} A = ", A, "B = ", B )
   Fit_N = 1.0/(Vt*B) # Fit n with Vt at 25 C
   Is_String = ' {0:.2e} '.format(A)
   AmA = A * 1000.0 # convert A to mA
   User3Entry.delete(0,END)
   User3Entry.insert(5, Is_String)
   N_String = ' {0:.2f} '.format(Fit_N)
   User4Entry.delete(0,END)
   User4Entry.insert(5, N_String)
   #print ("Vt = ", Vt, "Fit N = ", Fit_N)
   plt.figure()
   plt.plot(VBuffB[0:500], IBuffA[0:500], 'g', label='Raw Data')
   plt.plot(VBuffB[0:500], [AmA * (numpy.exp(B*x)-1) for x in VBuffB[0:500]], 'b', label='Fit')
   #plt.plot(VBuffB[0:500], [2.2e-9 * (numpy.exp(x/(2.0*0.0259))-1) for x in VBuffB[0:500]], 'r', label='Guess')
   plt.title('Exponential Diode Fit')
   plt.xlabel('Volts')
   plt.ylabel('Amps')
   plt.legend(loc='best')
   plt.tight_layout()
   plt.show(block=False)

The following screenshots show the results:

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/diode-exp-time.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Time waveforms


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/diode-exp-x-y.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3, V-I X,Y plot


.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/diode-exp-fit.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4, Curve fit results


Polynomial Fit Example
^^^^^^^^^^^^^^^^^^^^^^

The numpy library contains a polynomial fitting function. The following example shows how to use the polyfit and poly1d function in numpy to fit a 5\ :sup:`th` order polynomial to the voltage characteristics of the same diode circuit and plot the polynomial over the plot of the measured data points.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/poly-fit-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Plot of Diode Voltage


Open the Command Line interface ( with the program stopped ). We want to fit a polynomial using the polyfit function to the first 500 samples where CH-A ramps from 0 to 5 V. Type the following line into the entry space and hit return.

**global Zpoly; Zpoly = numpy.polyfit(VBuffA[0:499], VBuffB[0:499], 5)**

To check the terms of the polynomial, type the following line into the entry space and hit return.

**print Zpoly**

In the ALICE desktop console window you should see something like this.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/poly-fit-2.png
   :align: center
   :width: 600px

.. container:: centeralign

   ALICE console showing polynomial terms


We can use the poly1d function to make an object that makes this easy to plot on the screen. Type the following line into the entry space and hit return.

**global ZBuff; ZBuff = numpy.poly1d(Zpoly)**

Again to check the results type the following line into the entry space and hit return.

**print ZBuff**

In the ALICE desktop console window you should now see something like this.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/poly-fit-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   ALICE console showing polynomial equation


To plot the polynomial on the screen we will use the Math waveform feature. From the Math menu select Math Axis and set it to V-B to use the same axis as the diode voltage plot. From the Math menu select Enter Formula and enter the following:

**ZBuff(VBuffA[t])-CHBOffset**

This plots the value of the polynomial evaluated at each point in VBuffA as the time index t goes from 0 to 499 ( 5 mSec ). Be sure to note that () are used for ZBuff and not [] because it is a function and not an array like VBuffA. You should now see something like figure 3 on the display. The magenta Math plot is the polynomial.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/poly-fit-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Plot of measured data and polynomial


Using gnuplot
~~~~~~~~~~~~~

Change the resistor in diode test circuit to 470 Ω (could be 2 1 kΩ resistors in parallel). Be sure you have the channel A voltage and current traces selected as well as the channel B voltage trace.

Hit the run button and wait a few seconds for the trace averaging to smooth out the random noise. Hit the Stop button. We now have captured a set of data points of the diode voltage in the Channel B voltage trace and the diode current in the channel A current trace.

Using the X-Y plotter you should see something like the following when plotting CB-V (diode voltage) on the X axis and CA-I (diode current) on the Y axis.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-9.png
   :align: center
   :width: 400px

.. container:: centeralign

   figure 4, Diode Voltage va Current Plot


Open the ALICE command line screen and enter the following line:

numpy.savetxt('diode-data.dat', numpy.vstack((VBuffB[0:500],IBuffA[0:500])).T, delimiter=' ', fmt='%2.4f')

::

   numpy.savetxt('diode-data.dat', numpy.column_stack((VBuffB[0:500],IBuffA[0:500])), delimiter=' ', fmt='%2.4f')

This will save the first 500 data points to a the diode-data.dat file in two columns separated by a space character. This is in a form that gnuplot can easily read.

Using gnuplot and the captured data set, plot the diode current vs. the diode voltage.

Add a plot of the diode current equation to your plot.

:math:`\displaystyle I_d = I_s(e^\frac{V_D}{nV_T}-1)`

-  Start with n=2, guess a value for I\ :sub:`s`, and plot function vs v\ :sub:`D` from 0 to about 0.8 volts.
-  Use 25.9mV for V\ :sub:`T`.
-  Vary the value of I\ :sub:`s` until you get a reasonable fit to your measured data.

An example gnuplot scripting .plt file below shows how you might do this. This should only serve as a guide. Adjustments might be needed to work with your data set.

::

   # plot measured diode data vs ideal equation
   reset
   set title "Real Diode Data"
   set xlabel "V diode"
   set ylabel "I diode"
   # Set line styles to blue (#0060ad) red (#dd181f) and green
   set style line 1 linecolor rgb '#0060ad' linetype 1 linewidth 2
   set style line 2 linecolor rgb '#dd181f' linetype 1 linewidth 2
   set style line 3 linecolor rgb '#18dd1f' linetype 1 linewidth 2
   set grid
   set xrange [-0:0.8]
   set yrange [-0.1:9]
   # some constants
   # Saturation current
   is = 1.0e-9
   # Ideality factor
   n = 2
   # Thermal voltage, KT/q
   vt = 0.0259
   # Function to plot
   # scale in mA
   # guess values for Is and n
   iguess(x)=1000*1.0e-9*(exp(x/(2*vt))-1.0)
   # Function to fit data
   id(x)=1000*is*(exp(x/(n*vt))-1.0)
   # fit equation to data
   fit id(x) 'diode-data.dat' via is, n
   # Plot
   plot iguess(x) with lines linestyle 1, id(x) with lines linestyle 2, "diode-data.dat" with lines linestyle 3

.. _curve-fitting-1:

Curve Fitting:
^^^^^^^^^^^^^^

The fit command in gnuplot can fit a user-defined function to a set of data points (x,y), using an implementation of the nonlinear least-squares (NLLS) Marquardt-Levenberg algorithm. Any user-defined variable occurring in the function may serve as a fit parameter.

After each iteration step, detailed information about the current state of the fit is written to the display. The same information about the initial and final states is written to a log file, "fit.log". This file is always appended to, so as to not lose any previous fit history; it should be deleted or renamed as desired.

Be sure to include your "guess" values for I\ :sub:`s` and n as well as the gnuplot fit results.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-10.png
   :align: center
   :width: 500px

.. container:: centeralign

   figure 5, gnuplot results for 1N914 diode


To circle back around as a further check of the curve fitting result we can use the math functions in the X-Y plotter in ALICE to plot the ideal diode equation with the fitting results for Is and N. In the following screen shot we show the measured diode current vs voltage (dark green trace) and the ideal diode equation (magenta trace) using the gnuplot fitting results. The measured data should be the same as what we saw in figure 4. The math equation to calculate the ideal diode current will look something like this but you will have to substitute your fit values for I\ :sub:`s` and n \* V\ :sub:`T`. Note that value for I\ :sub:`s` is scaled by 1000 to give mA for the current:

::

   5.0e-6*(math.exp(VBuffB[t]/(1.9*0.0259))-1.0)

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/data-anal-fig-11.png
   :align: center
   :width: 400px

.. container:: centeralign

   figure 6, gnuplot fitting results vs measured 1N914 diode


Repeat the same process for your LED data, save and annotate your I-V plot.

Resources and Going Further
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you should understand the concepts of basic data analysis are related. Congratulations!

These concepts are just the tip of the iceberg. If you're looking to study further into more complex applications of data analysis and the design of electrical circuits, be sure to check out the following hands on activities.

**For Further Reading:**

`Diode modelling <https://en.wikipedia.org/wiki/Diode_modelling>`__

**Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
