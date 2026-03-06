ADXL345 - No-OS Driver for Renesas Microcontroller Platforms
============================================================

.. include:: ../adxl345.rst

**HW Platform(s):**

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`__
-  `Renesas Demo Kit for RX62N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`__

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL345 RL78G13 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g13.zip>`__
   -  `ADXL345 RX62N Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rx62n.zip>`__
   -  \**ADXL345 Driver: \*\* :git-no-OS:`drivers/accel/adxl345`
   -  \**PmodACL Demo for RL78G14: \*\* :git-no-OS:`Renesas/RL78G14/PmodACL`
   -  \**RL78G14 Common Drivers: \*\* :git-no-OS:`Renesas/RL78G14/Common`
   


Renesas RL78G13 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL345 demonstration project on a Renesas RL78G13 platform.

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`__
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`__ (optional, because an ADXL345 part is installed on Renesas Demonstration Kit (RDK) for RL78G13)

Required Software
~~~~~~~~~~~~~~~~~

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`__

Hardware Setup
~~~~~~~~~~~~~~

There are two options:

-  The ADXL345 part installed on the Renesas Demonstration Kit (RDK) for RL78G13 can be used. In this case, the I2C protocol has to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g13.jpg
   :align: center

-  A PmodACL can be connected to the PMOD1 connector. In this case, the SPI protocol has to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl_rl78g13.jpg
   :align: center

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, the output data of each axis is read and displayed on the Renesas Demonstration Kit for RL78G13 board’s LCD. Were also activated “Single Tap”, “Double Tap” and “Free-Fall” interrupts. When one of them occurs, on the LCD screen appears a corresponding message.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g13_screen.jpg
   :align: center

Software Project Setup
~~~~~~~~~~~~~~~~~~~~~~


.. note::

   See `rl78g13_software_tutorial_without_applilet3 <https://wiki.analog.com/rl78g13_software_tutorial_without_applilet3>`__


Renesas RL78G14 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL345 demonstration project on a Renesas RL78G14 platform using the PmodACL.

.. _required-hardware-1:

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Renesas Demo Kit for RL78G14 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g14-yrdkrl78g14-demonstration-kit-rl78g14>`__
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`__ (optional, because an ADXL345 part is installed on Renesas Demonstration Kit (RDK) for RL78G14)

.. _required-software-1:

Required Software
~~~~~~~~~~~~~~~~~

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`__
-  The ADXL345 demonstration project for the Renesas RL78G14 platform.

.. note::

   The ADXL345 demonstration project for the Renesas RL78G14 platform consists of three parts: the **ADXL345 Driver**, the **PmodACL Demo for RL78G14** and the **RL78G14 Common Drivers**.

   
   All three parts have to be downloaded.


.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

There are two options:

-  The ADXL345 part installed on the Renesas Demonstration Kit (RDK) for RL78G14 can be used. In this case, the I2C protocol has to be chosen with 'ADXL345_Init()' function.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g14.jpg
   :align: center

-  A PmodACL can be connected to the PMOD1 connector. In this case, the SPI protocol has to be chosen with 'ADXL345_Init()' function.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl_rl78g14.jpg
   :align: center

.. _reference-project-overview-1:

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

The reference project:

-  reads and displays the data for each axis on LCD;
-  it displays also on LCD if the interrupts “Single Tap”, “Double Tap” or “Free-Fall” were activated.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rl78g14_screen.jpg
   :align: center

Software Project Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~


.. note::

   See `rl78g14_software_tutorial <https://wiki.analog.com/rl78g14_software_tutorial>`__


Renesas RX62N Quick Start Guide
===============================

This section contains a description of the steps required to run the ADXL345 demonstration project on a Renesas RX62N platform.

.. _required-hardware-2:

Required Hardware
~~~~~~~~~~~~~~~~~

-  `Renesas Demo Kit for RX62N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`__
-  `PmodACL <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL>`__ (optional, because an ADXL345 part is installed on Renesas Demonstration Kit (RDK) for RX62N)

.. _required-software-2:

Required Software
~~~~~~~~~~~~~~~~~

-  `High-performance Embedded Workshop for RX62N family <https://www.renesas.com/us/en/software-tool/high-performance-embedded-workshop>`__
-  `Renesas Peripheral Driver Library for RX62N family <https://www.renesas.com/us/en/software-tool/renesas-peripheral-driver-library>`__

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

There are two options:

-  The ADXL345 part installed on the Renesas Demonstration Kit (RDK) for RX62N can be used. In this case, the I2C protocol has to be chosen.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rx62n.jpg
   :align: center

-  A PmodACL can be connected to the Renesas Demonstration Kit (RDK) for RX62N (in this case, the SPI protocol has to be chosen):

::

     PmodACL Pin 1 (CS)   → YRDKRX62N J8 connector Pin 15
     PmodACL Pin 2 (MOSI) → YRDKRX62N J8 connector Pin 19
     PmodACL Pin 3 (MISO) → YRDKRX62N J8 connector Pin 22
     PmodACL Pin 4 (CLK)  → YRDKRX62N J8 connector Pin 20
     PmodACL Pin 5 (GND)  → YRDKRX62N J8 connector Pin 4
     PmodACL Pin 6 (VCC)  → YRDKRX62N J8 connector Pin 3

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl_rx62n.jpg
   :align: center

.. _reference-project-overview-2:

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, the output data of each axis is read and displayed on the Renesas Demonstration Kit for RX62N board’s LCD. Were also activated “Single Tap”, “Double Tap” and “Free-Fall” interrupts. When one of them occurs, on the LCD screen appears a corresponding message.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl345_rx62n_screen.jpg
   :align: center

.. _software-project-setup-1:

Software Project Setup
~~~~~~~~~~~~~~~~~~~~~~


.. note::

   See `rx62n_software_design <https://wiki.analog.com/rx62n_software_design>`__


More information
================

.. include:: ../more-information.rst
