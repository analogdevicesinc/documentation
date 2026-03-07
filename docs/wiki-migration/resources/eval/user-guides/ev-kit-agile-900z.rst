EV-KIT-AGILE-900Z
=================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/pkit_flyer_1.png

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/pkit_flyer_2.png

Description
-----------

AgileNet-6T is a sub GHz wireless mesh networking solution based on the 6TiSCH networking protocol. The EV-KIT-AGILE-900Z is the primary kit required to demo AgileNet-6T.

Evaluation kit contents
-----------------------

-  8 EV-MTE-AGILE-900Z evaluation boards. These boards are mainly used as the network nodes.
-  2 EV-COG-AGILE-900Z evaluation boards. These boards can act as nodes or the access points (APs) for the network and flash the EV-MTE-AGILE-900Z evaluation boards.
-  EV-GEAR-EXPANDER1Z add on board. This board brings out the general-purpose input/output (GPIO) lines from the EV-COG-AGILE-900Z evaluation board. The EV-GEAR-EXPANDER1Z board helps the user debug an application more effectively.
-  10 antenna pigtails.
-  10 antennas.
-  10-pin ribbon cable.
-  8 Li batteries, 3.6 V AA size.

Evaluation board hardware
-------------------------

EV-COG-AGILE-900Z
~~~~~~~~~~~~~~~~~

The EV-COG-AGILE-900Z evaluation board is used for development purposes. The board provides a J-Link® and additional Arm® Mbed™ interface to flash and debug the on-board microcontroller unit (MCU). The J-Link interface can also debug the on-board radio.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig2_final.png
   :width: 400px

Figure2. EV-COG-AGILE-900Z

The EV-COG-AGILE-900Z board enables the user to track and profile the live current consumption of the board. For more information on the hardware aspects of the EV-COG-AGILE-900Z board, refer to the EV-COG-AGILE-900Z Hardware Reference Manual.

EV-MTE-AGILE-900Z
~~~~~~~~~~~~~~~~~

The EV-MTE-AGILE-900Z evaluation board can be used to deploy and rapidly prototype user defined applications with the AgileNet-6T solution. The EV-MTE-AGILE-900Z board provides a J-Link interface to flash and debug the MCU. For more information on the hardware aspects of the EV-MTE-AGILE-900Z board, refer to the EV-MTE-AGILE-900Z Hardware Reference Manual.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig3_final.png
   :width: 400px

Figure3. EV-MTE-AGILE-900Z

SOFTWARE QUICK START GUIDE
--------------------------

AgileNet-6T software package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install the AgileNet-6T software package by following the steps provided in the :doc:`AgileNet-6T wiki page </wiki-migration/resources/eval/user-guides/agilenet6t>`.

Elements provided in the software package-

The following firmware tests LED functionality:

-  01bsp_led_blue.hex.
-  01bsp_led_green.hex.
-  01bsp_led_red.hex.

The following firmware and software perform range testing, which is testing the effect of distance between two nodes in a network:

-  01bsp_radio_tx.hex: firmware to be loaded on the transmitting device, which, depending on user preference, can either be the EV-MTE-AGILE-900Z board or the EV-COG-AGILE-900Z board.
-  01bsp_radio_rx.hex: firmware to be loaded on the receiving device, the EV-COG-AGILE-900Z board.
-  01bsp_radio_rx.exe: software that communicates with the receiving device and prints statistics related to the range testing.
-  The following firmware and software build networks (see the Networking section):
-  03oos_agilenet_pkgen.hex: loads firmware on all the devices the user wants in the network.
-  AgileNet.exe: contains software that connects to the APs in the network and displays network information (see the Networking section).
-  PkGenClient.exe: contains an example application that interacts with nodes in the network using the HTTP/JSON interface of the AgileNet.exe, and displays packet information, statistics, and other information (see the Networking section).

SETTING UP THE EVALUATION BOARDS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Programming the EV-COG-AGILE-900Z Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Program the EV-COG-AGILE-900Z board with the hex/binary file provided in the software package by completing the following steps:

-  Ensure the antenna is connected to the EV-COG-AGILE-900Z board, as shown in Figure 4. Note that excluding the antenna may potentially damage the board.
-  To connect the EV-COG-AGILE-900Z evaluation board to the PC, connect the microUSB end of the USB to microUSB cable to the board and connect the USB end to the PC. The necessary drivers are downloaded when using the Windows operating system (OS).
-  After the drivers are installed, a new drive named DAPLINK appears on the PC (see Figure 5). This is a virtual drive that the EV-COG-AGILE-900Z creates and allows the user to reprogram using a drag and drop method.
-  Open the DAPLINK drive and drag and drop the firmware image (.hex file), provided in the software package, from the computer onto this drive.
-  After the file is copied, the file disappears and then reappears from the DAPLINK window indicating that the new firmware has been flashed.
-  Press the middle button labeled RST on the EV-COG-AGILE-900Z to reset the board and to run the new firmware.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig4_final.png
   :width: 400px

Figure 4. EV-COG-AGILE-900Z with Antenna Connected

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig5_final.png
   :width: 400px

Figure 5. DAPLINK Drive

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig6_final.png
   :width: 400px

Figure 6. Flashing through Drag and Drop Procedure

Programming the EV-MTE-AGILE-900Z Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Program the EV-MTE-AGILE-900Z board with the hex/binary file provided in the software package by completing the following steps:

-  Ensure the antenna is connected to the EV-MTE-AGILE-900Z evaluation board, as shown in Figure 7. Note that excluding the antenna may potentially damage the board.
-  Ensure both boards are disconnected from any power source. The USB cable must be disconnected from the EV-COG-AGILE-900Z board and the battery must be removed from the EV-MTE-AGILE-900Z board.
-  Install a ribbon cable between the 10-pin header (P26) on the EV-COG-AGILE-900Z board and the 10-pin header on the EV-MTE-AGILE-900Z board (P6). Figure 8 shows how to connect the two boards.
-  Remove Jumper JH6 from the back of the EV-COG-AGILE-900Z board. Removing the jumper instructs the EV-COG-AGILE-900Z to program an external board (the EV-MTE-AGILE-900Z board in this case), instead of the on-board module.
-  Power up the two boards. Connect the EV-COG-AGILE-900Z board to a PC using a USB to microUSB cable and connect the battery to the EV-MTE-AGILE-900Z board.
-  After the DAPLINK drive appears on the PC, perform the same drag and drop operation as detailed in Step 4 in the Programming the EV-COG-AGILE-900Z Board section.
-  After resetting the board by pressing the on-board button labeled RST, reinstall the JH6 jumper (removed in Step 4) to flash the EV-COG-AGILE-900Z board at any later point.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig7_final.png
   :width: 400px

Figure 7. EV-MTE-AGILE-900Z with Antenna Connected

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig8_final.png
   :width: 400px

Figure 8. Connecting the EV-MTE-AGILE-900Z Evaluation Board to the EV-COG-AGILE-900Z Evaluation Board

VERIFYING THE DOWNLOAD
^^^^^^^^^^^^^^^^^^^^^^

The basic firmwares shown in Table 1 verify if the EV-COG-AGILE-900Z and EV-MTE-AGILE-900Z boards are successfully flashed. Each firmware blinks one of the three LEDs on either evaluation board. If the LED blinks, this indicates that the flashing is successful.

Table 1

NETWORKING
----------

The AgileNet-6T solution can create a mesh network with several nodes, which are the boards in the network. The network is made up of either the EV-MTE-AGILE-900Z board or the EV-COG-AGILE-900Z board as a transmitting device, depending on user preference, and an access point, typically the EV-COG-AGILE-900Z board connected to the PC. See Figure 12 for a diagram of the network setup.

OVERVIEW
~~~~~~~~

All evaluation boards must be flashed with the same firmware (03oos_openwsn_pkgen.hex). Users must run AgileNet.exe and PkGenClient.exe, provided in the AgileNet-6T software package, on the PC. AgileNet.exe configures one of the devices as the AP of the network based on the serial port the user enters. All other boards act as nodes in the network. When running the default firmware, 03oos_openwsn_pkgen.hex, each node contains the following:

-  An application that publishes a data packet containing an ever incrementing counter every minute.
-  A protocol stack that publishes the following every minute:

   -  A health report containing internal counters
   -  A routing update containing the routing parent of the node

The AgileNet.exe application performs the following actions using the data packets from the nodes:

-  Based on the received health reports, the application maintains a copy of the latest counter for each node that is queried with the steps listed in the Command Line Interface section.
-  Based on the routing updates, AgileNet.exe maintains information about the topology of the network and supplies a web interface for the user to visualize the network topology. This web interface is accessed with the information in the Web Interface section.

The PkGenClient.exe application executes the following:

-  Receives the periodic data packets from nodes.
-  Changes the publication period or turns off publication for nodes.
-  Triggers an echo request and response interaction with any node.
-  Displays reliability and latency statistics for the network.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig10_final.png
   :width: 400px

Figure 10. Using the Device Manager Port List to Identify COM Port

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig12_final.png
   :width: 400px

Figure 12. Network Setup

NETWORK FORMATION
~~~~~~~~~~~~~~~~~

The following procedure allows the user to create a network with the EV-COG-AGILE-900Z board and the EV-MTE-AGILE-900Z board as nodes:

-  Load the 03oos_openwsn_pkgen.hex firmware on all nodes, either the EV-COG-AGILE-900Z board or the EV-MTE-AGILE-900Z board.
-  Connect the EV-COG-AGILE-900Z board to the PC to use the board as an AP.
-  Identify the serial port assigned to the AP (EV-COG-AGILE-900Z) by opening the Windows Device Manager and selecting the Ports (COM & LPT) dropdown list (see Figure 10) to view all ports connected to the PC.A new port is added when the AP is powered on while connected to the PC. This port disappears if the AP is powered off. Note that the new port is the serial port assigned to the AP.
-  Start the AgileNet.exe firmware on the computer by double clicking the file.
-  After the banner shown in Figure 13 prints, enter the serial port of the EV-COG-AGILE-900Z board connected to the PC and press the Enter key.

The following actions occur after completing the previous steps:

-  The green LED (DS4) of the AP device switches on.
-  Shortly thereafter, the green LEDs (DS3) of the nodes switch on, indicating that the nodes are synchronized to the network. Because of the way the synchronization is done, it is normal for the nodes not to synchronize with the network at the same time.
-  Up to a minute after synchronizing, the node starts publishing the data packets, health reports, and routing updates.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig13_final.png
   :width: 400px

Figure 13. AgileNet.exe Initialization

COMMAND LINE INTERFACE (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AgileNet.exe application contains a CLI for user interaction. The CLI uses the following commands:

-  Type help to see the list of available commands. The commands in Figure 14 show the alias of each command in parenthesis.
-  The info command prints the internal state of the AgileNet.exe application.
-  The uptime command indicates how long the application has been running.
-  The trace command allows users to view all messages received from the network. Each message appears on the CLI of AgileNet.exe in a different color (see Figure 18). The elements printed without highlight are internal messages. For each packet received, the AgileNet.exe software plays a beep, as detailed in Table 3.
-  The hr command shows the latest counters contained in the health reports generated by the nodes and the counters are grouped per category for easier reading. Given how the health reports are generated, it takes approximately three minutes for all counters to refresh.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig14_final.png
   :width: 400px

Figure 14. AgileNet.exe help Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig15_final.png
   :width: 400px

Figure 15. AgileNet.exe info Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig16_final.png
   :width: 400px

Figure 16. AgileNet.exe uptime Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig17_final.png
   :width: 400px

Figure 17. AgileNet.exe trace Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig18_final.png
   :width: 400px

Figure 18. Network Status

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig19_final.png
   :width: 400px

Figure 19. AgileNet-6T.exe hr Command

WEB INTERFACE
~~~~~~~~~~~~~

By navigating a web browser to http://127.0.0.1:8888, the user can find a visualization of the current topology of the network (see Figure 20).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig20_final.png
   :width: 400px

Figure 20. Topology of the AgileNet-6T Network Viewed via the Web Interface

HTTP/JSON INTERFACE
~~~~~~~~~~~~~~~~~~~

PkGenClient.exe
^^^^^^^^^^^^^^^

The PkGenClient.exe application runs on the PC and allows the user to interact with the PkGen application that runs on the nodes. The PkGenClient.exe application uses the HTTP/JSON application program interface of the AgileNet.exe application to interact with the nodes of the network.

Ensure that AgileNet.exe is running before attempting to use PkGenClient.exe. Start the PkGenClient.exe firmware on the PC by double clicking the file and wait for the banner to be shown (see Figure 21).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig21_final.png
   :width: 400px

Figure 21. PkGenClient.exe Initialization

Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^

The PkGenClient.exe application has a CLI for user interaction. The CLI uses the following commands:

-  Type help to see the list of available commands. The commands in Figure 22 show the alias of each command in parentheses.
-  The trace command allows users to view the messages received from the application running in the nodes. (see Figure 17 and Figure 23).
-  The poll command allows the user to trigger an echo request and response interaction with each node in a round-robin fashion (See Figure 24). To view the request/response packets during polling, trace needs to be on. The PkGenClient.exe only discovers a node after receiving a periodic data packet. Therefore, the user must wait for a period to discover all the motes and poll them. If periodic data generation is disabled in a node, the node cannot be polled.
-  The stats command prints the network statistics such as reliability, round trip time (RTT), and number of packets lost (see Figure 25).

   -  Column 1, Column 2, and Column 3 in Figure 25 relate to the periodic data packets (periodic_num_received, num\_
   -  lost, \_reliability and \_lastcounter).
   -  Column 4, Column 5, and Column 6 relate to the polling packets (echo_num_received, \_num_lost, \_reliability, and \_rtt (min/avg/max)).
   -  Column 7, last_heard, indicates the time the last periodic data packet was received by the nodes.
   -  Column 8, version, shows the version of the firmware running on each node.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig22_final.png
   :width: 400px

Figure 22. PkGenClient.exe help Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig23_final.png
   :width: 400px

Figure 23. PkGenClient.exe trace Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig24_final.png
   :width: 400px

Figure 24. PkGenClient.exe poll Command

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-kit-agile-900z/fig25_final.png
   :width: 400px

Figure 25. PkGenClient.exe stats Command

Additional resources
--------------------

:doc:`AgileNet-6T wiki page </wiki-migration/resources/eval/user-guides/agilenet6t>`
