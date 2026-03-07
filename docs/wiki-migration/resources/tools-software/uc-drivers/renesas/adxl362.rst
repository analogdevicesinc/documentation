ADXL362 - No-OS Driver for Renesas Microcontroller Platforms
============================================================

.. include:: ../adxl362.rst

**HW Platform(s):**

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `Renesas Demo Kit for RX63N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx63n-yrdkrx63n-demonstration-kit-rx63n>`_

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  `ADXL362 Generic Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adxl362_generic.zip>`_
   -  `ADXL362 RL78G13 Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl362_rl78g13.zip>`_
   -  `ADXL362 RX63N Driver <https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/adxl362_rx63n.zip>`_
   -  \**ADXL362 Driver: \*\* :git-no-OS:`drivers/accel/adxl362`
   -  \**PmodACL2 Demo for RL78G14: \*\* :git-no-OS:`Renesas/RL78G14/PmodACL2`
   -  \**RL78G14 Common Drivers: \*\* :git-no-OS:`Renesas/RL78G14/Common`
   


Renesas RL78G13 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Renesas RL78G13 platform using the PmodACL2.

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G13 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_

Hardware Setup
--------------

A PmodACL2 has to be connected to the PMOD1 connector.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g13.jpg
   :align: center

Reference Project Overview
--------------------------

The reference project continuously displays on the LCD the accelerations on x-axis, y-axis and x-axis and simultaneously detects any activity or inactivity detected by the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g13_screen.jpg
   :align: center

Software Project Tutorial
-------------------------


.. note::

   See `rl78g13_software_tutorial_without_applilet3 <https://wiki.analog.com/rl78g13_software_tutorial_without_applilet3>`_


Renesas RL78G14 Quick Start Guide
=================================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Renesas RL78G14 platform using the PmodACL2.

.. _required-hardware-1:

Required Hardware
-----------------

-  `Renesas Demo Kit for RL78G14 (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g14-yrdkrl78g14-demonstration-kit-rl78g14>`_
-  `PmodACL2 <http://www.digilentinc.com/Products/Detail.cfm?Prod=PMOD-ACL2>`_

.. _required-software-1:

Required Software
-----------------

-  `IAR Embedded Workbench for Renesas RL78 Kickstart <http://www.iar.com/en/Products/IAR-Embedded-Workbench/Renesas-RL78/>`_
-  The ADXL362 demonstration project for the Renesas RL78G14 platform.

.. note::

   The ADXL362 demonstration project for the Renesas RL78G14 platform consists of three parts: the **ADXL362 Driver**, the **PmodACL2 Demo for RL78G14** and the **RL78G14 Common Drivers**.

   
   All three parts have to be downloaded.


.. _hardware-setup-1:

Hardware Setup
--------------

A PmodACL2 has to be connected to the PMOD1 connector (see image below).

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g14.jpg
   :align: center

.. _reference-project-overview-1:

Reference Project Overview
--------------------------

The reference project:

-  displays the acceleration values on x, y and z axis;
-  displays temperature;
-  detects any activity or inactivity supported by the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rl78g14_screen.jpg
   :align: center

.. _software-project-tutorial-1:

Software Project Tutorial
-------------------------


.. note::

   See `rl78g14_software_tutorial <https://wiki.analog.com/rl78g14_software_tutorial>`_


Renesas RX63N Quick Start Guide
===============================

This section contains a description of the steps required to run the ADXL362 demonstration project on a Renesas RX63N platform.

.. _required-hardware-2:

Required Hardware
-----------------

-  `Renesas Demo Kit for RX63N (Renesas) <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/yrdkrx63n-yrdkrx63n-demonstration-kit-rx63n>`_
-  PmodACL2

.. _required-software-2:

Required Software
-----------------

-  `High-performance Embedded Workshop for RX63N family <https://www.renesas.com/us/en/software-tool/high-performance-embedded-workshop>`_
-  `Renesas Peripheral Driver Library for RX63N family <https://www.renesas.com/us/en/software-tool/renesas-peripheral-driver-library>`_

.. _hardware-setup-2:

Hardware Setup
--------------

A PmodACL2 has to be connected to the PMOD1 connector.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rx63n.jpg
   :align: center

.. _reference-project-overview-2:

Reference Project Overview
--------------------------

The reference project continuously displays on the LCD the accelerations on x-axis, y-axis and x-axis and simultaneously detects any activity or inactivity detected by the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/pmod_acl2_rx63n_screen.jpg
   :align: center

Software Project Setup
----------------------


.. note::

   See `rx63n_software_design <https://wiki.analog.com/rx63n_software_design>`_


More information
================

.. include:: ../more-information.rst
