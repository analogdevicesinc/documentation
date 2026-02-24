.. _ad-quadmxfe1-ebz-quickbringup:

Quad-MxFE Quick Start Guide
=============================

.. _quadmxfe-equipment-needed:

Equipment Needed
----------------

Equipment Included with Quad MxFE Kits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 1x :adi:`ADQUADMXFE1EBZ Quad-MxFE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>` instructions card
- 1x 12V, 9A+ Wall Supply and power cable
- 2x MMCX-to-SMA cables. Used to test with equipment
- 1x FMC+ Extender
- 2x 6" MMCX-to-MMCX cables
- 3x Board Standoffs
- 4x Fan/Heat Sinks --- **Install Prior to First Use Per**
  :ref:`Fan Installation Directions <quadmxfe-thermal-considerations>`

.. tip::

   See unboxing video here:
   :adi:`Quad MxFE Unboxing Video <en/education/education-library/videos/6257116746001.html>`

Equipment Included with Calibration Board Kits (ADQUADMXFE-CAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 1x :doc:`ADQUADMXFE-CAL Calibration Board <calboard>` instructions card
- 1x 12V, 9A+ Wall Supply and power cable
- 2x 3" MMCX-MMCX cables. Used to connect between Quad MxFE Board &
  Calibration Board

  - NOTE that you will need to purchase an additional 30 of these to interface
    to the Calibration Board/Quad MxFE board

- 4x Board Standoffs
- 1x PMOD ribbon cable
- 1x Male to male 0.1" 12 pin header for PMOD cable

.. tip::

   See unboxing video here:
   :adi:`Calibration Board Unboxing <en/education/education-library/videos/6257116696001.html>`

Required Additional Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 1x 500 MHz Reference Oscillator or Waveform Generator
- 1x Ethernet Cable
- 1x USB to Ethernet Dongle
- 2x USB Micro Cables
- 50 Ohm SMA Cables --- As Needed
- 32x MMCX-MMCX cables (2 are provided with the ADQUADMXFE-CAL kit). Used to
  connect between Quad MxFE Board & Calibration Board
- 1x Fan
- 1x :xilinx:`VCU118 FPGA Board <products/boards-and-kits/vcu118.html>`

.. warning::

   Do not use the Ethernet cable that comes with the VCU118 board. It is a
   crossover cable and will not work with the platform.

Optional, But Helpful Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 1x :doc:`ADQUADMXFE-CAL 16Tx/16Rx Calibration Board <calboard>` (Optional,
  Sold Separately) --- Includes Power, PMOD Cabling, & Board Standoffs

Test Setup
~~~~~~~~~~

.. figure:: quadmxfe/qmxfe_quadmxfeinterconnectivitydiagram.png
   :align: center

   Quad-MxFE interconnectivity diagram

.. _quadmxfe-software-needed:

Software Needed
---------------

- :ref:`Supported Use Cases / Bitstreams Available For Download <quadmxfe-downloads>`
- :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`

  - `Latest IIO Oscilloscope release <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__
  - `Latest Libiio release <https://github.com/analogdevicesinc/libiio/releases>`__

- `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`__
- :xilinx:`Xilinx Vivado Toolchain <support/download.html>`
- MATLAB (Optional)

HDL/Image
~~~~~~~~~

The required FPGA files and ``.tcl`` scripts can be downloaded from
:ref:`the downloads section <quadmxfe-downloads>`.

Once downloaded, unzip these files to a folder on the desktop called QuadMxFE
(this directory will be used in XSCT).

IIO Oscilloscope / LibIIO
~~~~~~~~~~~~~~~~~~~~~~~~~~

The main IIO interface is provided in the install of IIO Oscilloscope which uses
LibIIO to communicate through IIO to the chips on the Quad MxFE board. The
install process for IIO Oscilloscope and a walkthrough of opening the program can
be found in the :doc:`Software Quick Start Guide <quick_start>`.

PuTTY
~~~~~

PuTTY helps to provide a view into the Linux and give additional controls and
debug abilities. PuTTY can be downloaded from the
`PuTTY Download Page <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`__.
Ensure that the proper version for the computer is downloaded.

Once downloaded the COM port to the FPGA can be opened. This COM port can be
identified through the device manager:

.. image:: comport.png
   :align: center

In PuTTY, this should be opened with a baudrate of 115200:

.. image:: putty_comport.png
   :align: center

Xilinx Software Command Line Tool (XSCT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to program the FPGA, the Vitis/Vivado tool suite is required:
:xilinx:`Vivado Toolchain <support/download.html>`.

.. warning::

   Make sure to grab Vitis 2020.2 or earlier. The 2020.3 version does not
   support the VCU118.

Grab the Self Extracting Web Installer from the full product installation
section and run the installer. Choose the Vitis installation option which will
include the Vivado install.

.. image:: quadmxfe/vitis_install.png
   :align: center

The main tool used for programming the FPGA is the Xilinx Software Command Line
Tool, included as part of the installation of the Xilinx Vitis platform.

.. code-block::

   xsct% cd Desktop/Quad_Mxfe_Files
   xsct% source run.vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.tcl

MATLAB 2019b or 2020a (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MATLAB 2020a is the primary version that all the code is tested with.

.. warning::

   MATLAB 2020b IS NOT SUPPORTED.

MATLAB is used to exercise the board through LibIIO objects and provide higher
level application functionality. Required toolboxes:

#. MATLAB Communications Toolbox
#. DSP System Toolbox
#. Signal Processing Toolbox
#. Curve Fitting Toolbox
#. Instrument Control Toolbox
#. Communications Toolbox Support Package for Xilinx Zynq-Based Radio (installed
   through MATLAB Add-On Explorer)
#. `Analog Devices High Speed Converter Toolbox <https://github.com/analogdevicesinc/HighSpeedConverterToolbox>`__

Quick Start Bringup with Hardware
---------------------------------

This section assumes the following:

#. Standoffs have been attached to Quad MxFE board
#. VCU118 and Quad MxFE have been attached via a FMC+ extender on the FMC+
#. Ethernet cable has been connected to VCU118 and connected to USB to Ethernet
#. USB to Ethernet dongle has IP address of ``192.168.2.5``. For locally
   connected FPGAs (i.e. Ethernet cable from VCU118 to USB to Ethernet dongle),
   the Hostname is ``192.168.2.1``.

   .. image:: usb_to_ethernet.png
      :align: center

#. 2x micro USB cables have been connected to PC and VCU118 for JTAG and Serial
#. All required software programs have been installed
#. All FPGA images/script files have been downloaded and unzipped to a folder on
   the Desktop called QuadMxFE
#. 500 MHz ~0 dBm source has been attached to Quad MxFE central clock input SMA
#. 12V power bricks (>8A for Quad MxFE and >5A for VCU118) have been connected
   to boards
#. Fans have been turned on

General Board Power Up/Programming Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power up sequence is not difficult:

#. Power up the 500 MHz oscillator
#. Power up the Quad MxFE Board
#. Power on the VCU118 board

Once these are powered up, program the FPGA:

#. Open PuTTY at the correct COM port and baudrate of 115200
#. Open Xilinx Command Line Tool (XSCT). Open it from the Start Menu under
   Xilinx > Xilinx Software Command Line Tool. Once the prompt is open, type:
   ``cd Desktop\QuadMxFE``
#. Run the loading script for the particular build by typing the following in
   XSCT:
   ``source run.vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.tcl``
#. Wait for the programming to finish in XSCT.

   .. image:: running_fpgaload.png
      :align: center

#. Wait for the build to boot completely by checking the PuTTY terminal window.
   Wait for the login prompt.

   .. image:: putty_quad_mxfe.png
      :align: center

   Login credentials: Username: ``root``, Password: ``analog``

#. At this point the FPGA has booted and all of the blue PLL lights should be
   illuminated. The FPGA is ready to be controlled from MATLAB or from IIO
   Oscilloscope.

.. _quadmxfe-matlab-control:

MATLAB Control Overview
-----------------------

The Quad-MxFE Platform can be controlled via MATLAB using example scripts which
are available as part of the
`Analog Devices, Inc. High Speed Converter Toolbox <https://github.com/analogdevicesinc/HighSpeedConverterToolbox>`__
add-on. This add-on can either be manually downloaded from the Releases section
of the GitHub page or downloaded and installed via MATLAB Add-On Explorer.

.. note::

   It is recommended to install via the download from GitHub as this is
   generally more up to date than the MATLAB Add-On Explorer page.

.. image:: quadmxfe/github.png
   :align: center

.. image:: quadmxfe/matlab_addon_xilinx_zynqbased_radio_communications_toolbox.png
   :align: center

Example scripts are located within the add-on install directory, which is usually
located in the
``C:\Users\<username>\AppData\Roaming\MathWorks\MATLAB Add-Ons\Toolboxes``
directory. The example scripts are specifically located in:
``Analog Devices, Inc. High-Speed Converter Toolbox\hsx_examples\qmxfe``

Controlling Quad-MxFE With MATLAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The control interface for the Quad-MxFE is implemented using standard system
objects in MATLAB. Here is an example instantiation of the objects:

.. code-block:: matlab

   tx = adi.QuadMxFE.Tx()
   rx = adi.QuadMxFE.Rx()

.. _quadmxfe-calboardvcu118:

CalBoardVCU118.m
~~~~~~~~~~~~~~~~

This folder also contains a driver file ``CalBoardVCU118.m`` for controlling the
optional :doc:`16 Tx / 16 Rx Calibration Board <calboard>` via the VCU118 PMOD
interface. This driver file allows the user to perform the following functions
after instantiation using ``CalibrationBoard = CalBoardVCU118``:

#. ``CalibrationBoard.ConfigureCombinedLoopback``: Loop Combined Tx Channels
   Back Into Combined Rx Path
#. ``CalibrationBoard.ConfigureAdjacentIndividualLoopback``: Loop Individual Tx
   Channels Back Into Adjacent Rx Path
#. ``CalibrationBoard.ConfigureTxOutSMA``: Send Combined Tx Channels Out
   ``J502`` SMA Connector
#. ``CalibrationBoard.ConfigureRxInFromSMA``: Send Combined Rx Input Into
   ``J501`` SMA Connector
#. ``CalibrationBoard.ConfigureTxOutToLTC5596``: Send Combined Tx Channel Signal
   Into LTC5596 Power Detector
#. ``CalibrationBoard.QueryAD8318_voltage``: Poll the AD8318 Power Detector
   Voltage
#. ``CalibrationBoard.QueryHMC948_voltage``: Poll the HMC948 Power Detector
   Voltage
#. ``CalibrationBoard.QueryLTC5596_voltage``: Poll the LTC5596 Power Detector
   Voltage

If the user intends to use the Calibration Board, then be sure to enable
``tx.CalibrationBoardAttached = 1`` and ``rx.CalibrationBoardAttached = 1``.

LoadVcu118Code.m
~~~~~~~~~~~~~~~~

For convenience, there is a function file ``LoadVcu118Code.m`` which allows the
user to load new .tcl files via the MATLAB interface.
``LoadVcu118Code(xsctpath,tclpath)`` --- first parameter: installed xsct.bat
folder; second parameter: downloaded .run.tcl file location.

.. _quadmxfe-simpletxrx:

QuadMxFE_SimpleTxRx.m
~~~~~~~~~~~~~~~~~~~~~~

The default test setup for this script uses the
:doc:`16Tx/16Rx Calibration Board <calboard>` as shown below in which each Tx
channel is looped back into the adjacent Rx channel after going through a 10 dB
attenuator.

.. figure:: quadmxfe/script_test_setup.png
   :align: center

   SimpleTxRx test setup

This script demonstrates relatively simple MATLAB control of the system. It
allows the user to configure the Tx and Rx aspects of the system by using the
``tx = adi.QuadMxFE.Tx`` and ``rx = adi.QuadMxFE.Rx`` system objects. The script
then loads transmit waveforms and captures receive data for all channels on the
system. **No Rx nor Tx calibration is performed, nor are any multi-chip
synchronization algorithms.**

.. figure:: quadmxfe/screenshot_quadmxfe_systemalignmentfir.png
   :align: center

   SimpleTxRx output example

Using this script as a basis, the user can:

#. Inject Custom Tx Waveforms: ``tx(waveformDataMatrix)``
#. Change Tx NCO Frequencies: e.g. ``tx.MainNCOFrequenciesChipA``
#. Change Tx NCO Phases: e.g. ``tx.MainNCOPhasesChipA``
#. Capture Simultaneous Complex-Valued Rx Data: ``rxData=rx()``
#. Change Rx NCO Frequencies: e.g. ``rx.MainNCOFrequenciesChipA``
#. Change On-Board DSA Value: ``rx.ExternalAttenuation``
#. Change Calibration Board Configuration
#. Perform MxFE Register Reads/Writes
#. Analyze and Post-Process Captured Waveforms

.. _quadmxfe-systemalignmentfir:

QuadMxFE_SystemAlignmentFIR.m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default test setup uses the :doc:`Calibration Board <calboard>` in combined
loopback mode.

.. warning::

   Once the pFIRs have been enabled through this script, they will remain on and
   will cause problems if other non pFIR scripts are run. Therefore a complete
   platform reboot is required between running the pFIR script followed by any
   other MATLAB script.

.. figure:: quadmxfe/script_test_setup_combined_loopback.png
   :align: center

   SystemAlignmentFIR test setup (combined loopback)

This script demonstrates MATLAB control of the programmable finite impulse
response (pFIR) filters and NCO phase offsets in order to phase align all Rx and
Tx channels in the system. It uses the on-system DSP blocks to phase-align the
:adi:`ADF4371` device clocks, then phase-aligns all Tx channels and loads a
broadband chirp waveform. It ends by also phase- and amplitude-aligning all Rx
RF channels using the NCO phase offsets and pFIRs assigned to each Rx channel.

**Figure 1**: PLL phase alignment results.

.. image:: quadmxfe/pll_phase_alignment_results.png
   :align: center

**Figure 2**: Tx pulse phase alignment results.

.. image:: quadmxfe/tx_pulse_phase_alignment.png
   :align: center

**Figure 3**: pFIR alignment results --- time domain ADC capture, chirp FFT,
and amplitude and phase errors before and after Rx calibration.

.. image:: quadmxfe/pfir_alignment_quadmxfe.png
   :align: center

**Figure 4**: Calculated error response of each Rx channel.

.. image:: quadmxfe/pfir_error_response_quadmxfe.png
   :align: center

**Figure 5**: Designed pFIR magnitude and phase response.

.. image:: quadmxfe/pfir_magnitude_phase_response_quadmxfe.png
   :align: center

**Figure 6**: Individual pFIR tap coefficients before and after quantization.

.. image:: quadmxfe/pfir_tap_coefficients_quadmxfe.png
   :align: center

**Figure 7**: Combined Rx system performance using a single-tone waveform after
all Rx channels are aligned.

.. image:: quadmxfe/combined_rx_improvements_quadmxfe.png
   :align: center

.. _quadmxfe-mcs-script:

QuadMxFE_MCS.m
~~~~~~~~~~~~~~

This script demonstrates MATLAB control of the multi-chip synchronization (MCS)
algorithm. It allows the user to configure the Tx and Rx aspects of the system,
load transmit waveforms, and capture receive data. The script uses on-system DSP
blocks to align the device clocks and output/input RF channels using the NCO
phase offsets. Finally, it plots the results and allows the user to save a .mat
file containing the run results.

The test setup is the same as that used for the QuadMxFE_SystemAlignmentFIR.m
script. More information on MCS can be found in the
:doc:`Multi-Chip Synchronization Guide <multichip_sync>`.

**Figure 1**: ADF4371 PLL/synthesizer calibration results.

.. image:: quadmxfe/mcs_1.jpg
   :align: center

**Figure 2**: Tx phase-alignment results using pulsed baseband waveform.

.. image:: quadmxfe/mcs_2.jpg
   :align: center

**Figure 4**: Full I/Q band chirp signal and CW signal results.

.. image:: quadmxfe/mcs_3.jpg
   :align: center

**Figure 5**: MCS results comparison between new and baseline NCO phase offsets.

.. image:: quadmxfe/mcs_4.jpg
   :align: center

.. _quadmxfe-adctodac-loopback:

QuadMxFE_ADCtoDAC_Loopback.m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Quad-MxFE Platform is capable of configuring each :adi:`AD9081` into a mode
such that the digitized ADC output can be sent through the DDCs and looped back
on-chip into the DUCs prior to being synthesized by the DACs. This allows the
user to bypass the JESD204c digital interface and therefore achieve a
low-latency loopback capability.

.. figure:: quadmxfe/qmxfe_mxfe_loopback_path.png
   :align: center

   MxFE loopback path

.. figure:: quadmxfe/qmxfe_script_test_setup_adctodac_loopback.png
   :align: center

   ADC-to-DAC loopback test setup

Debug
-----

No Blue Lights Visible on Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no blue lights are visible on the board, then the PLLs are not locked. The
most likely cause of this is the lack of a 500 MHz source into J41. Check the
input power and state of the source. It should be 500 MHz @ ~0 dBm. Once the
500 MHz signal is verified, the FPGA programming must be rerun.
