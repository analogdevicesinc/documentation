FMC-IMAGEON Xilinx Reference Design
===================================

|

.. warning::

   \ **NOTE:**

   | Support for the fmc-imageon is discontinued starting with 2022_r2 Kuiper Linux release and it will not be supported in future releases. Last Kuiper Linux release that contains pre-build files is 2021_r2. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases. The HDL project source code can still be found on :git-hdl:`hdl_2021_r2 <projects/imageon>` release branch.


.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/imageon/index.html\


Introduction
------------

The `FMC-IMAGEON <https://products.avnet.com/shop/en/ema/kits-and-tools/development-kits/aes-fmc-imageon-v2000c-g-3074457345623596557/>`__ is a HDMI input/output FMC card that provides high definition video interface for Xilinx FPGAs. The HDMI input interface is implemented with the :adi:`ADV7611`, a 165MHz, 24bit pixel output, HDCP capable HDMI 1.4a receiver. The HDMI output interface is implemented with the :adi:`ADV7511`, a 225MHz, 36bit deep color, HDMI 1.4 transmitter. This reference design provides the video and audio interface between the FPGA and ADV7511/ADV7611 on board. The video uses a 16bit 422 YCbCr interface and the audio uses a single bit SPDIF interface in both directions.

Supported Devices
-----------------

-  `FMC-IMAGEON <https://products.avnet.com/shop/en/ema/kits-and-tools/development-kits/aes-fmc-imageon-v2000c-g-3074457345623596557/>`__

Supported Carriers
------------------

-  `ZedBoard <http://zedboard.org/product/zedboard>`__

Required Hardware
~~~~~~~~~~~~~~~~~

-  One of the supported carrier and FMC-IMAGEON boards.
-  HDMI Monitor (should be capable of supporting 1080p and/or 720p for the demo files).

Required Software
~~~~~~~~~~~~~~~~~

-  We upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.
-  A UART terminal (Tera Term/Hyperterminal), Baud rate 57600.

Using the reference design
--------------------------

Functional description
~~~~~~~~~~~~~~~~~~~~~~

Xilinx block diagram
^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/imageon_Xilinx.svg
   :alt: HDL Block Diagram
   :width: 800px

FMC-IMAGEON block diagram
^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/imageon_fmc_1.svg
   :alt: HDL Block Diagram
   :width: 600px

The reference design consists of two independent IP modules.

The video part consists of an AXI DMAC interface and the ADV7511/ADV7611 video interface. The video interface consists of a 16bit YCbCr 422 with embedded synchronization signals.

Video Transmit (DMA to HDMI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the transmit direction, the DMA streams frame data to this core. The internal buffers of this IP are small (1k) and do NOT buffer any frames as such. Additional resources may cause loss of synchronization due to DDR bandwidth requirements. The video core is capable of supporting any formats through a set of parameter registers (given below). The pixel clock is generated internal to the device and must be configured for the correct pixel frequency. It also allows a programmable color pattern for debug purposes. A zero to one transition on the enable bits trigger the corresponding action for HDMI enable and color pattern enable.

The reference design defaults to the 1080p video mode. Users may change the video settings by programming the video size registers. The core requires a corresponding pixel clock to generate the video. This clock must be generated externally.

Note that the pixel frequency for 1080p is 148.5MHz.

The reference design reads 24bits of RGB data from DDR and performs color space conversion (RGB to YCbCr) and down sampling (444 to 422). If bypassed, the lower 16bits of DDR data is passed to the HDMI interface as it is.

A color pattern register provides a quick check of any RGB values on the monitor. If enabled, the register data is used as the pixel data for the entire frame.

Video Receive (HDMI to DMA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the receive direction, the HDMI data is first decoded and the synchronization signals are generated. The core then streams video data to DMA. The internal buffers of this IP are small (1k) and do NOT buffer any frames as such. Additional resources may cause loss of synchronization due to DDR bandwidth requirements. The video core is capable of supporting any formats through a set of parameter registers (given below). The core runs at the pixel clock from ADV7611.

The core decodes the active video size from the received data and compares it against an expected video size. If they do not match, the core will NOT stream data to DMA to avoid possible lock up conditions in the DMA core due to byte length mismatches. Also, the reference design performs color space conversion (YCbCr to RGB) and up sampling (422 to 444). If bypassed, the lower 16bits of DDR data is passed to the DMA interface as it is.

Test pattern generators and monitors are provided at each interface and clock domain boundaries. The default configuration is in loop back mode with the HDMI interface acting as a direct pass through.

Audio
~~~~~

The audio part consists of an AXI DMAC interface and the ADV7511 spdif audio interface. The audio clock is derived from the bus clock. A programmable register (see below) controls the division factor. The audio data is read from the DDR as two 16bit words for the left and right channels. It is then transmitted on the SPDIF frame. The sample frequency and format may be controlled using the registers below. The reference design defaults to 48KHz.

Registers
~~~~~~~~~

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

.. include:: ../../docs/hdl/regmap.rst

Audio Registers (axi_spdif_tx)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
| QW Address\ :sup:`1`                           | Bits  | Default | Name         | Description                                                                         |
+================================================+=======+=========+==============+=====================================================================================+
| 0x00                                           | 23:20 | 0       | mode         | Sample format 0 to 8 (0-16bit, 8-24bit).                                            |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 15:8  | 0       | ratio        | Clock divider for the transmit frequency = bus_clock/(1+ratio).                     |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 1     | 0       | txdata       | Transmit data buffer enable (0x1) or disable (0x0).                                 |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 0     | 0       | txenable     | Transmitter enable (0x1) or disable (0x0).                                          |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
| 0x01                                           | 7:6   | 0       | frequency    | Sample frequency 0(44.1KHz), 1(48KHz), 2(32KHz) or 3(sample rate converter) (RO).   |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 3     | 0       | gstat        | Generation status original/commercially pre-recorded data (0x1) or none (0x0) (RO). |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 2     | 0       | pre-emphasis | Pre-emphasis 50/15s (0x1) or none (0x0) (RO).                                       |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 1     | 0       | copy         | Copy permitted (0x1) or inhibited (0x0) (RO).                                       |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
|                                                | 0     | 0       | audio        | Data format is non-audio (0x1) or audio (0x0) (RO).                                 |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+
| 1. For AXI-Lite byte addresses, multiply by 4. |       |         |              |                                                                                     |
+------------------------------------------------+-------+---------+--------------+-------------------------------------------------------------------------------------+

Using the ADV7511 Transmitter Library
-------------------------------------

The transmitter library is a collection of APIs that provide a consistent interface to ADV7511. The library is a software layer that sits between the application and the TX hardware. The library is intended to serve two purposes:

-  Provide the application with a set of APIs that can be used to configure HDMI TX hardware without the need for low-level register access. This makes the application portable across different revisions of the hardware and even across different hardware modules.
-  Provide basic services to aid the application in controlling the TX module, such as interrupt service routine, HDCP high-level control and status information.

The Demo project uses the ADV7511 Transmitter Library. The project is an example of how to:

-  Initialize the ADV7511 High-Definition Multimedia Interface (HDMI®) transmitter.
-  Check current AVR operating mode and depending on this result set the AV mute state.
-  Display an image and play a sound.

The project contains 2 components: the Demo project files and the ADV7511 Transmitter Library. All the components have to be downloaded from the links provided in the **Downloads** section.

Software Setup
~~~~~~~~~~~~~~

The **ADV7511 Transmitter Library Demo** contains a folder called **SDK_Workspace** which stores the Xilinx SDK project files needed to build the no-OS software and also the .bit files with the HDL design that must be programmed into the FPGA. These are the steps that need to be followed to recreate the software project:

-  Copy the **SDK_Workspace** folder on your PC. Make sure that the path where it is stored does not contain any spaces.
-  Copy the library file to the **SDK_Workspace/sw/lib** folder.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/lib_files.png
   :alt: Library file
   :width: 600px

-  Copy the library headers to the **SDK_Workspace/sw/inc** folder.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/inc_files.png
   :alt: Library headers
   :width: 600px

-  Copy the ADV7511 Transmitter Library Demo files to the **SDK_Workspace/sw/src** folder.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/src_files.png
   :alt: ADV7511 Transmitter Library Demo files
   :width: 600px

-  Open the Xilinx SDK. When the SDK starts it asks for a to provide a folder where to store the workspace. Any folder can be provided.
-  In the SDK select the **File->Import** menu option to import the software projects into the workspace.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/file_import.png
   :alt: Import Projects
   :width: 300px

-  In the *Import* window select the **General->Existing Projects into Workspace** option.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/existing_project_import.png
   :alt: Existing Projects Import
   :width: 300px

-  In the *Import Projects* window select the **SDK_Workspace** folder as root directory. After the root directory is chosen the projects that reside in that directory will appear in the *Projects* list. Press *Finish* to finalize the import process.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/projects_import.png
   :alt: Projects Import
   :width: 300px

-  The *Project Explorer* window now shows the projects that exist in the workspace and the files for each project. The SDK should automatically build the projects and the *Console* window will display the result of the build. If the build is not done automatically select the **Project->Build Automatically** menu option.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/fmc-imageon/project_explorer.png
   :alt: Project Explorer
   :width: 300px

Downloads
---------

**HDL Reference Designs:**

.. include:: ../../docs/hdl/downloads_insert.rst

| **ADV7511 Transmitter Library Demo Software**

.. admonition:: Download
   :class: download

   | \* \**ADV7511 Transmitter Library: \*\* https:*www.analog.com/media/en/dsp-hardware-software/software-modules/ADV7511_API_Library.exe
     \* \**ADV7511 Transmitter Library Demo files: \*\* https:*\ github.com/analogdevicesinc/no-OS/tree/adv7511_rework/projects/adv7511
   |

.. include:: ../../docs/hdl/downloads_insert.rst
