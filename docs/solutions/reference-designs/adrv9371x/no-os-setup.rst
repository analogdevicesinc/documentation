AD9371/AD9375 No-OS Setup
=========================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD9371 mykonos
on:

-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `ZC706 <https://www.xilinx.com/ZC706>`_
-  `ZCU102 <https://www.xilinx.com/ZCU102>`_

Required Software
~~~~~~~~~~~~~~~~~

-  We're upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.

.. note::

   See `resources/eval/user-guides/mykonos/../../../../../resources/fpga/xilinx/software_setup <https://wiki.analog.com/resources/eval/user-guides/mykonos/../../../../../resources/fpga/xilinx/software_setup>`_

Files
~~~~~

-  **AD9371/AD9375 No-OS Software**

   -  Download from :git-no-OS:`projects/ad9371/src`

      -  Next copy the files intro the src folder of your newly created project.
         You can do this with Ctrl+C Ctrl+V or simple drag and drop

-  **API Source Code**

   -  Download from http://www.analog.com/en/design-center/landing-pages/001/transceiver-evaluation-software.html

      -  Unzip the archive and go into **src->api** folder
      -  Next copy the **ad9528** and **mykonos** folder to the **src** folder of your project. Do **NOT** copy the common.c and common.h files provided by the api. For now, use the ones downloaded from github.
      -  Make sure the paths for the directories are included. Right click on
         the src folder from Project Explorer and go to Properties -> C/C++
         Build -> Settings -> ARM v7 gcc compiler -> Directories

      |resources-eval-user-guides-mykonos-src_properties.jpg|

   * Click Add -> Workspace... ->ad9528

       .. image:: images/folder_selection.png

   * Repeat the procedure for mykonos, src and mykonos_debug. The included paths
     should look like this:

       .. image:: images/included_paths.png

   * Add the above folders also for **Configuration: Debug**

       .. image:: images/configuration_debug.png

-  **Transceiver Evaluation Software**

   -  Download from http://www.analog.com/en/design-center/landing-pages/001/transceiver-evaluation-software.html

      -  Next, generate the profile by using the :doc:`MATLAB Profile Generator </solutions/reference-designs/adrv9371x/software/filters>`. The profiles can be used with the **Transceiver Evaluation Software** to evaluate system performance.
      -  Further, import the profile into TES, and generate the Mykonos initialization structures which are used by the No-OS driver (Tools -> Create Script -> C Script). Follow the *AD9370 Quick Start Guide.pdf* from AD9371 Transceiver Evaluation Software\\Resources folder.
      -  The script generates **headless.c, headless.h, myk.c, myk.h and myk_ad9528init.c** files. Add **myk.c**, **myk.h** and **myk_ad9528init.c** to the **src** folder of your project. Do NOT add headless.c and headless.h, instead use the files provided in github.
      -  The build should return no error and Project Explorer should look like
         this:

.. image:: images/project_explorer.png
   :align: center
   :width: 250

-  Note: The AD9371/AD9375 evaluation board contains an on-board voltage
   controlled crystal oscillator (VCXO), there are limitations with the default
   hardware configuration in the scenario where user desired device frequencies
   are not related to the on-board 122.88 MHz VCXO by a rational fraction.

Push data into/out of the AD9371/AD9375
---------------------------------------

Below is defined the dac_core structures used by the dac_setup() and
dac_write_custom_data() functions:

.. code:: C

       typedef struct
       {
           uint32_t base_address;
           uint8_t  resolution;
           dac_channel *channels;
           uint32_t dac_ddr_baseaddr;
       }dac_core;

       typedef struct
       {
           uint32_t dds_frequency_tone0;       // in hz (1000\*1000 for MHz);
           uint32_t dds_phase_tone0;           // in milli(?) angles (90\*1000 for 90 degrees = pi/2)
           int32_t dds_scale_tone0;            // in micro units (1.0\*1000\*1000 is 1.0)
           uint32_t dds_frequency_tone1;       // in hz (1000\*1000 for MHz)
               uint32_t dds_phase_tone1;           // in milli(?) angles (90\*1000 for 90 degrees = pi/2)
               int32_t dds_scale_tone1;            // in micro units (1.0\*1000\*1000 is 1.0)
               uint32_t dds_dual_tone;         // if using single tone for this channel, set to 0x0
               uint32_t pat_data;              // if using SED/debug that sort of thing
               dac_data_src sel;               // set to one of the enumerated type above.
       }dac_channel;

Below is defined the adc_core structure used by the adc_setup() and
adc_capture() functions:

.. code:: C

       typedef struct
       {
           uint32_t base_address;
               uint8_t  master;
               uint8_t  no_of_channels;
               uint8_t  resolution;
               uint32_t start_address;
       }adc_core;

**DDS Mode**

-  Set dac_data_src to **DAC_SRC_DDS** and configure dac_core and dac_channel with the desired options.

**DMA Mode**

-  Set dac_data_src to **DAC_SRC_DMA**.
-  dac_write_custom_data() function takes as argument the **sine_lut_iq** array which contains the custom data to be transmitted.
-  The format for each I and Q is 16-bit signed two's complement. I and Q
   together make up one 32-bit tx sample.

**Capture data**

-  Once DDS or DMA mode is selected and the project configuration can be ran.
-  Open an UART terminal, set the baud rate to 115200bps and make sure the
   initialization was completed, as in the screenshot bellow:

.. image:: images/tera_term_init.png
   :align: center
   :width: 650

-  Next, download the capture scripts from the `git repository <https://github.com/analogdevicesinc/no-OS/tree/2018_R2/ad9371/scripts>`_.
-  **capture.bat** script contains the path of the Xilinx SDK, the default is **"C:\\Xilinx\\SDK\\$VERSION"**; if on your PC the path is different, you need to update it according to your project setup.
-  By running **capture.bat**, the **iq_rx1.csv** and **iq_rx2.csv** files will be generated.
-  Start :adi:`VisualAnalog <en/design-center/interactive-design-tools/visualanalog.html>` and open the **visual_analog.vac** file downloaded from the git repository.
-  From the **Pattern Loader** window, browse for the newly generated .csv files and click **Run**. The result should look something like in the screenshot below:

.. image:: images/visual_analog_3.png
   :align: center

Intel/Altera Platform
---------------------

This guide provides some quick instructions on how to setup the AD9371 mykonos
on:

-  `Intel/Altera Arria 10 <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`_

Required Software
~~~~~~~~~~~~~~~~~

-  The supported version number can be found in our :git-hdl:`git repository <tree/master>`.

Altera Software setup
~~~~~~~~~~~~~~~~~~~~~

This section is intended to give a briefly review about how the user can make a
new application project for his or her hdl design. If you are an advanced user,
you probably want to skip this section.

Before the image can be loaded the **Quartus Prime 16.0** tool or the `Quartus Prime 16.0 Programmer <http://dl.altera.com/16.0/>`_ must be installed on your computer.

-  The first step before get started is to `build <https://wiki.analog.com/resources/fpga/docs/hdl>`_ the desired HDL design.
-  Open the NIOS II Software Build Tools for Eclipse. When NIOS II starts it asks to provide a folder, where to store the work space. Any folder can be provided.
-  Go to **File -> New -> NIOS II Board Support Package**

.. image:: images/nios_ii_new_bsp.png
   :align: center

-  Browse for the **SOPC Information File**:

.. image:: images/sopc_file.png
   :align: center

-  Type a **Project name** and click **Finish**:

.. image:: images/proj_name.png
   :align: center

-  Go to **File -> New -> NIOS II Application**

.. image:: images/nios_ii_new_app.png
   :align: center

-  Select the **BSP location**, type a **Project name** and click **Finish**

.. image:: images/bsp_location.png
   :align: center

-  The brand new **NIOS II Application** should look like:

.. image:: images/new_app.png
   :align: center

-  The next step is to copy all the relevant source code into the **software** directory.
-  **AD9371/AD9375 No-OS Software**

   -  Download from :git-no-OS:`projects/ad9371/src`

      -  Next copy the files intro the src folder of your newly created project.
         You can do this with Ctrl+C Ctrl+V or simple drag and drop

-  **API Source Code**

   -  Download from http://www.analog.com/en/design-center/landing-pages/001/transceiver-evaluation-software.html

      -  Unzip the archive and go into **src->api** folder
      -  Next copy the **ad9528** and **mykonos** folder to the **src** folder of your project. Do **NOT** copy the common.c and common.h files provided by the api. For now, use the ones downloaded from github.

-  **Transceiver Evaluation Software**

   -  Download from http://www.analog.com/en/design-center/landing-pages/001/transceiver-evaluation-software.html

      -  Next, generate the profile by using the :doc:`MATLAB Profile Generator </solutions/reference-designs/adrv9371x/software/filters>`. The profiles can be used with the **Transceiver Evaluation Software** to evaluate system performance.
      -  Further, import the profile into TES, and generate the Mykonos initialization structures which are used by the No-OS driver (Tools -> Create Script -> C Script). Follow the *AD9370 Quick Start Guide.pdf* from AD9371 Transceiver Evaluation Software\\Resources folder.
      -  The script generates **headless.c, headless.h, myk.c, myk.h and myk_ad9528init.c** files. Add **myk.c**, **myk.h** and **myk_ad9528init.c** to the **src** folder of your project. Do NOT add headless.c and headless.h, instead use the files provided in github.
      -  Note: The AD9371/AD9375 evaluation board contains an on-board voltage
         controlled crystal oscillator (VCXO), there are limitations with the
         default hardware configuration in the scenario where user desired
         device frequencies are not related to the on-board 122.88 MHz VCXO by a
         rational fraction.

-  Nios II Eclipse should automatically build the projects and the Console window will display the result of the build. If the build is not done automatically select the **Project**→**Build Automatically** menu option.
-  Note: if you get this error: warning: Unable to reach (null) (at 0x00088608) from the global pointer (at 0x000752b8) because the offset (78672) is out of the allowed range, -32678 to 32767, a quick workaround can be found on the `Altera support page <https://www.altera.com/support/support-resources/knowledge-base/solutions/rd02132012_291.html>`_: modify the linker.x file from your bsp by deleting **+ SIZEOF (.rwdata)** from this one line:

.. image:: images/linker.png
   :align: center

-  At this point the software project setup is complete, the FPGA can be programmed and the software can be downloaded into the system. You can program the FPGA by using **Quartus Prime Programmer**. Load your **.sof** file and click **Start**, the **Progress** bar should indicate **100% (Successful)**

.. image:: images/quartus_programmer.png
   :align: center

-  Next, go to Nios II eclipse and select **Run -> Run Configurations...**

.. image:: images/run_configurations.png
   :align: center

-  Select the **Nios II Hardware** configuration type.

.. image:: images/nios_ii_hw.png
   :align: center

-  Press the **New** button to create a new configuration.
-  On the **Target Connection** tab, press the **Refresh Connections** button. You may need to expand the window or scroll to the right to see this button.

.. image:: images/refresh_connection.png
   :align: center

-  Check the **Ignore mismatched system ID option**.
-  Check the **Ignore mismatched system timestamp** option.
-  Press the **Run** button in the **Run Configurations** window.
-  This will re-build the software project to create an up–to-date executable and then download the code into memory.

Push data into/out of the AD9371/AD9375
---------------------------------------

Below is defined the dac_core structures used by the dac_setup() and
dac_write_custom_data() functions:

.. code:: C

       typedef struct
       {
           uint32_t base_address;
           uint8_t  resolution;
           dac_channel *channels;
           uint32_t dac_ddr_baseaddr;
       }dac_core;

       typedef struct
       {
           uint32_t dds_frequency_tone0;       // in hz (1000\*1000 for MHz);
           uint32_t dds_phase_tone0;           // in milli(?) angles (90\*1000 for 90 degrees = pi/2)
           int32_t dds_scale_tone0;            // in micro units (1.0\*1000\*1000 is 1.0)
           uint32_t dds_frequency_tone1;       // in hz (1000\*1000 for MHz)
               uint32_t dds_phase_tone1;           // in milli(?) angles (90\*1000 for 90 degrees = pi/2)
               int32_t dds_scale_tone1;            // in micro units (1.0\*1000\*1000 is 1.0)
               uint32_t dds_dual_tone;         // if using single tone for this channel, set to 0x0
               uint32_t pat_data;              // if using SED/debug that sort of thing
               dac_data_src sel;               // set to one of the enumerated type above.
       }dac_channel;

Below is defined the adc_core structure used by the adc_setup() and
adc_capture() functions:

.. code:: C

       typedef struct
       {
           uint32_t base_address;
               uint8_t  master;
               uint8_t  no_of_channels;
               uint8_t  resolution;
               uint32_t start_address;
       }adc_core;

**DDS Mode**

-  Set dac_data_src to **DAC_SRC_DDS** and configure dac_core and dac_channel with the desired options.

**DMA Mode**

-  Set dac_data_src to **DAC_SRC_DMA**.
-  dac_write_custom_data() function takes as argument the **sine_lut_iq** array which contains the custom data to be transmitted.
-  The format for each I and Q is 16-bit signed two's complement. I and Q
   together make up one 32-bit tx sample.

**Capture data**

-  Once DDS or DMA mode is selected and the project configuration can be ran.
-  Open an UART terminal, set the baud rate to 115200bps and make sure the
   initialization was completed, as in the screenshot bellow:

.. image:: images/nios_ii_console_done.png
   :align: center

-  Next, download the capture scripts from the `git repository <https://github.com/analogdevicesinc/no-OS/tree/2018_R2/ad9371/scripts>`_.
-  By running **capture.bat**, the **iq_rx1.csv** and **iq_rx2.csv** files will be generated inside the **nios2eds** folder
-  Start :adi:`VisualAnalog <en/design-center/interactive-design-tools/visualanalog.html>` and open the **visual_analog.vac** file downloaded from the git repository.
-  From the **Pattern Loader** window, browse for the newly generated .csv files and click **Run**.

=== Download no-OS =====

The source code of the no-OS software and the scripts can be downloaded from the
Analog Devices github.

.. admonition:: Download
   :class: download

   
   -  **AD9371/AD9375 No-OS Software** :git-no-OS:`projects/ad9371/src`
   -  **AD9371/AD9375 No-OS Scripts** https://github.com/analogdevicesinc/no-OS/tree/2018_R2/ad9371/scripts
   -  **API Source Code** http://www.analog.com/en/design-center/landing-pages/001/transceiver-evaluation-software.html
   

.. |resources-eval-user-guides-mykonos-src_properties.jpg| image:: images/src_properties.jpg
