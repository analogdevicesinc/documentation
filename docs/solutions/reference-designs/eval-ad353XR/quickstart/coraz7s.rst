.. _eval-ad353xr quickstart coraz7s:

CoraZ7s Quick start
===============================================================================

.. todo::

   Add a photo of the CoraZ7s with the EVAL-AD353XR connected and label
   ports (UART, Ethernet, SD card slot).

.. esd-warning::

This guide provides step-by-step instructions to set up the
:adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` on:

- `CoraZ7-07s <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development/>`_

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

- :digikey:`CoraZ7-07S <DIGILENT-410-346>` FPGA board and its power supply
- :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` evaluation board
- Jumper wires for SPI and GPIO connections

  .. todo::

     Confirm exact adapter board / connector used to mate eval board to
     CoraZ7s and add it here.

- Micro-USB to USB Type-A cable (UART)
- Ethernet cable
- microSD card (at least 16 GB)

More details can be found at :ref:`eval-ad353xr prerequisites`.

.. _eval-ad353xr quickstart coraz7s hw-setup:

Hardware setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   Provide hardware setup steps with photos once hardware is available.
   Include:

   - How to connect the eval board to the CoraZ7s
   - JP2 jumper placement (short both pins)
   - JP3 selection depending on power source (USB or external)
   - SPI and GPIO wiring matching the pin table in the user guide

Setting the boot jumpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the CoraZ7s, place a jumper on **JP2**, shorting both pins together.
Select **JP3** based on your power supply source (USB or external supply).

.. todo::

   Add figure of JP2/JP3 jumper configuration.

Inserting the SD card and connecting cables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Insert the prepared microSD card into the CoraZ7s SD card slot.
#. Connect the Micro-USB cable to the UART port on the CoraZ7s.
#. Connect the Ethernet cable to the Ethernet port.
#. Power on the board.
#. Observe serial console output in your terminal at 115200 baud.

Programming the bitstream
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   Confirm the exact bitstream copy/boot flow for CoraZ7s (SD card vs JTAG)
   and add the steps here once verified with hardware.

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
