.. _eval-ad353xr quickstart zed:

ZedBoard Quick start
===============================================================================

.. todo::

   Add a photo of the ZedBoard with the EVAL-AD353XR connected and label
   ports (UART, Ethernet, SD card slot, FMC connector).

.. esd-warning::

This guide provides step-by-step instructions to set up the
:adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` on:

- `ZedBoard
  <https://digilent.com/reference/programmable-logic/zedboard/start>`_
  via SPI + GPIO (FMC LPC)

.. warning::

   The ZedBoard FMC connector is **low pin count**. Ensure VADJ is set to
   **2.5 V** before powering on. Incorrect VADJ may damage the evaluation
   board.

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``system_top.bit``, HDL bitstream built from
  :external+hdl:ref:`Build an HDL project <build_hdl>`
- Kuiper Linux image written to the SD card; follow
  :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
- Copy the bitstream to the SD card boot partition after flashing.

.. note::

   Pre-built files for this reference design are not yet available.
   The bitstream must be built manually. Official release artifacts will
   be provided here once available. For now, refer to:

   :external+hdl:ref:`Build an HDL project <build_hdl>`

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- A UART terminal (e.g. PuTTY, Tera Term, Minicom) at 115200 baud (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `ZedBoard
  <https://digilent.com/reference/programmable-logic/zedboard/start>`_
  and its power supply
- :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` evaluation board
- Jumper wires for SPI and GPIO connections via the FMC LPC connector

  .. todo::

     Confirm exact adapter board / connector used to mate eval board to
     ZedBoard FMC LPC and add it here.

- Micro-USB to USB Type-A cable (UART)
- Ethernet cable
- microSD card (at least 16 GB)

More details can be found at :ref:`eval-ad353xr prerequisites`.

.. _eval-ad353xr quickstart zed hw-setup:

Hardware setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   Provide hardware setup steps with photos once hardware is available.
   Include:

   - How to connect the eval board to the ZedBoard FMC LPC connector
   - SPI and GPIO wiring matching the pin table in the user guide

Setting the boot jumpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set jumpers **MIO[6:2]** to ``01100`` for SD card boot mode.

.. todo::

   Add figure of ZedBoard MIO jumper configuration.

Setting VADJ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VADJ must be set to **2.5 V** before powering the board. Refer to the
ZedBoard hardware guide for the VADJ selection jumper location.

Inserting the SD card and connecting cables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Insert the prepared microSD card into the ZedBoard SD card slot.
#. Connect the Micro-USB cable to the UART port on the ZedBoard.
#. Connect the Ethernet cable to the Ethernet port.
#. Power on the board.
#. Observe serial console output in your terminal at 115200 baud.

Login information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- User: ``root``
- Password: ``analog``

Useful commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To find the IP address of the board:

.. shell::

   $ifconfig

To list detected IIO devices:

.. shell::

   $iio_info | grep iio:device

To power off the system cleanly:

.. shell::

   $poweroff

IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` is a
cross-platform GUI application that connects to the board over the network
and allows reading and writing IIO device attributes.

Connect using the board IP from ``ifconfig``:

.. code-block:: none

   ip:<board-ip>

.. todo::

   Add IIO Oscilloscope screenshots showing AD3530R/AD3531R channel
   attributes and DAC output configuration once hardware captures are
   available.
