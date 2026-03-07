SDP-H1 Getting Started
======================

This page provides specific information to assist you with using the SDP board as part of your evaluation system.

Package Contents
----------------

Your EVAL-SDP-CH1Z board package contains the following items.

-  :adi:`EVAL-SDP-CH1Z <sdp>` board
-  1m USB Standard-A to mini-B cable
-  12V 30W wall wart

Contact the vendor where you purchased your SDP board or contact Analog Devices, Inc. if any item is missing.

PC Configuration
----------------

For correct operation of the SDP board, your computer must have the following minimum configuration

-  Windows XP Service Pack 2 32 bit, Windows Vista 32/64 bit, Windows 7 32/64 bit
-  USB 2.0 port

.. warning::

   The SDP board evaluation system contains ESD (electrostatic discharge) sensitive devices. Electrostatic charges readily accumulate on the human body and equipment and can discharge without detection. Permanent damage may occur on devices subjected to high-energy discharges. Proper ESD precautions are recommended to avoid performance degradation or loss of functionality. Store unused SDP boards in the protective shipping package.

   
   When removing the SDP board from the package, handle the board carefully to avoid the discharge of static electricity, which can damage some components.


USB Installation
----------------

Perform the following tasks to safely install the SDP board onto the computer.

There are two stages in the software application installation procedure. The first installs the application software. The second installs the .NET Framework 3.5 and the necessary drivers.

-  Run the application install provided. The first stage will install the Applications GUI and necessary support files onto the computer
-  Immediately following the application install, the .NET Framework 3.5 and the driver package for the SDP board is installed. If the .NET Framework 3.5 is already pre-installed on the computer in question, this stage will be skipped and step two will consist of a driver package installation only

Connecting the SDP-H1 Board to the PC
-------------------------------------

-  Attach the SDP-H1 board to a USB 2.0 port on the computer via the Standard-A to Mini-B cable provided.The SDP-H1 must be powered using the enclosed wall-wart power supply.

Verifying Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before using the SDP-H1 board, verify the driver software has installed properly.

-  Open the Windows Device Manager and verify the SDP-H1 board appears under ADI Development Tools as shown in figure GS1.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-h1/sdp-h1_dm.png
   :width: 200px

Figure GS1 : Device Manager showing correct SDP installation

Powering Up the SDP-H1 Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Connect the daughter board to the SDP-H1 board through either the 120-pin mating connector or the FMC connector (whichever is applicable).
-  Power the daughter board (May not be required for FMC daughterboards (mezzanine cards). See daughterboard documentation for further details).
-  Power the SDP-H1 board with the enclosed power supply.
-  Connect the USB port on the computer to the SDP-H1 board.

Powering Down the SDP-H1 Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Disconnect the SDP-H1 board power supply.
-  Disconnect any daughterboard power supplies.
-  Disconnect the USB port on the computer from the SDP-B board.
-  Disconnect the daughterboard from the SDP-H1 board.
