Activity: Reading Push Button Switches, For ADALM1000
=====================================================

Objective:
----------

Push buttons as well as other types of switches provide a simple way for users to interact with and control a physical device and are found in most electronic devices (for example the on/off button on your computer or tablet). In this activity you will learn how to detect when a button is pressed and then modify the code to count the number of times the button is pressed.

Common Notes:
-------------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 - PIO 3 on the ALM1000 board silkscreen.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Background:
~~~~~~~~~~~

Through Python we can get the input state of any or all of the general purpose digital pins on the ALM1000.

To get an input state:

::

   # assign digital pins
   PIO_0 = 28
   PIO_1 = 29
   PIO_2 = 47
   PIO_3 = 3 
   # get state of PIO0\\
   Pio0 = devx.ctrl_transfer(0xc0, 0x91, PIO_0, 0, 0, 1, 100)

The value after 0x91 is the number of the I\\O pin. The rest of the values are the always the same and should not be changed.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 4 - Tactile push button switches
| 4 - 1 KΩ resistors

Directions:
~~~~~~~~~~~

On your solder-less breadboard connect the four digital I/O pins from the ADALM1000 digital connector to read back the four switches as shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial2_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1 Switches connected to digital inputs


Hardware Setup:
~~~~~~~~~~~~~~~

Plug the USB cable into the ALM1000.

Procedure:
~~~~~~~~~~

Open the read_buttons.py Python program (from `read_buttons.zip <https://wiki.analog.com/_media/university/tools/python-tutorial/read_buttons.zip>`__) in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there. Scroll down to the Digital_in() function. You will see a series of if statements that read the state of an input pin, high or low depending on which of the buttons is pressed. The program then changes the background color of label for each input pin based on what was read. The Digital_in() function is called continuously whenever the Run button is selected.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial2_f2.png
   :align: center
   :width: 200px

Questions:
~~~~~~~~~~

Can you think of any other program techniques to detect which of the switches is being pressed? Can you think of ways to read back the state of more than 4 switches?

Challenges:
~~~~~~~~~~~

Combine the LED and push button programs to turn on and off two LEDs based on which of two buttons are pressed.

**For Further Reading:**

`Novel Switch Interface Scheme Reduces Microprocessor Pin Count <https://www.radiolocman.com/review/article.html?di=653075>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to Python Tutorial** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`
