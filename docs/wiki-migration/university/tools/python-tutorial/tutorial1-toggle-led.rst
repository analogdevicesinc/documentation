Activity: Controlling Multiple LEDs, For ADALM1000
==================================================

Objective:
----------

Light Emitting Diodes (LEDs) are high efficiency lights commonly used in indicators and for illumination. In this Activity you will learn how to manually toggle four LEDs on and off when you click on a control button and then modify the program to program to display a binary number.

Common Notes:
-------------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The blue shaded rectangles indicate connections to the M1000 digital I/O connector.

The digital I/O channel pins are referred to as D0 through D3. These correspond to the pins labeled PIO 0 - PIO 3 on the ALM1000 board silkscreen.

The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

Background:
~~~~~~~~~~~

The Python software development layer (libsmu and pysmu) for the ADALM1000 provides a way to write specific control routines for external hardware. Be sure to install the libsmu and Python bindings, if you have not done so already, before continuing with this activity.

:git-libsmu:`libsmu on GitHub <tree/master>`

The first thing to do is connect / initialize to the ADALM1000 by doing the following commands:

::

   #
   # Setup ADAML1000
   session = Session(ignore_dataflow=True, queue_size=10000)
   if not session.devices:
       print 'no device found'
       exit()
   #
   devx = session.devices[0]
   #

This sets up a "session" to communicate with the hardware. This will find and use the first board found. This simple approach works well when only one board is connected to the computer.

Now through Python we can set as outputs and control any or all of the general purpose digital pins on the ALM1000.

To set a pin to output a low ( logic 0 ):

::

   # assign digital pins
   PIO_0 = 28
   PIO_1 = 29
   PIO_2 = 47
   PIO_3 = 3 
   # set PIO0 low
   devx.ctrl_transfer(0x40, 0x50, PIO_0, 0, 0, 0, 100)

   # To set a pin to output a high ( logic 1 ):
   # set PIO1 high
   devx.ctrl_transfer(0x40, 0x51, PIO_1, 0, 0, 0, 100)

The hex number 0x50 sets a pin low, the hex number 0x51 sets a pin high. The next value after the 0x50 or 0x51 is the number of the I\\O pin. The rest of the values are the always the same and should not be changed.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| 4 - LEDs
| 4 - 100 Ω resistors

Directions:
~~~~~~~~~~~

On your solder-less breadboard connect the four digital I/O pins from the ADALM1000 digital connector to drive four LEDs as shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial1_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Drive circuit for four LEDs


Hardware Setup:
~~~~~~~~~~~~~~~

Plug the USB cable into the ALM1000.

Procedure:
~~~~~~~~~~

Open the toggle_led.py Python program in your favorite editor (from this archive `toggle-leds.zip <https://wiki.analog.com/_media/university/tools/python-tutorial/toggle-leds.zip>`__). The IDLE that comes with Python is handy because you can run the program directly from there. Scroll down to the sel() function. You will see a series of if statements that set a pin high or low depending on how the buttons are set in the window. The sel() function is called whenever a button is pushed. Run the program, and you should see something like this.

.. image:: https://wiki.analog.com/_media/university/tools/python-tutorial/python_tutorial1_f2.png
   :align: center
   :width: 150px

Push some of the buttons to toggle on and off the LEDs.

Close the previous program and now open toggle_led_alt.py in the editor. Scroll down to the sel() function. In this example we use an alternate approach where we use the value, either 1 or 0, of the button variables to set a pin by adding it to 0x50 and sending that through the devx.ctrl_transfer() function.

Questions:
~~~~~~~~~~

Can you think of any other program techniques to select which of the LEDs to turn on and off? Can you think of a way to control more than four LEDs?

Extra Challenge:
~~~~~~~~~~~~~~~~

Modify the program to display the binary representation of a user specified number from 0 to 15.

**For Further Reading:**

| `LEDs <https://en.wikipedia.org/wiki/LED>`__
| `LED circuit <https://en.wikipedia.org/wiki/LED_circuit>`__
| `Charlieplexing <https://en.wikipedia.org/wiki/Charlieplexing>`__

| **Return to** :doc:`Introduction to Electrical Engineering </wiki-migration/university/labs/intro_ee>` **Lab Activity Table of Contents**
| **Return to Python Tutorial** :doc:`Table of Contents </wiki-migration/university/tools/python-tutorial/table-of-contents>`
