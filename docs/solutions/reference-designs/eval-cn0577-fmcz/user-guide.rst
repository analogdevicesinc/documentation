.. _eval-cn0577-fmcz user-guide:

User guide
===============================================================================

.. _eval-cn0577-fmcz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

.. _eval-cn0577-fmcz hardware-configuration:

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cn0577_block_terminal.png
   :width: 500px

   CN0577 Block Assignments

.. csv-table::
   :file: resources/block-assignments.csv

.. _eval-cn0577-fmcz power-supply:

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power to the :adi:`EVAL-CN0577-FMCZ <CN0577>` comes directly from
the +12 V supply provided through the FMC connector.

.. figure:: images/power_supply_1.png

   CN0577 Power Supply

.. _eval-cn0577-fmcz analog-inputs:

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SMA connectors on the :adi:`EVAL-CN0577-FMCZ <CN0577>` (VIN+
and VIN−) provide analog inputs from a low noise, audio precision
signal source (such as the Audio Precision audio analyzer).

.. _eval-cn0577-fmcz clock-reference:

Onboard clock reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-CN0577-FMCZ <CN0577>` clock diagram is shown in the figure below.
An onboard 120 MHz voltage controlled crystal oscillator is used to provide the
clock for the :adi:`EVAL-CN0577-FMCZ <CN0577>` and the FPGA. This ultralow noise
oscillator has a typical phase noise of -162 dBc/Hz at 10 kHz offset, a tuning
voltage range of 0 V to 3.3 V, and a frequency pulling range of 28 ppm to 55
ppm. Additionally, this crystal oscillator has an RMS jitter of <50 fs to 100 fs
at 100 MHz carrier.

The clock is fanned out to the retiming flip-flop and the FPGA. An
:adi:`ADG3241` level shifter converts the clock's 3.3 V logic level to the 2.5 V
level required by the retiming flip-flop. An :adi:`ADN4661` converts the 3.3 V
clock to LVDS signaling, which is then forwarded to a global clock connection on
the FMC connector.

.. figure:: images/cn0577_clock.png

   CN0577 Onboard Clock Reference

.. _eval-cn0577-fmcz external-clock:

External clock reference option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the :adi:`EVAL-CN0577-FMCZ <CN0577>` is to be synchronized to other circuits,
or if tighter frequency accuracy or drift is required, an external clock can be
applied to the external clock connector (J3). Along with connecting it, you will
also need to update the solder jumper (JP14) to change from the onboard crystal
oscillator. If the external clock frequency is significantly higher or lower
than the on-board 120 MHz clock, reanalyze the entire circuit including the FPGA
timing constraints.

.. figure:: images/jp14.png
   :width: 300 px

   External Clock Option

The external clock circuitry also includes a high speed single inverter that
provides AC coupling and balances the rise and fall times. This device has a
typical time propagation delay of 2.4 ns and achieves a high output drive, while
maintaining low static power dissipation over a broad VCC operating range.

.. _eval-cn0577-fmcz schematic:

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`EVAL-CN0577-FMCZ Design & Integration Files <resources/cn0577-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project
   - LTspice Simulation File

.. _eval-cn0577-fmcz software-guide:

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0577-FMCZ <CN0577>` is supported with the Libiio library. This
library is cross-platform (Windows, Linux, Mac) with language bindings for C,
C#, Python, MATLAB, and others. Two easy examples that can be used with the
:adi:`EVAL-CN0577-FMCZ <CN0577>` are:

- :ref:`iio-oscilloscope`
- :ref:`Python (via Pyadi-iio) <pyadi-iio>`

.. _eval-cn0577-fmcz connection:

Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend used to
connect to the device as well as the platform where the EVAL-CN0577-FMCZ is
attached. The platform currently supported for the CN0577 is the ZedBoard
through the ADI Kuiper Linux. The user needs to supply a URI which will be used
in the context creation. The Libiio is a library for interfacing with IIO
devices.

Install the :git-libiio:`Libiio package <releases+>` on your machine.

The :ref:`libiio iio_info` command is a part of the libIIO package that reports
all IIO attributes. Upon installation, simply enter the command on the terminal
command line to access it.

For Windows machine connected to ZedBoard via Ethernet cable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using SSH Terminal Software:

Open SSH Terminal Software (PuTTY, TeraTerm or similar). User should now start
the PuTTY application and enter certain values in the configuration window. In
the terminal, run:

.. shell::
   :show-user:

   $iio_info -u ip:<ip_address>

Using Command Terminal:

.. shell::

   $iio_info -s

Prompting this on the command terminal in your windows PC will give you the ip
address to access the EVAL-CN0577-FMCZ.

.. shell::

   $ssh analog@<ip_address>

.. shell::
   :show-user:

   $iio_info -u ip:<ip_address>

.. _eval-cn0577-fmcz iio-commands:

IIO Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are different commands that can be used to manage the device being used.
The :ref:`libiio iio_attr` command reads and writes IIO attributes.

.. shell::

   $iio_attr [OPTION]...

Example:

To look at the context attributes, enter this code on the terminal:

.. shell::

   $iio_attr -a -C

.. _eval-cn0577-fmcz iio-oscilloscope:

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   Make sure to download/update to the latest version of IIO Oscilloscope at
   :git-iio-oscilloscope:`releases+`

#. Once done with the installation or an update of the latest IIO Oscilloscope,
   open the application. You can either use the automatic scan to discover
   available devices on the network, or manually enter the URI
   (``ip:<ip_address>``) if you already know the ZedBoard's IP address.
#. Press refresh to display available IIO Devices, once ltc2387 appeared, press
   connect.

.. figure:: images/577_osc.png

   IIO Oscilloscope — automatic scan

.. figure:: images/cn0577_osc_manual.png

   IIO Oscilloscope — manual URI connection

#. After the board is connected and a channel is enabled, hit the play button.
   The data capture window will display the sampled data.

   .. image:: images/cn0577_zed_time_domain.png
      :width: 1000

Debug Panel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below is the Debug panel of ltc2387 wherein you can directly access the
attributes of the device.

.. figure:: images/577_debug_panel.png

   CN0577 Debug Panel

DMM Panel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the ADC
voltages and the device temperature.

.. figure:: images/577_dmm_panel.png

   CN0577 DMM Panel

.. _eval-cn0577-fmcz pyadi-iio:

Pyadi-IIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`pyadi-iio` is a python abstraction module for ADI hardware with IIO
drivers to make them easier to use.

This module provides device-specific APIs built on top of the current libIIO
python bindings. These interfaces try to match the driver naming as much as
possible without the need to understand the complexities of libIIO and IIO.

Running the Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. figure:: images/scopy_diff_input.png

   CN0577 Sample Output in Scopy

The expected output should look like this:

.. figure:: images/output_time_domain.png

   CN0577 Time Domain Output

GitHub link for the python sample script:
:git-pyadi-iio:`CN0577 Python Example <examples/ltc2387_example.py>`
