ADXRS453 - No-OS Driver for Renesas Microcontroller Platforms
=============================================================

.. include:: ../adxrs453.rst

**HW Platform(s):**

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `Renesas Demo Kit for RX62N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXRS453 Generic Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adxrs453_generic.zip>`_
   -  `ADXRS453 RL78G13 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxrs453_rl78g13.zip>`_
   -  `ADXRS453 RX62N Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxrs453_rx62n.zip>`_
   -  \**ADXRS453 Driver: \*\* :git-no-OS:`drivers/gyro/adxrs453`
   -  \**PmodGYRO2 Demo for RL78G14: \*\* :git-no-OS:`Renesas/RL78G14/PmodGYRO2`
   -  \**RL78G14 Common Drivers: \*\* :git-no-OS:`Renesas/RL78G14/Common`
   


Renesas RL78G13 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXRS453 demonstration project on a Renesas RL78G13 platform.

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`_

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_

Hardware Setup
--------------

A PmodGYRO2 has to be connected to the PMOD1 connector, pins 1 to 6 (see image below).

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_gyro2_rl78g13.jpg
   :align: center

Reference Project Overview
--------------------------

The reference project:

-  reads the 10-Bit Temperature Data and the 16-Bit Rate Data;
-  displays the values on the LCD as degrees Celsius and degrees/sec respectively.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_gyro2_rl78g13_screen.jpg
   :align: center

Software Project Tutorial
-------------------------


.. note::

   See `rl78g13_software_tutorial_without_applilet3 <https://wiki.analog.com/rl78g13_software_tutorial_without_applilet3>`_


Renesas RL78G14 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXRS453 demonstration project on a Renesas RL78G14 platform using the PmodGYRO2.

.. _required-hardware-1:

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G14 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g14-yrdkrl78g14-demonstration-kit-rl78g14>`_
-  `PmodGYRO2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-GYRO2>`_

.. _required-software-1:

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_
-  The ADXRS453 demonstration project for the Renesas RL78G14 platform.

.. note::

   The ADXRS453 demonstration project for the Renesas RL78G14 platform consists of three parts: the **ADXRS453 Driver**, the **PmodGYRO2 Demo for RL78G14** and the **RL78G14 Common Drivers**.

   
   All three parts have to be downloaded.


.. _hardware-setup-1:

Hardware Setup
--------------

A PmodGYRO2 has to be connected to the PMOD1 connector, pins 1 to 6 (see image below).

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_gyro2_rl78g14.jpg
   :align: center

.. _reference-project-overview-1:

Reference Project Overview
--------------------------

The reference project:

-  reads the 10-Bit Temperature Data and the 16-Bit Rate Data;
-  displays the values on the LCD as degrees Celsius and degrees/sec respectively.

.. important::

   
   -  If you rotate the Pmod slowly, you will see a smaller value (e.g. 30 Degrees/Second), while rotating the Pmod at a higher speed will result in a higher value (e.g. 300 degrees/second). Afterwards the device will auto calibrate according to its new position, thus displaying a value close to 0 degrees/second.
   


.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_gyro2_rl78g14_screen.jpg
   :align: center

.. _software-project-tutorial-1:

Software Project Tutorial
-------------------------


.. note::

   See `rl78g14_software_tutorial <https://wiki.analog.com/rl78g14_software_tutorial>`_


Renesas RX62N Quick Start Guide
===============================

This section contains a description of the steps required to run the ADXRS453 demonstration project on a Renesas RX62N platform.

.. _required-hardware-2:

Required Hardware
-----------------

-  `Renesas Demo Kit for RX62N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx62n-yrdkrx62n-demonstration-kit-rx62n>`_
-  PmodGYRO2

.. _required-software-2:

Required Software
-----------------

-  `High-performance Embedded Workshop for RX62N family <https://www.renesas.com/us/en/software-tool/high-performance-embedded-workshop>`_
-  `Renesas Peripheral Driver Library for RX62N family <https://www.renesas.com/us/en/software-tool/renesas-peripheral-driver-library>`_

.. _hardware-setup-2:

Hardware Setup
--------------

A PmodGYRO2 has to be interfaced with the Renesas Demonstration Kit (RDK) for RX62N:

::

     PmodGYRO2 Pin 1 (CS)   → YRDKRX62N J8 connector Pin 15
     PmodGYRO2 Pin 2 (MOSI) → YRDKRX62N J8 connector Pin 19
     PmodGYRO2 Pin 3 (MISO) → YRDKRX62N J8 connector Pin 22
     PmodGYRO2 Pin 4 (CLK)  → YRDKRX62N J8 connector Pin 20
     PmodGYRO2 Pin 5 (GND)  → YRDKRX62N J8 connector Pin 4
     PmodGYRO2 Pin 6 (VCC)  → YRDKRX62N J8 connector Pin 3

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_gyro2_rx62n.jpg
   :align: center

.. _reference-project-overview-2:

Reference Project Overview
--------------------------

The reference project reads the 10-Bit Temperature Data and the 16-Bit Rate Data. The values are displayed on the LCD as degrees Celsius and degrees/sec respectively.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_gyro2_rx62n_screen.jpg
   :align: center

Software Project Setup
----------------------


.. note::

   See `rx62n_software_design <https://wiki.analog.com/rx62n_software_design>`_


More information
================

.. include:: ../more-information.rst
