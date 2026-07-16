.. _ad57xx-ardz quickstart de10nano:

DE10-Nano Quickstart
===============================================================================

This guide provides quick instructions on how to set up the
AD57xx on:

- :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
  on Arduino shield connector

.. image:: ../../images/de10nano.jpg
   :align: center
   :width: 500

.. esd-warning::

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed to boot the system:

- ``system_top.rbf``, HDL bitstream built from
  :external+hdl:ref:`Build an HDL project <build_hdl>`
- ``u-boot-with-spl.sfp``, SPL and U-Boot bootloader
- ``socfpga.dtb``, compiled device tree blob
- ``zImage``, the Linux kernel image

.. note::

   Pre-built files for this reference design are not yet
   available. The bitstream must be built manually following the
   :external+hdl:ref:`ad57xx_ardz` build documentation.
   For general HDL build instructions, see
   :external+hdl:ref:`build_hdl`.

   HDL source: :git-hdl:`/projects/ad57xx_ardz/de10nano`

Copy the built files to the ``BOOT`` partition of the SD card.
The Kuiper boot flow loads the bitstream automatically via the
extlinux boot sequence.

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

- :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
  FPGA board

  - 5V/2A wall power supply with barrel jack (comes with
    DE10-Nano)
  - Mini-USB to USB Type A cable (comes with DE10-Nano)

- :adi:`EVAL-AD5780ARDZ`/ :adi:`EVAL-AD5781ARDZ`/
  :adi:`EVAL-AD5791ARDZ` evaluation board
- Voltage reference daughter board (EV-ADR445-REFZ included
  with evaluation kit)
- Class 10 16GB SD Card
- LAN cable (Ethernet)
- DMM or oscilloscope for measuring DAC output voltage

More details as to why you need these can be found at
:ref:`ad57xx prerequisites`.

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AD57xx/DE10-Nano
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   .. figure:: ../images/ad57xx_setup_hardware_de10nano.jpg
      :align: center
      :width: 500

      AD57xx/DE10-Nano hardware setup.

In the following example, we will prepare the evaluation setup
by connecting the AD57xx board to the DE10-Nano and configuring
it to produce a DAC output.

Follow the steps in this order, to avoid damaging the
components:

#. Get the
   :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
#. Verify the FPGA Configuration Mode Switch (S10) is
   configured properly:

    .. image:: ../../images/de10-nano_fpga_switch_matrix.png
        :align: center
        :width: 800

    The DE10-Nano comes ready to use out of the box, but it is
    important to double check that the FPGA Configuration Mode
    Switch (S10) is set correctly. If more information is
    needed, check out the
    `DE10-Nano Getting Started Guide <https://www.intel.com/content/www/us/en/developer/articles/guide/terasic-de10-nano-get-started-guide.html>`__.

#. Prepare the SD card:

   #. Validate, Format, and Flash the SD Card following the
      :external+kuiper:doc:`Use Kuiper Image <use-kuiper-image>`
      guide.
   #. Copy the built ``system_top.rbf``, ``socfpga.dtb``, and
      ``zImage`` to the ``BOOT`` partition of the SD card.

#. Insert the microSD card into the DE10-Nano card slot

   .. grid::
      :widths: 50% 50%

      .. figure:: ../../images/de10-nano_sdcard_insert.jpg
         :width: 400

         Insert SD card

      .. figure:: ../../images/de10-nano_sdcard_connected.jpg
         :width: 400

         SD card connected

#. Plug-in an Ethernet cable from your router/switch to the
   Ethernet port on the FPGA board

   .. admonition:: Info

      If you don't have a network available and want to stream
      data directly from the Ethernet port of the DE10-Nano to
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
   the DE10-Nano
#. Connect a DMM or oscilloscope to the VOUT or VOUT_BUFF
   connector on the evaluation board to measure the DAC output
   voltage.
#. Connect the UART port of DE10-Nano to a PC via Mini-USB
   cable (DO NOT power on the device yet)

   .. note::

      A driver for the board should automatically be detected
      and installed on your PC. If this does not happen, you
      may need to manually install the driver. Here is a link
      to the
      `UART Serial Driver <https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers>`__.

#. Plug the 5V/2A power supply into the wall outlet and power
   up the setup
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

   .. Add full iio_info output once available.

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
