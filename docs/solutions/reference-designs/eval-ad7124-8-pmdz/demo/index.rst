.. _eval-ad7124-8-pmdz demo:

EVAL-AD7124-8-PMDZ Demo Project
===============================

The **ADuCM3029_demo_ad7124_8PMDZ** project provides a solution to control the
:adi:`AD7124-8` ADC on the :adi:`EVAL-AD7124-8-PMDZ` Pmod Board using a simple CLI
on the **USB**. The demo showcases the flexibility of the AD7124 in choosing
inputs, filters and different ranges for the available 16 channels.

General Description
-------------------

The :adi:`EVAL-AD7124-8-PMDZ` is a minimalist 8-Channel, Low Noise, Low Power,
24-bit, Sigma-Delta ADC (Analog to Digital Converter) with PGA and Reference,
SPI Pmod board for the :adi:`AD7124-8`. This module is designed
as a low-cost alternative to the fully-featured :adi:`AD7124-8`
evaluation board and has no extra signal conditioning for the ADC.

The initial configuration of the **ADuCM3029_demo_ad7124_8PMDZ** engages all
inputs in a mix of differential and single-ended channels. The input assignation
to channels is the following:

- Channel 0: AIN0-AIN1, differential;
- Channel 1: AIN2-AIN3, differential;
- Channel 2: AIN4-AIN5, differential;
- Channel 3: AIN6-AIN7, differential;
- Channel 4: AIN8-AIN9, differential;
- Channel 5: AIN10-AIN11, differential;
- Channel 6: AIN12-AIN13, differential;
- Channel 7: AIN14-AIN15, differential;
- Channel 8: AIN0-AGND, single-ended;
- Channel 9: AIN1-AGND, single-ended;
- Channel 10: AIN2-AGND, single-ended;
- Channel 11: AIN3-AGND, single-ended;
- Channel 12: AIN4-AGND, single-ended;
- Channel 13: AIN5-AGND, single-ended;
- Channel 14: AIN6-AGND, single-ended;
- Channel 15: AIN7-AGND, single-ended;

By default only channel 0 is active at first, but this can be adjusted using the
appropriate CLI commands (described below). At first all channels are using the
configuration register 0 which is set to sinc4 filter option and the first
option of PGA corresponding to the widest range. The filter sample rate is set
at maximum. Each configuration register has a different PGA setting so that each
channel can be set using the CLI to any PGA. The demo does this by assigning
each channel to the corresponding configuration register that contains the
desired PGA setting. Most of the demo CLI commands work in this configuration,
but the CLI also offers access to the individual registers for the user to set
the desired configuration manually.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

**Hardware**

  - :adi:`EVAL-ADICUP3029`
  - :adi:`EVAL-AD7124-8-PMDZ`
  - Micro USB to USB cable
  - PC or Laptop with a USB port

**Software**

  - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ demo application <master:projects/ADuCM3029_demo_ad7124_8PMDZ>`
  - CrossCore Embedded Studio (2.9.1 or higher)
  - ADuCM302x DFP (3.2.0 or higher)
  - ADICUP3029 BSP (1.1.0 or higher)
  - Serial Terminal Program

    - Such as Putty or TeraTerm

Setting up the Hardware
-----------------------

#. Connect **EVAL-AD7124-8-PMDZ** board to the **EVAL-ADICUP3029**.

    .. figure:: ad7124_pmod_unplug.jpg

       EVAL-AD7124-8-PMDZ and EVAL-ADICUP3029 before connection

#. Connect a micro-USB cable to P10 connector of the **EVAL-ADICUP3029** and connect
   it to a computer. The final setup should look similar to the picture below.

    .. figure:: ad7124_pmod_plug.jpg

       EVAL-AD7124-8-PMDZ connected to EVAL-ADICUP3029

Configuring the Software
------------------------

The software needs no configuration.

Outputting Data
---------------

Serial Terminal Setup
~~~~~~~~~~~~~~~~~~~~~

A serial terminal is an application that runs on a PC or laptop that is
used to display data and interact with a connected device
(including many of the Circuits from the Lab reference designs). The
device’s UART peripheral is most often connected to a UART to USB interface
IC, which appears as a traditional COM port on the host PC/ laptop.
(Traditionally, the device’s UART port would have been connected to an RS-232
line driver / receiver and connected to the PC via a 9-pin or 25-pin serial
port.) There are many open-source applications, and while there are many
choices, typically we use one of the following:

- `TeraTerm <https://ttssh2.osdn.jp/index.html.en>`__
- `Putty <https://www.putty.org/>`__
- `Real Term <https://realterm.sourceforge.io/>`__

Before continuing, please make sure you download and install one of the above
programs.

There are several parameters on all serial terminal programs that must be
setup properly in order for the PC and the connected device to communicate.
Below are the common settings that must match on both the PC side and the
connected UART device.

#. **COM Port** - This is the physical connection made to your PC or laptop,
   typically made through a USB cable but can be any serial communications
   cable. You can determine the COM port assigned to your device by visiting the
   device manager on your computer. Another method for identifying which COM
   port is associated with a USB-based device is to look at which COM ports are
   present before plugging in your device, then plug in your device, and look
   for a new COM port.
#. **Baud Rate** - This is the speed at which data is being transferred from the
   connected device to your PC. These parameters must be the same on both
   devices or data will be corrupted. The default setting for most of the
   reference designs in 115200.
#. **Data Bits** - The number of data bits per transfer. Typically, UART
   transmits ASCII codes back to the serial port so by default this is almost
   always set to 8-Bits.
#. **Stop Bits** - The number of **“stop”** conditions per transmission. This
   is typically set to 1, but can be set to 2 for redundancy..
#. **Parity** - Is a way to check for errors during the UART transmission.
   Unless otherwise specified, set parity to **“none”**.
#. **Flow Control** - Is a way to ensure that data lose between fast and slow
   devices on the same UART bus are not lost during transmission. This is
   typically not implemented in a simple system, and unless otherwise specified,
   set to **“none”**.

In many instances there are other options that each of the different serial
terminal applications provide, such as **local line echo** or **local line
editing**, and features like this can be turned on or off depending on your
preferences. This setup guide will not go over all the options of each tool,
but just the minor features that will make it easier to read back data from
the connected devices.

Example Setup using PuTTY
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Plug in your connected device using a USB cable or other serial cable.
#. Wait for the device driver of the connected device to install on your PC or
   Laptop.
#. Open your device manager, and find out which COM port was assigned to your
   device.

   .. figure:: device_manager.png

      Windows Device Manager showing COM port

#. Open up your serial terminal program (e.g., PuTTY).
#. Click on the serial configuration tab or window, and input the settings to
   match the requirements of your connected device. The default baud rate for
   most of the reference designs is 115200. Make sure that you use the correct
   baud rate for your application.

   .. figure:: putty_serial_config.png

      PuTTY serial configuration

#. Ensure you click on the checkboxes for **Implicit CR in every LF** and
   **Implicit LF in every CF**.

#. Ensure that local echo and line editing are enabled, so that you can see what
   you type and are able to correct mistakes. (Some devices may echo typed
   characters - if so, you will see each typed character twice. If this happens,
   turn off local echo.)

   .. figure:: putty_terminal_options.png
      :width: 600

      PuTTY terminal options

#. Click on the ``Open`` button, and as long as your connected device and serial
   terminal program are setup the same, then you should be able to start
   entering commands.

Available Commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the
list of commands and their short versions. Below is the short command list:

.. csv-table:: Available Commands
  :file: available-commands.csv

.. figure:: ad71248pmdz_terminal_sample.png

   Terminal output sample

Obtaining the Software
----------------------

There are two basic ways to program the EVAL-ADICUP3029 with the software for the
AD7124-8 PMOD.

#. Dragging and Dropping the .Hex to the DAPLINK drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_ad7124_8PMDZ** can be found here:

.. admonition:: Download

  Prebuilt AD7124-8 Pmod Hex File

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ.Hex <releases/download/Latest/ADuCM3029_demo_ad7124_8PMDZ.hex+>`

  Complete AD7124-8 Pmod Source Files

    - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ Source Code <projects/ADuCM3029_demo_ad7124_8PMDZ>`

How to Use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the
:dokuwiki:`Tools Overview page </resources/eval/user-guides/eval-adicup3029/tools>`.

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to import existing projects into your workspace </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_import_existing_projects_into_your_workspace>`
section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to configure the debug session </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_configure_the_debug_session_for_an_aducm3029_application>`
section.

Project Structure
~~~~~~~~~~~~~~~~~

The application contains the platform drivers with the sources in
**platform_source** and the headers in **platform_include**. In the **src** root
directory there is the ad7124 driver as found on GitHub, but with a custom
initialization vector in **ad7124_regs** module.

.. figure:: ad7124pmdz_file_structure.png

   AD7124 PMDZ project file structure
