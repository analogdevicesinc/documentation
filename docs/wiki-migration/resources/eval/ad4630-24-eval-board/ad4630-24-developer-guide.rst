AD463x and AD403x Developer's Guide
===================================

Overview
--------

| The :adi:`ad4630-24` and :adi:`ad4030-24` are part of a family of 16 and 24-bit SAR analog-to-digital converters that support sampling rates of 2 MSPS and 500 kSPS. This family of ADCs offers market-leading linearity and noise performance, enabling an evolution in the performance of ATE, electronic test and measurement, health care and scientific instrumentation systems. The evaluation boards that support these converters have been designed to work with off-the-shelf 3rd party system boards that can be used to manage the data capture process as well as host embedded applications development.
| This developer's guide contains information and resource links that are intended to support users that desire to develop a custom application using the `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_. The DUT board may be either the evaluation board for the AD463x/AD403x, or a board that the user has designed. The only requirements for the user designed board are:
| 1. The board should have an FMC connector.
| 2. The digital interface through the FMC connector should use the same pin and signal assignments used on the EVAL-AD4630-24FMCZ/EVAL-AD4030-24FMCZ board (see :adi:`EVAL-AD4630-24 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-24.html#eb-documentation>` / :adi:`EVAL-AD4030-24 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4030-24.html>` for schematics). Otherwise, changing these assignments will require a modification of the HDL and a recompile. ADI provides the source files for the FPGA HDL, but it cannot support debug of the user modifications to the source.
| 3. It is recommended that the board provide a reference clock (100 MHz or less, see the :doc:`EVAL-AD4630-24FMCZ User Guide </wiki-migration/resources/eval/ad4630-24-eval-board>` for more information on the reference clock requirements.
| 4. It is recommended to derive the digital IO voltage from the ZedBoard. The EVAL-AD4630-24FMCZ schematics provide an example of this.
| 5. Optional: The ZedBoard provides a 12 volt supply rail through the FMC connector which can be used to provide the main power supply for the user board. However, the latter may also be powered from a separate external supply.

The user should consult the relevant EVAL-AD463x/EVAL-AD403x eval board user guide to access the basic details of the evaluation board hardware. The evaluation board schematics can be downloaded from the relevant evaluation board web page.

Supported Platforms
~~~~~~~~~~~~~~~~~~~

ZedBoard
--------

| The AD463x/AD403x family uses the Digilent ZedBoard as the default system controller. The `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_ web page contains more technical documentation on the board. In addition to the ZedBoard, other 3rd party boards that have an FMC form factor may also be used with the AD463x/AD403x family of boards. As an example, see Arrow's `DataStorm DAQ <https://www.arrow.com/en/products/datastormdaq/trenz-electronic-gmbh>`_, which uses the Intel Cyclone V SoC.
| |image1| |image2|
| \*\* Figure 1. ZedBoard (EVAL-AD463x/AD4030x system board) \*\*

While ADI provides software that runs within the Linux environment on the ZedBoard, it also offers device drivers that can be used with other system boards, with or without an RTOS. These options will be covered in the **Software** section below.

Basic HW and SW Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware
--------

The AD463x evaluation board connects to the ZedBoard through an FMC connector. This connector hosts the following signal groups

-  The digital interface between the ADC and the host processor (SoC).
-  The digital I/O power supply rail.
-  12V power from the ZedBoard to the evaluation board.
-  A high speed system clock used by the SoC, sourced on the evaluation board.

The ZedBoard hosts a Xilinx Zynq7000 class SoC with dual ARM Cortex-9 hard processors and FPGA fabric. The board boots from an SD card that is shipped with each evaluation board. The **Software** section below provides more information on the software that is provided with the evaluation system.

Software
--------

| Two use cases are supported for developing a custom application using the EVAL-AD463x system. They are basically distinguished by the nature of the host processor for the ADC. ADI provides software components that support both use cases. The following table summarizes the use cases and ADI software components.
| **Table 1. Use cases and supporting SW components**

+-----------------+-----------------------+----------------------------------------+
| Host processor  | Host Environment      | Available SW Components                |
+=================+=======================+========================================+
| SoC + FPGA      | Embedded Linux        | Linux image, Linux device drivers, HDL |
+-----------------+-----------------------+----------------------------------------+
| Microcontroller | Embedded RTOS/No RTOS | No OS drivers                          |
+-----------------+-----------------------+----------------------------------------+

| The **SD card** image that ships with the evaluation board contains multiple files that can be used to reconfigure the personality of the system to match one of the valid operating modes of the ADC. The /boot directory contains a Linux image (see below), a boot.bin file which contains the FPGA configuration (among other files), and a device tree file (device.dtb). The latter two files together define the operating configuration of the system. For most user-developed applications, the configuration files provided on the SD card, along with tools that can be used to set the desired configuration, are sufficient, meaning the user should not need to build a unique Linux image, rebuild HDL, or manually modify the devicetree.dtb file.
| The following paragraphs provide additional details on the nature of these files.

-  An ADI-maintained Kuiper **Linux** distribution (uImage). Currently, the version that is installed on the SD card is customized to support product evaluation and has features that enable compatibility with :adi:`ACE <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`. Like the standard Kuiper Linux image, it also includes IIO support, which consists of:

   -  **LibIIO subsystem** - a library of IIO functions that are used to create custom device drivers that run within the Linux system (see :doc:`LibIIO </wiki-migration/resources/tools-software/linux-software/libiio>` for more details). These drivers have already been generated for the AD463x/AD4030x and incorporated in the uImage file.
   -  **IIOD** - An IIO daemon that exposes IIO devices over a network connection to a remote host.

::

     (More information on the general Kuiper Linux distribution can be found at **[[/resources/tools-software/linux-software/kuiper-linux|ADI Kuiper Linux]]**
   * **Device tree file** that describes the attributes of the AD4630/AD4030 configuration. The attributes of the ADC node in the device tree set the clocking mode (SPI or Echo), data rate (single or dual edge), output data format (see data sheet), and number of active lanes per channel (1, 2, or 4). During boot, the system loads the device.dtb file contained in the boot directory. If the operating configuration of the ADC needs to be changed, the device tree must be updated with the new ADC attributes. Instructions for changing the operating configuration of the ADC and HDL are provided in a later section of this guide.  
   * **BOOT.BIN** files that are used to configure the FPGA. The default boot.bin file in the boot directory will correspond to a specific interface operating mode, distinguished by clocking mode (SPI vs. Echo), number of active lanes per channel (1, 2, or 4), and data rate (SDR vs. DDR). **The boot.bin must be synchronized to the ADC attributes in the device tree**. Unique boot.bin files have been pre-generated and stored on the SD card for several different configurations. Table 2 lists the available configurations (boot.bin files) that correspond to clocking modes, lanes, data rate mode. These files are available on the SD card in sub-directories that are labeled according to the configuration. This simplifies the HDL architecture and avoids the introduction of bugs due to unnecessary complexity.

| To change the ADC operating mode, two optional methods are available. See the section below entitled **How to Modify the SD Card Image**.
| **Table 2. BOOT.BIN partitioning for AD4630/AD4030 clocking modes, lane modes and data rates**

+---------------+-------------------------+--------------+--------------------------+
| Clocking Mode | Lane Mode (per channel) | Data Rate    | Requires unique BOOT.BIN |
+===============+=========================+==============+==========================+
| SPI           | 1                       | Single (SDR) | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               | 2                       | SDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               | 4                       | SDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+
| Echo Clock    | 1                       | SDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               |                         | Dual (DDR)   | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               | 2                       | SDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               |                         | DDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               | 4                       | SDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+
|               |                         | DDR          | X                        |
+---------------+-------------------------+--------------+--------------------------+

The following sections will specifically address the Linux driver, No-OS driver, and HDL for the AD463x family.

Linux Driver
~~~~~~~~~~~~

The user guide for the AD463x family Linux driver can be found here: :doc:`AD463x Linux Driver User Guide </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad463x>`. The user guide provides:

-  links to the driver source code and device tree;
-  an overview of the AD463x device tree options and their attributes;
-  examples of how to test the driver using console commands;
-  examples on how to directly access device registers for debug
-  Other links to resources that have more information on IIO usage.

HDL
~~~

The AD463x HDL user guide can be found here: :doc:`AD463x HDL User Guide </wiki-migration/resources/eval/user-guides/ad463x/hdl>`. The HDL user guide provides a high level description of the AD4630 HDL architecture, functionality, a link to the source file repository, and how to build a desired boot.bin configuration. Table 2 above lists all of the preconfigured modes, so in most cases it is not necessary for the user to build a unique boot.bin file. **Note:** The currently available boot.bin options only support **Zone 2 capture**, as this enables relaxed timing requirements for the interface. See the ADC data sheet for a description of Zone 2 capture.

No-OS Drivers
~~~~~~~~~~~~~

The No-OS driver can be used in a bare metal application or in a non-Linux RTOS environment. Some customization, or creation of an adaptation layer for the specific platform may be required. The :doc:`AD463x No-OS user guide </wiki-migration/resources/tools-software/uc-drivers/ad463x>` provides a general description of the driver, code documentation, and source code links.

How to Modify the SD Card Image for alternative operating configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users that are developing a custom application for the AD4630/AD4030 outside the ACE environment, using the ZedBoard running Linux, can modify the boot image to match one of the existing configurations listed in Table 2. Generating the appropriate boot image can be done using the method below. Once the ACE Environment method is executed, the boot directory on the SD card will retain the desired boot configuration until such time that the user performs another configuration update.

ACE Environment
---------------

The :doc:`AD4630/AD4030 Evaluation Board User Guide </wiki-migration/resources/eval/ad4030-24-eval-board>` contains instructions on how to change the operating configuration of the board using ACE. Note that this method assumes that the DUT board is the standard EVAL-AD4630-24FMCZ board (or AD4030-24 version), supported by an ACE plug-in. You can alter the configuration inside of the board view of the AD4630-24 ACE plugin, click apply, wait 30 seconds and the new configuration will load.

How to Re-image the SD card
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If SD card contents have been corrupted, or the user desires to create another copy of the SD card image, instructions on how to program the SD card with a replacement/new image can be found at :doc:`ADI Kuiper Linux with support for ACE </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`.

System Operational Constraints
==============================

Sampling Frequency
------------------

The following table illustrates the maximum sampling rates that can be achieved based on the device configuration. Note that the FPGA SPI engine only supports Zone 2 data transfers from the AD4630/AD4030.

\**Table 3. Maximum sampling rate by device configuration **^ Clocking Mode ^ Lane Mode (per channel) ^ Data Rate ^ Data format ^ Max sampling rate ^ \| SPI \| 1 \| Single (SDR) \| 32-bit \| 1.75 MSPS (**\ note 1\ **) \| \|     \|     \| SDR \| 24-bit \| 2 MSPS \| \|     \|     \| Dual (DDR) \| 32 or 24-bit \| 2 MSPS \| \|     \| 2 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \| \|     \| 4 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \| \| Echo Clock \| 1 \| SDR \| 32-bit \| 1.75 MSPS (**\ note 1\ **) \| \|     \|     \| SDR \| 24-bit \| 2 MSPS \| \|     \|     \| DDR \| 32 or 24-bit \| 2 MSPS \| \|     \| 2 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \| \|     \| 4 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \|**\ Note 1*\*: The sampling rate in Single lane, 32-bit output formats in SDR mode are limited by the FPGA SPI engine. This is not a limitation of the AD4630/AD4030 device.

Application Frameworks
======================

Python
------

PyADI-IIO is an ADI maintained Python library of device specific abstraction modules. Each device module supports the simplified development of Python applications that use IIO by providing an API that takes care of many of the underlying IIO details. This section of the developer's guide will describe information on using the PyADI bindings for the AD4630/AD4030 family.

Installation
------------

These instructions assume a fresh installation of all required software

-  Download `latest version <https://wiki.analog.com/https/www.python.org/downloads>`_ of python3. The Python downloader should recognize the host operating system and then download the appropriate installer. If downloading for a different machine select the Python installer accordingly. (Do not run installer yet)
-  Run the installer as Administrator. During installation, **check "Add Python 3.x,x to PATH" before clicking "Install Now"**

|image3|

-  Optional Python install: download and install a Python distribution such as `Anaconda <https://www.anaconda.com/products/distribution>`_. Ensure to select the proper Python version and host operating system. Recommended - install a Python editor (eg. `PyCharm <https://www.jetbrains.com/pycharm/download/#section=windows>`_ **community version**). One can also use `Spyder <https://wiki.analog.com/https/www.spyder-ide.org>`_ that comes with Anaconda.
-  Recommended - If using Anaconda, create a virtual environment for each project. Once the environment is created and activated, then:
-  Install **pyadi-iio**. If running Anaconda in Windows, run the Anaconda prompt and enter **pip install pyadi-iio**. Detailed py-adi installation guide can be found :doc:`here. </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
-  PyADI-IIO updates are published quarterly. It is recommended to run **pip** quarterly to get the latest updates.

Running the AD463x/AD403x example Python scripts
------------------------------------------------

| Generic examples for AD463x/AD403x are available in the :git-pyadi-iio:`source repo <examples/ad4630>`. The example code can be used for either AD4630-24 or AD4030-24 (and derivatives). Set the device_name parameter to ensure that channel operations are appropriately handled. Basic documentation can be found at `API documentation <https://analogdevicesinc.github.io/pyadi-iio/devices/>`_.
| Note that python does not automatically scan for usb context or an IP address unless a scan is embedded in the python script. If a ZedBoard is connected via an ethernet cable, then the argument passed in the ADC device instantiation statement is **uri="ip:analog.local"** which is the default host name for the ZedBoard (see code example below). If the default hostname of the board has been changed, this should be used instead. If using at USB connection to the board, then pass the IP address for the USB port (see code example for alternative USB connection below). The USB context/IP address can be read from the board by opening a terminal/command-prompt on the PC and entering:

::

   iio_info -s

.. image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/ad4630-scan-usb-context.jpg
   :width: 800px

As seen above, the USB argument can be either **"usb:1.17.6"**, or **"ip:169.254.26.1"** to instantiate the device.

The generic examples can be downloaded and executed, or custom code (see below) can be created.

.. code:: python

   # Import library
   import adi

   # Setup actual device from ad463x family
   device_name = "ad4630-24"  #  

   #Instantiate ADC if using Ethernet connection
   adc = adi.ad4630(uri="ip:analog.local", device_name=device_name)
   #ADC instantiation if using USB
   #adc = adi.ad4630(uri="usb:1.17.6", device_name=device_name)
   # To connect via USB 

   # Configure properties
   adc.rx_buffer_size = 2**12  # Rx Buffer Size
   adc.sample_rate = 2000000  # Sampling Frequency

   # Get data
   data = adc.rx()

Troubleshooting
===============

A troubleshooting guide can be found :doc:`here </wiki-migration/resources/tools-software/linux-software/adi-kuiper_ace_troubleshooting>`. The latter covers some tips related to ZedBoard startup and the SD card containing the Kuiper Linux image.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/zedboard_image-top.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/zedboard_image-bottom.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/ad4630-python-installation.png
   :width: 800px
