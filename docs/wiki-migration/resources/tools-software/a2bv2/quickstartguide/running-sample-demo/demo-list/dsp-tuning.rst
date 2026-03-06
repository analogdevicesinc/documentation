:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

Running Sample Demo Remote DSP tuning with ADAU1452
===================================================

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

