.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

Kernel Update Guide
===================

| The update process requires newer version of the kernel image file. The download links for these pieces of software are provided below:
| Latest Kernel Image File
| Quick 'n Easy FTP Server Software

Option 1: Flashing uImage through FTP
-------------------------------------

Once the latest uImage file has been downloaded, place it in a folder bearing the same name as the kernel version then rename the update file “uImage”. .

FTP Server Software Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

Open the “Quick 'n Easy FTP Server Software” application:

|image1| Navigate to the configuration menu by clicking on “show configuration” on the left-hand side of the application window:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/ftpserverconfiguration.jpg
   :align: center

In the PASV settings choose the IP address that matches the network that the ezLINX board is connected to using the drop-down menu.

Navigate to the user account menu by clicking on “show user accounts” on the left-hand side of the application window:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/useraccounts.jpg
   :align: center

Click on the “browse” button, select the directory where the image file is saved and click “OK”

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/browseforfolder.jpg
   :align: center

Navigate to the server log page by clicking on “show server log” on the left-hand side of the application window:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/servertrace.jpg
   :align: center

Click on the “start” button. A message will display in the server log to indicate that the FTP Server has been started:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/servertracestarted.jpg
   :align: center

Sending Update File Request From the ezLINX® PC Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the ezLINX® board to the host PC via the supplied USB cable and to the power supply via the supplied AC adapter.

Open the ezLINX PC application and navigate to the Board configuration window by clicking on the picture of the ezLINX board in the bottom left corner:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/PCApplicationInterface.jpg
   :align: center
   :width: 600px

Connect the ezLINX board by connecting to the same network.

Tick the box marked “Update Firmware” and in the box marked “server IP” type in the IP address used previously in the PASV settings (the address that was selected from the drop down menu). Click on the “send” button and a message will briefly display indicating that the update file has been sent and that the PC application should be reset. Now close the application window.

FTP Server Software Data Log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return to the server log window on the FTP server software. After a brief period of time the server log will fill with data:

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/UpdateComplete.jpg
   :align: center
   :width: 600px

The board will reset itself after a brief period of time.

Reconnecting to the ezLINX® PC Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Open the ezLINX PC application again and navigate to the board configuration screen by clicking on the picture of the ezLINX board in the bottom left-hand corner.
| Reset the board using SW1 on the board and wait for the board to reconnect. With the same IP address that was used earlier, connect to the board. Click on the "check" button and the updated embedded version will show:
| |image2|

The embedded version has now been updated.

Option 2: Flashing uImage through UART
--------------------------------------

To flash the ezLINX board through UART, follow the following steps:

-  Step 1: Connect the RS-232 port of the PC to the UART1 connector J4 of the board (If the PC does not contain an RS-232 port you may use an external USB converter)


|image3|

-  Step 2: Open HyperTerminal (Hyperterminal is delivered with windows XP and no longer exist with newer versions so we suggest to use TeraTerm instead) and set the Baud rate to 57600, Data bit :8, Parity: none, flow control :none,
-  Step 3: Upon turning on the board, uBoot is loaded and you should Press [Enter] or any key in the HyperTerminal within 5 sec to avoid auto-boot for the first time. Then you should see in the HyperTerminal the ‘bfin>’ prompt.

.. image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/flashingthroughUARThyperterminal.jpg
   :align: center

-  Step 4: Run the following command in HyperTerminal window.

::

     ''bfin> loadb'' \\ \\
     

| U Boot is now waiting for a Kermit connection to be made. Under the Transfer menu in HyperTerminal select Send File. The Send File dialog should now appear:
| |image4|

-  In the Filename field select the file to load onto the target.
-  In the Protocol field select Kermit.
-  Click Send.

| A dialog showing you the progress of the transfer should now be displayed:
| |image5|

| Once the transfer is complete you should be returned to the main HyperTerminal window and the U-Boot prompt. Run the following commands one by one in HyperTerminal window.
| ``bfin> protect off bank 1;erase 0x200A0000 0x206FFFFF;cp.b 0x1000000 0x200A0000 $(filesize); cmp.b 0x1000000 0x200A0000 $(filesize)  bfin> protect off bank 1;erase 0x20900000 0x20EFFFFF;cp.b 0x1000000 0x20900000 $(filesize); cmp.b 0x1000000 0x20900000 $(filesize)  bfin> set bootcmd run flashboot  bfin> save``
| Once these commands are executed the board is ready to boot from flash.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/ftpserver.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/ReconnectionofBoard.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/ez+PC.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/SendFiledialogwindow.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/kernelupdateguide/Sendprogresswindow.jpg
