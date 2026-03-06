:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

:doc:`Click here to return to Running sample Demo: Target as Host </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/target>`

Running sample Demo BF as Host
==============================

The sample demo can be run using BF527 as the host processor. In this case the host processor controls the discovery and programming of A2B nodes in the system. The block diagram of a 3 node A2B system with BF527 as Host is shown :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` below.


|image1|

.. container:: centeralign

   \ **Figure:** A2B system with BF527 as Host


System Requirements
-------------------

-  System Requirements as mentioned `here <https://wiki.analog.com/[[/resources/tools-software/a2bv2/quickstartguide/systemrequirements>`__
-  CCES 2.11.0 or later
-  SDP-B board with BF527 (EVAL-SDP-CB1Z) - Rev1.3 used as Host
-  JTAG Emulator to program ADSP-BF527 DSP or Flash on SDP board

Hardware Setup
--------------

Hardware connections shall be done as described `here <https://wiki.analog.com/[[/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>`__ . SDP-B board shall be mounted on EVAL-AD2433WA1BZ board that acts as A2B master.

Jumper settings
~~~~~~~~~~~~~~~

No configurable Jumpers available on SDP-B board. EVAL-AD2433WA1BZ and EVAL-AD2433WB1BZ board jumpers shall be set as mentioned in Table of the earlier section above.

A2B Demo System
~~~~~~~~~~~~~~~

After completing all the connections, the A2B system should look as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.

-  Mount ‘Connector A’ of SDP-B on J5 of EVAL-AD2435WA3LZ
-  Connect a JTAG Emulator from PC to SDP-B board

|image2|

.. container:: centeralign

   \ **Figure:** A2B demo setup with BF527 as host


Running sample demo
~~~~~~~~~~~~~~~~~~~

The SigmaStudio+ schematic for this demo can be found at C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC\\adi_a2b_AD2433WA1BZ.ssprj. The demo application already uses the exported BCF from this schematic.

If there is a change in schematic required, after the changes are done export the busconfig.c file from sigmastudio+ and paste the busconfig file in the target software project in the location C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\app.

When using BF527 as the host, demo can be run either from flash or by downloading from CCES over JTAG. The following steps shall be followed depending on the preferred way of execution.

-  Flash the SDP-B with A2B target software(as mentioned in the sections below)OR
-  Download A2B target software from CCES after each power up (as mentioned in the sections below)

Flash SDP-B with A2B target software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open CCES and import Target project into the workspace using ‘File->Import->Existing Projects into Workspace’ browse and select a2bstack_frmwrk-bf (available in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo).
-  Build the project using ‘Project->Build Project’ option.
-  Run the Flash utility batch file from C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\Flash depending on the type of Emulator used to connect to Target (Flash-ICE100.bat for ICE-1000).
-  The batch utility will start flashing the board as shown in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>`.
-  After the flashing is complete disconnect from Target, remove JTAG and Reset the SDP-B board.

|image3|

.. container:: centeralign

   \ **Figure:** A2B demo setup with BF527 as host


Download A2B target software from CCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open CCES and import Target project into the workspace using ‘File->Import->Existing Projects into Workspace’ browse and select a2bstack_frmwrk-bf (available in C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo).
-  Build the project using ‘Project->Build Project’ option
-  Create a new debug configuration using Run->Debug Configurations, create new session, select ADSP-BF527 and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (typically: ADSP527 via ICE-1000) and click NEXT, then click FINISH.
-  Ensure Custom board support file BF527-SDP-HW-CCES.XML (C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\system\\BF527-SDP-HW-CCES.XML) is applied as shown below
-  Run the project by selecting a debug configuration. Ensure that JTAG is connected to the SDP-B board on the Master node.

|image4|

.. container:: centeralign

   \ **Figure:** Custom Board Support


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/blank_diagram.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bf527_host.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/bf527_host_cmd.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/customboardinfocces.png
