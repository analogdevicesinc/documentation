:doc:`Click here to return to 'SigmaStudio for SHARC - Quick start guide' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide>`

Hardware Setup
==============

| The SigmaStudio for SHARC (ADSP-SC5xx) demonstration setup includes a Host PC running SigmaStudio which is connected to the ADSP-SC573/ADSP-SC584/ADSP-SC589 Ez-Board. The connection is achieved using a USB-to-SPI converter. The EVAL-ADUSB2EBZ acts as the USB-to-SPI converter, which is connected to the PC through a USB port and to the Target Ez-Board through SPI lines. The basic steps to set up the Target for SigmaStudio for SHARC (ADSP-SC5xx) demonstration are given below. The setup required to run the demo application is illustrated in Figure 1 below. |image1|
| =====Hardware Switches/Connections.===== |image2|
| |image3|
| |image4|
| ====Connect EZ-BOARD to PC using USBi==== Connect EVAL-ADUSB2EBZ to the PC running SigmaStudio using a USB cable. The EVAL-ADUSB2EBZ (hereafter referred to as the ‘USBi’) has a 10 pin socket. This socket should be connect to the header P2 (marked SIGMASTUDIO) on EZ-BOARD. When connected, Pin 1 of the USBi socket should match pin 1 of header P2 on the EZ-BOARD. This connection is used to download SigmaStudio packets from host PC to the EZ-BOARD.
| The USBi to EZ-board connection (direction) is different across different EZ-Boards. Please refer to Figure 2, Figure 3 and Figure 4 above on how to connect to the specific EZ-Board.
| ====Connect to PC using ICE-2000/ICE-1000==== Connect ADZS-ICE-2000/ICE-1000 to the PC running SigmaStudio using a USB cable. In case of ADZS-ICE-2000, the ribbon cable of ICE-2000 should be connected to header P1 (marked DEBUG) on EZ-BOARD. In case of ICE-1000, connect header J2 of ICE-1000 directly to header P1 (marked DEBUG) on EZ-BOARD. This connection is used to download/debug/flash the framework to the target.
| ====Connect Audio Input and Output==== Connect an analog audio source and headphones/speakers to the audio ports on the EZ-KIT.
| ====Connect Power to the EZ-KIT==== Connect the power and reset the board by pressing the ‘RESET’ button on the EZ-BOARD.
| ====Switch/Jumper/Port Settings====

ADSP-SC584 EZ-BOARD
-------------------

The board settings for running SigmaStudio on ADSP-SC584 EZ-BOARD, using the Default Application is given in the table below.

====== ==========================
Switch Setting
====== ==========================
SW1    Position 0
SW6    ON, OFF, ON, OFF, ON, OFF
SW7    ON, OFF, ON, OFF, OFF, OFF
SW8    OFF,OFF
====== ==========================

| Table 2: Switch Settings for ADSP-SC584 EZ-BOARD
| ^ Jumper ^ Setting ^

=== =============
JP1 Not connected
JP2 Not connected
JP3 Not connected
JP4 Not connected
=== =============

| Table 3: Jumper Settings for ADSP-SC584 EZ-BOARD
| ^ Port ^ Setting ^

=== ================================
P2  Connected with SigmaStudio USBi
P3  Not connected
P12 Not connected
P17 Connected
P18 Connected
P20 Connected
P21 Connected
P24 Not connected
P25 Pins (3,4) (5,6) (7,8) Connected
=== ================================

| Table 4: Port Settings for ADSP-SC584 EZ-BOARD
| ===ADSP-SC589 EZ-BOARD=== The board settings for running SigmaStudio on ADSP-SC589 EZ-BOARD, using the Default Application is given in the table below.

====== ==========================
Switch Setting
====== ==========================
SW1    Position 0
SW5    ON, OFF, ON, OFF, ON, OFF
SW6    ON, OFF, ON, OFF, OFF, OFF
====== ==========================

| Table 5: Switch Settings for ADSP-SC589 EZ-BOARD
| ^ Jumper ^ Setting ^

=== =========
JP1 Connected
=== =========

| Table 6: Jumper Settings for ADSP-SC589 EZ-BOARD
| ^ Port ^ Setting ^

=== ====================================
P2  Connected with SigmaStudio USBi
P14 Connected
P15 Connected
P16 Connected
P17 Connected
P18 Connected
P19 Connected
P21 Connected
P23 All 3 pairs of jumpers are connected
=== ====================================

| Table 7: Port Settings for ADSP-SC589 EZ-BOARD
| ===ADSP-SC573 EZ-BOARD=== The board settings for running SigmaStudio on ADSP-SC573 EZ-BOARD, using the Default Application is given in the table below.

=== ==========================
SW1 Position 0
SW6 ON, OFF, ON, OFF, ON, OFF
SW7 ON, OFF, ON, OFF, OFF, OFF
SW8 OFF, OFF
=== ==========================

| Table 8: Switch Settings for ADSP-SC573 EZ-BOARD
| ^ Jumper ^ Setting ^

=== =============
JP1 Not connected
JP2 Not connected
JP3 Not connected
JP4 Not connected
=== =============

| Table 9: Jumper Settings for ADSP-SC573 EZ-BOARD
| ^ Port ^ Setting ^

=== ==================================
P2  Connected with SigmaStudio USBi
P17 Connected
P18 Connected
P20 Connected
P21 Connected
P24 Connected
P25 All pairs of jumpers are connected
=== ==================================

| Table 10: Port Settings for ADSP-SC573 EZ-BOARD

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_1.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_2.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_3.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide/ss4gquickguide_4.jpg
