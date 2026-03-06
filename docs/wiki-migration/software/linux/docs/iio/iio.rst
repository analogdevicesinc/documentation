Linux Industrial I/O Subsystem
==============================

.. image:: https://wiki.analog.com/_media/software/linux/docs/iio.png
   :alt: iio.png

IIO Overview
------------

-  The Industrial I/O subsystem is intended to provide support for devices that in some sense are analog to digital or digital to analog converters (ADCs, DACs).
-  Devices that fall into this category are:

   -  ADCs
   -  Accelerometers
   -  Gyros
   -  IMUs
   -  Capacitance to Digital Converters (CDCs)
   -  Pressure Sensors
   -  Color, Light and Proximity Sensors
   -  Temperature Sensors
   -  Magnetometers
   -  DACs
   -  DDS (Direct Digital Synthesis)
   -  PLLs (Phase Locked Loops)
   -  Variable/Programmable Gain Amplifiers (VGA, PGA)

-  The overall aim is to fill the gap between the somewhat similar hwmon and input subsystems.
-  Hwmon is very much directed at low sample rate sensors used in applications such as fan speed control and temperature measurement.
-  The input is⁠ (as its name suggests) focused on human interaction input devices:

   -  Keyboard
   -  Mouse
   -  Touch Screen
   -  Joystick

-  In some cases, there is considerable overlap between these and IIO.

-  A typical device falling into the IIO category would be connected via SPI or I2C.
-  However typical DMA operated devices such as ones connected to a high speed synchronous serial (McBSP, SPORT) or high speed synchronous parallel (EPI, PPI) or FPGA peripherals are also subject to this subsystem.
-  Since latter ones unlike SPI or I2C are not generally abstracted by Linux bus drivers they are subject to processor platform dependent implementations.

IIO Subsystem Overview
----------------------

.. image:: https://wiki.analog.com/_media/software/linux/docs/iio/iio_block_view.png
   :alt: iio_block_view.png
   :width: 600px

Functionality of IIO
~~~~~~~~~~~~~~~~~~~~

-  Basic device registration and handling
-  Polled access to device channels via sysfs.
-  Event chrdevs

   -  These are similar to input in that they provide a route to user space for hardware triggered events. Such events include threshold detectors, free-fall detectors and more complex action detection. The events themselves are currently very simple with merely an event code and a timestamp. Any data associated with the event must be accessed via polling.

.. hint::

   A given device may have one or more event channel. These events are turned on or off (if possible) via sysfs interfaces.


-  Hardware ring buffer support
-  Some recent sensors have included fifo / ring buffers on the sensor chip.
-  These greatly reduce the load on the host CPU by buffering relatively large numbers of data samples based on an internal sampling clock.
-  Each ring buffer typically has an event chrdev (similar to the more general ones above) to pass on events such as buffer 50% full and an access chrdev via which the raw data it self may be read back.
-  Trigger and software ring buffer (kfifo) support

Trigger and software ring buffer support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  In many data analysis applications it is useful to be able to capture data based on some external signal (trigger).
-  These triggers might be a

   -  data ready signal
   -  gpio line connected to some external system
   -  on processor periodic interrupt.
   -  User space reading a specific file in sysfs.

-  A single trigger many initialize data capture or reading from a number of sensors.
-  These triggers are used in iio to fill software ring buffers acting in a very similar fashion to the hardware buffers described above.
-  Triggers can be completely unrelated to the sensor itself

Standalone trigger drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+-------------------------------------------------------------------------------+
| name                                          | description                                                                   |
+===============================================+===============================================================================+
| iio-trig-gpio                                 | Provides support for using GPIO pins as IIO triggers.                         |
+-----------------------------------------------+-------------------------------------------------------------------------------+
| iio-trig-rtc                                  | Provides support for using periodic capable real time clocks as IIO triggers. |
+-----------------------------------------------+-------------------------------------------------------------------------------+
| `iio-trig-sysfs <iio-trig-sysfs>`__           | Provides support for using SYSFS entry as IIO triggers.                       |
+-----------------------------------------------+-------------------------------------------------------------------------------+
| `iio-trig-bfin-timer <iio-trig-bfin-timer>`__ | Provides support for using a Blackfin timer as IIO triggers.                  |
+-----------------------------------------------+-------------------------------------------------------------------------------+


Industrial I/O Subsystem In-Kernel Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IIO subsystem can act as a layer under other elements of the kernel providing a means of obtaining ADC type readings or of driving DAC type signals. The functionality supported will grow as use cases arise.

IIO Ring Buffer / kfifo
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/software/linux/docs/ringbuffer.png
   :alt: ringbuffer.png

-  IIO uses a ring buffer also called circular buffer which is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end.
-  This structure is well suited for buffering data streams. These buffers are typically used to solve the producer-consumer problem. In some applications it is desired for the producer (e.g., an ADC) to overwrite old data if the consumer (e.g., the User Space Application) is unable to momentarily keep up. But typically the buffer is sized to provide adequate space so that this circumstance should never happen.

Pointers
========

-  IIO mailing list: linux-iio@vger.kernel.org
-  `IIO Linux Kernel Documentation sysfs-bus-iio-\* <https://www.kernel.org/doc/Documentation/ABI/testing>`__
-  `IIO Documentation <https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio>`__
-  :doc:`IIO test and visualization application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`libiio - IIO system library </wiki-migration/resources/tools-software/linux-software/libiio>`
-  :doc:`libiio - Internals </wiki-migration/resources/tools-software/linux-software/libiio_internals>`
-  :doc:`Pointers and good books </wiki-migration/resources/tools-software/pointers>`
-  `IIO High Speed <https://events.static.linuxfound.org/sites/events/files/slides/iio_high_speed.pdf>`__
-  `Software Defined Radio using the IIO framework <http://video.fosdem.org/2015/devroom-software_defined_radio/iiosdr.mp4>`__
-

|libiio introduction|

.. image:: https://wiki.analog.com/_media/page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn
   :alt: page>resources/tools-software/linux-drivers/need_help#need help&noheader&firstseconly&noeditbtn

.. |libiio introduction| image:: https://wiki.analog.com/_media/youtube>p_VntEwUe24

