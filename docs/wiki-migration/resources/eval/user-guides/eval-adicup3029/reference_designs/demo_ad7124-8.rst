AD7124-8 PMOD EVAL_ADICUP3029 Demo (w/ EVAL-AD7124-8-PMDZ)
==========================================================

The **ADuCM3029_demo_ad7124_8PMDZ** project provides a solution to control the :adi:`AD7124-8` ADC on the :doc:`EVAL-AD7124-8-PMDZ </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/eval-ad7124-8-pmdz>` PMOD using a simple CLI on the **USB**. The demo showcases the flexibility of the AD7124 in choosing inputs, filters and different ranges for the available 16 channels.

General Description/Overview
----------------------------

The :adi:`EVAL-AD7124-8-PMDZ` is a minimalist 8-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC (Analog to Digital Converter) with PGA and Reference, SPI Pmod board for the :adi:`AD7124-8`. This module is designed as a low-cost alternative to the fully-featured :adi:`AD7124-8` evaluation board and has no extra signal conditioning for the ADC.

The initial configuration of the **ADuCM3029_demo_ad7124_8PMDZ** engages all inputs in a mix of differential and single-ended channels. The input assignation to channels is the following:

-  Channel 0: AIN0-AIN1, differential;
-  Channel 1: AIN2-AIN3, differential;
-  Channel 2: AIN4-AIN5, differential;
-  Channel 3: AIN6-AIN7, differential;
-  Channel 4: AIN8-AIN9, differential;
-  Channel 5: AIN10-AIN11, differential;
-  Channel 6: AIN12-AIN13, differential;
-  Channel 7: AIN14-AIN15, differential;
-  Channel 8: AIN0-AGND, single-ended;
-  Channel 9: AIN1-AGND, single-ended;
-  Channel 10: AIN2-AGND, single-ended;
-  Channel 11: AIN3-AGND, single-ended;
-  Channel 12: AIN4-AGND, single-ended;
-  Channel 13: AIN5-AGND, single-ended;
-  Channel 14: AIN6-AGND, single-ended;
-  Channel 15: AIN7-AGND, single-ended;

By default only channel 0 is active at first, but this can be adjusted using the appropriate CLI commands (described below). At first all channels are using the configuration register 0 which is set to sinc4 filter option and the first option of PGA corresponding to the widest range. The filter sample rate is set at maximum. Each configuration register has a different PGA setting so that each channel can be set using the CLI to any PGA. The demo does this by assigning each channel to the corresponding configuration register that contains the desired PGA setting. Most of the demo CLI commands work in this configuration, but the CLI also offers access to the individual registers for the user to set the desired configuration manually.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-AD7124-8-PMDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ demo application <projects/ADuCM3029_demo_ad7124_8PMDZ>`
   -  CrossCore Embedded Studio (2.9.1 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-AD7124-8-PMDZ** board to the **EVAL-ADICUP3029**.


|image1|

-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect it to a computer. The final setup should look similar to the picture below.

|image2|

Configuring the Software
------------------------

The software needs no configuration.

Outputting Data
---------------


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#serial_terminal_setup>`_


Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the list of commands and their short versions. Bellow is the short command list:

+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Function             | Command  | Description                                                                                                                                                 | Example                                                                                           |
+======================+==========+=============================================================================================================================================================+===================================================================================================+
| General commands     |          |                                                                                                                                                             |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Help                 | **h**    | Display available commands.                                                                                                                                 |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Reset                | **rst**  | Reset the application.                                                                                                                                      | **rst dev** - perform only device reset (datasheet defaults);                                     |
|                      |          | <*opt*> = 'dev' to perform only a device reset; do not include to perform an application reset.                                                             | **rst** - perform application reset (application defaults).                                       |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ADC commands         |          |                                                                                                                                                             |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Register read        | **arr**  | Read an ADC register of a specific address.                                                                                                                 | **arr 2a** - Read register 0x2A                                                                   |
|                      |          | <*addr*> = Address of the register to be read in hexadecimal base.                                                                                          |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Register write       | **awr**  | Write an ADC register of a specific address with a new value.                                                                                               | **arw 9 8002** - Write 0x8002 to register 0x9.                                                    |
|                      |          | <*addr*> = Address of the register to be written in hexadecimal base.                                                                                       |                                                                                                   |
|                      |          | <*val*> = New value of the register.                                                                                                                        |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Get data             | **ags**  | Get a number of samples per enabled channels. If the operation takes too long press 'q' to abort.                                                           |                                                                                                   |
|                      |          | <*no*> = Number of samples (maximum 2048). If sample rate is smaller than 3000 setting the argument 0 or no argument means continuous streaming.            |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Enable channels      | **aces** | Choose ADC channels to be activated.                                                                                                                        | **aces 0xAAAA** - activate every other channel. '0x' is necessary for hexadecimal interpretation. |
|                      |          | <*mask*> = 16-bit mask of the channels to be activated. Can be hexadecimal or binary.                                                                       |                                                                                                   |
|                      |          | A bit of 1 means activated the channel, a bit of 0 means deactivate                                                                                         |                                                                                                   |
|                      |          | the channel.                                                                                                                                                |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Get enabled channels | **aceg** | Get enable status of ADC channels. Returns a hexadecimal 16-bit mask where bits of 1 represent enabled channels, and bits of 0 represent disabled channels. |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Set PGA              | **aps**  | Set PGA for a channel.                                                                                                                                      | **aps 0 opt3** - set ADC channel 0 to PGA 3, gain value of 8.                                     |
|                      |          | <*chan*> = ID of the channel to be changed.                                                                                                                 |                                                                                                   |
|                      |          | <*opt*> = PGA option; values are: opt0, opt1, ... opt7 corresponding to the datasheet.                                                                      |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Get PGA              | **apg**  | Display a channel's PGA option; return values are: opt0, opt1, ... opt7 corresponding to the datasheet.                                                     | **apg 0** - read the PGA value of channel 0.                                                      |
|                      |          | <*chan*> = ID of the channel to be read.                                                                                                                    |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Set sample           | **aos**  | Set ADC sample rate. Filter option, power mode and reference clock must be taken into consideration.                                                        | **aos 2000** - set sample rate to 2000 samples per second.                                        |
| rate                 |          | <*odr*> = New sample rate value.                                                                                                                            |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Get sample rate      | **aog**  | Read the current sample rate.                                                                                                                               |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Set filter           | **afs**  | Set ADC filter option.                                                                                                                                      | **afs fflt4** - set filter option to fast settling sinc4.                                         |
| option               |          | <*opt*> = filter option; can be: 'sinc4', 'sinc3', 'fflt4', 'fflt3' and 'postf'.                                                                            |                                                                                                   |
|                      |          | <*post*> = post-filter option; can be: 'opt0', 'opt1', ... 'opt3'; add only when opt=postf.                                                                 |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Get filter           | **afg**  | Read the current filter.                                                                                                                                    |                                                                                                   |
| option               |          |                                                                                                                                                             |                                                                                                   |
+----------------------+----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad71248pmdz_terminal_sample.png
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the AD7124-8 PMOD.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that Analog Devices creates for testing and evaluation purposes. This is the EASIEST way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters and customize the software to fit your needs, but will be a bit more advanced and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_ad7124_8PMDZ** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt AD7124-8 PMOD Hex File

   
   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ.Hex <releases/download/Latest/ADuCM3029_demo_ad7124_8PMDZ.hex>`
   
   Complete AD7124-8 PMOD Source Files
   
   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad7124_8PMDZ Source Code <projects/ADuCM3029_demo_ad7124_8PMDZ>`
   


How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </wiki-migration/resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

The application contains the platform drivers with the sources in **platform_source** and the headers in **platform_include**. In the **src** root directory there is the ad7124 driver as found on Github, but with a custom initialization vector in **ad7124_regs** module.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad7124pmdz_file_structure.png
   :align: center

// End of Document //

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad7124_pmod_unplug.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad7124_pmod_plug.jpg
