| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

Troubleshooting Guide
=====================

Troubleshooting guide:

| **I'm experiencing difficulty in connecting the ezLINX® board to my PC**

-  Ensure that the board is correctly connected to both the PC using the USB cable and to the AC mains using the AC adapter.
-  If the hardware prompt box on the desktop pops up then the PC is able to recognize the board. If you still can't connect to the board then there is most likely a problem with the IP address of the adapter/board.
-  Connect the board to the HyperTerminal application and reset the board. Press any key to interrupt the autoboot sequence, type ifconfig into the entry field and hit the return key. On one of the lines that pop up there will be the current IP address of the board. Try to reconnect to the board using an address on the same network of the IP address of the board.

| **The interface that I am using is not working correctly**

-  Ensure that the connections between the interfaces are correct and that the same configuration settings are used for each board. Consult the test procedure for the ezLINX® board for a list of connections for each interface.
-  Check the jumper settings if it is applicable to the interface you are using. A full list of jumper settings can be found on the ezLINX® wiki homepage.
-  If the interface still isn't sending/receiving try disabling the interface, disconnecting the board and resetting the board.
