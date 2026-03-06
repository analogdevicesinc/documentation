Software example using EV-COG-SMARTMESH1Z
=========================================

This document explains how temperature data can be sent via EV-COG-SMARTMESH1Z configured in the slave mode to the E-manager connected to the users PC. It also explains the software flow and how to view the expected output.

Software Details
----------------

A modular software framework is provided for quick application prototyping. Based on the application use case, developers need to download the respective software packs.

The EV-COG-SMARTMESH1Z interfaced EV-COG-AD3029LZ , software development kit consists of these packs:-

#. :adi:`BSP - Board Support Package for EV-COG-AD3029LZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-aducm3029-ezkit.html#eb-relatedsoftware>`- This pack along with the DFP is required to develop applications using the on-board drivers.

::

   -[[https://github.com/dustcloud/sm_clib|SmartMesh C library]]- This pack is required for the implementation of the serial APIs of the EV-COG-SMARTMESH1Z and nullifies  the need for  application software  to deal low level processes.

For details on the C-Library, follow this\ `link <https://dustcloud.atlassian.net/wiki/spaces/CLIB>`__

Software Overview
-----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/software_over.png
   :align: center
   :width: 300px

::

   *Application software has provisions to handle sensor data collection or preprocessing of collected data and can draw implications on the collected data.
   *BSP handles sending and receiving of packets over UART interface.
   *C-LIB is a library for handling API calls, HDLC packetisation, etc.

Software Architecture
---------------------

This section gives user a basic understanding on how the software is designed for handling both transmission and reception of packets between the EV-COG-SMARTMESH1Z and EV-COG-AD3029LZ.

To download the software source from Analog Devices Git - click on :git-EV-COG-AD3029LZ:`"SmartMesh-Temperature-Sensor-Software" <SmartMesh_temp_slavemode_licensed_v2.0>`

Transmission of Packets
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/transmit.png
   :align: center
   :width: 300px

The Application level software handles tasks such as invoking API commands, handling API replies and performing user-application specific tasks. The C-Lib later performs HDLC packetization and other tasks there by making it easy for the user to send commands to the EV-COG-SMARTMESH1Z. In the BSP, APIs specific to UART communication aid in sending transmit packets over the UART lines.

Reception of Packets
~~~~~~~~~~~~~~~~~~~~

When EV-COG-SMARTMESH1Z sends a packet to EV-COG-AD3029LZ, the received packet is written to a circular buffer using the UART specific APIs of the BSP. At the application level software , the circular buffer is continuously checked for data written. When a byte of data is written to the circular buffer, the application level software calls routines that handle the data written to the buffer. The C-Lib processes the received packet and sends a callback to the application level software with only the required field in the received packet.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/receive.png
   :align: center
   :width: 305px

Software Flow:-
---------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/iamge6.jpg
   :align: center
   :width: 600px

Interface Guide
---------------

This section covers the various steps involved in the interface of the EV-COG-SMARTMESH1Z with EV-COG-AD3029LZ and thereby run the C-library on the EV-COG-AD3029LZ and get it to talk to EV-COG-SMARTMESH1Z.

Following are the steps involved :-

::

   *Connect the EV-COG-SMARTMESH1Z with EV-COG-AD3029LZ  as shown in the Board Interface section.
   *Download and Install the necessary soft wares for working with  the EV-COG-SMARTMESH1Z and EV-COG-AD3029LZ as mentioned in the Software Details section.
   *For setting up  the SmartMesh-IP-Manager  follow [[http://cds.linear.com/docs/en/application-note/SmartMesh_IP_Easy_Start_Guide_for_the_Embedded_Manager.pdf|this]]  link.
   *Download the  [[https://bitbucket.analog.com/projects/IOTTGAPPS/repos/dust-ev-cog-ad3029lz/browse|Source code]].
   *Place the contents of the SmartMesh C-Library in the your project folder.
   *Here is a list of files of the SmartMesh C-Library you need to include in the project folder:-
   * dn_endianness.c
   *  dn_hdlc.c
   * dn_ipmt.c
   * dn_lock.c
   * dn_serial_mt.c
   *Import the source into IAR and run the application software.

Importing source file to IAR
----------------------------

:doc:`Here </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz/tools/iar_guide>` is the link for working with IAR Embedded Workbench for programming EV-COG-3029LZ which cover topics related to initial settings and project importing tasks and running the projects.

Successful Interface of EV-COG-SMARTMESH1Z with EV-COG-AD3029LZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Steps to obtain output as shown in fig.1 :-
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/image_7.png
   :align: center

::

   *Open Tera Term.
   *Click on Serial and select the Com port to which the manager is connected.
   *Type “login user” .
   *Type “sm” which is  a command for showing all the motes connected to the manager.

Steps to obtain output as shown in fig.2 :-
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/image_8.png
   :align: center

::

   *Click on APIExplorer.exe.
   *Select Manager and click on connect through “serialMux” or through specific Com port.
   *In the command window select “subscribe”.
   *To subscribe to all notifications  fill “FFFFFFFF” in the filter section and “00000000” in the unackFilter.
   *In the “ notifications “ section, one can see the data and other notifications.

Steps to obtain output as shown in fig.3 :-
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/tools/image_9.png
   :align: center

::

   *Click on TempMonitor.exe.
   *Press  “load” manager.
   *In the mote list, the temperature data sent by the mote is visible.

Example project
---------------

.. admonition:: Download
   :class: download

   To download an example project to interface EV-COG-SMARTMESH1Z with EV-COG-AD3029LZ click on :git-EV-COG-AD3029LZ:`"SmartMesh-Temperature-Sensor-Software" <SmartMesh_temp_slavemode_licensed_v2.0>`

   
   The example project sends temperature data or a dummy data to the manager which can be viewed on TempMonitor(GUI) or on the APIExplorer(GUI) of the manager.


:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`

*End of Document*
