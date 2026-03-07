FTHR-PMD-INTZ Feather-to-PMOD Interposer Hardware User Guide
============================================================

|

.. important::

   **Notice:** This page has been fully migrated to GitHub.io and is no longer maintained on the Wiki. Please refer to the GitHub link below for the most current and accurate information.

   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/fthr-pmd-intz/index.html
   | If you would like to contribute updates to this document, please submit your suggestions via a Pull Request on the GitHub page.
   | Thank you for your understanding, and we apologize for any inconvenience this transition may cause.
   


Overview
--------

The :adi:`FTHR-PMD-INTZ` is an add-on adapter board especially built for the MAXIM MCU boards. Maxim Feather Boards, namely the :adi:`MAX32630FTHR`, :adi:`MAX32650FTHR`, :adi:`MAX32655FTHR`, :adi:`MAX32666FTHR`, and :adi:`MAX78000FTHR`, are very small form factors called "feathers", and they require special connectors to be used with other Pmod boards.

This interposer board provides such solution and allows interfacing with up to two Pmod boards via SPI or I2C interface. Furthermore, this add-on adapter board adheres to the standards, such as the Digilent Pmod™ Interface Specification and Adafruit Feather Specification.


|image1|

.. container:: center

   *<fc>Figure 1. FTHR-PMD-INTZ</fc>*


.. note::

   **Evaluation Kit Contents:**

   
   -  :adi:`FTHR-PMD-INTZ` Adapter Board (:adi:`Buy <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/FTHR-PMD-INTZ>`)
   


Adapter Board Hardware
----------------------

|image2|

.. container:: center

   *<fc>Figure 2. Hardware Parts</fc>*


Power Configuration
~~~~~~~~~~~~~~~~~~~

| The circuit is powered by the voltage coming from the Maxim Feather headers. |image3|

.. container:: center

   *<fc>Figure 3. Power Jumpers</fc>*


| The table below lists the power configuration for this interposer board. The default voltage configuration for all is 3V3.

+----------+---------------------------+---------------------+----------------------+
| **Part** | **Description**           | **Left Connection** | **Right Connection** |
+----------+---------------------------+---------------------+----------------------+
| P2       | Feather Voltage Selector  | 3V3                 | 1V8                  |
+----------+---------------------------+---------------------+----------------------+
| P4       | I2C PMOD Voltage Selector | 3V3                 | VBUS (5V)            |
+----------+---------------------------+---------------------+----------------------+
| P5       | SPI PMOD Voltage Selector | 3V3                 | VBUS (5V)            |
+----------+---------------------------+---------------------+----------------------+

SPI Pmod Connector (P6)
~~~~~~~~~~~~~~~~~~~~~~~

Connect Pmod devices that use SPI interface to the left-hand side Pmod connector, as shown below.


|image4|

.. container:: center

   *<fc>Figure 4. SPI PMOD Connector</fc>*


The table below lists the corresponding pin assignment

+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| SPI Pmod Connector (P6) Pinout |                                                                 |                |                                                                     |
+================================+=================================================================+================+=====================================================================+
| **Pin Number**                 | **Pin Function on FTHR-PMD-INTZ**                               | **Pin Number** | **Pin Function on FTHR-PMD-INTZ**                                   |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| 1                              | **CS**. SPI Chip select #1 from MAXFTHR to the Pmod device.     | 7              | **SPI_GPIO0**. Interrupt Signal from the Pmod device to the MAXFTHR |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| 2                              | **MOSI_GPIO1**. SPI data from MAXFTHR to the Pmod device.       | 8              | **SPI_GPIO1**. Reset Signal from MAXFTHR to Pmod device             |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| 3                              | **MISO**. SPI data from MAXFTHR to the Pmod device.             | 9              | **SPI_GPIO2**. SPI Chip select #2 from MAXFTHR to the Pmod device.  |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| 4                              | **SCLK**. SPI Clock from MAXFTHR to the Pmod device.            | 10             | **SPI_GPIO3**. SPI Chip select #3 from MAXFTHR to the Pmod device.  |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| 5                              | **GND**. Ground                                                 | 11             | **GND**. Ground                                                     |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+
| 6                              | **VCC**. Connected to 3V3 or VBUS from MAXFTHR (shorted in P5). | 12             | **VCC**. Connected to 3V3 or VBUS from MAXFTHR (shorted in P5).     |
+--------------------------------+-----------------------------------------------------------------+----------------+---------------------------------------------------------------------+

I2C Pmod Connector (P7)
^^^^^^^^^^^^^^^^^^^^^^^

Pmod devices that use I2C interface should be connected to the right Pmod connector.


|image5|

.. container:: center

   *<fc>Figure 5. I2C PMOD Connector</fc>*


| The table below lists the corresponding pin assignment
| ^ I2C Pmod Connector (P7) Pinout ^^^^

+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| **Pin Number** | **Pin Function on FTHR-PMD-INTZ**                                    | **Pin Number** | **Pin Function on FTHR-PMD-INTZ**                                    |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| 1              | **I2C_GPIO0**. Interrupt Signal from the Pmod device to the MAXFTHR. | 7              | **I2C_GPIO0**. Interrupt Signal from the Pmod device to the MAXFTHR. |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| 2              | **I2C_GPIO1**. Reset Signal from the MAXFTHR to the Pmod device.     | 8              | **I2C_GPIO1**. Reset Signal from the MAXFTHR to the Pmod device.     |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| 3              | **SCL**. I2C Clock from the MAXFTHR to the Pmod device.              | 9              | **SCL**. I2C Clock from the MAXFTHR to the Pmod device.              |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| 4              | **SDA**. I2C Data from the MAXFTHR to the Pmod device.               | 10             | **SDA**. I2C Data from the MAXFTHR to the Pmod device.               |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| 5              | **GND**. Ground                                                      | 11             | **GND**. Ground                                                      |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+
| 6              | **VCC**. Connected to 3V3 or VBUS from MAXFTHR (shorted in P4).      | 12             | **VCC**. Connected to 3V3 or VBUS from MAXFTHR (shorted in P4).      |
+----------------+----------------------------------------------------------------------+----------------+----------------------------------------------------------------------+

| 

Schematic, PCB Layout, Bill of Materials
========================================

.. admonition:: Download
   :class: download

   
   :adi:`FTHR-PMD-INTZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/fthr-pmdz-intz-designsupport.zip>`
   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


Additional Information and Useful Links
=======================================

-  :adi:`FTHR-PMD-INTZ Product Page <FTHR-PMD-INTZ>`
-  :adi:`MAX32630FTHR Product Page <MAX32630FTHR>`
-  :adi:`MAX32650FTHR Product Page <MAX32650FTHR>`
-  :adi:`MAX32655FTHR Product Page <MAX32655FTHR>`
-  :adi:`MAX32666FTHR Product Page <MAX32666FTHR>`
-  :adi:`MAX78000FTHR Product Page <MAX78000FTHR>`

Reference Demos & Software
==========================

-  :doc:`EVAL-ADXL355-PMDZ User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/eval-adxl355-pmdz>`
-  :doc:`EVAL-ADT7420-PMDZ Digital Temperature PMOD User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/eval-adt7420-pmdz>`
-  :doc:`MAX31855PMB1 Thermocouple-to-Digital PMOD User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/max31855pmb1>`

|

| // End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/fthr/fthr-pmd-intz_rev_0_angle.png
   :width: 450px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/fthr/fthr-pmd-intz_hardware.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/fthr/power_jumpers_with_label.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/fthr/spi.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/fthr/i2c.png
   :width: 600px
