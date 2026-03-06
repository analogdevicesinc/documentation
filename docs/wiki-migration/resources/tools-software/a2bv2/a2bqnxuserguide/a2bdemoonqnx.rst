:doc:`Click here to return to A2B QNX User Guide Homepage. </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide>`

A2B Demo on QNX
===============

Demo Set Up
-----------

The sample demo is run using BeagleBone Black as the host. In this case the demo application running on QNX in ARM core of BeagleBone Black controls the discovery and programming of A2B nodes in the system. It is also responsible for initializing clock to the A2B transceiver/codecs. The block diagram of a 3 node A2B system with BeagleBone Black as Host is shown in below image.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/demo_block_diagram.png
   :align: center
   :width: 600px

Connections
-----------

To run the sample demo, the following setup connections are to be made as shown in below image.


|image1|

BeagleBone Black
~~~~~~~~~~~~~~~~

The below shows the setup for BeagleBone black.


|image2|

-  Connect an Ethernet cable (RJ45) from the P5 connector on BeagleBone Black Board to Ethernet port of the Network and windows host also needs to connect to the same network. The Ethernet connection is required to run the example application on the target.
-  Connect the USB A to mini-USB B cable from the P4 connector on BeagleBone Black Board to the USB connector of windows host. This acts as the power source for the board.
-  Connect the USB to TTL Serial cable from J1 on the BeagleBone Black board to the windows host. The UART connection is required to view the console output from u-boot (bootloader) and QNX. Identify the COM port for the USB to TTL serial cable connected to the Host in the Device Manager under the Ports (COM and LPT) section and specify in the serial connection settings. The rest of the settings for the serial connection as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/serial_port_settings.png
   :align: center
   :width: 400px

A2B network
~~~~~~~~~~~

In this demo EVAL-AD2428WD1BZ is used as A2B master and EVAL-AD2428WC1BZ and EVAL- AD2428WB1BZ are used as slave nodes. Connect twisted-pair wire between the “B” slave connector J2 on the EVAL-AD2428WD1BZ board and the “A” connector on the EVAL-AD2428WC1BZ Slave board. Connect the “B” side connector on EVAL-AD2428WC1BZ Slave board to the “A” connector on EVAL- AD2428WB1BZ board.

Audio In/Out
~~~~~~~~~~~~

-  Connect an audio sink (e.g., active speakers) to ‘Audio Line- out’ port of AD2428WB1BZ board.

Connections for Custom platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a custom platform running QNX, the following connections need to be made to the A2B master board from the target processor

-  Connect the I2C SDA and SCK pins to the A2B master node’s SDA and SCK pins
-  Supply 48 kHz frame sync to the frame SYNC pin of the A2B master node.

Booting QNX on BeagleBone Black
-------------------------------

Follow the steps mentioned in Chapter 3 of `QNX BeagleBone Black BSP User Guide <https://support7.qnx.com/download/download/30074/SDP7_BSP_UG_TI_AM335xBB.pdf>`__ to boot QNX on the target. The modifications in the image needed for running this demo are mentioned in the following section. Upon successful booting, the serial console should be similar to below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/bbb_terminal.png
   :align: center
   :width: 600px

IFS image modifications for BeagleBone Black
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer Build the BSP (IDE) section under Chapter 5 in the `QNX BeagleBone Black BSP User Guide <https://support7.qnx.com/download/download/30074/SDP7_BSP_UG_TI_AM335xBB.pdf>`__ for steps to modify and rebuild the images. Following changes need to be made in the .build file for this demo:

-  I2C driver: The a2b application on QNX uses i2c1 device. Add the following two lines in the I2C driver section. ``i2c-omap35xx -j5 -i 70 -p0x4802A000 –u1 
   waitfor /dev/i2c1``
-  Remote debugging support: The Momentics IDE uses qconn daemon to connect to target and debug applications. Add the following lines REMOTE_DEBUG section. Note that this must be added only after the Network Drivers section. ``devc-pty
   waitfor /dev/pttyp0 4
   waitfor /dev/socket 4 
   qconn port=8000``
-  HDMI Audio driver: The HDMI audio driver drives the Frame Sync that is required for the a2b network setup. Add the following lines to enable this. ``io-audio -d mcasp-dm814x_tda19988 
   waitfor /dev/snd/pcmC0D0p``
-  This also needs the following libraries to be added in the Shared Libraries section ``libasound.so
   deva-ctrl-mcasp-dm814x_tda19988.so``

Configuring SigmaDSP as Audio Host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This demo is built to use the SigmaDSP (ADAU1452) present on the EVAL-AD2428WD1BZ board. Following are the steps to configure the SigmaDSP from SigmaStudio.

-  Connect the power supply to the EVAL-AD2428WD1BZ and connect the USBi from the PC to the EVAL-AD2428WD1BZ. Ensure that the self-boot jumper (JP4) is enabled as shown in image below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/boot_jumper_enabled.png
   :align: center
   :width: 600px

-  Open the adi_a2b_master_ADAU1452.dspproj file located in the ADI_A2B_Software-Android-RelX.Y.Z/Schematics/SigmaDSP Schematics folder.
-  Link-compile and download the schematic.
-  Navigate to the Hardware view, right-click on the ADAU1452 IC, and select "Write Latest Compilation through USB" as shown in the image below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/self_boot_write.png
   :align: center
   :width: 600px

-  Disable the self-boot for SigmaDSP on the EVAL-AD2428WD1BZ evaluation board, then press reset to configure the SigmaDSP through the self-boot, as shown in the image below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/boot_jumper_disabled.png
   :align: center
   :width: 600px

Running the Demo
----------------

Follow the steps below to run the application

-  Ensure that serial cable is connected from the board to the windows host.
-  Ensure that Ethernet Cable is conncted to the Network and the Windows host also connected to the same network.
-  Connect Fly wires between BeagleBone Black I2C1 to EVAL-AD2428WD1BZ P1 I2C ports.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/i2c_pins.png
   :align: center
   :width: 400px

-  Boot up QNX on the BeagleBone Black board with the image modifications as explained in previous sections.
-  Check the Ethernet interface address before connecting to the BeagleBone Black. For Example, we consider The BeagleBone Ethernet interface in QNX has the address like 192.168.0.2.
-  Build the a2b application as explained in :doc:`QNX Build </wiki-migration/resources/tools-software/a2bv2/a2bqnxuserguide/a2bstackdemoapplicationbuild>`
-  Add a Launch target

   -  Click on New Launch Target from the toolbar, as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/new_launch_target.png
   :align: center
   :width: 400px

-  Specify the IP address as 192.168.0.2 and click Finish as shown in below Figure

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/new_target_ip.png
   :align: center
   :width: 400px

-  Add a new launch configuration

   -  Click on New Launch Configuration from the toolbar as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/new_launch_configuration.png
   :align: center
   :width: 400px

-  Select the initial launch configuration as Debug
-  Select the launch configuration type as C/C++ QNX application
-  Specify the Project and C/C++ application and Target as shown in below Figure

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/c_qnx_target.png
   :align: center
   :width: 400px

-  Launch and run the debug session on the target created in above steps.
-  Discovery successful message should appear as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/console_output.png
   :align: center
   :width: 400px

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/qnx_setup.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bqnxuserguide/bbb_board.png
   :width: 400px
