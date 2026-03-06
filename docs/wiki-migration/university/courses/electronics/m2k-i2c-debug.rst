Debugging I2C with the ADALM2000
================================

Objective
---------

The objective of this tutorial is to use the Logic Analyzer instrument provided by the :adi:`ADALM2000` (M2K) board and the :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` software toolset to visualize I2C (Inter-Integrated Circuit) transactions between two devices.

The :doc:`ADT7420 PMOD Temperature Demo </wiki-migration/resources/eval/user-guides/eval-adicup360/reference_designs/demo_adt7420>` project will be used as an example. The project uses the :adi:`EVAL-ADT7420-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adt7420-pmdz.html>` connected to the :adi:`EVAL-ADICUP360` microcontroller board. The PMOD includes the :adi:`ADT7420` high accuracy digital temperature sensor.

The Demo application includes a function that reads and displays the temperature data from the ADT7420 and one that reads and displays the ID register data for ADT7420.

Background
----------

I2C is a serial protocol for connecting low-speed peripheral integrated circuits like EEPROMs, A/D and D/A converters and other similar peripherals in embedded systems to processors and microcontrollers in short-distance (intra-board communication).

I2C supports multiple slave devices; a single master can communicate with one or more slaves, provided each slave is set to a unique address (this is either factory-programmed, or set through address pins on the device). Multiple masters are also supported through an arbitration scheme, useful, for example, when several microcontrollers require access to a single memory device.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   Figure 1. I2C master-slave configuration


I2C physical layer signals:

-  **SDA (Serial Data)** – bidirectional data line for the master and slave to send and receive data
-  **SCL (Serial Clock)** – line that carries the clock signal, driven by the master

Being a serial communication protocol, I2C data is transferred bit by bit along a single wire (the SDA line). I2C is synchronous, meaning data transfer is synchronized by a clock signal driven by the master to one or more slaves. Both SDA and SCL are open-drain logic, requiring a pullup resistor (or active pullup circuit) to the bus's logic high level. Refer to the references at the end of this page for further details on the operation of the I2C bus.

Data is transferred in transactions composed of one or more 9-bit frames. Each transaction has an address frame that contains the binary address of the slave, and one or more data frames. The transaction also includes start and stop conditions, read/write bits, and ACK/NACK bits between each data frame as shown in Figure 2.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   Figure 2. I2C transaction content


Transaction components:

-  **Start** - SDA line transitions from a high logic level to a low logic level while the SCL line is high.
-  **Address Frame** - master indicates the slave to which the transaction is being sent
-  **Read/Write Bit** - bit that indicates if the master is sending (low voltage level) or receiving (high voltage level) data from slave.
-  **Data Frame** - 8-bit data passed from master to slave or vice versa, starting with the most significant bit first (MSB)
-  **ACK/NACK Bit** - the ACK bit is returned from the receiving device if an address frame or data frame is received.
-  **Stop** - SDA line transitions from a low logic level to a high logic level while the SCL line is high.

Hardware Configuration
----------------------

Figure 3. shows the hardware connection between M2K board and EVAL-ADICUP360 + EVAL-ADT7420-PMDZ.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 3. I2C Debug Hardware Setup


The I2C pins are available for monitoring at port PWMH of the EVAL-ADICUP360.

**EVAL-ADICUP360 I2C pin configuration:** Port PWMH:

-  Pin9 - SDA
-  Pin10 - SCL

Port POWER:

-  Pin6 - DGND

**M2K I2C pin configuration:**

-  DIO0 - SCL
-  DIO1 - SDA

Connect the M2K pins to the EVAL-ADICUP360 as follows:

-  Pin9 - DIO1
-  Pin10 - DIO0
-  GND - DGND

Scopy Logic Analyzer Configuration
----------------------------------

Open the Logic Analyzer instrument, select DIO0-DIO1 lines and press the “Group with selected” button.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   Figure 3. I2C Group Channels


Select the channel group formed and apply the I2C decoder. While the group is selected, open settings menu by pressing the |image5| button on the top right side of the user interface. A settings panel will appear for the I2C decoder, allowing the signal-channel configuration and parameters setup.

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   Figure 4. Group Settings


The Logic Analyzer must be set up to "catch" the I2C transfer on the Logic Analyzer plot. Therefore we need to configure a trigger. Since the I2C transfer starts with a falling edge on the SDA signal, this event can be used as the trigger.

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   Figure 5. Trigger Settings


I2C Transfer Example
--------------------

This example verifies that for a given software command, the correct transactions are transferred over I2C between master (EVAL-ADICUP360) and slave (EVAL-ADT7420-PMDZ).

The default I2C device address for EVAL-ADT7420-PMDZ is 0x48.

Read ID Register
~~~~~~~~~~~~~~~~

Set the Time Base of the Logic Analyzer instrument to 50us and the Trigger Position at 200us and run a Single sweep.

.. container:: centeralign

   \ |image8|\


.. container:: centeralign

   Figure 6. General Settings


The Logic Analyzer will wait for the falling edge of the SDA signal to be triggered.

Run the "ADT7420_Read_One_Reg (ID_REG)" function. This will initiate the I2C transfer.

The result is presented in Figure 7.

.. container:: centeralign

   \ |image9|\


.. container:: centeralign

   Figure 7. I2C Read ID Register


Analyzing the plot, the fist half of the transaction contains a write sequence composed of the device address (0x48) with the R/W bit set low (write) followed by the address of the ID register. The master then issues a repeat-start condition for the second half of the transaction - the device address is re-sent with the R/W bit set high(read), and the byte of data containing the contents of the ID register (0xCB) is read out.

Read Temperature
~~~~~~~~~~~~~~~~

Set the Time Base of the Logic Analyzer instrument to 75us and the Trigger Position at 250us and run a Single sweep.

The Logic Analyzer will wait for the falling edge of the SDA signal to be triggered.

Run the "ADT7420_Read_Temp()" function. This will initiate the I2C transfer.

The result is presented in Figure 8.

.. container:: centeralign

   \ |image10|\


.. container:: centeralign

   Figure 8. I2C Read Temperature


Analyzing the plot, the fist half of the transaction contains a write sequence composed of the device address (0x48) with the R/W bit set low (write) followed by the address of the temperature value MSB register. The master then issues a repeat-start condition for the second half of the transaction - the device address is re-sent with the R/W bit set high(read), and two bytes of data representing content of the temperature value most significant byte (0x0E) and temperature value least significant byte (0xE8). This illustrates the fact that the address pointer in the ADT7420 automatically increments as the master reads out data bytes.

Conclusion
----------

| In addition to I2C, the application includes a set of decoders covering a large number of communication protocols such as SPI, I2S, UART, JTAG, and others, making ADALM2000 a powerful tool for analyzing and debugging digital signals.

Further Reading:
^^^^^^^^^^^^^^^^

-  `I2C specification (External link to NXP) <https://www.nxp.com/docs/en/user-guide/UM10204.pdf>`__
-  :adi:`I2C Primer: What is I2C? (Part 1) <en/technical-articles/i2c-primer-what-is-i2c-part-1.html>`
-  :adi:`I2C Timing: Definition and Specification Guide (Part 2) <en/technical-articles/i2c-timing-definition-and-specification-guide-part-2.html>`
-  :adi:`I2C-Cabling <media/en/technical-documentation/technical-articles/I2C-Cabling.pdf>`
-  :doc:`EVAL-ADICUP360 User Guide </wiki-migration/resources/eval/user-guides/eval-adicup360>`
-  :doc:`ADALM2000 Overview </wiki-migration/university/tools/m2k>`
-  :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>`
-  :doc:`ADT7420 PMOD Temperature Demo </wiki-migration/resources/eval/user-guides/eval-adicup360/reference_designs/demo_adt7420>`
-  :adi:`EVAL-ADT7420-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adt7420-pmdz.html>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_diagram.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_message.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/hw_i2c_m2k.png
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_group.png
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/grp_set_butt.png
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_grp_settings.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_trigger_grp.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/la_settings_i2c.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_read_id_plot.png
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/i2c_read_temp_plot.png
