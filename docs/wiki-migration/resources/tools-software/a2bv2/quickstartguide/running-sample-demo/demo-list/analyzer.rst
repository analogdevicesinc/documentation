:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

Running sample Demo A2B Bus Analyzer
====================================

The following steps describe the procedure to run a sample demo in PC mode

-  Refer :doc:`AD2433 jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` and :doc:`AD2428 jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>` for jumper setting depending on the schematic of analyzer.
-  Open an A2B schematic from (<A2B plugin for SigmaStudio+ installation path>>\\Schematics\\A2BBusAnalyzer
-  Refer :doc:`Using A2B Bus Analyzer UI from SigmaStudio+ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-g>` Using A2B Bus Analyzer UI from SigmaStudio+ for steps to launch A2B Bus Analyzer UI from SigmaStudio+
-  Click on “LinkCompileDownload” icon in SigmaStudio+.
-  Discovery and configuration of A2B nodes and peripheral devices as per the schematic will be done by the A2B Bus Analyzer Device if it is used for Main Node Emulation
-  All the events through the A2B network will be captured by the A2B Bus Analyzer Device when used as Bus Monitor
-  A2B Bus Analyzer Device will be discovered as a Sub Node by the A2B Eval Main Node when used as a Sub Node Emulator.
-  After successful discovery and initialization, audio routing can be observed as per the stream configuration for the schematic. The sink and source audio streams of A2B Bus Analyzer Main/Sub Node Emulator and audio streams detected by the A2B Bus Analyzer Bus Monitor will be displayed on the A2B Bus Analyzer UI.

Here are some more examples for analyzer
----------------------------------------

-  :doc:`Multi-Main Analyzer setup </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/analyzer/multimain>`
-  :doc:`Opto A2B Setup </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/analyzer/optoa2b>`
