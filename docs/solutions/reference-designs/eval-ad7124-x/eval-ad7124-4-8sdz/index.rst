.. _eval-ad7124-4-8sdz_index:

EVAL-AD7124-4SDZ / EVAL-AD7124-8SDZ User Guide
===============================================================================

.. toctree::
   :hidden:

   hardware

The :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` and
:adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` are full-featured
evaluation boards for the :adi:`AD7124-4` and :adi:`AD7124-8`, low power, low
noise, completely integrated analog front ends for high precision measurement
applications.

- The :adi:`AD7124-4` provides 4 differential or 7
  single-ended/pseudo-differential inputs.
- The :adi:`AD7124-8` provides 8 differential or 15
  single-ended/pseudo-differential inputs.

The evaluation boards connect to the :adi:`SDP-B` controller
board via the 120-pin SDP connector, and can also be used with the STM32
Nucleo-L476RG via an :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`.

Features
-------------------------------------------------------------------------------

- Full-featured evaluation board for the :adi:`AD7124-4` / :adi:`AD7124-8`
- On-board 2.5 V ADR4525 precision voltage reference
- PC control with :adi:`SDP-B`
- PC software for control and data analysis (time domain)
- Standalone SPI breakout capability

Related Documents
-------------------------------------------------------------------------------

- :adi:`AD7124-4 Data Sheet <AD7124-4>`
- :adi:`AD7124-8 Data Sheet <AD7124-8>`
- :adi:`EVAL-AD7124-4SDZ Product Page <EVAL-AD7124-8>`
- :adi:`EVAL-AD7124-8SDZ Product Page <EVAL-AD7124-8>`

Required Software
-------------------------------------------------------------------------------

**For use with the SDP-B:**

- - AD7124 Eval+ Software (included on CD or :download:`downloadable <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`)

**For use with the Nucleo-L476RG:**

- `STM32CubeIDE <https://www.st.com/en/development-tools/stm32cubeide.html>`_
- `ad7124_stm32_example.zip <https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_example/ad7124_stm32_example.zip>`_

Quick Start Guide
-------------------------------------------------------------------------------

Equipment required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` or
  :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` evaluation board
- Controller board:

  - **Option A:** :adi:`SDP-B` and a USB cable
  - **Option B:** `Nucleo-L476RG <https://www.st.com/en/evaluation-tools/nucleo-l476rg.html>`_
    with :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>` and a USB cable

- 7--9 V DC power supply (wall wart or bench top)
- DC signal source
- PC running Windows with a USB 2.0 port

Getting started with SDP-B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   The evaluation software and drivers must be installed **before** connecting
   the evaluation board and controller board to the USB port of the PC, to
   ensure the system is correctly recognized.

#. With the :adi:`SDP-B` disconnected from the PC, install the AD7124 Eval+
   Software. Restart the PC after installation.
#. Connect the :adi:`SDP-B` to the evaluation board via the 120-pin SDP
   connector (J1).
#. Screw the two boards together using the plastic screw and washer set.
#. Apply 7--9 V DC to connector J3 (bench top) or J5 (wall wart/DC plug).
#. Connect the :adi:`SDP-B` to the PC using a USB cable.
#. From the Start menu, navigate to **Programs > Analog Devices > AD7124
   Eval+** and select **EVAL-AD7124-4SDZ** or **EVAL-AD7124-8SDZ**.

See the :ref:`SDP-B quickstart guide <eval-ad7124-x quickstart sdp_b>` for
detailed software installation and operation instructions.

Getting started with Nucleo-L476RG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install STM32CubeIDE and the AD7124 example code.
#. Connect the evaluation board to the Nucleo-L476RG via the
   :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`. See the
   :ref:`Nucleo quickstart guide <eval-ad7124-x quickstart nucleo>` for
   wiring details.
#. Connect a 7--9 V DC supply to the evaluation board.
#. Connect the Nucleo-L476RG to your PC via USB.
#. Build and program the firmware using STM32CubeIDE.
#. Open a serial terminal and reset the board.

For detailed step-by-step instructions, see the
:ref:`Nucleo-L476RG quickstart guide <eval-ad7124-x quickstart nucleo>`.

Software Resources
-------------------------------------------------------------------------------

- :git-no-OS:`AD7124 no-OS driver <drivers/adc/ad7124>`
- :external+linux:ref:`ad7124` (Linux driver)

Design and Integration Files
-------------------------------------------------------------------------------

Schematics, layout files, and bill of materials are available on the
:adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` and
:adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` product pages.
