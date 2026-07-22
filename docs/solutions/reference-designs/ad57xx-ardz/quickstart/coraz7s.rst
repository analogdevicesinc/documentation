.. _ad57xx-ardz quickstart coraz7s:

CoraZ7-07S Quickstart
===============================================================================

This guide provides quick instructions on how to set up the
AD57xx on:

- `Cora Z7S
  <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
  on Arduino shield connector

.. image:: ../../images/coraz7s.webp
   :align: center
   :width: 500

.. esd-warning::

Using linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``BOOT.BIN``, built from the HDL project;
  follow :external+hdl:ref:`build_hdl`
- ``devicetree.dtb``, compiled from the device tree source
- ``uImage``, the linux kernel image;
  follow :ref:`linux-kernel zynq`

.. note::

   Pre-built files for this reference design are not yet
   available. The files must be built manually using the links
   above.
   For the HDL project, see :external+hdl:ref:`ad57xx_ardz`
   build documentation.
   For general HDL build instructions, see
   :external+hdl:ref:`build_hdl`.

   HDL source: :git-hdl:`/projects/ad57xx_ardz/coraz7s`

Copy ``BOOT.BIN``, ``devicetree.dtb``, and ``uImage`` to the
``BOOT`` partition of the SD card before inserting it.

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- SD Card 16GB imaged with
  :external+kuiper:doc:`Kuiper <index>` (provides the root
  filesystem; the HDL bitstream must be built separately as
  described above)
- A UART terminal (Putty/Tera Term/Minicom, etc.) with baud
  rate 115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Cora Z7S
  <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
  FPGA board
- :adi:`EVAL-AD5780ARDZ`/ :adi:`EVAL-AD5781ARDZ`/
  :adi:`EVAL-AD5791ARDZ` evaluation board
- Voltage reference daughter board (EV-ADR445-REFZ included
  with evaluation kit)
- Class 10 16GB SD Card
- Micro-USB cable (UART / Power)
- LAN cable (Ethernet)
- DMM or oscilloscope for measuring DAC output voltage

More details as to why you need these can be found at
:ref:`ad57xx prerequisites`.

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AD57xx/CoraZ7-07S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. figure:: ../images/ad57xx_setup_hardware_coraz7s.jpeg
   :align: center
   :width: 800

   AD57xx/CoraZ7-07S hardware setup for linux.

In the following example, we will prepare the evaluation setup
by connecting the AD57xx board to the CoraZ7-07S and configuring
it to produce a DAC output.

Follow the steps in this order, to avoid damaging the
components:

#. Get the `Cora Z7S
   <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
#. Configure CoraZ7-07S jumpers:

    .. figure:: ../../images/cora_hw_config.jpg
        :align: center
        :width: 500

        CoraZ7-07S jumper configuration.

    .. list-table::
       :header-rows: 1
       :widths: 20 60 20

       * - Jumper Location
         - Description
         - Shunt Placement
       * - JP2
         - Selects how the CoraZ7-07s board boots. We want to
           boot from the microSD card.
         - Across Pins 1 & 2
       * - JP3
         - Selects how the CoraZ7-07s board is powered. We are
           powering from the USB port.
         - Across Pins 3 & 2 (labeled USB)

#. Prepare the SD card:

   #. Validate, Format, and Flash the SD Card following the
      :external+kuiper:doc:`Use Kuiper Image <use-kuiper-image>`
      guide.
   #. Copy the built ``BOOT.BIN``, ``devicetree.dtb``, and
      ``uImage`` to the ``BOOT`` partition of the SD card.

#. Insert the microSD card into the CoraZ7-07S card slot

   .. grid::
      :widths: 50% 50%

      .. figure:: ../../images/cora_sdcard_insert.jpg
         :width: 400

         Insert SD card

      .. figure:: ../../images/cora_sdcard_connected.jpg
         :width: 400

         SD card connected

#. Plug-in an Ethernet cable from your router/switch to the
   Ethernet port on the FPGA board

   .. admonition:: Info

      If you don't have a network available and want to stream
      data directly from the Ethernet port of the CoraZ7-07s to
      the Ethernet port of your PC, that is still possible, but
      requires some extra configuration. Please see the
      :dokuwiki:`[Wiki] Network Configuration
      <resources/tools-software/linux-software/network-config>`
      page for complete details.

#. Ensure the voltage reference daughter board (EV-ADR445-REFZ
   or equivalent) is connected to the J1, J4, and J9 connectors
   on the evaluation board.
#. Using the Arduino pins, plug the :adi:`EVAL-AD5780ARDZ`/
   :adi:`EVAL-AD5781ARDZ`/ :adi:`EVAL-AD5791ARDZ` on top of
   the CoraZ7-07S
#. Connect a DMM or oscilloscope to the VOUT or VOUT_BUFF
   connector on the evaluation board to measure the DAC output
   voltage.
#. Connect the UART port of CoraZ7-07S to a PC via Micro-USB
   cable (DO NOT power on the device yet)
#. Power up the setup by plugging the Micro-USB cable into your
   PC's USB port
#. Observe Kernel and serial console output messages on your
   terminal

Boot messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is what is printed in the serial console, after
you have connected to the proper ttyUSB or COM port:

.. collapsible:: Complete boot log

   .. Add boot log output once available.

Useful commands for the serial terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below commands are to be run in the serial terminal
connected to the FPGA.

**Login Information**

user: analog

password: analog

To find out the IP of the FPGA board, run the following command
and take the IP specified at "eth0 inet":

.. shell::

   $ifconfig

To see the IIO devices detected, run:

.. shell::

    $iio_info | grep iio:device

.. collapsible:: Complete iio_info output

   Add full iio_info output once available.

To power off the system, run the following command, and wait for
the final message to be printed, then power off the FPGA board
from the switch as well.

.. shell::

   $poweroff

To reboot the system, run:

.. shell::

   $reboot

.. important::

   Even though this is Linux, this is a persistent file system.
   Care should be taken not to corrupt the file system -- please
   shut down things, don't just turn off the power switch.
   Depending on your monitor, the standard power off could be
   hiding. You can do this from the terminal as well with
   :code:`sudo shutdown -h now` or the above-mentioned command
   for powering off.

Scopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   Make sure to download/update to the latest version of
   :external+scopy:doc:`Scopy <index>`.

:external+scopy:doc:`Scopy <index>` can be used to control the
DAC output voltage through the IIO plugin. Connect to the board
via its IP address, then use the DAC channel controls to set the
desired output code or voltage.

.. Add Scopy DAC control screenshot.

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   Make sure to download/update to the latest version of
   :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`.

#. Once done with the installation or an update of the latest
   IIO Oscilloscope, open the application. The user needs to
   supply a URI which will be used in the context creation of
   the IIO Oscilloscope.
#. Press ``Refresh`` to display available IIO Devices and press
   ``Connect``.

   .. Add IIO Oscilloscope connect screenshot.

#. After the board is connected and a channel is enabled, hit
   the play button. Then the data capture window can be seen
   like in the shown picture.

   .. Add IIO Oscilloscope data capture screenshot.

Using no-OS as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed for the system to boot:

- HDL boot file: ``system_top.xsa``
- no-OS project:
  :git-no-os:`No-OS AD5791 driver <drivers/dac/ad5791>`

Instructions on how to build the boot files from source can be
found here:

- :git-no-os:`No-OS AD5791 driver source <drivers/dac/ad5791>`.
  More no-OS build details at
  :external+no-OS:doc:`build_guide`.
- :external+hdl:ref:`ad57xx_ardz`. More HDL build details at
  :external+hdl:ref:`build_hdl`.

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- AMD Xilinx Vivado and Vitis (downloading Vitis from `here
  <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>`_
  will include Vivado as well)
- An UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate
  115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Cora Z7S
  <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
  FPGA board
- :adi:`EVAL-AD5780ARDZ`/ :adi:`EVAL-AD5781ARDZ`/
  :adi:`EVAL-AD5791ARDZ` evaluation board
- Voltage reference daughter board (EV-ADR445-REFZ included
  with evaluation kit)
- Micro-USB cable (UART / Power / JTAG)
- DMM or oscilloscope for measuring DAC output voltage

More details as to why you need these can be found at
:ref:`ad57xx prerequisites`.

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AD57xx/CoraZ7-07S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. figure:: ../images/ad57xx_setup_hardware_coraz7s.jpeg
   :align: center
   :width: 500

   AD57xx/CoraZ7-07S hardware setup for no-OS.

In the following example, we will prepare the evaluation setup
by connecting the :adi:`EVAL-AD5780ARDZ`/
:adi:`EVAL-AD5781ARDZ`/ :adi:`EVAL-AD5791ARDZ` board to the
CoraZ7-07S and configuring the board for JTAG boot.

Follow the steps in this order, to avoid damaging the
components:

#. Get the `Cora Z7S
   <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
#. Configure CoraZ7-07S for JTAG boot. Remove jumper JP2 to set
   JTAG boot mode. JP3 should remain set to USB power
   (Pins 3 & 2).

   .. figure:: ../../images/cora_hw_config.jpg
      :align: center
      :width: 500

      CoraZ7-07S jumper configuration for JTAG boot mode.

   .. important::

       You can keep the JP2 jumper in place, but it is important
       to make sure no SD card is inserted in the CoraZ7-07S
       when booting in JTAG mode.

#. Ensure the voltage reference daughter board is connected to
   the evaluation board.
#. Using the Arduino pins, plug the :adi:`EVAL-AD5780ARDZ`/
   :adi:`EVAL-AD5781ARDZ`/ :adi:`EVAL-AD5791ARDZ` on top of
   the CoraZ7-07S.
#. Connect a DMM or oscilloscope to the VOUT or VOUT_BUFF
   connector to measure the DAC output.
#. Connect the UART port of CoraZ7-07S to a PC via Micro-USB
   cable.
#. Power up the setup by plugging the Micro-USB cable into your
   PC's USB port.
#. Observe serial console output messages on your terminal.

Console output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is what is printed in the serial console, after
you have connected to the proper ttyUSB or COM port:

.. collapsible:: Complete boot log

   .. To be added once available.

.. note::

   The DAC configuration output will print in the console
   showing the register writes and voltage output status. The
   program will complete once the DAC is configured with the
   target output value.
