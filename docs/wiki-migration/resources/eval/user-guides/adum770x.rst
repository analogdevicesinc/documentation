ADuM7701 - Reference Design
===========================

Supported Devices
-----------------

-  :adi:`ADuM7701`
-  :adi:`AD7405`
-  :adi:`AD7403`

Supported Carrier Board
-----------------------

-  `Zedboard <http://zedboard.org/product/zedboard>`_

Overview
~~~~~~~~

The :adi:`ADuM7701` is a high performance, second-order, Σ-Δ modulator that converts an analog input signal into a high speed, single-bit data stream, with on-chip digital isolation based on Analog Devices, Inc., iCoupler® technology. The device operates from a 4.5 V to 5.5 V power supply range (VDD1) and accepts a pseudo differential input signal of ±250 mV (±320 mV full-scale). The pseudo differential input is ideally suited to shunt voltage monitoring in high voltage applications where galvanic isolation is required.

The analog input is continuously sampled by a high performance analog modulator and converted to a ones density digital output stream with a data rate of up to 21 MHz. The original information can be reconstructed with an appropriate sinc3 digital filter to achieve an 86 dB signal-to-noise ratio (SNR) at 78.1 kSPS with a 256 decimation rate and a 20 MHz master clock. The serial input and output operates from a 5 V or a 3 V supply (VDD2).

The serial interface is digitally isolated. High speed complementary metal-oxide semiconductor (CMOS) technology, combined with monolithic transformer technology, results in the on-chip isolation providing outstanding performance characteristics, superior to alternatives such as optocoupler devices. The :adi:`ADuM7701` device is available in both a 16-lead and an 8-lead wide-body SOIC and has an operating temperature range of −40°C to +125°C.

Applications
------------

-  Shunt current monitoring
-  AC motor controls
-  Power and solar inverters
-  Wind turbine inverters
-  Analog-to-digital and optoisolator replacements

HDL Reference Design
~~~~~~~~~~~~~~~~~~~~

The provided HDL reference design support's both the ADuM7701 and AD7405 devices. One of the main difference between thees two devices is the type of the digital data lines. In case of ADuM7701 it is a single ended lines, and in case of the AD7405 is differential.

User can configure the corresponding interface type, by setting the **adc_port_type** Tcl variable in the system_project.tcl file. Note that this variable should be set before generating any bit file.

The output of the device is a continuous digital bit stream, to reconstruct the original input signal information, this output bit stream needs to be digitally filtered and decimated. A simple |sinc filter| is recommended to reconstruct the original input signal information received from the ADuM7701. The following equation describes the transfer function of the sinc filter:

:math:`\displaystyle H(z) = (1/DR \frac{1-Z^-DR}{1 - Z^-1})^N`

where **DR** is the decimation rate and **N** is the sinc filter order. The implemented filter is a 3rd order sinc filter.

The output of the filter is connected to a DMA, which will handle the data transfer into the system memory. See the data path in block diagram bellow:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7405_data_path_1.png
   :alt: ADuM7701/AD7405 data path
   :align: center

The external clock rate (MCLKIN) can be set in the system_bd.tcl file, by changing the value of the **ext_clk_rate** variable.

Create the project with SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    * Open Xilinx Software Development Kit (XSDK) and provide the workspace location.

::

    * Create a new Application Project: go to **File -> New -> Application Project**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new_app_project.png
   :alt: Creating a new application project
   :align: center
   :width: 650px

::

    * Create a new Hardware Platform: click **New** from the **Target Hardware** section

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_new_hardware.png
   :alt: Creating a new hardware platform
   :align: center
   :width: 450px

::

    * Specify the already generated Hardware Platform Specification File (more details about the generation: :doc:`/wiki-migration/resources/fpga/docs/build`): in the **Target Hardware Specification** section browse the desired file

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_hw_project.png
   :alt: Import hardware description file
   :align: center
   :width: 450px

::

    * Give a name to the project and to the board support package and click **Next**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_app_project.png
   :alt: Application project settings
   :align: center
   :width: 450px

::

    * Select the **Empty Application** templeta and click **Finish**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/project_templates.png
   :alt: Choose application template
   :align: center
   :width: 450px

::

    * The new **Empty Application project** should look like:


    |Empty application project|

.. important::

   Some applications (e.g. FMCOMMSx), when a Microblaze processor is used, requires an increased HEAP size for dynamic memory allocation. Make sure the HEAP size is at least **0x100000**.


   |image1|

::

    * Copy the source code files into the **src** directory
    * Make sure you uncomment the the required carrier vendor and CPU architecture from the **app_config.h** (or **config.h**) header file.

-  Example for choosing the Altera carrier in the **app_config.h** header file:

::

   //#define XILINX
   #define ALTERA

::

    * If there are multiple folders present in in the src one, include all the paths of the folders: go to the settings of the project and in the **C/C++ Build -> Settings -> Tool Settings -> gcc compiler -> Directories** section and add the paths of all the folders.

::

    * The SDK should automatically build the projects and the Console window will display the result of the build. If the build is not done automatically select the **Project -> Build Automatically** menu option.
     
    * At this point the software project setup is complete, the FPGA can be programmed and the software can be downloaded into the system. You can program the FPGA by clicking on **Xilinx Tools -> Program FPGA** 

::

    * After the FPGA was programmed, we need to create a new Run configuration, by selecting **Run** -> **Run Configurations...**, in the Run Configuration windows select the Xilinx C/C++ application (System Debugger) and click at the **New Configuration** button at the upper left corner.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new_run_configurations.png
   :alt: Create new run configuration
   :align: center
   :width: 650px

::

    * If your target carrier has a Zync SoC, make sure, that you specify the **Initialization file**, and select the **Run ps7_init** and **Run ps7_post_config** options.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/zynq_init_file.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

    * At the **Application** tab define your current project name and application executable. (.elf)

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/elf_app.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

       * The output of the example program can be viewed in the SDK console by enabling the Connect STDIO Console option and setting the baud rate of the UART port to 115200.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/stdio_config.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

       * As an alternative a UART terminal can be used to capture the output of the example program. The number of used UART port depends on the computer's configuration. The following settings must be used in the UART terminal:
       * **Baud Rate:** 115200bps
       * **Data:** 8 bit
       * **Parity:** None
       * **Stop bits:** 1 bit
       * **Flow Control:** none

::

     * When the run configuration is done, the software can be started by clicking the **Run** button.

::

     * Your new bare metal application should run  

.. |Empty application project| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/empty_project.png
   :width: 650px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/ad9361_no_os_microblaze_heap_size.png


Driver Description
~~~~~~~~~~~~~~~~~~

Functions Declarations
----------------------

+--------------------------------------------------------------------------------+--------------------------------------------------+
| Function                                                                       | Description                                      |
+================================================================================+==================================================+
| ``int32_t adum7701_init(adum7701_dev **dev, adum7701_init_param init_param);`` | Initialize the device.                           |
+--------------------------------------------------------------------------------+--------------------------------------------------+
| ``int32_t adum7701_remove(adum7701_dev *dev);``                                | Free the resources allocated by adum7701_init(). |
+--------------------------------------------------------------------------------+--------------------------------------------------+

Types Declarations
------------------

+---------------------------------------+


| ``typedef struct {                    |

|         /* GPIO */                    |
|         gpio_desc *dec_ratio;         |
|         gpio_desc *filter_reset;      |
| } adum7701_dev;                       |
|                                       |
| typedef struct {                      |
|         /* GPIO */                    |
|         gpio_init_param dec_ratio;    |
|         gpio_init_param filter_reset; |
| } adum7701_init_param;``              |
+---------------------------------------+

Downloads
~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of ADuM7701 Driver.|

   -

   |Header file of ADuM7701 Driver.|

   -

   |No-OS Reference Design.|

   -

   |HDL Reference Design|

bbbbbbbb

.. |sinc filter| image:: https://wiki.analog.com/_media/:git-hdl:`library/common/util_dec256sinc24b`.v
.. |Implementation of ADuM7701 Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`adum7701_fmc/adum7701`.c
.. |Header file of ADuM7701 Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`adum7701_fmc/adum7701`.h
.. |No-OS Reference Design.| image:: https://wiki.analog.com/_media/:git-no-OS:`adum7701_fmc`
.. |HDL Reference Design| image:: https://wiki.analog.com/_media/:git-hdl:`tree/adum7701`
