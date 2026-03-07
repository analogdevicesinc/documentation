MAX9611 Current-Sense Amplifier with MAX5380 DAC PMOD User Guide
================================================================

The :adi:`MAX9611PMB1` peripheral module provides the necessary hardware to interface the MAX9611 current-sense amplifier with 12-bit ADC and op amp, along with the MAX5380 8-bit DAC, to any system that utilizes Pmod™-compatible expansion ports configurable for I²C communication. The IC is configured with an external p-channel FET and a current-sense resistor to form a current-limiting circuit capable of handling currents up to 1A.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611.png
   :align: center
   :width: 400px

The :adi:`MAX5380` 8-bit DAC (U1) is used to set the current-limit point programmatically by the host through the I²C bus. In addition to providing a programmable current-limit function, the ADC within the IC measures the load current/voltage and the set-point voltage that can be read by the host through the I²C bus.

Hardware
--------

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

| When using the MAX9611 PMOD board, the 3.3 V power comes directly from the host board it is connected to. The power from the host is generally capable of providing up to 100 mA at 3.3 V; but for complete PMOD power specifications, please click\ `here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`_.
| ==== External Power Supply and Load ==== The peripheral module provides high-side current limiting for an external power supply and load. The supply and load should be connected to the peripheral module, as shown in the setup figure below. Although the IC is capable of operation up to 60V, the external supply should not exceed 30V due to the voltage limitations of the Si2303 pFET. While the pass components are rated to 2.7A, operation above 1A may not yield reliable results due to thermal limitations. Reliable operation of this circuit above 1A should be possible in the user’s application if additional surface/heatsink area for both the Si2303 pFET and the 0.2I sense resistor is provided.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611_external_load.png
   :align: center
   :width: 400px

The J3 connector provides for the attachment of an external power supply and load. See table below.


|image1|

| 
| ==== Current Limit with MAX5380 ==== The point at which current limiting begins is determined by the voltage at pin 4 on the :adi:`MAX9611` (VSET). This voltage is set by the output of the DAC (:adi:`MAX5380`) and the setting of the shunt on JP1, which selects either VDAC or VDAC/10. The nominal 2.00V output of the DAC is divided to 1.26V full scale by the divider formed by R3 and R8 + R9. The lower tap of that divider (R3 + R8 and R9) provides 0.126V full scale.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611-currentlimit.png
   :align: center
   :width: 400px

The position of the shunt on JP1 determines which of the two voltages is connected to VSET on the MAX9611. With the shunt connected between JP1-1 and JP1-2, the higher voltage (VDAC) is connected to VSET. This setting allows full-scale current limit at 2.56A with 10mA steps. When the shunt is connected between JP1-2 and JP1-3, the full-scale current is 256mA with 1mA steps.

.. important::

   The total power dissipation for the pass FET (Q1) should not exceed 1.5W. This can easily be exceeded with even moderate output current if the load voltage is high and the load resistance is low.


| 
| ==== I2C Interface (Daisy-Chaining Modules) ==== Connector J2 allows the module to be connected through a daisy chain from another I2C module and/or provide I2C and power connections to other I2C modules on the same bus using a 4-conductor ribbon cable. In this situation, pins 1-4 and 5-8 on J2 provide two connections to the I2C bus, allowing the module to be inserted into an I2C bus daisy-chain.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611_i2c_expansion.png
   :align: center
   :width: 400px

| 
| ==== I2C Addressing Options ==== Both the MAX5380M and MAX9611 reside on the I2C bus. The MAX5380M has a fixed I2C slave address of 0x62. The I2C slave address for the MAX9611 can be one of nine different values depending on the settings on jumpers JP2 and JP3. Table below lists the settings of those jumpers and the corresponding values of the slave read and write address.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611_i2c_address.png
   :align: center
   :width: 400px

| 
| ==== Digital Interface (PMOD) ==== The PMOD interface is a series of standardized digital interfaces for various digital communication protocols such as SPI, I2C, and UART. These interface types were standardized by Digilent, which is now a division of National Instruments. Complete details on the PMOD specification can be found `here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`_.

Connector J1 provides a connection of the module to the Pmod host. The pin assignments and functions adhere to the Pmod standard recommended by Digilent.

| |image2|
| ===== Device Driver Support ===== There are two device driver solutions that are provided for controlling the **MAX9611PMB1**:

-  **MAX9611 no-OS Driver**

   -  The :doc:`MAX9611 no-OS driver </wiki-migration/resources/tools-software/uc-drivers/max9611>` is used in bare-metal applications, typically running on low-power, embedded microcontrollers.

-  **MAX5380 no-OS Driver**

   -  The :doc:`MAX5380 no-OS driver </wiki-migration/resources/tools-software/uc-drivers/max5380>` is used in bare-metal applications, typically running on low-power, embedded microcontrollers.

-  **MAX9611 Linux Driver**

   -  The :git-linux:`MAX9611 Linux driver <drivers/iio/adc/max9611.c>` is used in applications running the Linux operating system, typically on larger processors and SoC devices.

      -  The MAX9611 Linux driver uses the Industrial Input/Output (IIO) framework, greatly simplifying the development of application code via the cross-platform Libiio library, which is written in C and includes bindings for Python, MATLAB, C#, and other languages. Application code can run directly on the platform board, communicating with the device over the local backend, or from a remote host over the network or USB backends.

| 
| ===== More information and Useful links =====

-  :adi:`MAX9611 Product Page <MAX9611>`
-  :adi:`MAX5380 Product Page <MAX5380>`
-  :adi:`MAX9611PMB1 Product Page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max9611pmb1.html>`
-  :doc:`MAX9611 No-OS driver </wiki-migration/resources/tools-software/uc-drivers/max9611>`
-  :git-linux:`MAX9611 Linux driver <drivers/iio/adc/max9611.c>`
-  :doc:`MAX5380 No-OS driver </wiki-migration/resources/tools-software/uc-drivers/max5380>`

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   
   -  :adi:`MAX9611PMB1 Datasheet <media/en/technical-documentation/data-sheets/MAX9611PMB1.pdf>`
   -  :adi:`MAX5380 Datasheet <en/products/max5380.html>`
   


Additional Information
----------------------

-  `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_
-  :doc:`PyADI-IIO Installation Guide </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
-  :doc:`IIO Oscilloscope Installation Guide </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/MAX9611PMB1?&v=Rev A>`_ to receive all these great benefits and more!


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611_j3_table.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/max9611/max9611_i2c.png
   :width: 400px
