LIMITATIONS
===========

The following are some of the important limitations known at the time of this release:

-  AD243x specific limitations

   -  Power calculation feature in SigmaStudio Plus is yet to be updated for AD243x.

      -  BERT PRBS mode results in errors for AD243x when Data tunnels are enabled.
      -  Partial discovery is not supported for AD2435

-  Bus configuration merge option is not supported.
-  The node connected to A2B port of AD2430WC1BZ, should set CONTROL.XCVRBINV bit.
-  All AD2437 products connected through RJ45 should set CONTROL.XCVRBINV bit.
-  Crossbar view does not represent PDM pin data explicitly.
-  The Upper bounds value of the sync offset in main-node-settings -> General View -> Audio tab is incorrect.
-  Shapes within the standard platforms (which are obtained by double-clicking a2b shapes in system tab), should not be deleted or added.
-  SPI Full Duplex Size, SPI Full Duplex Target node and FD Target SSEL functions are not supported.
-  Bandwidth window values configured manually will be reset to default if the window is closed.
-  AD2437 Line Diagnostics are not supported.
-  SPI based command list is not supported in sequence window
-  Transceiver settings can be refreshed through switching between the tabs within the settings window or through re-open of settings page.
-  Partial Discovery is supported only when upstream is configured
-  Custom Node Authentication:

   -  Backspace or delete from the middle of the identifier text in the number (hex) notation is not supported.

-  Thrift limitations:

   -  Bandwidth parameters updated through thrift do not reflect in SS+
   -  Some of the thrift APIs do not return failures. Limitation in Core SS+, will be fixed in future releases.
   -  Thrift APIs are not available for multi-main networks.

-  Bandwidth:

   -  Response cycle calculation always use the No TDM offset when during schematic link compile download.
   -  Bandwidth Break Down Chart numbers doesn't match with Bandwidth Excel Sheet 7.0

-  Custom Platform:

   -  Expected HPSW_CFG is CFG-0 for AD2435 in Custom Platform, this has to be explicitly change for first time to CFG-4 configuration.

-  Peripheral programming window below are supported.

   -  Program during discovery
   -  Embed XML
   -  Generate XML
   -  Register Read/Write
   -  Add command
   -  Address in Hex
   -  save sequence file
