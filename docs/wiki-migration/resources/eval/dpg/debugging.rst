Debugging the DPG 2/3
=====================

DPGDownloader Only Shows Generic Eval
-------------------------------------

Verify Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that the DPG2 and the eval board are detected in the Device Manager:|image1| If the two devices do not appear as shown, reinstall the latest version of DPGDownloader.

Verify DLL File is Present
~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify that the appropriate DLL for your evaluation board is present in: C:\\Program Files (x86)\\Analog Devices\\DPG\\ the file is named: AnalogDevices.DPG.EvalBoard.ADXXXX.dll where XXXX is the part number of your evaluation board. If the file is not present install the DAC update file for your evaluation board.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/devicemanager.png
   :width: 200px
