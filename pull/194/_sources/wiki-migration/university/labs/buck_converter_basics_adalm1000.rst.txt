Activity: Buck Converter Basics, for ADALM1000
==============================================


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#objective>`_


.. include:: ../courses/alm1k/circuits1/alm-cir-15a.rst


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#background>`_


Materials
---------

| ADALM1000 Active Learning Module
| PC running LTspice and ALICE
| Solder-less breadboard and jumper wire kit
| Components from ADALP2000 parts kit as required
| Optional: :doc:`ADALM-BUCK-ARDZ Module </wiki-migration/university/tools/lab_hw/adalm_buck>`
| 12V power supply (preferred), 9 V battery or 5V USB power supply (workable)
| Voltmeter (optional)
| LTspice files for this activity:
| `buck_converter_basics_ltspice_files.zip <https://wiki.analog.com/_media/university/courses/electronics/buck_basics/buck_converter_basics_ltspice_files.zip>`_

Activity 1: An Open-Loop 2:1 Buck Converter
-------------------------------------------


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#theory_and_simulation>`_


Circuit Testing
~~~~~~~~~~~~~~~

**Software Requirements**

To measure this circuit with the ADALM1000 module you will need to use the Equivalent Time Sampling functionality within the ALICE 1.3 user interface. One of the advanced features that can be enabled in ALICE is Equivalent Time Sampling which, for certain classes of periodic waveforms, can increase the apparent sampling to MSPS rates. How to use ETS is outlined in the :doc:`ALICE Equivalent Time Sampling User’s Guide </wiki-migration/university/tools/m1k/alice/advanced-equivalent-time-sampling-guide>`

An assembled PC board version of the buck converter circuit is available as the ADALM-BUCK-ARDZ experiment board.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice/alice-ets-guide-f10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure A1.12, ADALM-BUCK-ARDZ test board


This board is actually an Arduino compatible shield and for the tests is used in conjunction with an Arduino running the following sketch:

.. admonition:: Download
   :class: download

   
   -  Arduino Sketch: :git-Linduino:`LT1054 closed loop buck with duty cycle control <LTSketchbook/Active%20Learning/LT1054_voltage_mode_buck_DC_ctrl>`
   


While there are a number of connections required to construct this test circuit, it can be assembled on a solderless breadboard as in figure A1.13. Note that the HPH1-1400L has six inductors that can be connected in any way (series, parallel, or a combination of the two). Be sure to observe proper polarity, connecting all inductors in series as shown.

   


|image1|

.. container:: centeralign

   Figure A1.13. Breadboard Circuit


The circuit could also be constructed on a solderable breadboard which matches the layout of typical solderless breadboards. Or on an Arduino compatible proto-typing shield following the wiring of the ADALM-BUCK-ARDZ experiment board.



|image2|

.. container:: centeralign

   Figure A1.14. Alternate Construction Method


Measure the ripple current for different numbers of series-connected inductors. The figure below shows the ripple current for 2, 3, 4, 5, and 6 inductors. How well does this match the LTspice simulation?

.. image:: https://wiki.analog.com/_media/university/labs/m1k-buck-ardz-ripple-current.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure A1.15. Ripple Current for 2 to 6 Windings in Series


*(Notice the "steps" in the switch node voltage as the inductor current passes through zero. After switching, current initially flows through diodes D1 or D2. As the current passes through zero and switches direction, the LT1054 output driver "takes over" and drives the switch node. In the LTspice simulation, try probing the LT1054 CAP+ current, D1 current, and D2 current separately, noting that the inductor current is the sum of the three.)*

Measure the ripple voltage at the output of the converter, with a 22uF output capacitor. Then place an additional 47uF capacitor in parallel, for a total of 69uF. Does the measured ripple match the simulated ripple reasonably well? Note that both the inductor and electrolytic capacitors can have a very wide tolerance - tolerances of +/-20% are common for inductors, and -20%/+80% is a common tolerance for electrolytic capacitors. The animated figure below shows the ripple voltage for output capacitances of 22uF and 22uF+47uF.

.. image:: https://wiki.analog.com/_media/university/labs/m1k-buck-ardz-ripple-voltage.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure A1.16. Output Ripple for 22uF, 22+47uF output capacitance


Activity 2: An Open-Loop Variable Buck Converter
------------------------------------------------


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#theory_and_simulation1>`_


.. _circuit-testing-1:

Circuit Testing
~~~~~~~~~~~~~~~

Use M1K to override the LT1054's internal oscillator. Use the AWG controls and take measurements at 20%, 40%, 60%, 80% duty cycle.

<<add setup details, make a ALICE config file.>>

Set back to 50%, then connect a 50-ohm load. Calculate the approximate output impedance.

Activity 3: A closed-Loop, Voltage Mode Buck Converter
------------------------------------------------------


.. note::

   See `university/labs/buck_converter_basics <https://wiki.analog.com/university/labs/buck_converter_basics#theory_and_simulation2>`_


.. _circuit-testing-2:

Circuit Testing
~~~~~~~~~~~~~~~

Connect the buck output to the A0 analog pin on the Arduino and the Arduino's D3 digital signal to the buck converter's control input. Figure A2.17 shows connections to an Arduino Uno clone. The yellow wire connects the buck output to the Arduino's A0 input, and the blue wire connects the Arduino's PWM output on Digital Pin 3 to the oscillator override input. (Using two ground wires ensures a lower inductance connection between circuit grounds.)


|image3|

.. container:: centeralign

   Figure A2.17. Buck Converter with Arduino Control


Copy this Arduino sketch into your Arduino sketchbook (and restart the Arduino IDE if it's open.)

.. admonition:: Download
   :class: download

   
   -  Arduino Sketch: :git-Linduino:`LT1054 closed loop buck with duty cycle control <LTSketchbook/Active%20Learning/LT1054_voltage_mode_buck_DC_ctrl>`
   


The following figure shows the operation of the closed-loop circuit. The set point voltage is 3.141V, and the purple trace starts out close to this value at the left hand side of the screen shot. A 50 ohm load is then connected to the output, drawing approximately 120mA, and producing a dip in the output voltage. The Arduino loop detects this and increases the PWM frequency accordingly, restoring the voltage to its correct value. Then the resistor is removed, producing an increase in the output voltage. Once again, the Arduino loop detects this disturbance and compensates.

.. image:: https://wiki.analog.com/_media/university/labs/m1k-buck-ardz-transient-step.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure A2.18. Arduino Controlled Buck Transient Response


.. admonition:: Download
   :class: download

   **Resources:**

   
   -  LTspice files: :git-education_tools:`m2k/ltspice/buck_ltspice`
   -  Fritzing files: :git-education_tools:`m2k/fritzing/buck_bb`
   -  Python Script files:
   


Going Further
-------------

This activity borrows heavily from Analog Devices Application Note 140, which is an excellent reference to build upon concepts in this activity:

http://www.analog.com/media/en/technical-documentation/application-notes/AN140fb.pdf

AN19 is the LT1070 design manual, rich with examples:

http://www.analog.com/media/en/technical-documentation/application-notes/an19fc.pdf

Article on simulating SMPS loop gain (and why it's often unnecessary):

http://www.analog.com/en/technical-articles/ltspice-extracting-switch-mode-power-supply-loop-gain-in-simulation-and-why-you-usually-don-t-need.html

Questions:
----------

Slide Deck
----------

A slide deck is provided as a companion to this exercise, and can be used to help in presenting this material in classroom, lab setting, or in hands-on workshops.

.. admonition:: Download
   :class: download

   `Buck Converter Basics Slide Deck <https://wiki.analog.com/_media/university/courses/electronics/buck_basics/workshop_buck_converter_basics.pptx>`_


**Return to Lab Activity** :doc:`Power Lab Table of Contents </wiki-migration/university/labs/power>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/buck_basics/lt1054_2_to_1_bb.png
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/buck_basics/lt1054_buck_perma_proto_sm.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/buck_basics/lt1054_arduino_in_loop.jpg
   :width: 400px
