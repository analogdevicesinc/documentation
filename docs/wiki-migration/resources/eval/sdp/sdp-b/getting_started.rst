SDP-B Getting Started
=====================

This chapter provides specific information to assist you with using the SDP board as part of your evaluation system.

.. image:: http://www.analog.com/static/imported-files/images/Product_Descriptions/BF527SDP-HW_381x246.gif
   :alt: http://www.analog.com/static/imported-files/images/Product_Descriptions/BF527SDP-HW_381x246.gif

Package Contents
----------------

Your EVAL-SDP-CB1Z board package contains the following items.

-  :adi:`EVAL-SDP-CB1Z <sdp>` board
-  1m USB Standard-A to mini-B cable

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

There are two stages in the software application installation procedure. The first installs the application software. The second installs the .NET Framework 3.5 and the necessary drivers.

-  Run the application install provided. The first stage will install the Applications GUI and necessary support files onto the computer
-  Immediately following the application install, the .NET Framework 3.5 and the driver package for the SDP board is installed. If the .NET Framework 3.5 is already pre-installed on the computer in question, this stage will be skipped and step two will consist of a driver package installation only

Connecting the SDP Board to the PC
----------------------------------

-  Attach the SDP board to a USB 2.0 port on the computer via the Standard-A to Mini-B cable provided.

Verifying Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before using the SDP board, verify the driver software has installed properly.

-  Open the Windows Device Manager and verify the SDP board appears under ADI Development Tools as shown in figure GS1.

.. image:: https://wiki.analog.com/_media/eval/sdp/fig1-1.jpg

Figure GS1 : Device Manager showing correct SDP installation

Powering Up/Down the SDP
~~~~~~~~~~~~~~~~~~~~~~~~

The following sections describe how to safely power up and down the SDP.

Powering Up the SDP Board
^^^^^^^^^^^^^^^^^^^^^^^^^

-  Connect the SDP board to the daughter evaluation board through the 120 pin mating connectors.
-  Power the daughter board
-  Connect the USB port on the computer to the SDP board.

Powering Down the SDP Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Power down the daughter evaluation board
-  Disconnect the USB port on the computer from the SDP board
-  Disconnect the SDP board from the daughter evaluation board
