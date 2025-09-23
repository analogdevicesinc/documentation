.. _eval-cn0577-fmcz:

EVAL-CN0577-FMCZ
================

Analog Front End and Digital Interface for Serial LVDS SAR ADCs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Overview
--------

.. figure:: cn0577_1.jpg
   :align: right
   :width: 600px

   EVAL-CN0577-FMCZ Board

Instrumentation applications such as flow cytometry, optical pulse
measurement, fast control loops, fast digital distortion correction, and image
sensor digitization present unique data acquisition challenges. These
applications often require a combination of high sample rate, high linearity,
low drift, low noise, and low latency.

The :adi:`EVAL-CN0577-FMCZ <CN0577>` is an 18-bit, 15 MSPS, 2 ppm linear data
acquisition system with an easy to drive input impedance of 1.1 kΩ. The analog
input range is 8.096 V peak-to-peak and can be driven in either single-ended
or differential mode, providing flexibility for many different applications.

The circuit is in field programmable gate array (FPGA) mezzanine card (FMC)
form factor, powered with 12 V either from the FMC connector or an external
supply. The digital interface uses serial low voltage differential signaling
(LVDS), minimizing the input/output requirements and enabling easy integration
with other FPGA designs

A separate data clock eases the timing requirements of the host FPGA. An
on-board 120 MHz clock is forwarded to the FPGA and a CONVERT retiming
flip-flop reduces jitter from the convert signal of the FPGA.

Simplified Functional Block Diagram
-----------------------------------

.. figure:: cn0577_block_diag.png

   CN0577 Simplified Block Diagram

Features
--------

- 15 MSPS Throughput Rate
- Guaranteed 18-Bit, No Missing Codes
- No Pipeline Delay, No Cycle Latency
- 96 dB SNR (Typical)
- 164.5 dB dynamic range
- 2 ppm INL (Typical)
- Serial LVDS Digital Interface
- Flexible analog input drive (single-ended or differential mode)
- On-board 120 MHz precision voltage-controlled crystal oscillator (VCXO)

Hardware Configuration
----------------------

Block Assignments
~~~~~~~~~~~~~~~~~

.. figure:: cn0577_block_terminal.png
   :width: 500px

   CN0577 Block Assignments

.. csv-table::
   :file: block-assignments.csv

Power Supply
~~~~~~~~~~~~~

Power to the :adi:`EVAL-CN0577-FMCZ <CN0577>` comes directly from the
+12 V supply provided through the FMC connector.

.. figure:: power_supply_1.png

   CN0577 Power Supply

Analog Inputs
~~~~~~~~~~~~~~~~

The SMA connectors on the :adi:`EVAL-CN0577-FMCZ <CN0577>` (VIN+
and VIN−) provide analog inputs from a low noise, audio precision signal
source (such as the Audio Precision audio analyzer).

Onboard Clock Reference
~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-CN0577-FMCZ <CN0577>` clock diagram is shown in the figure below.
An onboard 120 MHz voltage controlled crystal oscillator is used to provide
the clock for the :adi:`EVAL-CN0577-FMCZ <CN0577>` and the FPGA. This
ultralow noise oscillator has a typical phase noise of -162 dBc/Hz at 10 kHz
offset, a tuning voltage range of 0 V to 3.3 V, and a frequency pulling range of
28 ppm to 55 ppm. Additionally, this crystal oscillator has an RMS jitter of <50
fs to 100 fs at 100 MHz carrier.

The clock is fanned out to the retiming flip-flop and the FPGA. An
:adi:`ADG3241` level shifter converts the clock’s 3.3 V logic level
to the 2.5 V level required by the retiming flip-flop. An
:adi:`ADN4661` converts the 3.3 V clock to LVDS signaling, which is
then forwarded to a global clock connection on the FMC connector.

.. figure:: cn0577_clock.png

   CN0577 Onboard Clock Reference

External Clock Reference Option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the :adi:`EVAL-CN0577-FMCZ <CN0577>` is to be synchronized to
other circuits, or if tighter frequency accuracy or drift frequency drift is
required, an external clock can be applied to the external clock connector
(J3). Along with connecting it, you will also need to update the solder jumper
(JP14) to change from the onboard crystal oscillator. If the external clock
frequency is significantly higher or lower than the on-board 120 MHz clock,
reanalyze the entire circuit including the FPGA timing constraints.

.. figure:: jp14.png
   :width: 300 px

   External Clock Option

The external clock circuitry also includes a high speed single inverter that
provides AC coupling and balances the rise and fall times. This device has a
typical time propagation delay of 2.4 ns and achieves a high output drive,
while maintaining low static power dissipation over a broad VCC operating
range.

System Setup
------------

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is the list of items needed in order to replicate this demo.

Hardware
^^^^^^^^

- :adi:`EVAL-CN0577-FMCZ <CN0577>` Circuit Evaluation Board
- ZedBoard (AES-Z7EV-7Z020-G)
- 12 V power supply
- Host PC
- SD card (16 GB or larger)
- LAN cable
- SMA cables
- XLR to SMA adapter cable
- Audio analyzer (Audio Precision© APX525) or other input source (e.g., ADALM2000)

If using :adi:`ADALM2000` as input source:

- :adi:`AD-M2KBNC-EBZ`
- BNC to SMA cable


Software
^^^^^^^^

- :ref:`kuiper` Image

For the device to run, the SD card should be loaded with Analog Devices Kuiper
Linux, a distribution based on Raspbian from the Raspberry Pi Foundation. It
incorporates Linux device drivers for ADI products as well as tools and other
software products designed and created with ease of use in mind. The reasoning
behind creating this distribution is to minimize the barriers to
integrating ADI hardware devices into a Linux-based embedded system.

Access to the embedded system can be through a remote PC connected either via
LAN cable or Wi-Fi.

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

In order to control the :adi:`EVAL-CN0577-FMCZ <CN0577>`, you will
need to install ADI Kuiper Linux on an SD card. Complete instructions, including
where to download the SD card image, how to write it to the SD card, and how to
configure the system are provided at
:dokuwiki:`Kuiper Project List <resources/tools-software/linux-software/kuiper-linux/project-list>`.

Write the image and follow the system configuration procedure. Follow the directions for
preparing the image for the CN0577.

Preparing the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

To prepare the SD card for the Zedboard:

#. :dokuwiki:`Download the ADI Kuiper Image <resources/tools-software/linux-software/kuiper-linux/project-list>`

#. Validate, format, and :external+adi-kuiper-gen:doc:`flash the SD Card <use-kuiper-image>`.

#. Configuring the SD Card. Follow instructions for Xilinx projects.

   * Directory on SD image: cn0577_zed
   * Image files on SD card: zynq-common

System Block Diagram
--------------------

.. figure:: sys_block_diag.png

   CN0577 System Block Diagram

Running the System
~~~~~~~~~~~~~~~~~~

To set up the complete system using **Audio Precision audio analyzer** as input
source, follow these steps:

#. Download and install the IIO Oscilloscope application on the PC, Mac, or
   Linux host.
#. Load the Analog Devices Kuiper Linux image onto the SD card.
#. Configure the SD card for the :adi:`EVAL-CN0577-FMCZ <CN0577>`.
#. Place the SD card into the ZedBoard.
#. Connect :adi:`EVAL-CN0577-FMCZ <CN0577>` to the ZedBoard through
   the FMC pin connector.
#. Connect the 12 V power supply jack on the ZedBoard.
#. Plug in the LAN cable from the ZedBoard to the host computer.
#. Connect the :adi:`EVAL-CN0577-FMCZ <CN0577>` to the Audio
   Precision audio analyzer using the XLR to SMA adapter cable.
#. Connect the ground of the :adi:`EVAL-CN0577-FMCZ <CN0577>` to the
   Audio Precision audio analyzer.
#. Connect the Audio Precision audio analyzer USB cable to PC.
#. Run the IIO Oscilloscope software and capture the resulting ADC data.


.. figure:: demo_with_ap.png

   CN0577 Evaluation Setup

Using :adi:`ADALM2000` as input source:

#. Download and install the IIO Oscilloscope application on the PC, Mac, or
   Linux host.
#. Load the Analog Devices Kuiper Linux image onto the SD card.
#. Configure the SD card for the :adi:`EVAL-CN0577-FMCZ <CN0577>`.
#. Place the SD card into the ZedBoard.
#. Connect :adi:`EVAL-CN0577-FMCZ <CN0577>` to the ZedBoard through
   the FMC pin connector.
#. Connect the 12 V power supply jack on the ZedBoard.
#. Plug in the LAN cable from the ZedBoard to the host computer.
#. Connect the :adi:`AD-M2KBNC-EBZ` to the ADALM2000.
#. Connect the ADALM2000 to :adi:`EVAL-CN0577-FMCZ <CN0577>` using
   BNC to SMA cable (W1 to J1 and W2 to J2)
#. Plug the ADALM2000 to the host PC. Open Scopy and use the Signal Generator
   feature to set input. More information on using the Scopy Signal Generator in :dokuwiki:`here <university/tools/m2k/scopy/siggen>`.
#. Run the IIO Oscilloscope software and capture the resulting ADC data.

.. figure:: demo_with_m2k.png

   CN0577 Setup with ADALM2000 Portable Oscilloscope

Software
--------

The :adi:`EVAL-CN0577-FMCZ <CN0577>` is supported with the Libiio
library. This library is cross-platform (Windows, Linux, Mac) with language
bindings for C, C#, Python, MATLAB, and others. Two easy to examples that can be
used with the :adi:`EVAL-CN0577-FMCZ <CN0577>` are:

- :ref:`iio-oscilloscope`
- :ref:`Python (via Pyadi-iio) <pyadi-iio>`

Connection
~~~~~~~~~~

To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend used to
connect to the device as well as the platform where the EVAL-CN0577-FMCZ is
attached. The platform currently supported for the CN0557 is the ZedBoard through the
ADI Kuiper Linux. The user needs to supply a URI which will be used in the
context creation. The Libiio is a library for interfacing with IIO devices.

Install the :git-libiio:`Libiio package <releases+>` on your
machine.

The :ref:`libiio iio_info`
command is a part of the libIIO package that reports all IIO attributes.

Upon installation, simply enter the command on the terminal command line to
access it.

For Windows machine connected to ZedBoard via Ethernet cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using SSH Terminal Software:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open SSH Terminal Software (PuTTY, TeraTerm or similar). User should now start
the PuTTY application and enter certain values in the configuration window. In
the terminal, run:

.. shell::
   :show-user:

   $iio_info -u ip:<ip_address>

Using Command Terminal:
^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   $iio_info -s

Prompting this on the command terminal in your windows PC will give you the ip
address to access the EVAL-CN0577-FMCZ.

.. shell::

   $ssh analog@<ip_address>

.. shell::
   :show-user:

   $iio_info -u ip:<ip_address>

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage the device being used.
The :ref:`libiio iio_attr` command reads and writes IIO attributes.

.. shell::

   $iio_attr [OPTION]...

Example:

To look at the context attributes, enter this code on the terminal:

.. shell::

   $iio_attr -a -C

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. admonition:: Download

  Make sure to download/update to the latest version of IIO Oscilloscope at
  :git-iio-oscilloscope:`releases+`

#. Once done with the installation or an update of the latest IIO Oscilloscope,
   open the application. The user needs to supply a URI which will be used in
   the context creation of the IIO Oscilloscope and the instructions can be seen
   from the previous section.
#. Press refresh to display available IIO Devices, once ltc2387 appeared, press
   connect.

.. figure:: 577_osc.png

   IIO Oscilloscope Connection

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of ltc2387 wherein you can directly access the
attributes of the device.

.. figure:: 577_debug_panel.png

   CN0577 Debug Panel

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the ADC voltages and
the device temperature.

.. figure:: 577_dmm_panel.png

   CN0577 DMM Panel

Pyadi-IIO
~~~~~~~~~

:ref:`pyadi-iio` is a python abstraction module for ADI hardware with IIO drivers
to make them easier to use.

This module provides device-specific APIs built on top of the current
libIIO python bindings. These interfaces try to match the driver naming as
much as possible without the need to understand the complexities of libIIO and
IIO.

Running the Example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO in your machine, you are now ready to
run python script examples. In our case, run the ltc2387_example.py found in the
examples folder.

#. Connect the :adi:`EVAL-CN0577-FMCZ <CN0577>` to the ZedBoard.
#. Open command prompt or terminal and navigate through the examples folder
   inside the downloaded or cloned *pyadi-iio* directory.
#. Run the example script using the command.

.. shell::

   /path/to/pyadi-iio/examples
   $python3 ltc2387_example.py

Running example with ADALM2000 with the setting below:

.. figure:: scopy_diff_input.png

   CN0577 Sample Output in Scopy

The expected output should look like this:

.. figure:: output_time_domain.png

   CN0577 Time Domain Output


GitHub link for the python sample script:
:git-pyadi-iio:`CN0577 Python Example <examples/ltc2387_example.py>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :download:`EVAL-CN0577-FMCZ Design & Integration Files <CN0577-DesignSupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project
   - LTspice Simulation File

Reference Demos & Software
----------------------------

- :git-pyadi-iio:`/`
- :ref:`pyadi-iio`
- :ref:`iio-oscilloscope`
- :ref:`kuiper`
- :external+hdl:ref:`cn0577`

More Information and Useful Links
---------------------------------

- :adi:`CN0577 Circuit Note Page <ADCN0577>`
- :adi:`LTC2387-18 Product Page <LTC2387-18>`
- :adi:`ADR4520 Product Page <ADR4520>`
- :adi:`ADA4945-1 Product Page <ADA4945-1>`
- :adi:`ADN4661 Product Page <ADN4661>`
- :adi:`ADG3241 Product Page <ADG3241>`
- :adi:`LT3042 Product Page <LT3042>`
- :adi:`LT3080 Product Page <LT3080>`
- :adi:`LT3094 Product Page <LT3094>`
- :adi:`LT1931 Product Page <LT1931>`

Registration
------------

Receive software update notifications, documentation
updates, view the latest videos, and more when you register your hardware.
`Register <https://my.analog.com/en/app/registration/hardware/EVAL-CN0577-FMCZ?&v=RevB>`__ to receive all these great benefits
and more!

HDL Reference design
--------------------

The HDL Reference Design is documented at :external+hdl:ref:`cn0577`.

..
   Enable after adding content
   User Guides
   -----------

   .. toctree::
      :titlesonly:
      :maxdepth: 2
      :glob:

      */index