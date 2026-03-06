SDP-K1 Getting Started
======================

This chapter provides specific information to assist you with using the SDP board as part of your evaluation system.

Package Contents
----------------

Your EVAL-SDP-CB1Z board package contains the following items.

-  :adi:`EVAL-SDP-CK1Z <sdp>` board
-  1m USB-C cable

Contact the vendor where you purchased your SDP board or contact Analog Devices, Inc. if any item is missing.

PC Configuration
----------------

For correct operation of the SDP board, your computer must have the following minimum configuration

-  Windows XP Service Pack 2 or Windows Vista
-  USB 2.0 port

.. warning::

   The SDP board evaluation system contains ESD (electrostatic discharge) sensitive devices. Electrostatic charges readily accumulate on the human body and equipment and can discharge without detection. Permanent damage may occur on devices subjected to high-energy discharges. Proper ESD precautions are recommended to avoid performance degradation or loss of functionality. Store unused SDP boards in the protective shipping package.

   
   When removing the SDP board from the package, handle the board carefully to avoid the discharge of static electricity, which can damage some components.


USB Installation
----------------

Perform the following tasks to safely install the SDP board onto the computer.

Prior to connecting an SDP-K1 to a PC, the daughter board evaluation software must be installed. Installation of this software ensures that all the required support files, the .NET Framework version, and USB drivers are installed.

Connecting the SDP Board to the PC
----------------------------------

-  Attach the SDP board to a USB 2.0 port on the computer via the Standard-A to USB-C cable provided.

Verifying Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before using the SDP board, verify the driver software has installed properly.

-  Open the Windows Device Manager and verify that the SDP-K1 appears under ADI Development Tools as shown in figure GS1.

.. image:: https://wiki.analog.com/_media/eval/sdp/fig1-1.jpg

Figure GS1 : Device Manager showing correct SDP installation

Powering Up/Down the SDP
~~~~~~~~~~~~~~~~~~~~~~~~

The following sections describe how to safely power up and down the SDP-K1. Failure to follow the following steps may result in damage.

Powering Up the SDP-K1 Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Consult the daughter board documentation to determine the input/output voltage requirements and the proper configuration of the VIO_ADJUST header. Ensure that the VIO_ADJUST header is configured properly before power

is applied to the system, otherwise, damage can be caused to the SDP-K1 and the daughter board.

-  Connect the daughter board to the SDP-K1 board through

either the 120-pin mating connector or the Arduino headers (whichever is applicable).

-  Power-up the daughter board if this is an option (see

daughter board documentation for further details).

-  Power-up the daughter board if this is an option (see

daughter board documentation for further details).

Powering Down the SDP-K1 Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Disconnect any daughter board power supplies
-  Disconnect the USB port on the computer from the SDP board
-  Disconnect the SDP board from the daughter evaluation board
