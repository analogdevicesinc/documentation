ADA4250 - No-OS Driver
======================

Supported Devices
-----------------

-  :adi:`ADA4250`
-  :adi:`ADA4230`

Evaluation Boards
-----------------

-  :adi:`EVAL-ADA4250-ARDZ`

Overview
--------

The :adi:`ADA4250` is an instrumentation amplifier with SPI/pin-strap progammable gains that is optimized for ultra-low power systems. With a minimum supply voltage of 1.7V, 26uA of quiescent current, a shutdown mode, a sleep mode, and a fast wake up settling time, ADA4250 can be power cycled on a battery powered system for even futher savings.

By keeping the gain resistors internal to the product, better gain and CMR specs can be achieved due to the inherent matching and reduction is parasitics. Additionally, there is a BW mode for optimized noise performance.

AD4250 is available in a 3mm x 3mm 16-lead LFCSP package and a 1.8 mm, 16-ball WLCSP package, making it an excellent solution for applications where size and packing density are important considerations. Performance is specified over the -40°C to +125°C temperature range.

Applications:

-  Battery powered systems
-  Wearables
-  Biomedical analysis
-  Building automation

Driver Description
------------------

The driver contains two parts:

-  The driver for the :adi:`ADA4250` part, which may be used, without modifications, with any microcontroller.
-  The Communication Drivers, where the specific communication functions for the desired type of processor and communication protocol have to be implemented. This driver implements the communication with the device and hides the actual details of the communication protocol to the ADI driver.

The Communication Driver has a standard interface, so the :adi:`ADA4250` driver can be used exactly as it is provided.

The Communication Drivers must include SPI transmission methods for :adi:`ADA4250` and GPIO control methods for :adi:`ADA4230`.

For the SPI method, the :adi:`ADA4250` driver calls three functions:

-  spi_init() - initializes the SPI communication peripheral.
-  spi_remove() – frees memory allocated by the SPI communication driver.
-  spi_write_and_read() – conduct information transfer with the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_driver_architecture.png
   :align: center

For the GPIO control methods, the :adi:`ADA4230` driver calls three functions:

-  gpio_get() - initialize GPIO peripheral and allocate memory for one GPIO control.
-  gpio_remove() - frees memory allocated by the GPIO control driver.
-  gpio_direction_input() - set GPIO as input.

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `ADA4250 Header file <http://analogdevicesinc.github.io/no-OS/ada4250_8h.html>`__
-  `ADA4250 Source file <http://analogdevicesinc.github.io/no-OS/ada4250_8c.html>`__

Initialization example
----------------------

Downloads
---------

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of ADA4250 Driver.|

   -

   |Header file of ADA4250 Driver.|

.. |Implementation of ADA4250 Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/amplifiers/ada4250/ada4250`.c
.. |Header file of ADA4250 Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/amplifiers/ada4250/ada4250`.h
