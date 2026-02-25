.. _eval-cn0535-sdp-k1:

CN0535 and the SDP-K1
======================

General Setup
-------------

The following sections describe the steps for setting up the CN0535 board using
the :adi:`SDP-K1` and the
`mbed example program for CN0535-FMCZ
<https://os.mbed.com/teams/AnalogDevices/code/EVAL-CN0535-FMCZ>`__.

Equipment
---------

- :adi:`SDP-K1` microcontroller board
- :adi:`EVAL-CN0535-FMCZ <CN0535>` evaluation board
- PC with a USB port and Windows 7 (32-bit) or higher
- Serial terminal software (PuTTY, Tera Term, or similar)
- USB Standard-A to Mini-B cable
- 6 V wall wart power supply
- `SDP-K1 User Guide
  <https://www.analog.com/media/en/technical-documentation/user-guides/EVAL-SDP-CK1Z-UG-1539.pdf>`__

Hardware Setup
--------------

The following sections describe the process of setting up the hardware for both
the :adi:`SDP-K1` microcontroller board and the EVAL-CN0535-FMCZ evaluation
board.

EVAL-CN0535-FMCZ Prep for Use with SDP-K1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0535-FMCZ was designed to be evaluated using the :adi:`SDP-H1`. If
the user wants to evaluate the CN0535 using the :adi:`SDP-K1`, the following
components need to be installed. The table below shows the components that must
be installed to enable use of the EVAL-CN0535-FMCZ with the SDP-K1.

.. list-table:: Required Components for SDP-K1 Compatibility
   :header-rows: 1
   :widths: 10 30 50

   * - #
     - Component
     - Manufacturing Part Number
   * - 1
     - P2, P4
     - TSM-108-04-T-SV
   * - 2
     - P3
     - TSM-110-04-T-SV
   * - 3
     - R38, R5, R6, R7, R27
     - ERJ-3GEY0R00V or equivalent 0 ohm jumper
   * - 4
     - C25
     - 0603YC104KAT2A or equivalent
   * - 5
     - Y1
     - SIT8008BI-21-33E-16.38400G

The following figures show the board setup for SDP-K1, highlighting the
component locations on both sides of the board.

.. figure:: board_top.png
   :align: center

   EVAL-CN0535-FMCZ board top side -- SDP-K1 component locations

.. figure:: board_bot.png
   :align: center

   EVAL-CN0535-FMCZ board bottom side -- SDP-K1 component locations

SDP-K1 Connection
~~~~~~~~~~~~~~~~~~

The CN0535 board is mounted on the SDP-K1 board via the Arduino headers. The
SDP-K1 only requires a single Standard-A to type-C USB cable to connect to the
PC. Both the orange Connected LED and green SYS PWR LED should light on the
SDP-K1 if connected correctly.

.. figure:: setup_block_diagram2.png
   :align: center

   CN0535 board mounted on the SDP-K1 via Arduino headers

.. note::

   For SDP-K1 Rev E and below, a 6 V wall-wart power supply is needed on P15.

Software Setup
--------------

Importing the EVAL-CN0535-FMCZ MBED Example Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. If the user does not have an mbed online account, create one at
   https://ide.mbed.com/.
#. After having an account, open the example program for EVAL-CN0535-FMCZ at
   https://os.mbed.com/teams/AnalogDevices/code/EVAL-CN0535-FMCZ/.

   .. figure:: mbed_link.png
      :align: center

      MBED example program page

   .. figure:: mbed_link_2.png
      :align: center

      Import program into compiler

   .. figure:: mbed_link_3.png
      :align: center

      MBED online compiler with imported program

#. Import the program into the mbed online compiler.
#. Compile and download the binary to the SDP-K1.

Connecting to a Serial Terminal Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to communicate with the board using the SDP-K1, the user needs to
install a serial terminal software on their PC. It is recommended to use PuTTY.

#. Open Device Manager through the Windows control panel and plug the
   microcontroller board into the PC. When the board is detected it will appear
   in Device Manager, displaying as USB Serial Device with the assigned COM
   port number.

   .. figure:: device_manager.png
      :align: center
      :width: 450px

      Windows Device Manager showing the SDP-K1 as USB Serial Device

#. Open the serial terminal application and enter the correct values:

   - **Serial line**: COM port noted from Device Manager
   - **Speed**: 115200

   .. figure:: putty1.png
      :align: center

      PuTTY session configuration

   .. figure:: putty2.png
      :align: center

      PuTTY terminal configuration

#. Under the Terminal tab, configure local echo and line editing as needed.
#. Click **Open** to connect.
#. Upon connection, the interface menu should appear. If not, press the reset
   button on the microcontroller board to bring up the command menu.

   .. figure:: putty_terminal.png
      :align: center

      CN0535 serial terminal command menu

.. note::

   This does not work with version A and B of the SDP-K1.

#. From here, the user should type the number corresponding to their desired
   choice and press Enter. Note that many choices will create sub-menus,
   prompting the user to make another choice.

Command Summary
~~~~~~~~~~~~~~~~

The following table shows every command along with a brief description. Some
commands have recommended settings for optimal results for narrow bandwidth
measurements of 32 kHz.

.. list-table:: CN0535 + SDP-K1 Command Set
   :header-rows: 1
   :widths: 8 35 57

   * - #
     - Command
     - Description
   * - 1
     - Set LTC6373 PGIA Gain/Mode
     - Change the :adi:`LTC6373` gain or mode. Available options are Shutdown
       mode and gains of 0.25 V/V, 0.5 V/V, 1 V/V, 2 V/V, 4 V/V, 8 V/V,
       16 V/V.
   * - 2
     - Set ADA4945 FDA Power Mode
     - Change the :adi:`ADA4945-1 <ADA4945>` power mode to Full Power Mode or
       Low Power Mode.
   * - 3
     - Set AD7768-1 power mode
     - Change the :adi:`AD7768-1` to Low, Median, or Fast. Low power mode is
       recommended.
   * - 4
     - Set AD7768-1 MCLK clock divider
     - Change the :adi:`AD7768-1` clock divider to /16, /8, /4, or /2. /16 is
       recommended.
   * - 5
     - Set AD7768-1 filter type
     - Change the :adi:`AD7768-1` filter type used. Also allows the
       oversampling ratio to be changed. Recommended is the Low ripple FIR
       Filter, oversampled by 32.
   * - 6
     - Set AD7768-1 AIN buffers
     - Adjust the :adi:`AD7768-1` buffers for both AIN+ and AIN-. It is
       recommended to turn on both AIN+ and AIN- precharge buffers.
   * - 7
     - Set AD7768-1 REF buffers
     - Adjust the :adi:`AD7768-1` buffers for both REF+ and REF-. It is
       recommended to turn on both REF+ and REF- precharge REF buffers.
   * - 8
     - Set AD7768-1 VCM output
     - Choose the :adi:`AD7768-1` VCM output voltage. Recommended is
       (AVDD1 - AVSS)/2.
   * - 9
     - Set AD7768-1 data output mode
     - Set the :adi:`AD7768-1` data output mode.
   * - 10
     - Set AD7768-1 diagnostic mode
     - Change which diagnostic mode is used for the ADC.
   * - 11
     - Set AD7768-1 Gains and Offsets
     - Set :adi:`AD7768-1` Gain and Offset registers.
   * - 12
     - Read AD7768-1 master status
     - Shows faults in :adi:`AD7768-1` master status register, allowing the
       user to pinpoint the source of problems.
   * - 13
     - Read AD7768-1 desired register
     - Reads a desired :adi:`AD7768-1` register.
   * - 14
     - Read AD7768-1 data register
     - Reads the :adi:`AD7768-1` data register.
   * - 15
     - Read AD7768-1 continuous mode data
     - Reads raw data from the ADC over a user-defined number of samples.
   * - 16
     - Print AD7768-1 continuous mode measured data
     - Prints previously read raw data converted into voltages, codes, and
       read raw data to the terminal. Logging the terminal will allow the user
       to extract this data. Requires the "Read data" command to have been run.
   * - 17
     - AD7768-1 Scratchpad Check
     - Input an 8-bit number; if it is returned, the ADC is interfacing with
       the software. This is a useful quick check for debugging and is good to
       run after setup.
   * - 18
     - Reset AD7768-1 ADC
     - Resets the ADC, either a soft reset over SPI or hard reset using the
       reset pin.
   * - 19
     - Set to Board Default Config
     - Set the board to default configurations.
   * - 20
     - Update Vref and MCLK values
     - Update the Vref and MCLK values.
