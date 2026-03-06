MicroPython Overview
====================

<blockquote>MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimized to run on micro-controllers and in constrained environments. (http://micropython.org/)</blockquote>

To be short, MicroPython is a Python environment running on the bare metal.

Though the :adi:`SHARC Audio Module <sharcaudiomodule>` is powerful enough to run the full Python 3 on the Linux operating system, depending on the use case, it might be favorable to use the Python on bare metal. The MicroPython has been ported over to the SHARC Audio Module, and can be used in conjunction with the :doc:`Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` to utilize the on-chip :adi:`sharc` DSP. You can get the latest version of source code at https://github.com/analogdevicesinc/micropython

The SHARC Audio Module port of MicroPython currently has drivers for ``GPIO``, ``TWI``, ``SPI``, ``RTC``, ``Timer``, and ``SD`` card, and is compatible with the drivers in the official pyboard by MicroPython.

A user can either use the interactive shell (REPL) to write the Python program directly on the SAM through the FTDI USB-serial cable, or load and run a written program stored on the SD card.

Demo
----

This video demonstrates some basic features of the MicroPython for SHARC Audio Module as well as how it can be used in conjunction with the Bare Metal Framework.

.. image:: https://wiki.analog.com/_media/youtube>LwsSwZ6zaPQ
   :alt: youtube>LwsSwZ6zaPQ
   :align: center

Tutorials
---------

Follow these tutorials to become familiar with using MicroPython on the SHARC Audio Module.

.. tip::

   These tutorials are meant to help you with using SHARC Audio Module specific functions of MicroPython, but not Python or MicroPython in general. You can find more general information about them on their official Wiki sites.


-  :doc:`Tutorial: Running MicroPython on the SHARC Audio Module main board </wiki-migration/resources/tools-software/sharc-audio-module/micropython/running>`
-  :doc:`Tutorial: Using Hardware Peripherals with MicroPython </wiki-migration/resources/tools-software/sharc-audio-module/micropython/peripherals>`
-  :doc:`Tutorial: Using MicroPython in conjunction with the Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/micropython/bmsdk>`
-  :doc:`Tutorial: Building MicroPython with CrossCore Embedded Stuidio </wiki-migration/resources/tools-software/sharc-audio-module/micropython/building>`
-  :doc:`Tutorial: Creating a New C-language MicroPython Module </wiki-migration/resources/tools-software/sharc-audio-module/micropython/new-module>`

--------------

`Faust and the SHARC Audio Module#.|SHARC Audio Module#.|Back to main SHARC Audio Module <https://wiki.analog.com/_media/navigation SHARC Audio Module#.faust>`__
