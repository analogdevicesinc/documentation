ADRD3161-01Z Production Guide
=============================

.. note::

   These instructions are intended for bringing up your own board from scratch. There is no need to follow them if you bought a board.

Bootstrapping the TMC9660
-------------------------

.. warning::

   **USERS SHOULD NOT HAVE TO FOLLOW THE BOOTSTRAPPING SECTION.** These steps have already been done in the factory. Only follow them if you understand the TMC9660 bootstrap procedure. This permanently uses up one of the 4 configuration slots on the TMC9660. It cannot be undone and may only be overwritten at most 4 times on a given TMC9660 IC.

The :adi:`TMC9660` has reconfigurable I/O, clocking, LDO outputs, etc. Bootstrapping is the initial step of configuring these. Through bootstrapping, a configuration may be loaded in volatile memory, or "burned" to permanent nonvolatile memory to be loaded at power-up. These burn operations should be used sparingly, as they are limited to a total of 4 :abbr:`OTP (One Time Programmable)` configuration slots.

Configurations may be applied temporarily. If you want to try out a different configuration to the one provided as a default for this board, follow :adi:`AN-2601: TMC9660 Configuration and Bootstrapping
<en/resources/app-notes/an-2601.html>` and reference the :ref:`board schematic <adrd3161_design_files>` and :git-adrd3161-fw:`default configuration <scripts/ioconfig_adrd3161.toml>`.
These instructions assume the TMC9660 is unconfigured (or has an invalid config, as described in the TMC9660 datasheet, section *Configuration Storage*) and thus enters bootstrap mode at startup.

Preparation:

* Download :adi:`UBLTools <en/products/tmc9660.html#software-resources>`
* Download bootstrap :git-adrd3161-fw:`config file <scripts/ioconfig_adrd3161.toml>`.
* Obtain an UART probe (:adi:`MAX32625PICO` or other MAXDAP compatible)

Steps:

#. Connect the UART probe to header P7
#. Take note of which serial interface the probe took. In the following commands, replace ``COM123`` with the actual serial port name.
#. Verify the TMC9660 communicates and is in bootstrap mode:

   .. shell:: ps1

      $ ublcli.exe --port COM123 inspect chip
       Chip:                 TMC9660
       Bootloader Version:   v1.0

#. Upload the configuration and burn:

   .. shell:: ps1

      $ ublcli.exe --port COM123 write config --burn ioconfig_adrd3161.toml
       Proceed with OTP burn? (y/n): y
       Config burned successfully

Flashing the MAX32662
---------------------

The ADRD316-01Z firmware is based on Zephyr. The source code for the latest version may be found at :git-adrd3161-fw:`/ <+>`.

Prerequisites:

* MSDK
* Zephyr workspace

Install MSDK following the `MSDK User Guide
<https://analogdevicesinc.github.io/msdk/USERGUIDE/#download>`_. On WSL, we
recommend installing it as root in ``/MaximSDK``, instead of the default
user home install path.

.. tab-set::

   .. tab-item:: Create new west workspace

      If you do not have Zephyr SDK already set up, start by creating a Zephyr
      workspace, following the
      `Zephyr Getting Started <https://docs.zephyrproject.org/latest/develop/getting_started/index.html>`__
      tutorial. In short, the following commands should suffice:

      Set up virtualenv:

      .. shell::

         $ mkdir zephyrproject
         $ cd zephyrproject
         $ python3 -m venv .venv
         $ source .venv/bin/activate

      Set up west workspace:

      .. shell::

         $ pip install west
         $ west init -m https://github.com/analogdevicesinc/adrd3161-fw . # This might take a while - big download
         $ west update # This might take a while - big download
         $ west zephyr-export
         $ west packages pip --install
         $ cd zephyr
         $ west sdk install
         $ cd ..

   .. tab-item:: Use existing west workspace

      You may reuse a pre-existing West workspace. This is especially convenient if working on other boards in the ADRD family.

      .. shell::

         $ cd <path to west workspace>
         $ source .venv/bin/activate
         $ git clone https://github.com/analogdevicesinc/adrd3161-fw
         $ west config manifest.path adrd3161-fw
         $ west update

Enter the workspace and load the python virtual environment:

.. shell::

   $ cd <path to west workspace>
   $ source .venv/bin/activate
   $ cd adrd3161-fw

Build the firmware:

.. shell::

   $ west build -b adrd3161 -p auto app

Flash the firmware (will build if necessary):

.. shell::

   # Replace /MaximSDK/ with the path to MSDK
   $ west flash --openocd-search /MaximSDK/Tools/OpenOCD/scripts/ --openocd /MaximSDK/Tools/OpenOCD/openocd

If your debug probe supports this, you may also flash the firmware by dragging and dropping the ``build/zephyr/zephyr.hex`` file onto the debug probe virtual storage device.

Visual check
------------

A correctly prepared flashed board should do the following when power is applied:

* FAULT LED flashes briefly but stays off
* DS1 LED flashes briefly but stays off
* DS2 LED blinks at 2.5Hz indicating CANopen PRE-OPERATIONAL state

