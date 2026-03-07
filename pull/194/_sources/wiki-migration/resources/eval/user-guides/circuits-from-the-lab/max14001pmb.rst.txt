MAX14001PMB Single-channel 10-bit ADC PMOD User Guide
=====================================================

The :adi:`MAX14001PMB` peripheral module provides the hardware to evaluate the MAX14001 isolated ADC to measure two channels of data, line voltage (up to 230V AC or ±325V DC), and load current (up to 5A). All power and communication are with a simple USB cable—no separate field-side power is required. The integrated DC-DC converter provides power isolation for the system and powers all field-side circuitry. This integrated design reduces the BOM and board dimension for building an isolated ADC system.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max14001pmb/max14001_board.png
   :align: center
   :width: 400px

| The module has two MAX14001 devices (U11 and U51). One channel is configured to measure the line voltage with the maximum voltage range selected by a resistor chain. The other channel is configured to measure the voltage across a shunt resistor to provide load current. Both AC and DC signals can be measured. Connector X2 provides the connection of the input signal to the MAX14001 device.
| ===== Hardware =====

Power Supply Requirements
-------------------------

| When using the MAX14001 PMOD board, the 3.3 V power comes directly from the host board it is connected to. The power from the host is generally capable of providing up to 100 mA at 3.3 V; but for complete PMOD power specifications, please click\ `here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`_.
| ==== Digital Interface (PMOD) ==== The PMOD interface is a series of standardized digital interfaces for various digital communication protocols such as SPI, I2C, and UART. These interface types were standardized by Digilent, which is now a division of National Instruments. Complete details on the PMOD specification can be found `here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`_.

Connector X1 provides a connection of the module to the Pmod host. It has a 12-pin Pmod™-compatible connector for SPI communication. The pin assignments and functions adhere to the Pmod standard recommended by Digilent.

| |image1|
| ===== Device Driver Support ===== There are two device driver solutions that are provided for controlling the **MAX14001PMB**:

-  **MAX14001 no-OS Driver**

   -  The :doc:`MAX14001 no-OS driver </wiki-migration/resources/tools-software/uc-drivers/max14001>` is used in bare-metal applications, typically running on low-power, embedded microcontrollers.

More information and Useful links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`MAX14001 Product Page <MAX14001>`
-  :adi:`MAX14001PMB Product Page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max14001pmb.html>`
-  :doc:`MAX14001 No-OS driver </wiki-migration/resources/tools-software/uc-drivers/max14001>`
-  :adi:`UG-6636: Guide to Programming the MAX14001/MAX14002 Isolated ADCs <media/en/technical-documentation/user-guides/guide-to-programming-the-max14001max14002-isolated-adcs--maxim-integrated.pdf>`

Schematics, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :adi:`MAX14001PMB Datasheet <media/en/technical-documentation/data-sheets/MAX14001PMB.pdf>`
   


Additional Information
~~~~~~~~~~~~~~~~~~~~~~

-  `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_
-  :doc:`PyADI-IIO Installation Guide </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
-  :doc:`IIO Oscilloscope Installation Guide </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

Registration
~~~~~~~~~~~~

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/MAX14001PMB?&v=Rev A>`_ to receive all these great benefits and more!


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max14001pmb/max14001_spi.png
   :width: 300px
