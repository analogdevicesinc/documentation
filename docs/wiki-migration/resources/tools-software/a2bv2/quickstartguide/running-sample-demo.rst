:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

Running the Sample Demo
=======================

Using SigmaStudio+ the A2B system can be directly controlled from a connected computer without involving a microcontroller or a DSP. This mode is helpful for quick testing of the capabilities of AD24xx without the need for a microcontroller in the system.

.. note::

   Please refer Appendices :doc:`A </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-a>` and :doc:`B </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>` for information about navigating in SigmaStudio+ for A2B use-case.


A block diagram of a 3 node A2B system with PC as Host is shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/a2b_system_with_pc_as_host.jpg
   :align: center

.. container:: centeralign

   \ **Figure:** A2B system with PC as Host


The sample demo configuration is as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`. The audio source connected to sub-node 1 will be played out at main node. The microphone audio from sub node 0 will be played out at sub node 1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_a2b_demo_configuration_3.png
   :align: center

.. container:: centeralign

   \ **Figure:** Sample A2B demo configuration


The sample demo configuration can be run with either EVAL-AD2428WD1BZ, ADZS-21569 EZ-KIT, EVAL-AD2433WA1BZ , EVAL-AD2435WA3LZ, EVAL- AD2430WD1BZ or EVAL-AD2438WD1BZ, EVAL-AD2437A1NZ as the A2B main platform. The following sections describe the procedure for running the demo.

Refer section :doc:`Sample Demo Setup </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2430>` for sample demo using EVAL- AD2430WD1BZ or EVAL-AD2438WD1BZ

Refer section :doc:`Sample Demo Setup with PC </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2437>` for sample demo using EVAL – AD2437WA1NZ and AD2437B1NZ.

Software Setup
--------------

Setup PC software as explained in Section :doc:`Software Requirements </wiki-migration/resources/tools-software/a2bv2/quickstartguide/systemrequirements>`

Hardware Setup
--------------

High Power – AD243x
~~~~~~~~~~~~~~~~~~~

Hardware connections shall be done as described in :doc:`AD243x High Power </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>`

Jumper settings
^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2435WA3LZ (Main) and EVAL-AD2435WJ3LZ (Sub 0 and Sub 1) are as shown in :doc:`Table. </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`

.. container:: centeralign

   \ **Table:** Jumper Settings: High Power


+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| **Jumper** | **Purpose in EVAL-AD2435WA3LZ** | **Main**     |   | **Jumper** | **Purpose in EVAL-AD2435WJ3LZ** | **Sub 0** | **Sub 1** |
+============+=================================+==============+===+============+=================================+===========+===========+
| JP1        | Boot                            | x            |   | JP1        | Class D Standby                 | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP2        | /Output Source                  | 2-3          |   | JP2        | I2S/                            | 5-6       | 5-6       |
|            |                                 |              |   |            | CODEC/                          | 7-14      | 7-8       |
|            |                                 |              |   |            | TUNER/                          | 8-13      | 17-18     |
|            |                                 |              |   |            | CLASS-D                         | 19-20     | 19-20     |
|            |                                 |              |   |            |                                 | 21-22     | 21-22     |
|            |                                 |              |   |            |                                 | 23-24     | 23-24     |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP3        | Input Source                    | 2-3          |   | JP3        | PWM Select                      | 1-2       | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP4        | Clock Sel                       | 1-2          |   | JP4        | Not present                     | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP5        | Self-Discovery Mode             | 1-2          |   | JP5        | VBUS Supply                     | 2-3       | 2-3       |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP6        | ADC0/VR1                        | x            |   | JP6        |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP7        | ADC1/VR2                        | x            |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP8        | I2S Signals                     | 1-2          |   |            |                                 |           |           |
|            |                                 | 3-4          |   |            |                                 |           |           |
|            |                                 | 5-6          |   |            |                                 |           |           |
|            |                                 | 7-8          |   |            |                                 |           |           |
|            |                                 | 9-10         |   |            |                                 |           |           |
|            |                                 | 11-12        |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P1         | I2C/SPI                         | x            |   | P1         | I2C/SPI                         | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P2         | SigmaStudio+                    | Connect      |   | P2         | DCOP Module Connector           | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P3         | Not present                     | x            |   | P3         | Tuner Module Connector          | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P4         | Supply In                       | Connect      |   | P4         | CH2                             | x         | Connect   |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P5         | PWR                             | Keep default |   | P5         | CH1                             | x         | Connect   |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   | P6         | HWMUTE                          | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P12        | Fuse                            | Keep default |   |            |                                 | x         | x         |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+

A2B Demo system
^^^^^^^^^^^^^^^

All steps mentioned in :doc:`AD243x high Power </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>` shall be completed before running the demo using PC as a Host. The demo system shall look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-high-power>`.

High Power – AD2437
~~~~~~~~~~~~~~~~~~~

Hardware connections shall be done as described in :doc:`AD2437 High Power </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2437>`

XLR Platform Jumper settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2437A1NZ (Main) and EVAL-AD2437B1NZ (Sub 0 and Sub 1) are as shown in :doc:`Table </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

.. container:: centeralign

   \ **Table:** 2437 XLR Platform Jumper Settings


+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| **Jumper** | **Purpose in EVAL-AD2437A1NZ** | **Main** |   | **Jumper** | **Purpose in EVAL AD2437B1NZ** | **Sub 0** | **Sub 1** |
+============+================================+==========+===+============+================================+===========+===========+
| JP1        | Self Discovery Mode            | 1-2      |   | JP1        | AD2437 SIO0 select             | 1-2       | 2-3       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| JP5        | Boot Disable                   | 1-2      |   | P9         | BOOT DISABLE                   | 1-2       | 1-2       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| JP6        | Clock Select                   | 1-2      |   | JP2        | GAIN                           | 1-2       | 1-2       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| P6         | AD1937 Clock Sel               | 1-2      |   | JP3        | MUTE                           | 1-2       | 1-2       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| X          | All Others                     | Open     |   | S1         | I2C BUS SEL                    | ALL ON    | ALL ON    |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+

.. _a2b-demo-system-1:

A2B Demo system
^^^^^^^^^^^^^^^

All steps mentioned in :doc:`AD2437 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2437>` shall be completed before running the demo using PC as a Host. The demo system shall look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2437>`

RJ45 Platform Jumper settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2437A1MZ (Main) and EVAL-AD2437B1MZ (Sub 0 and Sub 1) are as shown in :doc:`Table </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

.. container:: centeralign

   \ **Table:** 2437 RJ45 Platform Jumper Settings


+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| **Jumper** | **Purpose in EVAL-AD2437A1MZ** | **Main** |   | **Jumper** | **Purpose in EVAL AD2437B1MZ** | **Sub 0** | **Sub 1** |
+============+================================+==========+===+============+================================+===========+===========+
| JP1        | PDM Clock Source               | 1-2, 3-4 |   | P4         | SIO0 source select             | 1-2       | 2-3       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| JP4        | WAKE UP                        | 1-2      |   | P16        | PDM CLK                        | 1-2       | 1-2       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| JP6        | IRQ                            | 1-2      |   | P18        | WP                             | 1-2       | 1-2       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| JP9        | SIO2                           | 1-2      |   | P23        | MUTE                           | 2-3       | 2-3       |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| JP38       | Clock Select                   | 1-2      |   |            |                                |           |           |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+
| X          | All Others                     | Open     |   |            |                                |           |           |
+------------+--------------------------------+----------+---+------------+--------------------------------+-----------+-----------+

.. _a2b-demo-system-2:

A2B Demo system
^^^^^^^^^^^^^^^

All steps mentioned in :doc:`AD2437 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2437>` shall be completed before running the demo using PC as a Host. The demo system shall look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2437>`

Standard Power – AD243x
~~~~~~~~~~~~~~~~~~~~~~~

.. _jumper-settings-1:

Jumper settings
^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2433WA1BZ (Main) and EVAL-AD2433WB1BZ (Sub 0 and Sub 1) are as shown in Table.

.. container:: centeralign

   \ **Table:** Jumper Settings: Standard Power


+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| **Jumper** | **Purpose in EVAL-AD2433WA1BZ** | **Main**     |   | **Jumper** | **Purpose in EVAL-AD2433WB1BZ** | **Sub 0** | **Sub 1** |
+============+=================================+==============+===+============+=================================+===========+===========+
| JP1        | USBi Sel                        | 1-2          |   | JP1        | DRX0                            | 1-2       | 1-2       |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP2        | Boot                            | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP3        | DRX0                            | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP4        | DRX1                            | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP5        | Clock Sel                       | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP6        | PWM Select                      | X            |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| JP7        | Self-Discovery                  | 1-2          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
|            |                                 |              |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P1         | I2C/SPI                         | Keep default |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P2         | SigmaStudio+                    | Connect      |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P3         | PWR                             | Connect      |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P4         | +12V                            | Keep default |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P5         | IOVDD                           | 2-3          |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+
| P7         | I2S Connector                   | Keep default |   |            |                                 |           |           |
+------------+---------------------------------+--------------+---+------------+---------------------------------+-----------+-----------+

.. _a2b-demo-system-3:

A2B Demo system
^^^^^^^^^^^^^^^

All steps mentioned in :doc:`AD243x standard Power </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` shall be completed before running the demo using PC as a Host. The demo system shall look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>`.

Standard Power – AD2430 / AD2438
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _jumper-settings-2:

Jumper settings
^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2430WD1BZ / EVAL-AD2438WD1BZ (Main) is as shown in Table.

.. container:: centeralign

   \ **Table:** Jumper Settings – AD2430 / AD2438


============ =============================== =================
**Jumper**   **Purpose in EVAL-AD2433WA1BZ** **Main**
============ =============================== =================
JP1          Voltage Selector                1-2
JP2          Voltage Selector                1-2
JP3          Main / LPS Selector             1-2
JP4          MCLK                            1-2
JP5          Clock Sel                       1-2
JP6          Boot                            1-2
JP7          BCLK                            1-2
JP8          SYNC                            1-2
JP9          DTX0                            1-2
JP10         DRX1                            1-2
JP11         DRX0                            1 & 3
JP12         PDMCLK                          Open
\                                            
P2           DTx / DRx Probe Head            Keep default
P3           I2C / IRQ Probe Head            Keep default
P4           Line In                         Connect
P5           Line Out                        Connect
P6           SigmaStudio+                    Connect
P7           Power Input                     Connect
P9, P20, P22 Other                           Open
P8           +12V                            Keep default
P10          Extender                        Connect to Target
============ =============================== =================

.. _a2b-demo-system-4:

A2B Demo system
^^^^^^^^^^^^^^^

All steps mentioned in Section :doc:`Sample Demo Setup </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2430>` shall be completed before running the demo using PC as a Host. The demo system shall look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

Standard Power – AD242x
~~~~~~~~~~~~~~~~~~~~~~~

.. _jumper-settings-3:

Jumper settings
^^^^^^^^^^^^^^^

Jumper settings (default) for EVAL-AD2428WD1BZ(Main) is as shown in Table.

.. container:: centeralign

   \ **Table:** Jumper Settings


+---------+-----------+-----------+---------+---------+---------+---------+---------+---------+----------+---------+----------+
| **JP1** | **JP2**   | **JP3**   | **JP4** | **JP5** | **JP6** | **JP7** | **JP8** | **JP9** | **JP10** | **JP11  | **JP14** |
|         |           |           |         |         |         |         |         |         |          | 12/13** |          |
+=========+===========+===========+=========+=========+=========+=========+=========+=========+==========+=========+==========+
| 1-2     | 1-2 & 3-4 | 1-2 & 3-4 | 1-2     | 3-4     | 3-4     | 3-4     | 2-3     | 3-4     | 1-2      | Open    | 1-2      |
+---------+-----------+-----------+---------+---------+---------+---------+---------+---------+----------+---------+----------+

.. _a2b-demo-system-5:

A2B Demo system
^^^^^^^^^^^^^^^

All steps mentioned in Section :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>` shall be completed before running the demo using PC as a Host. The demo system shall look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`

Running sample Demo
-------------------

The following steps describe the procedure to run a sample demo in PC mode

-  Open an A2B schematic from (<A2B plugin for SigmaStudio+ installation path>>\\Schematics\\PC).


|image1|

.. container:: centeralign

   \ **Figure:** Sample demo schematic in PC mode


-  Make sure that .xml files are provided for programming SigmaDSPs (ADAU1361, ADAU1761, ADAU1452 and ADAU 1961) on main and sub A2B evaluation boards, the procedure to find the peripheral settings window is as follows:

   -  Open the platform view either by double clicking on the platform or by clicking on “Canvas” option under the platform in the Project tree as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.


   |image2|

.. container:: centeralign

   \ **Figure:** Platform view in SigmaStudio+


-  The peripheral settings can be opened by double clicking on the peripheral or by clicking on the “Settings” option under the peripheral in project tree and select the xml as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`



|image3|

.. container:: centeralign

   \ **Figure:** Peripheral Settings window


-  **Note:** The adi_a2b_main_ADAU1452.xml, adi_a2b_main_ADAU1761.xml, adi_a2b_sub_ADAU1961.xml files are available in <A2B plugin for SigmaStudio+ installation path>>\\Schematics\\PC\\xml folder

-  Make sure that USBi cable is connected to eval board as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>` and the board is powered on.
-  Click on “LinkCompileDownload” icon in SigmaStudio+ as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` This will start the discovery and configuration of A2B nodes and peripheral devices as per the schematic.

|image4|

.. container:: centeralign

   \ **Figure:** Link-Compile-Download option in SigmaStudio+


-  After successful discovery and initialization audio routing can be observed as per the sample demo configuration shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

Running Sample Demo Remote DSP tuning with ADAU1452
---------------------------------------------------

This demo uses two EVAL-AD2428WD1BZ boards. The following steps shows how to perform remote DSP tuning of the 1452 sigmaDSP on the subnode.

-  Connect and configure the hardware without bypassing the 1452 DSP as per :doc:`Local powered sub-nodes </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>` ,\ :doc:`EVAL-AD2428WD1BZ without 1452 DSP Bypass jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>`.
-  Connect the USBi to PC.
-  Launch SigmaStudio+ 2.0.0
-  Click on File -> open project. Browse to C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC and select the file adi_a2b_AD2428WD1BZ_LPS_Custom.ssprj.
-  Turn ON the power both the nodes and provide the audio sinks and sources
-  Click on Action -> “Link Compile Download”.
-  The schematic will download and audio will be heard.
-  This demo example allows remote DSP tuning of the 1452 DSP on the sub-node. This will multiplex between sine tone generator and audio source at sub-node. The difference can be heard through the audio sink at the main-node

   -  In the system tab, double-click the last sub-node platform and then double-click the ADAU1452 shape.
   -  A schematic as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` will open
   -  Click on the Mux towards the left of the schematic to switch the song playing at main-node to the sine tone generator.
   -  The frequency, gain, on/off state of the sine tone generator can be changed by interacting with the “Sine Tone” block.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/dsp_schematic_on_adau_1452.png
   :align: center

.. container:: centeralign

   \ **Figure:** DSP schematic on ADAU 1452


Running Sample Demo Multi-main
------------------------------

PC (Host) + ADSP-21569 SOM + SOM-CRR ez-kit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This demo uses either two ADZS-2435MINI or two ADZS-2433MINI. The following steps are applicable for both the A2B evaluation board pairs.

-  Perform the hardware setup as per :doc:`ADZS2435-MINI Hardware modifications </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`ADZS2435-MINI Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`EVAL-AD2435WJ3LZ Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`ADZS2433-MINI Hardware modifications </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` , :doc:`ADZS2433-MINI Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` , :doc:`EVAL-AD2433WB1BZ Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` . Maintain the hardware configuration for the SOM and SOM-CRR ez kit as per the recommended default configurations of their respective manuals
-  Launch SigmaStudio+ x.y.z
-  Click on file -> open project. Browse to C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC and select the file adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj for 2433 transceiver or adi_a2b_ADZS2435MINI_ADSP21569_Multi_Main.ssprj for 2435 transceiver.
-  Follow the procedure given in APPENDIX : Flashing ADSP-21569 SOM to flash the file C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\LDR\\SS_App_21569_Multi_Main.ldr onto the SOM board.
-  Turn OFF power to the SOM-CRR board and set boot-mode to 1 on the SOM.
-  Make all the connections described in sections :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` .
-  Connect the USB-Type A cable of USBi device to the PC.
-  Turn ON power to the SOM-CRR and A2B Main nodes.
-  Confirm that LEDs 8 (green) and 9 (amber) are lit on the SOM-CRR. These are just behind the A2B connector (also shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`).
-  Provide audio sinks and sources as per section :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` .
-  On SS+ toolbar, click on the Action -> “Link Compile Download”.
-  The schematic will download and Audio out’s as per section :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` will be heard.
-  **Note :**

   -  To re-download the schematic, the SOM-CRR must be reset by pushing the reset button.
   -  If the message “Target execution could not be verified” is displayed. Perform a re-download of the schematic by following point ‘a’ above.

-  This demo example has an audio-in at sub-node 1 of main-node 0 chain and an audio-out on sub-node 1 of main-node 1 chain (as per section :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>`). A cross fade can be performed between this audio-in and a 500 Hz sine-tone which is generated on the ADSP-21569.

   -  In the system tab of the schematic, double-click the custom platform and then double-click the ADSP-2156x shape.
   -  A schematic as shown in below Figure will open.
   -  Click once on the “On/Off switch” to put it to “ON” state and observe that the song will fade into a sine tone
   -  Click on the same switch again to get back the audio.
   -  Volume can be adjusted by operating the slider on the right end of the schematic near the outputs
   -  The frequency, gain and on/off state can be changed for each of the two sine tones by interacting with the “Sine Tone” block.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main-dsp.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main DSP schematic


SC594 (Host) + SOM-CRR ez kit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This demo uses SC594 as a host and it uses two ADZS-2435MINI’s. The following steps shows how to run this sample demo.

-  Perform the hardware setup as per :doc:`ADZS2435-MINI Hardware modifications </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`EVAL-AD2435WJ3LZ ADZS2435-MINI Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` . Maintain the hardware configuration for the SOM and SOM-CRR ez kit as per the recommended default configurations of their respective manuals.
-  Open CCES v2.11.0 and click on File -> Import -> ‘Existing projects into work space’
-  Browse to the folder C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\multimaster and select a2b-adsp-sc59x
-  Build the project using Project -> Build Project option.
-  Turn OFF power to the SOM-CRR board and set boot-mode to 0 on the SOM.
-  Make all the connections described in section :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`.
-  Turn ON power to the SOM-CRR and A2B Main nodes.
-  Connect the JTAG to PC.
   **Note:** If Emulator is used the first time: Create a new debug configuration using Run- >Debug Configurations, create new session, select ADSP-SC594 and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (typically: ADSP-SC594 via ICE1000) and click NEXT, then click FINISH.
-  Select a debug configuration and press F5 to run the project.
-  There are three audio configurations for this multi-main setup described in above Figures and section :doc:`Audio In/out for ADSP-SC594 as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` . Provide the audio sources and sinks as per these.

Running sample Demo A2B Bus Analyzer
------------------------------------

The following steps describe the procedure to run a sample demo in PC mode

-  Open an A2B schematic from (<A2B plugin for SigmaStudio+ installation path>>\\Schematics\\A2BBusAnalyzer
-  Refer :doc:`G.2.6(Using A2B Bus Analyzer UI from SigmaStudio+) </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-g>` Using A2B Bus Analyzer UI from SigmaStudio+ for steps to launch A2B Bus Analyzer UI from SigmaStudio+
-  Click on “LinkCompileDownload” icon in SigmaStudio+.
-  Discovery and configuration of A2B nodes and peripheral devices as per the schematic will be done by the A2B Bus Analyzer Device if it is used for Main Node Emulation
-  All the events through the A2B network will be captured by the A2B Bus Analyzer Device when used as Bus Monitor
-  A2B Bus Analyzer Device will be discovered as a Sub Node by the A2B Eval Main Node when used as a Sub Node Emulator.
-  After successful discovery and initialization, audio routing can be observed as per the stream configuration for the schematic. The sink and source audio streams of A2B Bus Analyzer Main/Sub Node Emulator and audio streams detected by the A2B Bus Analyzer Bus Monitor will be displayed on the A2B Bus Analyzer UI.

Running sample Demo BF as Host
------------------------------

The sample demo can be run using BF527 as the host processor. In this case the host processor controls the discovery and programming of A2B nodes in the system. The block diagram of a 3 node A2B system with BF527 as Host is shown :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` below.


|image5|

.. container:: centeralign

   \ **Figure:** A2B system with BF527 as Host


System Requirements
~~~~~~~~~~~~~~~~~~~

-  System Requirements as mentioned `here <https://wiki.analog.com/[[/resources/tools-software/a2bv2/quickstartguide/systemrequirements>`_
-  CCES 2.11.0 or later
-  SDP-B board with BF527 (EVAL-SDP-CB1Z) - Rev1.3 used as Host
-  JTAG Emulator to program ADSP-BF527 DSP or Flash on SDP board

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

Hardware connections shall be done as described `here <https://wiki.analog.com/[[/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>`_ . SDP-B board shall be mounted on EVAL-AD2433WA1BZ board that acts as A2B master.

.. _jumper-settings-4:

Jumper settings
~~~~~~~~~~~~~~~

No configurable Jumpers available on SDP-B board. EVAL-AD2433WA1BZ and EVAL-AD2433WB1BZ board jumpers shall be set as mentioned in Table of the earlier section above.

.. _a2b-demo-system-6:

A2B Demo System
~~~~~~~~~~~~~~~

After completing all the connections, the A2B system should look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

-  Mount ‘Connector A’ of SDP-B on J5 of EVAL-AD2435WA3LZ
-  Connect a JTAG Emulator from PC to SDP-B board

|image6|

.. container:: centeralign

   \ **Figure:** A2B demo setup with BF527 as host


.. _running-sample-demo-1:

Running sample demo
~~~~~~~~~~~~~~~~~~~

The SigmaStudio+ schematic for this demo can be found at C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC\\adi_a2b_AD2433WA1BZ.ssprj. The demo application already uses the exported BCF from this schematic.

If there is a change in schematic required, after the changes are done export the busconfig.c file from sigmastudio+ and paste the busconfig file in the target software project in the location C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\app.

When using BF527 as the host, demo can be run either from flash or by downloading from CCES over JTAG. The following steps shall be followed depending on the preferred way of execution.

-  Flash the SDP-B with A2B target software(as mentioned in the sections below) OR
-  Download A2B target software from CCES after each power up (as mentioned in the sections below)

Flash SDP-B with A2B target software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open CCES and import Target project into the workspace using ‘File->Import->Existing Projects into Workspace’ browse and select a2bstack_frmwrk-bf (available in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo).
-  Build the project using ‘Project->Build Project’ option.
-  Run the Flash utility batch file from C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\Flash depending on the type of Emulator used to connect to Target (Flash-ICE100.bat for ICE-1000).
-  The batch utility will start flashing the board as shown in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.
-  After the flashing is complete disconnect from Target, remove JTAG and Reset the SDP-B board.

|image7|

.. container:: centeralign

   \ **Figure:** A2B demo setup with BF527 as host


Download A2B target software from CCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open CCES and import Target project into the workspace using ‘File->Import->Existing Projects into Workspace’ browse and select a2bstack_frmwrk-bf (available in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo).
-  Build the project using ‘Project->Build Project’ option
-  Create a new debug configuration using Run->Debug Configurations, create new session, select ADSP-BF527 and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (typically: ADSP527 via ICE-1000) and click NEXT, then click FINISH.
-  Ensure Custom board support file BF527-SDP-HW-CCES.XML (C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\system\\BF527-SDP-HW-CCES.XML) is applied as shown below
-  Run the project by selecting a debug configuration. Ensure that JTAG is connected to the SDP-B board on the Master node.

|image8|

.. container:: centeralign

   \ **Figure:** Custom Board Support


Running Sample Demo ADSP-SC594 as Host
--------------------------------------

The sample demo can be run using ADSP-SC594 as the host. In this case the ARM core of host processor controls the discovery and programming of A2B nodes in the system. The following steps shows how to run sample demo

-  Perform hardware modification and jumper setting as per [[:resources:tools-software:a2bv2:quickstartguide:running-sample-demo#hardware_setup]AD2430 jumper setting]. Maintain the hardware configuration for the SOM and SOM-CRR ez kit as per the recommended default configurations of their respective manuals.
-  Open CCES v2.11.0 and click on File → Import → ‘Existing projects into work space’.
-  Browse to the folder C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-adsp-sc59x
-  Build the project using Project → Build Project option.
-  Make all the connections described in section connections.
-  Turn ON power to the SOM-CRR and A2B Main node.
-  Connect the JTAG to PC.
-  \* **Note:** If Emulator is used the first time: Create a new debug configuration using Run- >Debug Configurations, create new session, select ADSP-SC594 and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (typically: ADSP-SC594 via ICE1000) and click NEXT, then click FINISH.
-  Select a debug configuration and press F5 to run the project.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_demo_schematic_in_pc_mode.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/platform_view_in_sigmastudio_.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/peripheral_window_new.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/link_compile_download.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/blank_diagram.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bf527_host.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bf527_host_cmd.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/customboardinfocces.png
