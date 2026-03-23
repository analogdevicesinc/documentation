.. _eval-ad353xr quickstart de10nano:

DE10-Nano Quick start
===============================================================================

.. todo::

   Add a photo of the DE10-Nano with the EVAL-AD353XR connected and label
   ports (UART, Ethernet, SD card slot).

.. esd-warning::

This guide provides step-by-step instructions to set up the
:adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` on:

- `DE10-Nano FPGA Board
  <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_
  via SPI + GPIO

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``system_top.rbf``, HDL bitstream built from
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

- `DE10-Nano FPGA Board
  <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_
  and its power supply
- :adi:`EVAL-AD3530R` or :adi:`EVAL-AD3531R` evaluation board
- Jumper wires for SPI and GPIO connections

  .. todo::

     Confirm exact adapter board / connector used to mate eval board to
     DE10-Nano and add it here.

- Micro-USB to USB Type-A cable (UART)
- Ethernet cable
- microSD card (at least 16 GB)

More details can be found at :ref:`eval-ad353xr prerequisites`.

.. _eval-ad353xr quickstart de10nano hw-setup:

Hardware setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   Provide hardware setup steps with photos once hardware is available.
   Include:

   - How to connect the eval board to the DE10-Nano
   - SPI and GPIO wiring matching the pin table in the user guide

Setting the FPGA configuration switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adjust the FPGA configuration mode switch to the SD card boot position.

.. todo::

   Add figure of DE10-Nano switch configuration.

Inserting the SD card and connecting cables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Insert the prepared microSD card into the DE10-Nano SD card slot.
#. Connect the Micro-USB cable to the UART port on the DE10-Nano.
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
