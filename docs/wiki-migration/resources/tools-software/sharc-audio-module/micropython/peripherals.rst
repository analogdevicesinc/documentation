Tutorial: Using hardware peripherals with MicroPython
=====================================================

One advantage of MicroPython over a normal Python running on Linux for the SHARC Audio Module is that it has direct support of many hardware features, such as GPIO, TWI etc. This page gives a few examples of using these peripherals.

Getting Help
------------

MicroPython has a ``help()`` function builtin. You can always use the help to get a list of supported properties and functions:

::

   >>> help(machine)
   object <module 'umachine'> is of type module
     __name__ -- umachine
     info -- <function>
     unique_id -- <function>
     reset -- <function>
     soft_reset -- <function>
     freq -- <function>
     Pin -- <class 'Pin'>
     Signal -- <class 'Signal'>
     I2C -- <class 'I2C'>
     SPI -- <class 'SPI'>
     SD -- <SDCard>
     SDCard -- <class 'SDCard'>
     SOFT_RESET -- 0
     SYSSRC_RESET -- 1
     HARD_RESET -- 2
     UNKNOWN_RESET -- 3

Machine Module
--------------

The machine module is the base module for almost all hardware related functions. On some MicroPython ports it is also called ``pyb``, an acronym of ``pyboard``.

GPIO
~~~~

The GPIO support of MicroPython is part of the machine library, called the Pin class.

Here is a example using the Pin class to light up an LED:

.. code:: python

   from machine import Pin
   led = Pin("LED10", Pin.OUT)
   led.value(1)

Besides the name LED10, one may also refer to that pin by its number (``PD1``), or any alternative functions it has (``SPI0_SEL2``, ``ACM0_A4``, ``SMC0_AOE``, and ``SPI0_SS``). One may also select the alternative function when initializing the pin (but generally not necessary).

Pin mode can be either ``Pin.OUT`` or ``Pin.IN``, and value can be either ``0`` or ``1``.

Continue with the previous example, to blink the LED in a loop:

.. code:: python

   import time
   while True:
       led.value(1)
       time.sleep_ms(500)
       led.value(0)
       time.sleep_ms(500)

You can use Ctrl-C to stop the loop.

Here is another example to use a pin in input mode:

.. code:: python

   button = Pin("BTN1", Pin.IN)
   button.value()

When the SW1 is not pressed, ``value()`` should return 0. When the SW1 is pressed, it should return 1.

GPIO Interrupt
~~~~~~~~~~~~~~

GPIO interrupt is supported. See example below:

.. code:: python

   from machine import Pin
   button = Pin("BTN1", Pin.IN)
   button.irq(lambda p:print(p), trigger=Pin.IRQ_RISING)

In the example, the interrupt service routine (ISR) is a lambda function. It can also be a full Python function.

The trigger can be ``Pin.IRQ_RISING``, ``Pin.IRQ_FALLING``, or ``Pin.IRQ_LOW``.

.. important::

   Though this is in Python, the interrupt is still the real hardware interrupt. Just like in C, restrictions apply:

   
   -  One may not allocate memory inside an ISR.
   -  One needs to process all the errors raised before exiting the ISR.
   -  Keep the ISR as short as possible.
   


SPI
~~~

SPI support is also part of the machine library, called the SPI class. On the SHARC Audio Module main board, SPI0 is routed to the expansion interface, SPI1 is routed to the Sigma Studio connector, and SPI2 is connected to the SPI Flash. To test SPI1 on the Sigma Studio connector:

::

   from machine import SPI
   spi = SPI(1, baudrate=600000, polarity=1, phase=0)
   spi.write(b'1234')

Here is a list of possible initialization arguments:

-  ``baudrate``: SCK clock rate in Hz.
-  ``polarity``: 0 or 1, the level when the clock line is idle.
-  ``phase``: 0 or 1, 0 means to sample data on the first clock edge, and 1 means the second.
-  ``bits``: Can be 8, 16, or 32. It is the number of bits in each transferred word.

TWI
~~~

TWI, which is also called as I2C, is also supported by the machine library. On the SHARC Audio Module main board, TWI0 (I2C0) connects to the audio codec and A2B transceiver, also routed to the Sigma Studio connector. To scan the devices connected to the I2C0:

.. code:: python

   from machine import I2C
   i2c = I2C(0, freq=400000)
   i2c.scan()

Note the scan is accomplished by simply sending the address and wait for acknowledge. If no acknowledge is received, no such device exists. Unlike normal transmission, no actual data bytes will be sent out during the scan process.

SD card
~~~~~~~

.. note::

   If an SD card is inserted before powering up, it will automatically initialize the SD card and mount the filesystem to ``/sd`` during boot. So there is no need to manually go through the process.


The SD card is connected to the ADSP-SC589 through the MSI (or called RSI in the ADI drivers). SD is also a class of the machine module.

To print out the information about the SD card:

.. code:: python

   from machine import SD
   SD.power(True)
   SD.info()

To interface with the SD driver directly without using the filesystem, the SD driver provides these API:

-  present
-  power
-  info
-  read
-  write
-  readblocks
-  writeblocks
-  ioctl

.. note::

   In another way, any driver with this block device interface can work with the filesystem. ``drivers\sdcard\sdcard.py`` provides a good example of writing an SD card driver purely in Python language.


Refer to MicroPython's documentation for more information about the block device interface.

SHARC Core
----------

MicroPython only works on the ARM core. In order to utilize the SHARC core, a user can use MicroPython to boot the SHARC core with a pre-compiled loader file, and then use shared memory to exchange data with the SHARC core.

Here is a example of loading an audio pass-through application located on the SD card:

.. code:: python

   f = open('pass_through.ldr', 'rb')
   stream = f.read()
   import sharc
   sharc.boot(stream)

--------------

`Running MicroPython on the Board#..micropython|MicroPython Overview#.bmsdk|Using MicroPython with Bare Metal Framework <https://wiki.analog.com/_media/navigation SHARC Audio Module#.running>`__
