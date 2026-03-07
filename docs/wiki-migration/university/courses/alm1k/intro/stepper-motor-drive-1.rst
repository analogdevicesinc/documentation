Activity: Stepper Motor Control, For ADALM1000
==============================================

Objective:
----------

A stepper motor is a brushless DC electric motor that divides one full rotation into a number of equal steps. The motor's position can then be forced to rotate to and hold at one of these steps without a feedback sensor, as long as the motor is properly sized to the target application. In this activity you will learn how to rotate a stepper motor in both directions using full and half steps.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The blue shaded rectangles indicate connections to the ALM1000 digital I/O connector.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 – PIO 3 on the ALM1000 board silkscreen.

Background:
-----------

Stepper motors are used in floppy disk drives, flatbed scanners, computer printers, XY plotters, slot machines, image scanners, compact disc drives, intelligent lighting, camera lenses, CNC machines and, most recently, in 3D printers.

To rotate the stepper motor a sequence of “high” and “low” levels is applied to each of the 4 inputs in sequence. By setting the correct sequence of high and low levels the motor spindle will rotate. The direction can be reversed by reversing the sequence.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard adapter
| Jumper wires
| 2 – 74HC541 octal drivers
| 1 – 5 V Stepper motor (Mitsumi M35SP-7T bipolar stepper motor or similar)
| 1 Amp 5 V power supply, USB wall charger and micro USB to breadboard adapter is a good option

Program to Drive A Stepper Motor
--------------------------------

The Python software development layer (libsmu and pysmu) for the ADALM1000 provides a way to write specific control routines for external hardware like stepper motors. Be sure to install the libsmu and Python bindings, if you have not done so already, before continuing with this activity.

:git-libsmu:`libsmu on GitHub <tree/master>`

This activity will cover one example using Python to control a Mitsumi M35SP-7T stepper motor salvaged from a flatbed scanner. Other similar stepper motors can be substituted. The example driver circuit, shown in figure 1, is somewhat incidental to this programing discussion and the code examples can in general be used to control any similar driver circuit / motor combination. This particular stepper motor is of the bipolar drive (4 wire differential) variety and it thus needs to be driven by an H-Bridge configuration.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro_stepper_motor_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Differential stepper motor driver schematic


The M35SP-7T stepper motor has 9Ω windings and is specified to be driven nominally with 5 volts which would give a coil current of around 555 mA. Do not attempt to use the +5V supply from ADALM1000 for this. Use a supply that is capable of supplying at least 1A of current. A 1 Amp 5V USB wall charger and the micro USB to breadboard adapter from the ALP2000 kit will work.

To make the driver circuit simple for this activity, an octal CMOS buffer such as the 74HC541 can serve as an H-bridge. To supply sufficient current to the motor windings we will need to connect multiple buffers in parallel. The schematic example shows two of the 8 buffers connected in parallel to make the four H Bridge outputs. The ALM1000 digital output pins are 3.3V CMOS but for this simple demonstration the 3.3V output is sufficient to switch the 74HC541 running from +5 V. Using a 74HCT541 devices with lower TTL logic input thresholds would work even better.

Because of the on resistance of the CMOS buffer output transistors in the 74HC541, the coil voltage will not be the full 5 V power supply. Two buffers are strong enough to make the motor spin but not with full torque. Combining two 74HC541 packages will provide 4 buffers in parallel. Using 4 buffers in parallel results in about 250 mA of drive current which is about one half of the rated current so the maximum pulse rate will also be about one half of the specified rate or 50 Hz. One way to combine two 74HC541 packages with fewer breadboard wires is by piggy-backing the two DIP packages one on top of the other and soldering their leads together.

Two H-bridge circuits using four NMOS and four PMOS power transistors such as the ZVN2110A and ZVP2110A from the parts kit (ADALP2000) could be constructed to provide higher coil currents. To drive a 5 or 6 wire unipolar stepper motor single ended Darlington drivers like the ULN2003 can be used.

Hardware Setup:
~~~~~~~~~~~~~~~

Build the schematic shown in figure 1 on your solderless bread board.

Procedure:
~~~~~~~~~~

**Drive Waveforms**

The pulse waveform sequence for “forward” rotation is shown in figure 2. A pulse on PIO 0 will energize coil A with a positive polarity and a pulse on PIO 2 will energize coil A with an opposite negative polarity. Similarly, a pulse on PIO 1 will energize coil B with a positive polarity and a pulse on PIO 3 will energize coil B with an opposite negative polarity.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro_stepper_motor_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Pulse sequence for forward rotation


As we can see from the timing diagram the coils are energized in a +A, +B, -A, -B sequence. One cycle is four full steps.

For “reverse” rotation we need to swap the pulse sequence as shown in figure 3. As we can see this is essentially the sequence in reverse order.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro_stepper_motor_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Pulse sequence for reverse rotation


The libsmu Python layer for controlling the ADALM1000 contains a function to configure and control the digital input / output pins. The digital outputs can be configured as either static inputs or outputs.

**Code example 1:**

In this first code example we configure the four digital pins, PIO 0 – 3, as outputs using the basic devx.ctrl_transfer() function to turn them on and off one at a time in the desired sequence by looping through a look-up table.

::

   # assign digital pins
   PIO_0 = 28
   PIO_1 = 29
   PIO_2 = 47
   PIO_3 = 3 
   # step tables for full steps
   D0steptab = [1, 0, 0, 0]
   D1steptab = [0, 1, 0, 0]
   D2steptab = [0, 0, 1, 0]
   D3steptab = [0, 0, 0, 1]

While this is a fairly simple approach it is sort of brute force and the width and frequency of the pulses is highly dependent on the speed and activity level of the computer being used.

::

       while i < StepCount:
           pointer = pointer + 1
           if pointer > pointermax:
               pointer = 0
               
           D0stepcode = 0x50 + D0steptab[pointer] # 0x50 = set to 0, 0x51 = set to 1
           D1stepcode = 0x50 + D1steptab[pointer]
           D2stepcode = 0x50 + D2steptab[pointer]
           D3stepcode = 0x50 + D3steptab[pointer]
           devx.ctrl_transfer(0x40, D0stepcode, PIO_0, 0, 0, 0, 100) # set PIO 0
           devx.ctrl_transfer(0x40, D1stepcode, PIO_1, 0, 0, 0, 100) # set PIO 1
           devx.ctrl_transfer(0x40, D2stepcode, PIO_2, 0, 0, 0, 100) # set PIO 2
           devx.ctrl_transfer(0x40, D3stepcode, PIO_3, 0, 0, 0, 100) # set PIO 3     
           
           time.sleep(steptime)
           i = i + 1

We need to define two functions, one for forward rotation and one for reverse rotation. All that is different is the way we step through the look-up table by incrementing the pointer to go forward and decrementing the pointer to go in reverse. The time.sleep(steptime) function adds a delay which determines the time a bit is on before the next in the sequence is turned on. The StepCount variable is used to determine how many times the bit pattern is sent.

**Code example 2:**

To rotate the motor using half steps all we need to do is expand the look-up table as shown here:

::

   # step tables for 1/2 steps
   D0steptab = [1, 1, 0, 0, 0, 0, 0, 1]
   D1steptab = [0, 1, 1, 1, 0, 0, 0, 0]
   D2steptab = [0, 0, 0, 1, 1, 1, 0, 0]
   D3steptab = [0, 0, 0, 0, 0, 1, 1, 1]

As we can see there are now 8 bit patterns in the table. The half way between steps are produced when both coils are on at the same time.

Program files ( `alm1000_stepper.zip <https://wiki.analog.com/_media/university/courses/alm1k/intro/alm1000_stepper.zip>`_ ) for this activity are available. Stepper_test_1.py produces full step pulses. Stepper_test_2.py produces half step pulses. Open the Stepper_1.py or Stepper_2.py Python program in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there.

Stepper_test_1.py produces full step pulses. Stepper_test_2.py produces half step pulses. Run the program. You should see something like figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/intro_stepper_motor_f4.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 4 Stepper_1.py


Questions:
~~~~~~~~~~

Challenges:
~~~~~~~~~~~

**For Further Reading:**

`Stepper motor <https://en.wikipedia.org/wiki/Stepper_motor>`_

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
