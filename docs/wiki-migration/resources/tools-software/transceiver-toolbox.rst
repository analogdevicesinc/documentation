Analog Devices Transceiver Toolbox For MATLAB and Simulink
==========================================================

ADI maintains a set of tools to model, interface, and target with ADI transceiver devices within MATLAB and Simulink. These are combined into single Toolbox which contains a set of Board Support Packages (BSP). The list of supported boards is provided :doc:`below </wiki-migration/resources/eval/user-guides/matlab_bsp>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the :git-TransceiverToolbox:`Transceiver Toolbox GitHub Release Page <releases>`. Download the latest mltbx file then open that file within MATLAB. Opening the file will automatically install the Toolbox, adding the necessary components to your MATLAB path. The "Analog Devices, Inc. Transceiver Toolbox" will appear in your `Add-Ons Explore <https://www.mathworks.com/help/matlab/matlab_env/manage-your-add-ons.html>`__ within MATLAB.

.. admonition:: Download
   :class: download

   
   -  :git-TransceiverToolbox:`Analog Devices Inc, Transceiver Toolbox Release Page <releases>`
   


To interface and stream data with hardware will require installation of :doc:`libiio </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>` and one of two Hardware Support Packages from MathWorks. The libiio library can be obtained on the `Github <http://github.com/analogdevicesinc/libiio>`__ page of the project.

Libiio Installers
~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  :git-libiio:`Installers and source for latest stable build <releases>`
   -  `Installer for latest nighty build (Windows 32-bit / 64-bit) <https://ci.appveyor.com/project/analogdevicesinc/libiio/build/artifacts?branch=master>`__ (may be unstable / buggy)
   


Installation of either:

.. admonition:: Download
   :class: download

   
   -  for releases after R2024a
   
      -  `SoC Blockset Support Package for AMD FPGA and SoC Devices <https://www.mathworks.com/matlabcentral/fileexchange/70616-soc-blockset-support-package-for-amd-fpga-and-soc-devices>`__
   
   -  For Releases R2023b and before:
   
      -  `Communications Toolbox Support Package for Xilinx Zynq-Based Radio <https://www.mathworks.com/matlabcentral/fileexchange/48491-communications-toolbox-support-package-for-xilinx-zynq-based-radio>`__
      -  `Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <https://www.mathworks.com/help/supportpkg/plutoradio/index.html>`__
   


is required to use the streaming system objects or blocks. These support packages provide the necessary libIIO MATLAB bindings used by ADI's system objects. Starting in R2024a, the functionality of Communications Toolbox Support Package for Xilinx Zynq-Based Radio is included in SoC Blockset Support Package for AMD Devices.

Toolbox Dependencies
^^^^^^^^^^^^^^^^^^^^

Depending on your needs, different toolboxes will be required. For basic data streaming into MATLAB or Simulink only the following MathWorks toolboxes are required:

-  `Communications Toolbox <https://www.mathworks.com/products/communications/>`__
-  `DSP System Toolbox <https://www.mathworks.com/products/dsp-system/>`__
-  `Signal Processing Toolbox <https://www.mathworks.com/products/signal/>`__
-  `SoC Blockset <https://www.mathworks.com/products/soc.html>`__
-  `SoC Blockset Support Package for AMD FPGA and SoC Devices (FREE) <https://www.mathworks.com/matlabcentral/fileexchange/70616-soc-blockset-support-package-for-amd-fpga-and-soc-devices>`__

For HDL code generation the following are required:

-  `HDL-Coder <https://www.mathworks.com/products/hdl-coder>`__
-  `Xilinx Zynq Support from HDL Coder (FREE) <https://www.mathworks.com/hardware-support/zynq-hdl-coder>`__

Specific demos may require other toolboxes:

-  :doc:`QPSK Modem </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`
-  :doc:`Frequency Hopping </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/tutorials/frequency_hopping>`
-  :doc:`Loopback Delay Estimation </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/tutorials/loopback_delay_estimation>`
-  :doc:`ADALM-PLUTO LTE App </wiki-migration/resources/tools-software/transceiver-toolbox/examples/pluto_lte_app>`

Models of different transceivers may require different toolboxes as well. More information can be found :doc:`at the RF Blockset Model of AD9361 from MathWorks page </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`.

API Documentation
^^^^^^^^^^^^^^^^^

.. tip::

   \ `Latest Transceiver Toolbox API doc <https://analogdevicesinc.github.io/TransceiverToolbox/master/>`__\


Building the Toolbox Manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The toolbox can only be built under Linux or with Cygwin on a Windows platform. Conveniently, the entire process is automated with a Makefile located in the CI/scripts folder of the repository. The following is required on the system before the build process can be run:

-  A supported MATLAB version installed in the default location (/usr/local/MATLAB)
-  A supported Vivado version installed in the default location (/opt/Xilinx)
-  Packages: git zip unzip tar make wget sed

.. warning::

   You should only manually build the toolbox if you require a custom branch or no toolbox installer is available


First clone the repo and move into it:

::

   git clone --recurse-submodules https://github.com/analogdevicesinc/TransceiverToolbox.git
   cd TransceiverToolbox

To build the toolbox run the following:

::

   make -C CI/scripts build

Add the application libraries for AD936X based devices if desired

::

   make -C CI/scripts add_libad9361

To create a installable tlbx file run:

::

   make -C CI/scripts gen_tlbx

Running Integrated HDL Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This process assumes the toolbox has been built. To run tests for a specific carrier run the **test** target with the carrier name like so:

::

   make -C CI/scripts test BOARD=zed

Without specifying the carrier all tests will run (This takes a long time!):

::

   make -C CI/scripts test

Device Control and Data Streaming
---------------------------------

Device interfaces which provide control and data streaming are implemented with MATLAB System Objects and Simulink Blocks. These System Objects can be access under the "adi" namespace in MATLAB and are followed by their part number or board name and finally Tx or Rx:

::

   adi.<Part or Board Name>.<Tx or Rx>

For example, to instantiate an AD9361 object to control the Tx aspects of the transceiver it can be created as follows:

::

   tx = adi.AD9361.Tx;

All supported boards are derived from low level objects based on their parts. For example, the DAQ2 Evaluation board actually contains an AD9680 and AD9144. Therefore, it simply uses AD9680 and AD9144 objects under the hood. However, to interact with the more familiar DAQ2 interface naming the Rx side can be instantiated like above as:

::

   rx = adi.DAQ2.Rx;

For example usage of certain objects, it can be useful to inspect their related test code which exercises initiations in different configurations. The available code is available in the GitHub repo folder :git-MathWorks_tools:`here <test>`, where object tests have the naming convention <Object>Tests.m.

To get a list of currently available objects with the BSP installed simply run:

::

   help adi

To get more information on a given object run:

::

   help adi.<Part of Board Name>.<Tx or Rx>

or

::

   doc adi.<Part of Board Name>.<Tx or Rx>

Common Attributes
^^^^^^^^^^^^^^^^^

There are some common attributes that need to be set for system objects and parts.

-  ``uri`` Context address of IIO device. Possible options include:

   -  IP with usage ''rx.uri = 'ip:192.168.2.1' ''
   -  USB with usage ''rx.uri = 'usb:1.2.3' ''

Extending Interfaces
^^^^^^^^^^^^^^^^^^^^

If a driver attribute or setting is not available in the standard objects it can be easily extended to cover more IIO attributes. See this :doc:`guide </wiki-migration/resources/eval/user-guides/matlab_bsp_extend>`.

HDL Targeting with HDL-Coder
----------------------------

“\ *Targeting*\ ” is code generation that translates a designated MATLAB or Simulink subsystem to HDL code and creates a custom bitstream for the FPGA fabric. This custom bitstream is then downloaded to the FPGA on the development board. By moving part or all of your algorithm to the hardware, you speed up signal processing.

The Analog Devices Toolbox for MathWorks HDL Workflow Advisor is a collection of board definitions and reference designs that provide to the MathWorks HDL Workflow Advisor support to:

-  Generate IP blocks compatible with Analog Devices HDL reference designs for various Analog Devices platforms
-  Automatically insert the generated IPs into the Analog Devices Vivado HDL reference designs

This Analog Devices Toolbox is based on the `MathWorks Board and Reference Design Registration System <https://www.mathworks.com/help/hdlcoder/ug/board-and-reference-design-system.html>`__.

Functionality
^^^^^^^^^^^^^

The `MathWorks HDL Workflow Advisor <https://www.mathworks.com/help/hdlcoder/examples/getting-started-with-hardware-software-codesign-workflow-for-xilinx-zynq-platform.html>`__ enables users to automatically generate HDL code from a Simulink model. The user can choose from a selection of several different Target Workflows, including “ASIC/FPGA”, “FPGA-In-The-Loop”, and “IP Core Generation”. Target Platform selections include Xilinx Evaluation Boards and Altera Evaluation Boards as well as other custom evaluation boards.

The Analog Devices BSP for HDL Workflow Advisor extends the set of Target Workflows for IP Core Generation with the Analog Devices boards listed in the *Supported Platforms* section. The BSP consists of a set of board definitions that specify all the characteristics needed by the HDL Workflow Advisor to be able to incorporate a board in the code generation flow, as well as a set of Xilinx Vivado reference designs that are used by the Workflow Advisor to automatically insert the generated IPs into the Vivado designs. All the Analog Devices Vivado HDL reference designs have inside a ‘donut hole’ to accommodate custom IPs. Each design exposes a set of interface signals to which the IP can connect to. All these signals are specified in the board definition and are available in the Workflow Advisor GUI to connect to the generated IP’s ports.

When running the Workflow Advisor the first step if to select the Target Platform. The figure below shows some of the available Analog Devices target platforms.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/adi_bsps.png
   :alt: Analog Devices Target Platforms
   :align: center
   :width: 600px

The next step is to configure the interfaces between the IP and the reference design. Each target platform has a set of interface signals that are accessible in the *Target Platform Interfaces* drop down boxes form step 1.2 (Set Target Interface) of the HDL Workflow Advisor. The figure below shows an example of how to configure the target interface for a specific model.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/board_interface.png
   :alt: Target Interface Signals
   :align: center
   :width: 600px

All the Analog Devices AD9361 based SDR platforms have the same interface signals and they are dependent on the type of flow that is selected – receive (Rx) or transmit (Tx). The table below describes the interface signals for the AD9361 based SDR platforms.

Receive flow (Rx)
~~~~~~~~~~~~~~~~~

+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signal name        | Width | Description                                                                                                                                                       |
+====================+=======+===================================================================================================================================================================+
| IP Data 0 OUT      | 16    | Custom IP data output signal. This signal is connected to a DMA channel in the ADI reference design.                                                              |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IP Data 1 OUT      | 16    | Custom IP data output signal. This signal is connected to a DMA channel in the ADI reference design.                                                              |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IP Data 2 OUT      | 16    | Custom IP data output signal. This signal is connected to a DMA channel in the ADI reference design.                                                              |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IP Data 3 OUT      | 16    | Custom IP data output signal. This signal is connected to a DMA channel in the ADI reference design.                                                              |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IP Data Valid OUT  | 1     | Data valid signal from the custom IP. Used to signal to the rest of the design that the IP data out channels have valid data. The duration must be 1 clock cycle. |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 ADC Data I0 | 16    | AD9361 ADC I0 channel data.                                                                                                                                       |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 ADC Data Q0 | 16    | AD9361 ADC Q0 channel data.                                                                                                                                       |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 ADC Data I1 | 16    | AD9361 ADC I1 channel data.                                                                                                                                       |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 ADC Data Q1 | 16    | AD9361 ADC Q1 channel data.                                                                                                                                       |
+--------------------+-------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Transmit flow (Tx)
~~~~~~~~~~~~~~~~~~

+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| Interface signal name | Width | Description                                                                                                                           |
+=======================+=======+=======================================================================================================================================+
| IP Data 0 IN          | 16    | Custom IP data input signal. This signal is connected to a DMA channel in the ADI reference design.                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| IP Data 1 IN          | 16    | Custom IP data input signal. This signal is connected to a DMA channel in the ADI reference design.                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| IP Data 2 IN          | 16    | Custom IP data input signal. This signal is connected to a DMA channel in the ADI reference design.                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| IP Data 3 IN          | 16    | Custom IP data input signal. This signal is connected to a DMA channel in the ADI reference design.                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| IP Load Tx Data OUT   | 1     | Custom IP output signal used to notify the design that the IP is ready to receive new input data. The duration must be 1 clock cycle. |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 DAC Data I0    | 16    | AD9361 DAC I0 channel data. To be used as input into the custom IP.                                                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 DAC Data Q0    | 16    | AD9361 DAC I0 channel data. To be used as input into the custom IP.                                                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 DAC Data I1    | 16    | AD9361 DAC I0 channel data. To be used as input into the custom IP.                                                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+
| AD9361 DAC Data Q1    | 16    | AD9361 DAC I0 channel data. To be used as input into the custom IP.                                                                   |
+-----------------------+-------+---------------------------------------------------------------------------------------------------------------------------------------+

The custom IP always runs at the sample clock and must be able to process / generate a sample every clock cycle.

Once the target interface has been defined, make sure to select the "Target Language" as Verilog (defaults to VHDL) in Step 3.1.1 of the HDL Workflow Advisor. All the other settings of steps 2 and 3 of the HDL Workflow Advisor can be left in their default state and the project generation process can be started by running step 4.1 (Create Project). The result of this step is a Vivado project which has the custom IP core integrated into the Analog Devices HDL reference design. The bistream for the design can be generated either by running step 4.4 (Create bistream) or by compiling the generated Vivado Project directly in Vivado. The project can be found in the *hdl_prj/vivado_ip_prj* folder.

Further Reading
~~~~~~~~~~~~~~~

:adi:`Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio - Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Creating a BOOT.BIN from HDL Workflow Advisor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlike the support package provided by MathWorks, the update process for the bitstreams requires creation of a BOOT.BIN file which will be compatible with the ADI SD card.

First make sure you have a valid SD card for your platform with the necessary devicetree and kernel image selected. :doc:`Follow this process here </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.

Once your SD card is ready, in step 4.3 "Build FPGA Bitstream" of HDL Workflow Advisor select a custom Tcl file for synthesis build. Utilize this :git-TransceiverToolbox:`CI/scripts/adi_build.tcl` file located within the BSP as your custom tcl file.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/hwa_custom.png
   :align: center
   :width: 600px

Once the bitstream is built it will generate the BOOT.BIN necessary for booting your system. Place the generated BOOT.BIN in the root of your ADI SD card's BOOT partition.

Simulation Models of Hardware
-----------------------------

“Models” are typically used primarily in simulation only types of environments (they don't include any connection to hardware at all). Models can include many different aspects of devices:

-  analog impairments (internal PLLs, mixers, LNA, gain stages, etc),
-  baseband impairments (ADC/DAC noise shaping, quantization, noise)
-  Digital Signal Processing impairments (the fixed and programmable DSP in the parts, quantization, overflow, latency, filtering, etc).

Some models may include all three aspects, some may only include one. It's very common that as the model is of higher fidelity (includes more impairments, more details to be modeled) it runs slower. The fidelity vs simulation speed is always traded off by the model developer.

Some models are "complete" models, were developed and maintained by MathWorks, outside of ADI's transceiver toolbox:

-  `ad9361-models.html <https://www.mathworks.com/help/simrf/ug/ad9361-models.html>`__
-  `ad9371-models.html <https://www.mathworks.com/help/simrf/ug/ad9371-models.html>`__

Supported Boards
----------------

The following have device-specific implementations in MATLAB and Simulink. If a device has an IIO driver, MATLAB support is possible, but a device-specific MATLAB or Simulink interface may not exist yet.

+-----------------+--------------+-------------------+-----------+----------------------------------------+
| Evaluation Card | FPGA Board   | Streaming Support | Targeting | Variants and Minimum Supported Release |
+=================+==============+===================+===========+========================================+
| Pluto           |              | Yes               | Yes       | ADI (2018b) MathWorks (2017a)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| FMComms2/3/4    | Zedboard     | Yes               | Yes       | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZC702        | Yes               | Yes       | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZC706        | Yes               | Yes       | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZCU102       | Yes               | Yes       | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| FMComms5        | ZCU102       | Yes               | No        | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZC702        | Yes               | Yes       | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZC706        | Yes               | Yes       | ADI (2018b) MathWorks (2014b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ARRADIO         | Arrow SoCKit | Yes               | No        | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ADRV9361-Z7035  |              | Yes               | Yes       | ADI (2018b) MathWorks (2015b)          |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ADRV9364-Z7020  |              | Yes               | Yes       | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ADRV9371/5      | ZC706        | Yes               | Yes       | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZCU102       | Yes               | Yes       | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZYNQ3        | Yes               | No        | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ADRV9002        | ZCU102       | Yes               | Yes       | ADI (2020a)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ADRV9009/8      | ZC706        | Yes               | Yes       | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| :::             | ZCU102       | Yes               | Yes       | ADI (2018b)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| ADRV9009-ZU11EG |              | Yes               | No        | ADI (2020a)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+
| FMComms8        | ZCU102       | Yes               | Yes       | ADI (2021a)                            |
+-----------------+--------------+-------------------+-----------+----------------------------------------+

Examples
--------

Examples for streaming data and targeting FPGAs are listed within the Toolbox documentation itself. To view run the following with MATLAB:

::

   doc adi

They can also be viewed on GitHub:

-  :git-TransceiverToolbox:`Targeting examples <trx_examples/targeting>`
-  :git-TransceiverToolbox:`Streaming examples <trx_examples/streaming>`

Highlighted demos:

-  :doc:`Frequency hopping </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/tutorials/frequency_hopping>`
-  :doc:`Loopback delay estimation </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/tutorials/loopback_delay_estimation>`
-  :doc:`AGC Optimization </wiki-migration/resources/eval/user-guides/ad9361_agc_tuning>`

Help & Support
--------------

.. hint::

   
   -  Questions? :doc:`Ask Help & Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.
   


Common Issues
-------------

libad9361-iio pathing error:

::

   Error using loadlibrary
   Could not find file ad9361-wrapper.h.
   Error in loadlibrary
   Error in adi.AD9361.Base/setupLibad9361 (line 111)
                   [~, ~] = loadlibrary(libName, loadlibraryArgs{:});
   Error in adi.AD9361.Rx/setupInit (line 281)
               setupLibad9361(obj);
   Error in adi.common.RxTx/configureChanBuffers (line 226)
               setupInit(obj);
   Error in matlabshared.libiio.base/setupImpl
   Error in adi.common.RxTx/setupImpl (line 124)
               setupImpl@matlabshared.libiio.base(obj);

This error occurs when libad9361-iio is not on the MATLAB path. To fix it run the following within MATLAB:

::

   A = adi.utils.libad9361
   A.download_libad9361
