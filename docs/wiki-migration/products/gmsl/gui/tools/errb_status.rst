ERRB Status
===========

| The GMSL GUI allows for a convenient, graphical way to monitor errors that may occur. The ERRB status window shows all the possible errors to be monitored and their current status.
| ==== ERRB Status Window ==== When you open the tool, it will scan all of the error registers of the currently connected devices. You can also refresh the error statuses at any time by clicking the "**Refresh Error Status**" button.
| |image1|
| Each error has two bits to monitor and report the status: <error name>_FLAG and <error name>_OEN. The FLAG bit indicates that the error conditions of the specific have been met. The OEN bit is used to map this to the physical ERRB pin of the device.
| ==== Decoding the ERRB Statuses ==== Using the first block of errors on the :adi:`MAX96717 <en/products/max96717.html>` as an example, we can translate the current state of the device.
| |image2|
| The errors are organized based on which the registers that contain the OEN bit. This block corresponds to the INTR2 register of the MAX96717 located at address 0x1A. The subsequent register, INTR3 (0x1B), contains the FLAG bits which indicate if the error conditions are met.

Looking back at the block of errors, the bubbles on the right indicate the FLAG bit status. The various colors of the bubbles are detailed at the top of the tool.

The tick box next to the error indicates whether the OEN bit is set or not.

We can now decode this box to mean the following:

-  DEC_ERR and LFLT_INT errors are being mapped to the physical ERRB.
-  There are currently no monitored errors that have occurred, therefore overall ERRB = GREEN = no errors.
-  There was an error that occurred but we are not monitoring it.

.. |image1| image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/errb_status.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/products/gmsl/gui/tools/errb_status_zoom.png
   :width: 400px
