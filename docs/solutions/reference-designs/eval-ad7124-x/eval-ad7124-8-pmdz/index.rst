.. _eval-ad7124-8-pmdz_index:

EVAL-AD7124-8-PMDZ User Guide
===============================================================================

.. toctree::
   :hidden:

   hardware

The :adi:`EVAL-AD7124-8-PMDZ` evaluation board is a minimalist 8-channel,
low noise, low power, 24-bit, sigma-delta ADC with PGA and reference, SPI Pmod
board for the :adi:`AD7124-8`. This module is designed as a low-cost alternative
to the fully-featured :adi:`EVAL-AD7124-8` evaluation board and has no extra
signal conditioning for the ADC.

All pins of the :adi:`AD7124-8` are exposed, which makes the
:adi:`EVAL-AD7124-8-PMDZ` very flexible and easy to use.

.. figure:: ../images/eval-ad7124-pmdz-top.webp
   :alt: Photo of the EVAL-AD7124-8-PMDZ evaluation board (top view)
   :align: center
   :width: 600

   EVAL-AD7124-8PMDZ Top View

.. figure:: ../images/eval-ad7124-pmdz-bottom.webp
   :alt: Photo of the EVAL-AD7124-8-PMDZ evaluation board (bottom view)
   :align: center
   :width: 600

   EVAL-AD7124-8PMDZ Bottom View

Features
-------------------------------------------------------------------------------

- Minimalist Pmod board for the :adi:`AD7124-8`
- SPI Pmod interface for easy connectivity
- All AD7124-8 pins exposed via through-hole connectors
- Configurable solder jumpers for flexible operation
- Compatible with the :adi:`EVAL-ADICUP3029` via Pmod connector

Related Documents
-------------------------------------------------------------------------------

- :adi:`AD7124-8 Data Sheet <AD7124-8>`
- :adi:`EVAL-AD7124-8-PMDZ Product Page <EVAL-AD7124-8-PMDZ>`

Required Software
-------------------------------------------------------------------------------

- CrossCore Embedded Studio (2.9.1 or higher)
- ADuCM302x DFP (3.2.0 or higher)
- ADICUP3029 BSP (1.1.0 or higher)
- Serial terminal program

Quick Start Guide
-------------------------------------------------------------------------------

Equipment required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7124-8-PMDZ` evaluation board
- :adi:`EVAL-ADICUP3029` controller board
- Micro USB to USB cable
- PC or laptop with a USB port

Getting started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the :adi:`EVAL-AD7124-8-PMDZ` to the Pmod connector on the
   :adi:`EVAL-ADICUP3029`.

   .. figure:: ../images/ad7124_pmod_unplug.jpg
      :alt: EVAL-AD7124-8-PMDZ and EVAL-ADICUP3029 before connection
      :align: center
      :width: 500

      EVAL-AD7124-8-PMDZ and EVAL-ADICUP3029 before connection

#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer.

   .. figure:: ../images/ad7124_pmod_plug.jpg
      :alt: EVAL-AD7124-8-PMDZ connected to EVAL-ADICUP3029
      :align: center
      :width: 500

      EVAL-AD7124-8-PMDZ connected to EVAL-ADICUP3029

#. Program the EVAL-ADICUP3029 using one of the methods described in the
   :ref:`ADICUP3029 quickstart guide <eval-ad7124-x quickstart adicup3029>`.

#. Open a serial terminal program (e.g., PuTTY) configured for 115200 baud,
   8N1.

#. Reset the controller board. The AD7124-8 demo menu should appear in the
   terminal.

Software Resources
-------------------------------------------------------------------------------

- :git-no-OS:`AD7124 no-OS driver <drivers/adc/ad7124>`
- :git-no-OS:`AD7124-8 PMDZ no-OS project <projects/ad7124-8pmdz>`
- :external+linux:ref:`ad7124` (Linux driver)
- :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ <master:projects/ADuCM3029_demo_ad7124_8PMDZ>`

Design and Integration Files
-------------------------------------------------------------------------------

Schematics, layout files, and bill of materials are available on the
:adi:`EVAL-AD7124-8-PMDZ Design Support <eval-ad7124-8-pmdz-designsupport>`.
