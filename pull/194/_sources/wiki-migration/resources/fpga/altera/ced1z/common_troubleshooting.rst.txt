In case there is a communication problem with the board the follwing actions can be perfomed in order to try to fix the issues:

-  Check that the evaluation board is powered.
-  Make sure the USB cable is not connected to the CED1Z. In case it is, disconnect it and reset the board.
-  Check that the USB Blaster cable is properly connected to the device and to the computer and that the **USB Blaster Device Driver** driver is installed correctly. If the driver is not correctly installed perform the steps described in the **Getting Started -> Install te USB-Blaster Device Driver** section.
-  In uC-Probe right-click on the **System Browser** window select **Remove Symbols**. A dialog box will open to select the symbols to remove. Press OK to remove the symbols.

|ucproberemovesymbols.png|\ |ucproberemovesymbolsdlg.png|

-  After removing the symbols a new set of symbols must be added in order for the interface to be functional. In uC-Probe right-click on the **System Browser** window select **Add Symbols**. A dialog box will open to select the symbols to be added. If the lab was done according to the steps provided in the Quick Evaluation section, select the file **ADIEvalBoard/ucProbeInterface/ADIEvalBoard.elf** to be loaded as a symbol file, otherwise select the file **ADIEvalBoard/FPGA/software/ADIEvalBoard/ADIEvalBoard.elf** to be loaded as a symbol file.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/ucprobeaddsymbols.png
   :alt: ucprobeaddsymbols.png
   :align: center
   :width: 400px

-  If the communication problem persists even after performing the previous steps, restart the uC-Probe application and try to run the interface again.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/image081.png
   :alt: image081.png
   :align: center
   :width: 300px

More information
================

-  :ez:`ask questions about the FPGA reference design <community/fpga>`
-  Example questions:

|//ez.analog.com/community/feeds/allcontent/atom|

.. |ucproberemovesymbols.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/bemicro/ucproberemovesymbols.png
   :width: 400px
.. |ucproberemovesymbolsdlg.png| image:: https://wiki.analog.com/_media/resources/fpga/altera/ced1z/ucproberemovesymbolsdlg.png
   :width: 400px
.. |//ez.analog.com/community/feeds/allcontent/atom| image:: https://wiki.analog.com/_media/rss>http///ez.analog.com/community/feeds/allcontent/atom
