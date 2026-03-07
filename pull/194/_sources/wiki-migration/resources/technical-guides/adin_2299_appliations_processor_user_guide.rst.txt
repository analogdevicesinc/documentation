ADIN 2299 Applications Processor User Guide
===========================================

FEATURES
--------

-  Interacts with RPG2 as the Applications Processor in a system.

   -  Handles Unified Interface communication between the applications(The user has a choice for this) and communications processor (ADSPCM-409)

EQUIPMENT NEEDED
----------------

-  Ethernet cable
-  UART cable
-  SPI cable(for Embedded ST32 environment)

DOCUMENTS NEEDED
----------------

-  ADIN2299 User Guide

SOFTWARE NEEDED
---------------

-  ni-example-app Executable
-  Visual Studio
-  STM32 Cube IDE
-  Access to GIT

GENERAL DESCRIPTION With the RPG2 evaluation kit, there is a need to have a host processor initialize/interact with the evaluation kit.

The ni-example-app source code does just this. It interacts with RPG2 as a sample host processor. This is literally a starting point for interacting with RPG2. The end user is by no means limited to just the PC acting as the host, or the STM32 acting as the host.

The actual app can be run on any processor once the LPL has been created for the host processor with a given link type.

What this guide is going to walk a user through is how to build and interact with the ni-example-app out of the box. Customizations are expected but those topics are covered in detail in other documents(the RPG2 Unified Interface User Guide and the RPG2 IO Configuration Tool User Guide).

Once the ni-example-app has been built either for the PC , the app can be used from the PC as the host to do the corresponding quickstart guides for RPG2, as well as further customizations if necessary.

Revision History
~~~~~~~~~~~~~~~~

Initial Release

NI-EXAMPLE-APP GENERAL
~~~~~~~~~~~~~~~~~~~~~~

Ni-example-app is distributed with both a version for a windows executable and an STM32 example. Any platform can work as the layers common to the Unified Interface are the same both for RPG2 and the host platform. Figure 1 shows the breakdown of layers in ni-example-app.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_1.png
   :align: center

Figure 1:Network Applications IO Suite General Use Case

The ni-example-app software suite basically constructs what is known as a host processor application with the following high level tasks being done for a given platform/system.

::

    •    Calls to ui-init
    o    This initializes the ui-stk on the host platform.   
    •    Link type initialization
    o    This sets up the link type that shall be used.

::

    •    Set the response timeout
    o    This sets up the link between the host and RPG2. 
    o    This can vary from platform to platform.
    •    Wait for the signal SDONE to go high.
    o    This signal goes high when RPG2 is ready to receive commands.
    o    This one may or may not be needed but it is highly recommended to install between RPG2 and the host processor.
    •    Send out the NI-Discover message
    o    This expects an echo of the discover almost like a ping.
    •    Send out the NI-Init message 
    o    This tells RPG2 to initialize and be ready for further communication.
    o    There is some warning in the ni-example-app for ui-stk compatibility.
    •    Resets RPG2 from the Host Processor side.
    o    This is done for the purposes of reprogramming RPG2. Finalized devices might be able to do well without this command.
    •    Enable profile
    o    This is usually for specific Industrial Ethernet Profile not discussed in this guide.
    •    Enter the Event Handler
    o    This is a while 1 loop where events are continuously processed.

Inside of the Event handler, there are several different events that need to be handled.

::

    •    UI Synch State
    •    UI System Event
    •    UI Config Request
    •    UI Item out Data
    •    UI Item in Data Latch
    •    UI Http Tunnel Request
    •    UI Acyclic out Data
    •    UI IO mapping request
    •    UI Device State Change

What all of this does is the following tasks:

::

    •    Makes use of a Host Processor to initialize RPG2 regardless of the protocol in place.
    o    This allows for the QSG to be run.
    •    Once it is “network initialized” it will take the output data written to it from the PLC and echo it back on the input
    o    This is for the example application. The user’s actual application will operate differently.

=========== =========== ==========
Item Number Output size Input size
=========== =========== ==========
500         2           2
501         4           4
502         2           0
=========== =========== ==========

This allows for basic ladder logic construction and all of the QSGs essentially make an echo routine from host out to the network and back again.

NI-EXAMPLE-APP EVALUATION KIT RPG2 PIN POSITIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 1 shows a user how to hook up miscellaneous pins to use a given link type when having the PC act as the Applications Processor.

+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signal      | Connector | Pin Number | Notes                                                                                                                                                                                                                                                                                                      |
+=============+===========+============+============================================================================================================================================================================================================================================================================================================+
| UART - RX   | 604       | 9          | Dual purpose. If UART is selected it will be UART-RX. If SPI is selected this will be the BUSY Signal.                                                                                                                                                                                                     |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UART TX     | 604       | 10         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI MOSI    | 604       | 1          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI MISO    | 604       | 2          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI CLK     | 604       | 3          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI SS      | 604       | 4          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI - RREQ  | 604       | 7          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SPI-BUSY    | 604       | 9          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ethernet    | 302       | -          | This is an Ethernet Cable.                                                                                                                                                                                                                                                                                 |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDONE       | 604       | 12         | This signal goes high the moment RPG2 is ready to receive commands over the given link type.                                                                                                                                                                                                               |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reset       | 604       | 13         | This is the reset in pin for the ADIN2299.                                                                                                                                                                                                                                                                 |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3.3 V       | 603       | 7          | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5 V         | 603       | 11         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 602       | 14         | Not all grounds are needed.                                                                                                                                                                                                                                                                                |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 602       | 15         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 602       | 16         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 603       | 10         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 604       | 11         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 605       | 15         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND         | 605       | 16         | -                                                                                                                                                                                                                                                                                                          |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Type 0 | JP600     | -          | Link Types 0-2 are done to select which Link type is being used by RPG2. A user can also specify this with the Link Configuration File. The software will use the pins unless it is directed by means of an installed link configuration file. The default for the board is to use the Ethernet link type. |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Type 1 | JP601     | -          |                                                                                                                                                                                                                                                                                                            |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Type 2 | JP602     | -          |                                                                                                                                                                                                                                                                                                            |
+-------------+-----------+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Table 1: Pins for using the PC as the Applications Processor

For the purposes of running this example on the PC, the user will either use the UART or Ethernet link type.

NI-Example-App on a PC
~~~~~~~~~~~~~~~~~~~~~~

The pre-distributed ni-example-app runs on a PC out of the box. There are many different options that can be done as part of the ni-example-app on a command line. This can be done by navigating on a command line to the location of ni-example-app and putting in the -h in order to get the options.

Note that for the purposes of the protocol specific quickstart guides(EtherNet/IP, Profinet, etc) the simplest version of ni-example-app was used.

|image1| Figure 2: Navigating to location for ni-example-app

Seeing the options shown by this command sends out the following configuration options.

+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Syntax         | Command                                        | Argument                                           | Result                                                                                                                                                                        |
+================+================================================+====================================================+===============================================================================================================================================================================+
| -l             | Link Type                                      | UART / ETH                                         | The link type will be either Ethernet or UART.                                                                                                                                |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -c             | COM Port                                       | X where X is the com port number                   | The UART is used on the given USB/UART.                                                                                                                                       |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -n             | devString                                      | The syntax for the Ethernet Host Interface         | The Ethernet traffic goes out on the given RJ-45 connection.                                                                                                                  |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -h             | Help                                           | -                                                  | Displays the help section.                                                                                                                                                    |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -b             | Use the example Basket for configuration       | The Basket in place from the IO configuration Tool | The Host will use the “add Basket” method to configure RPG2.(Note that this basket is 1000. If another basket is in place, make sure to use that number.                      |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --no-reset     | There is no reset sent from the Host Processor | -                                                  | The Host will not send a reset to RPG2 during initialization.                                                                                                                 |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --no-configure | Don’t Configure RPG2                           | -                                                  | The Host will not do any configuration of RPG2 upon usage.                                                                                                                    |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --file-save    | Update or create the file on the file system   | --file-save “Module path” “Local path”             | This basically allows the user to put files onto the file system from the host processor. There are many applications to this. More is discussed in the ADIN2299 User's Guide |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --file-get     | Get file system content.                       | --file-get “Module path” “Local path”              | This allows the user to get content as it exists on the file system.                                                                                                          |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --file-delete  | Remove a file from the file system             | --file-delete “module path”                        | Deletes a file from the file system.                                                                                                                                          |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --file-mark    | Mark a file for an update on the file system   | --file-mark “module path”                          | Use this as a mark to update upon reset of RPG2.                                                                                                                              |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --file-listing | Get the contents of the file system            | --file-listing “”                                  | Gets the contents of the file system as they appear.                                                                                                                          |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --tcp-server   | Opens a TCP Server on the ADIN2299             | Local Port                                         | Open's a TCP Server on the local port.                                                                                                                                        |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --tcp-client   | Opens a TCP Client on the ADIN2299             | Local Port                                         | Open's a TCP Client on the local port.                                                                                                                                        |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --udp-server   | Opens a UDP Server on the ADIN2299             | Local Port                                         | Open's a UDP Server on the local port.                                                                                                                                        |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --udp-client   | Opens a UDP Client on the ADIN2299             | Local Port                                         | Open's a UDP Client on the local port.                                                                                                                                        |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --enable-dhcp  | Enables DHCP                                   | -                                                  | Makes the device use DHCP                                                                                                                                                     |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| --static-ip    | Gives a static IP address                      | IP Address, Subnet, Gateway, DNS1, DNS2, Domain    | The IP address is mandatory but the others are all optional.                                                                                                                  |
+----------------+------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Table 2: Command Line Help Display

CONNECTING THE EVALUATION KIT TO THE PC.
----------------------------------------

There is more information associated with how to connect this device in the following Quickstart Guides.

::

    •    RPG2 EtherCAT Quickstart Guide
    •    RPG2 Profinet Quickstart Guide
    •    RPG2 Ethernet/IP Quickstart Guide
    •    RPG2 Modbus/TCP Quickstart Guide

Please refer to these documents for how to use them from the network perspective.

Shown below are two of the ways that this can be connected for evaluation.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_3.png
   :align: center

Figure 3: Setup fora UART interface with ni-example-app.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_4.png
   :align: center

Figure 4: Setup for an Ethernet interface with ni-example-app

BUILDING THE NI-EXAMPLE-APP ON THE PC
-------------------------------------

The example application for Windows is called ni-example-app. This application is an application processor simulator that contains the needed API calls to interact with the Communications Controller. The ni-example-app application can be downloaded from the Analog Devices, Inc., Chronous Developer Portal. Extract the zipped file to a local directory and navigate to ..\\ni-example-app\\project\\vs\\ni-example-app. Open ni-example-app.sln with Visual Studio 2015 or later. The Solution Explorer will show the following five projects:

::

    •    ni-api-srv
    •    ni-example-app
    •    ni-windows-support-srv
    •    ui-stk
    •    ui-windows-lpl-srv

If not already selected, select ×86 as the Solution Platform. Specifying the Endianness To specify the endianness, take the following steps:

::

    -    In the Solution Explorer, right-click ui-stk. 
    -    Under Configuration Properties, expand C/C++. 
    -    Select Preprocessor.
    -    Select Preprocessor Definitions (see Figure 4).
    -    Click the dropdown arrow and select <Edit…>.

The default definition is UI_LITTLE_ENDIAN. A preprocessor definition is required either UI_LITTLE_ENDIAN or UI_BIG_ENDIAN. For a Windows platform, little endian is expected. For an embedded processor, endianness is something that varies depending on the application processor chosen.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_5.png
   :align: center

Figure 5: Specifying the Endianness of the Applications processor

Setting the Command Arguments
-----------------------------

To set the Command Arguments, take the following steps:

-  In the Solution Explorer, right-click ni-example-app.
-  Under Configuration Properties, select Debugging.
-  Select Command Arguments.

Click the dropdown arrow and select <Edit…>.

Ethernet as Application Processor Interface
-------------------------------------------

To set the Ethernet as an application processor interface, take the following steps:

-  To see all available network devices, enter -l ETH under Command Arguments (see Figure 5).
-  Click Apply
-  Click OK
-  Press Ctrl + Shift + B to build the solution.
-  Press Ctrl + F5 to start without debugging.

Take the following steps to set the Ethernet Command Arguments:

-  Select the appropriate network device and change the Command Arguments to -l ETH -n \\Device\\NPF\_ {E26E29A0-5899-4925-B0EF-2499B98570C8}.
-  Click Apply.
-  Click OK.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_6.png
   :align: center

Figure 6: Setting arguments for the Ethernet Application processor interface.

UART as Application Processor Interface
---------------------------------------

To set the UART as an application processor interface, take the following steps:

-  Open the Device Manager and expand the Ports (COM & LPT) section. A list of two Silicon Labs dual CP2105 USB to UART bridge: enhanced COM ports appears as follows:

   -  Silicon Labs Dual CP2105 USB to UART Bridge: Enhanced COM Port (COM6)

      -  Silicon Labs Dual CP2105 USB to UART Bridge: Standard COM Port (COM7)

-  Note the name of the enhanced COM port and enter -l UART -c COM6 under Command Arguments.
-  Click Apply.
-  Click OK.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_7.png
   :align: center

Figure 7: UART Command Line Arguments

The item and device constructs are the default values for the predistributed sample industrial Ethernet configuration database. For more information, see the ADIN2299 User Guide for more details on this.. While not in the Console display, once the user has called the configuration complete in the application processor code, the user then must make calls specific to the inputs and outputs as shown in Table 3 (NI_SetInputData and NI_GetOutputData). The program then continuously calls the NI_ProcessEvents() function to process events. Inside of NI_ProcessEvents() there is an input data subroutine and an output data subroutine.

NI-EXAMPLE-APP STM32
~~~~~~~~~~~~~~~~~~~~

BUILDING THE NI-EXAMPLE-APP FOR THE STM32 CUBE
----------------------------------------------

The ni-example-app suite can be built for any particular host processor. This set of instructions walks a user through how to do this for the STM32 CUBE.

The signals to connect when running the ni-example-app on the PC are shown in the table below.

+-------------+----------------+--------------+--------------+-----------------+---------------+
| EVAL Signal | EVAL Connector | EVAL Pin No. | STM32 Signal | STM32 Connector | STM32 Pin No. |
+=============+================+==============+==============+=================+===============+
| UART-RX     | 604            | 9            | UART-RX      | C9              | 25            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| UART-TX     | 604            | 10           | UART-TX      | C9              | 27            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-MOSI    | 604            | 1            | SPI-MOSI     | CN-7            | 12            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-MISO    | 604            | 2            | SPI-MISO     | CN-7            | 14            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-CLK     | 604            | 3            | SPI-CLK      | CN-7            | 15            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-SS      | 604            | 4            | SPI-SS       | CN-7            | 17            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-RREQ    | 604            | 7            |              | CN-9            | 7             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-BUSY    | 604            | 9            |              | CN-9            | 9             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ethernet    | 302            | -            | Ethernet     | CN-14           | -             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SDONE       | 604            | 12           | SDONE        | CN-8            | 14            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| RESET       | 604            | 13           | RESET        | CN-9            | 29            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| LINK TYPE   | JP600          | 0 or 1       |              | CN-9            | 4             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| LINK TYPE   | JP601          | 0 or 1       |              | CN-9            | 6             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| LINK TYPE   | JP602          | 0 or 1       |              | CN-9            | 8             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 14           | Ground       | CN-7            | 8             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 15           | Ground       | CN-8            | 11            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 16           | Ground       | CN-8            | 13            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 603            | 10           | Ground       | CN-9            | 12            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 604            | 11           | Ground       | CN-9            | 23            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 605            | 15           | Ground       | CN-10           | 5             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 605            | 16           | Ground       | CN-10           | 17            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| -           | -              | -            | Ground       | CN-10           | 22            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| -           | -              | -            | Ground       | CN-10           | 27            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 3.3V        | 603            | 7            | 3.3V         | CN-8            | 7             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 5V          | 603            | 11           | 5V           | CN-8            | 9             |
+-------------+----------------+--------------+--------------+-----------------+---------------+

This version of ni-example-app can run for any link type between RPG2 and the STM32. Connections required for a given link type are shown (as an example) for three different types below.

Connecting for an Ethernet Link Type
------------------------------------

+-------------+----------------+--------------+--------------+-----------------+---------------+
| EVAL Signal | EVAL Connector | EVAL Pin No. | STM32 Signal | STM32 Connector | STM32 Pin No. |
+=============+================+==============+==============+=================+===============+
| Ethernet    | 302            | -            | Ethernet     | CN-14           | -             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SDONE       | 604            | 12           | SDONE        | CN-8            | 14            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| RESET       | 604            | 13           | RESET        | CN-9            | 29            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 3.3V        | 603            | 7            | 3.3V         | CN-8            | 7             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 5V          | 603            | 11           | 5V           | CN-8            | 9             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 14           | Ground       | CN-7            | 8             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 15           | Ground       | CN-8            | 11            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 16           | Ground       | CN-8            | 13            |
+-------------+----------------+--------------+--------------+-----------------+---------------+

The link type is determined by setting the pins as shown in figure 8.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_8.png
   :align: center

Figure 8: Pin Setting for the Ethernet Interface.

========= ===== =
Link Type JP600 0
Link Type JP601 0
Link Type JP602 0
========= ===== =

Connecting for a UART link type
-------------------------------

+-------------+----------------+--------------+--------------+-----------------+---------------+
| EVAL Signal | EVAL Connector | EVAL Pin No. | STM32 Signal | STM32 Connector | STM32 Pin No. |
+=============+================+==============+==============+=================+===============+
| UART-RX     | 604            | 9            | UART-RX      | C9              | 25            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| UART-TX     | 604            | 10           | UART-TX      | C9              | 27            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SDONE       | 604            | 12           | SDONE        | CN-8            | 14            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| RESET       | 604            | 13           | RESET        | CN-9            | 29            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 3.3V        | 603            | 7            | 3.3V         | CN-8            | 7             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 5V          | 603            | 11           | 5V           | CN-8            | 9             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 14           | Ground       | CN-7            | 8             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 15           | Ground       | CN-8            | 11            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 16           | Ground       | CN-8            | 13            |
+-------------+----------------+--------------+--------------+-----------------+---------------+

The link type is determined by setting the pins as shown in figure 9.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_9.png
   :align: center

Figure 9: Pin Setting for the UART Interface.

========= ===== =
Link Type JP600 1
Link Type JP601 0
Link Type JP602 0
========= ===== =

Connecting for a SPI link type
------------------------------

+-------------+----------------+--------------+--------------+-----------------+---------------+
| EVAL Signal | EVAL Connector | EVAL Pin No. | STM32 Signal | STM32 Connector | STM32 Pin No. |
+=============+================+==============+==============+=================+===============+
| SPI-MOSI    | 604            | 1            | SPI-MOSI     | CN-7            | 12            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-MISO    | 604            | 2            | SPI-MISO     | CN-7            | 14            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-CLK     | 604            | 3            | SPI-CLK      | CN-7            | 15            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-SS      | 604            | 4            | SPI-SS       | CN-7            | 17            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-RREQ    | 604            | 7            |              | CN-9            | 7             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SPI-BUSY    | 604            | 9            |              | CN-9            | 9             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| SDONE       | 604            | 12           | SDONE        | CN-8            | 14            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| RESET       | 604            | 13           | RESET        | CN-9            | 29            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 3.3V        | 603            | 7            | 3.3V         | CN-8            | 7             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| 5V          | 603            | 11           | 5V           | CN-8            | 9             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 14           | Ground       | CN-7            | 8             |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 15           | Ground       | CN-8            | 11            |
+-------------+----------------+--------------+--------------+-----------------+---------------+
| Ground      | 602            | 16           | Ground       | CN-8            | 13            |
+-------------+----------------+--------------+--------------+-----------------+---------------+

The link type is determined by setting the pins as shown in figure 10.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_10.png
   :align: center

Figure 10: SPI Pin Strapping

========= ===== =
Link Type JP600 0
Link Type JP601 1
Link Type JP602 0
========= ===== =

BUILDING THE STM32 EXAMPLE APPLICATION
--------------------------------------

When you have checked out the STM32 example application, the software needs to be built to run on the STM32 on the user’s environment. The first step is to checkout the ni-example-app and set up the environment.

RUNNING THE NI-EXAMPLE-APP FOR THE STM32 CUBE
---------------------------------------------

From the main screen as shown below, the user will click on the debug symbol.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_11.png
   :align: center

Figure 11: Host Processor root directory

Open a Git Bash where the project is located.

.. image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_12.png
   :align: center

Figure 12: Opening a Git Bash

Type the following into the GIT Bash to checkout project files for the STM32. git clone -b v1.16.2 https://github.com/STMicroelectronics/STM32CubeF7.git

|image2| Figure 13: Entering Commands into the Git Bash.

This particular step takes a while, but once it is done you will see the project directory as shown.

|image3| Figure 14: Directory after running the git bash.

Open the STMCUBE IDE. Navigate to “C:\\Users\\cstelmar\\Desktop\\Documentation\\RapID_NI_Example_Applications_Software_Suite-Rel6.0.2\\example-application\\ni-example-app\\project\\cubeide\\STM32F767ZI” Or equivalent depending on where you have decided to store the project.

|image4| Figure 15: Select Workspace Directory.

Click “Select Folder”

|image5| Figure 16: Navigating to the Project.

Click on “Launch”

|image6| Figure 17: STM Home Screen.

Click on the “Information Center” tab at the top.

|image7| Figure 18: Selecting file import options.

From this point go to “File/Import”. |image8| Figure 19: Import Wizard.

From here click on “General\\Existing Projects into Workspace” |image9| Figure 20: Import Projects Options.

From here click on the “browse” method by the select root directory option. Then navigate to where the STMCubeF7 location with ni-example-app is located.

This will then bring a large number of projects into the main screen. |image10| Figure 21: Projects to import.

Click on the “Deselect All” and then add the following pages to the project and click Finish. |image11| Figure 22: Importing of Projects.

ni-api-srv ni-example-app ni-stm32xx-support-srv ui-stk ui-stm32f7xx-lpl-srv Download them all into the project page. Then close the “Information Center” tab at the top to see your imported project.

|image12| Figure 23: Project view with all needed projects downloaded.

Specify the Link Type in PLAT_Platform.c. It can be either SPI, UART or ETH from a hard coding standpoint.

|image13| Figure 24: Defining link parameters.

Now save the file and the build process can begin.

Start by building in the following way:

::

    • DBG ui-stk

|image14| Figure 25: Building the UI-stack.

::

    • DBG ui-stm32f7xx-lpl-srv

|image15| Figure 26: Building the lpl srv.

::

    • DBG – ni-stm32f7xx-support-srv

|image16| Figure 27: Building the STM32 support service.

::

    • DBG – ni-api-srv

|image17| Figure 28: Building the ni-api-srv

::

    • DBG – ni-example-app

|image18| Figure 29: Building the ni-api-srv

The example project is now built. The next step will be to build and then use the built project. To Build, first go to the debug symbol and select “Debug Configurations”. Then navigate as shown below to the ni-example-app-debug location.

|image19| Figure 30: Building the debug configuration.

Then click on “Debug”. Ni-example-app is now running fully on the STM32F7 platform. It can be used to interract with networks the same way the ni-example-app on the PC does.

Generic Use Case Vs Specific Use Cases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NI-Example-App is a good tool for evaluation on a PC, and then as a starting point for the Applications processor code in an embedded environment.

There are two pound defines that will change the behavior of ni-example-app. Shown below is a chart of what the user can expect:

+---------+----------------+-------------------------------------------------------------------------+
| Use_IRT | Enable Profile | Behavior                                                                |
+---------+----------------+-------------------------------------------------------------------------+
| 0       | 0              | Typical operation as shown above                                        |
+---------+----------------+-------------------------------------------------------------------------+
| 0       | 1              | This will make RPG2 conform and use the semi profile                    |
+---------+----------------+-------------------------------------------------------------------------+
| 1       | 0              | This will make RPG2 conform and make use of the IRT based configuration |
+---------+----------------+-------------------------------------------------------------------------+
| 1       | 1              | Not Applicable!!!!                                                      |
+---------+----------------+-------------------------------------------------------------------------+

The next two sections will walk a user through how to modify the code base so it can run with either the Semi Profile for EtherCAT or for Profinet IRT.

Using ni-example-app for a PROFINET IRT based Evaluation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NI-Example-App also has some capability built into it, that allow for the user to make use of an IRT based solution. As opposed to the previous configuration that has items 500, 501 and 502 built into it, when IRT is being used, there is a more complicated implementation in place from the perspective of the Unified Interface.

Due to some stress testing limitations, some users might find the 3 items in place are not enough for a real IRT based device. Therefore, there is a way of handling this from ni-example-app. There is a #define in the "ni-example-app" portion of the project(both for the STM32 and for the windows based application).

|image20| Figure 32: ni-example-app IRT #define

Before running ni-example-app(on either platform or even your own custom platform), make sure to change the 1 for the #define, then build the application and it will run using the IRT based configuration.

The IRT application will add 8 items of 8 bytes each to the IO-Configuration of the ADIN2299. Please make sure to have uploaded the proper IO-Config.bin or else the configuration of the ADIN2299 will fail.

NOTE: If the #define for IRT is based at 0, then operation will continue as expected for ni-example-app.

Using ni-example-app for a semi profile based EtherCAT implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the user is going to make use of ni-example-app as the Applications Processor for an EtherCAT Semiprofile application, the actual work to be done is very simple for the initialization of the SemiProfile.

|image21| Figure 33: ni-example-app #defines being set for SEMI-PROFILE

A simple example of end to end modifications for the ADIN2299
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generically, a user needs to make use of the ADIN2299 as close to the evaluation kit as they can. In other words, the design has been through conformance from both the hardware and software perspective. This particular section will walk through an example of how to make the NI-Example-App make use of other IO footprints as opposed to the 6 bytes in 8 bytes out IO footprint that is used throughout our example configuration.

Note that this section applies to customization of RPG2 as an example. There are many other examples that could be done, but this walks a user through a theoretical example.

Determine the IO Footprint of ADIN2299
--------------------------------------

The ADIN2299 is given out with an IO configuration data size of 6 bytes of input data and 8 bytes of output data.

Once a user determines their IO footprint, they can either make use of the API to create items and devices, or they can use the IO configuration tool to create their own IO footprint.

Either one of these options is acceptable.

Moving on from ni-example-app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following the completion of this document, there are other places a user can go to use ni-example-app in more real world PLC conditions.

::

    • RPG2 EtherCAT Quickstart Guide – Walks through the EtherCAT protocol and how to make PDO data be reflected between the host and RPG2.
    • RPG2 Profinet Quickstart Guide – Walks through the EtherCAT protocol and how to make inputs and output data be reflected by the PLC.
    • RPG2 EtherNet/IP Quickstart Guide – Walks through the Ethernet/IP protocol and how to make class1 data be reflected between the host and RPG2.
    • RPG2 EtherCAT Semi Profile User Guide – Walks a user through how EtherCAT can be used for the Semi Profile with minor application changes.
    • RPG2 Unified Interface User Guide – This walks a user through the API in detail for the Unified Interface on RPG2.

.. |image1| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_13.png
.. |image3| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_14.png
.. |image4| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_15.png
.. |image5| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_16.png
.. |image6| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_17.png
.. |image7| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_18.png
.. |image8| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_19.png
.. |image9| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_20.png
.. |image10| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_21.png
.. |image11| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_22.png
.. |image12| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_23.png
.. |image13| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_24.png
.. |image14| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_25.png
.. |image15| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_26.png
.. |image16| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_27.png
.. |image17| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_28.png
.. |image18| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_29.png
.. |image19| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_30.png
.. |image20| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_31.png
.. |image21| image:: https://wiki.analog.com/_media/resources/technical-guides/hpug_32.png
