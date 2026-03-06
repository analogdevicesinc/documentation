Activity: Precision Rectifiers, Absolute value circuits, For ADALM1000
======================================================================

Objective:
----------

The purpose of this lab activity is to investigate precision rectifiers or absolute value circuits. Rectifiers, or 'absolute-value' circuits are often used as detectors to convert the amplitudes of AC signals to DC values to be more easily measured. For this type of circuit, the AC signal is first high-pass filtered to remove any DC component and then rectified and perhaps low pass filtered.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

The ALM1000 generates and measures unipolar or single-ended signals in the range of 0 to 5 V. To simplify and better understand the concepts in this lab we would rather represent the signals as being bipolar swinging both positive and negative either side of the common node. With the ALM1000 we can use the fixed 2.5 V supply as the common node and then consider the allowed signal range as going from -2.5 V to +2.5 V.

In the ALICE desktop software we can make the following adjustments. As shown in figure 1, on the right hand side of the scope screen, enter 2.5 for the CA-V and CB-V offset adjustment. This is because in this lab we are referencing all the measurements to the +2.5 V common rail. Also enter 0 for the CH-A and CH-B vertical position settings (along bottom of scope screen). The vertical scale should now be centered on 0 and go from -2.5 to +2.5.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-lcres-d1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Adjust offset for 2.5 V signal reference


Background:
-----------

As we have seen in the simple rectifier circuits constructed with diodes, the circuit does not respond well to signals with a magnitude less than a diode-drop (0.7V for silicon diodes). This limits their use in designs where small amplitudes are to be measured. For designs in which a high degree of precision is needed, op-amps can be used in conjunction with diodes to build precision rectifiers.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 1 - OP484 quad rail-rail op-amp
| 5 – 10 KΩ Resistors
| 2 – small signal diodes (1N914 or similar)

Directions:
~~~~~~~~~~~

The inverting op-amp circuit can be converted into an “ideal” (linear precision) half-wave rectifier by adding two diodes as shown in figure 2. For the negative half of the input diode D\ :sub:`1` is reverse biased and diode D\ :sub:`2` is forward biased and the circuit operates as a conventional inverter with a gain of -1. For the positive half of the input, diode D\ :sub:`1` is forward biased, closing the feedback around the amplifier. Diode D\ :sub:`2` is reverse biased disconnecting the output from the amplifier. The output will be at the virtual ground potential ( - input terminal ) through the 10 KΩ resistor.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-precision-rectifier-f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2 Connection diagram for precision half-wave rectifier


Hardware Setup:
~~~~~~~~~~~~~~~

Configure AWG CHA in SVMI mode with a 300 Hz Sine Shape and with Min value set to 1.0 and Max value set to 4.0 (3 V p-p centered on 2.5 V). Channel B is set in Hi-Z mode and used to measure the voltage at the rectified output. Both scope channels should be set to 0.5 V per division.

Procedure:
~~~~~~~~~~

Under the curves drop down menu select CA-V and CB-V to be displayed. Using the Meas drop down menus select Max and Avg for CV-A. Select Max and Avg for CB-V to display the peak and average voltage on the output.

The peak of the rectified output should now equal to the peak value of the input. There is also a sharp transition as the input crosses zero. The experimenter should investigate the waveforms at different points in the circuit to explain why this circuit works better than the simple diode half wave rectifier.

For this laboratory exercise you should:

| a) Study the circuit and determine how it works. There is a very fundamental concept that should help in understanding how this circuit operates. Given an op-amp configured with negative feedback, the inverting and non-inverting input terminals will try to reach the same voltage level, often referred to as a "virtual ground".
| b) Plan some tests to see if this circuit indeed is a rectifying circuit. Perform these tests, fully documenting all tests and results in your lab report.
| c) Carefully measure and record voltages at all nodes in the circuit.

Questions:
~~~~~~~~~~

What happens if the direction of the diodes is reversed? Repeat experiment with the direction of both diodes reversed.

Full wave rectifier:
~~~~~~~~~~~~~~~~~~~~

The purpose of this part of the lab activity is to modify the half wave rectifier to make full wave rectifier or absolute value circuit.

.. _directions-1:

Directions:
~~~~~~~~~~~

The circuit shown in figure 3 is an absolute value circuit, often called a precision full-wave rectifier. It should operate like a full wave rectifier circuit constructed with ideal diodes ( the voltage across the diode, in forward conduction, equals 0 volts). The actual diodes used in the circuit will have a forward voltage of around 0.7 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-lab-precision-rectifier-f3.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 3 Connection diagram for absolute value circuit


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

The AWG CH-A waveform generator should be configured for a 300 Hz Sine wave with 1.0 volt Min value and 4.0 volt Max value (3 V p-p centered on 2.5 V). Channel B is set in Hi-Z mode and used to measure the voltage at the rectified output. Both scope channels should be set to 0.5 V per division.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Under the curves drop down menu select CA-V and CB-V to be displayed. Using the Meas drop down menus select Max and Avg for CV-A to display the peak and average voltage for Channel A. Select Max and Avg for CB-V to display the peak and average voltage for Channel B.

Carefully measure and record voltages at all nodes in the circuit.

.. _questions-1:

Questions:
~~~~~~~~~~

What happens if the direction of the diodes is reversed? Repeat experiment with the direction of both diodes reversed.

What happens if the direction of one diode is opposite of the other? Repeat experiment with the direction of one diode (D\ :sub:`1`) reversed.

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/precision_rect_abs_val_ckts_ltspice`
-  Fritzing files: :git-education_tools:`m1k/fritzing/precision_rect_abs_val_ckts_bb`

**For Further Reading:**

| :adi:`Half Wave Rectifier <media/en/training-seminars/tutorials/MT-212.pdf>`
| :adi:`Full Wave Rectifier <media/en/training-seminars/tutorials/MT-211.pdf>`

**Return to the ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm_circuits_lab_outline>`
