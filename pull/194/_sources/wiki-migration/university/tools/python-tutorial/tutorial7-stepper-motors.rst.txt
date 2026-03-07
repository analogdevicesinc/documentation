Activity: Stepper Motor
=======================

Objective:
----------

A stepper motor is a brushless DC electric motor that divides one full rotation into a number of equal steps. The motor's position can then be forced to rotate to and hold at one of these steps without a feedback sensor, as long as the motor is properly sized to the target application. Stepper motors are used in floppy disk drives, flatbed scanners, computer printers, XY plotters, slot machines, image scanners, compact disc drives, intelligent lighting, camera lenses, CNC machines and, most recently, in 3D printers. In this activity you will learn how to rotate a stepper motor in both directions using full and half steps.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 - PIO 3 on the ALM1000 board silkscreen.

Background:
~~~~~~~~~~~

To rotate the stepper motor a sequence of "high" and "low" levels is applied to each of the 4 inputs in sequence. By setting the correct sequence of high and low levels the motor spindle will rotate. The direction can be reversed by reversing the sequence.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 2 - 74HC541 octal drivers
| 1 - 5 V Stepper motor (Mitsumi M35SP-7T bipolar stepper motor or similar)

Directions:
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial7_f1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Differential stepper motor driver schematic


The M35SP-7T stepper motor has 9Ω windings and is specified to be driven nominally with 5 volts which would give a coil current of around 555 mA. Do not attempt to use the +5V supply from ADALM1000 for this. Use a supply that is capable of supplying at least 1A of current. To make the driver circuit simple for this demonstration, an octal CMOS buffer such as the 74HC541 can serve as an H-bridge. To supply sufficient current to the motor windings we will need to connect multiple buffers in parallel. The schematic example shows two buffers in parallel. Because of the on resistance of the CMOS buffer output transistors in the 74HC541, the coil voltage will not be the full 5 V power supply. Two buffers are strong enough to make the motor spin but not with full torque. Stacking two 74HC541s will provide 4 buffers in parallel, this is easy to accomplish by piggy backing the two DIP packages one on top of the other and soldering their leads together. Using 4 buffers results in about 250 mA of drive current which is about one half of the rated current so the maximum pulse rate will also be about one half of the specified rate or 50 Hz. Two H-bridge circuits using four NMOS and four PMOS power transistors such as the ZVN2110A and ZVP2110A from the Analog Parts Kit ( ADALP2000 ) could be constructed to provide higher coil currents.

Hardware Setup:
~~~~~~~~~~~~~~~

Build the schematic shown in figure 1 on your solderless bread board.

Procedure:
~~~~~~~~~~

The pulse waveform sequence for "forward" rotation is shown in figure 2. A pulse on D0 will energize coil A with a positive polarity and a pulse on D2 will energize coil A with an opposite negative polarity. Similarly, a pulse on D1 will energize coil B with a positive polarity and a pulse on D3 will energize coil B with an opposite negative polarity.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial7_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2, Pulse sequence for forward rotation


As we can see from the timing diagram the coils are energized in a +A, +B, -A, -B sequence. One cycle is four steps. For "reverse" rotation we need to swap the pulse sequence as shown in figure 3. As we can see this is essentially the sequence in reverse order.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial7_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Pulse sequence for reverse rotation


Open the Stepper_1.py or Stepper_2.py Python program in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there. Stepper_test_1.py produces full step pulses. Stepper_test_2.py produces half step pulses. Run the program. You should see something like figure 4.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial7_f4.png
   :align: center
   :width: 170px

.. container:: centeralign

   Figure 4 Stepper_1.py


The Python layer contains a function to configure and control the digital input / output pins on the ALM1000. The digital outputs can be configured as either static inputs or outputs.

**Code example 1:**

In this first code example we configure the four digital pins, PIO 0 - 3, as outputs using the basic devx.ctrl_transfer () function to turn them on and off one at a time in the desired sequence by looping through a look-up table.

| # step tables for full steps
| D0steptab = [1, 0, 0, 0]
| D1steptab = [0, 1, 0, 0]
| D2steptab = [0, 0, 1, 0]
| D3steptab = [0, 0, 0, 1]

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
         devx.ctrl_transfer(DevID, 0x40, D0stepcode, 0, 0, 0, 0, 100) # set PIO 0
         devx.ctrl_transfer(DevID, 0x40, D1stepcode, 1, 0, 0, 0, 100) # set PIO 1
         devx.ctrl_transfer(DevID, 0x40, D2stepcode, 2, 0, 0, 0, 100) # set PIO 2
         devx.ctrl_transfer(DevID, 0x40, D3stepcode, 3, 0, 0, 0, 100) # set PIO 3     
         
         time.sleep(steptime)
         i = i + 1

We need to define two functions, one for forward rotation and one for reverse rotation. All that is different is the way we step through the look-up table by incrementing the pointer to go forward and decrementing the pointer to go in reverse. The time.sleep(steptime) function adds a delay which determines the time a bit is on before the next in the sequence is turned on. The StepCount variable is used to determine how many times the bit pattern is sent.

**Code example 2:**

To rotate the motor using half steps all we need to do is expand the look-up table as shown here:

| # step tables for 1/2 steps
| D0steptab = [1, 1, 0, 0, 0, 0, 0, 1]
| D1steptab = [0, 1, 1, 1, 0, 0, 0, 0]
| D2steptab = [0, 0, 0, 1, 1, 1, 0, 0]
| D3steptab = [0, 0, 0, 0, 0, 1, 1, 1]
| As we can see there are now 8 patterns in the table. The half way between steps are produced when both coils are on at the same time.

Questions:
~~~~~~~~~~

**Challenges**

**For Further Reading:**

https://en.wikipedia.org/?title=Stepper_motor

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`
