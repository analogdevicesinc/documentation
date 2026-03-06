Transient Simulations with AD469x LTspice Model
===============================================

The purpose of this transient simulation is to evaluate and validate the performance of the AD4696 ADC in LTspice. The simulation aims to cover various aspects related to the ADC's analog inputs, acquisition time, channel sequencing, and settling performance of the analog front-end (AFE). By simulating these parameters, we can assess the overall functionality, accuracy, and stability of the ADC under different conditions.

Transient Glitches of ADC Analog Inputs
---------------------------------------

Transient glitches refer to short-duration voltage variations that may occur at the analog inputs of the ADC. These glitches can negatively impact the accuracy of the conversion process. In this simulation, we will analyze the ADC's response to transient glitches and evaluate the effectiveness of the kickback filter or other techniques employed to mitigate these glitches. By observing the output waveform and measuring the impact on accuracy, we can ensure that the design adequately handles transient glitches.

Acquisition Time of ADC
-----------------------

The acquisition time is the duration required for the ADC to accurately capture and convert an analog input signal. It is crucial to optimize this parameter to meet the system requirements. In the simulation, we will assess the acquisition time by applying various input signals and measuring the time it takes for the ADC to settle and provide a stable digital output. By adjusting the design parameters and observing the settling behavior, we can determine the optimal acquisition time for the ADC.

Channel Sequencing
------------------

Channel sequencing allows the ADC to process multiple analog input channels one after another. The timing and sequencing logic need to be implemented correctly to ensure efficient utilization of the ADC's capabilities. In this simulation, we will verify the channel sequencing functionality by applying different input signals to multiple channels and monitoring the conversion results. By analyzing the timing, order, and accuracy of the converted signals, we can validate the proper operation of the channel sequencing mechanism.

Settling Performance of AFE
---------------------------

The settling performance of the AFE plays a vital role in the accuracy and stability of the ADC's measurements. The AFE circuitry should settle quickly and accurately to minimize errors introduced during the conversion process. In the simulation, we will evaluate the settling performance of the AFE by applying step or ramp input signals and observing the settling behavior of the output. By analyzing the settling time, overshoot, and stability, we can assess the AFE's performance and ensure it meets the desired specifications. Overall, this transient simulation serves the purpose of verifying the functionality and performance of the AD4696 ADC, specifically addressing transient glitches, acquisition time, channel sequencing, and settling performance of the AFE. By simulating these aspects, we can identify and rectify any design flaws or optimizations required to achieve accurate and reliable ADC measurements in real-world applications.

Schematic Setup
===============

In this section, the sample transient simulation model for AD4696 is discussed. To perform the transient analysis for the AD4696 ADC in LTspice, you will need the following voltage sources and analog components in your simulation setup:

1 - Operating Conditions
------------------------

Operating Conditions represents the various supply rails used in the circuit. It includes the following parameters:

-  AVDD: Voltage supply for the analog section.
-  VDD: Voltage supply for other specific circuit blocks.

Voltage REF: It indicates the reference voltage used in the circuit. This voltage is essential for accurate analog-to-digital conversions.

Analog Input Voltages: It represents the inputs to the analog-to-digital converter (ADC). Configure the input voltages based on your intended signal levels or test scenarios.

2 - AFE Parameters
------------------

AFE Parameters contains the following elements related to the analog front-end (AFE):

-  Kickback Filter: A filter used to minimize any voltage spikes or glitches during the ADC conversion process.
-  Resistor and Capacitor Value: These components contribute to the AFE's overall performance and should be chosen carefully based on the system requirements.

3 - Sampling Dynamics and Timing Delay
--------------------------------------

These options account for the specific timing requirements and sequencing of the ADC channels. This section determines how the ADC samples and processes analog inputs.

Timing Delays:
~~~~~~~~~~~~~~

Delay to account for the ADC reset pulse is introduced in this schematic. In this sample, we have the following values set as:

-  .param reset_delay 1u = 1 usec
-  .param cnv_delay = reset_delay +50u (here, the cnv_delay is also accommodating the delay for the AFE to settle RESET glitch)

.. _channel-sequencing-1:

Channel Sequencing:
~~~~~~~~~~~~~~~~~~~

In case of this LTspice model, the channel sequencing is being carried out by explicitly stating the number of channel sequences to iterate and defining the number of channels per sequence. Following parameters are defined in the schematic to outline the channel sequencing:

-  .param num_sequences=16 (16 sequences are being carried out per channel)
-  .param num_channels=2 (2 channels will be iterated per sequence)

Simulation Parameters
=====================

It includes the statement necessary for LTspice simulation. It consists of the following parameters:

-  .tran 0 {tstop} {tstart} = Add the stop time and the time to start saving sample data
-  .param tstart = cnv_delay - tstart_buffer = Defining the time to initiate the sampling of ADC and subtracting the extra time buffer from the cnv_delay
-  .param tstop = cnv_delay + (t_cnv*num_samples) + tstop_buffer = The time to end the sampling for ADC is set, where the cnv_delay is added along with the total time taken to accumulate the samples prorated over the sampling speed and some extra time to add the stopping time buffer
-  .param tsart_buffer t_cnv = The buffer time is set over here as the reciprocal of sampling rate
-  .param tstop_buffer t_cnv = The buffer time is set over here as the reciprocal of sampling rate

Analyzing Settling Performance
==============================

The purpose of this section is to guide users in analyzing the settling performance of the ADC using LTspice simulation and graphs. Proceed with the following steps in order to get the simulation results.

Simulation Setup
----------------

--------------

1 - Parameter Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before proceeding with the simulation, ensure that all the necessary parameters are set to their required values. This includes the specifications of the ADC model, kickback filter components, AFE circuitry, and any other relevant parameters.

2 - LTspice Simulation Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define the values and parameters in the LTspice simulation command statement. Verify that the simulation parameters align with the desired settling time and duration.

3 - Running the Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Execute the simulation by clicking the "Run" button. Allow sufficient time for the simulation to complete, which will be displayed at the bottom of the terminal window or you can start seeing the real time results as well as soon as the first few samples get sampled by the ADC model.

Settling Error Measurements
---------------------------

--------------

1 - Settling Error Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the simulation has completed, navigate to the Settling Error Measurements box on the schematic. In this example, we will consider channels 0 and 1, so locate the in0_err and in1_err outlets within the schematic.

2 - Probe Settling Error Outlets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place the probe on the in0_err and in1_err outlets to measure the settling error in volts. This will indicate the difference between the sampled voltages and the actual voltage fed into the ADC.

3 - Viewing Settling Error
~~~~~~~~~~~~~~~~~~~~~~~~~~

To observe the settling error, the user should wait for the settling tails in in0_err and in1_err to reach a steady state value. With this available graph user can perform signal conditioning and gain adjustment to their system.

Appended below is an example simulation where the RC filters are too slow, and settling error occurs over a number of samples as a result.

.. image:: https://wiki.analog.com/_media/resources/quick-start/ad469x-ltspice-user-guide/tran-sample.png
   :alt: Sample transient sim
   :align: center
   :width: 600px

--------------

--------------

Sample Circuit
==============

The sample circuit can be downloaded using this link `ad4696_transient.zip <https://wiki.analog.com/_media/resources/quick-start/ad469x-ltspice-user-guide/ad4696_transient.zip>`__.

Appended below are some screenshots of the LTspice running simulations for the ADC AD4696 model. In this simulation, transient glitches are being model when only two channels are being probed against the CNV pulse over time.

.. image:: https://wiki.analog.com/_media/resources/quick-start/ad469x-ltspice-user-guide/tansient-sim-sample.gif
   :align: center
