DroneTRX Hardware User Guide
============================

**DroneTRX** is an HDL reference modem showcasing ADI’s best-in-class RF transceivers in wireless communications applications. The design is implemented using the ADRV9361-Z7035 System-on-Module (SoM), which is based on the AD9361 RF Transceiver and the Xilinx Zynq®-7000 All Programmable (AP) System-on-Chip (SoC).

DroneTRX integrates an HDL PHY layer with a demo application for video streaming. The DroneTRX HDL PHY layer originally supports Orthogonal Frequency Domain Multiplexing 1T1R Single-Input Single-Output (OFDM-SISO) mode. This is further extended to support multiple input multiple output (OFDM-MIMO) spatial diversity mode. The wireless standard is based on a modified IEEE 802.11n protocol.

This page provides instructions on how to set up the hardware for the DroneTRX reference modem.

| 
| ===== System Setup ===== The hardware setup for the DroneTRX system is composed of two ADR SDR platforms/boards. The first board setup (labeled as Board 1 or drone board) has a web camera connected and performs the drone functionalities, while the other board setup (labeled as Board 2 or controller board) acts as the controller where it receives the video feed from the drone board.

|image1|

.. container:: center

   **DroneTRX Hardware Setup Block Diagram (wired connection)**


The DroneTRX hardware setup may be operated in a wireless or wired configuration. The default setup for operation is the wireless setup. However, the user may also evaluate the system using the wired setup due to the following reasons: 

-  DroneTRX operates at 2.4 GHz or 5 GHz ISM band, which is a shared spectrum used by other radios such as Wi-Fi, Bluetooth, Zigbee, and other mobile communications. Depending on the operating environment, this spectrum may be noisy due to co-existence with other radios. Switching to a wired setup would allow the user to avoid RF noise that may be detrimental to the link quality.

-  Some countries require regulatory approval for transmitting over-the-air. In the absence of regulatory approval, the user must test the system using a wired connection, inside an RF box or an anechoic chamber.  

For the wireless configuration, you must connect two sets of antennas for each SDR board. You may connect the antenna directly on the TX and RX RF ports, or after the attenuator and PA blocks. The path loss is determined by the environment and distance between the antennas. For the wired configuration, the path loss is simulated by the insertion of attenuation in the RF path. Optionally, an external power amplifier may be also introduced to boost the transmit signal.

| 

Equipment Needed
----------------

This section describes the key hardware components needed for setting up the DroneTRX system and demonstrating its capabilities for building communication links for UAVs and drone applications.

+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Qty | Component Needed                 | Description                                                                                                                                                                                                              | Recommendation                                                                                                                                                                                                                                                                                                                                |
+=====+==================================+==========================================================================================================================================================================================================================+===============================================================================================================================================================================================================================================================================================================================================+
| 2   | **SDR Platform**                 | RF Transceiver Module                                                                                                                                                                                                    | :adi:`ADRV9361-Z7035 System-on-Module <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ADRV9361-Z7035.html>` together with the :adi:`ADRV1CRR-FMC SDR Module Carrier/FMC Carrier board <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>`                                         |
|     |                                  | The SDR platform boots from an SD card where Kuiper Linux OS and the DroneTRX software files are loaded.                                                                                                                 | The DroneTRX system can be also run using a Zedboard with the AD-FMCOMMS3-EBZ platform. However, this has limited functionality as HDMI and MIMO are not currently supported as of May 2024.                                                                                                                                                  |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **Antenna**                      | Any antenna, that operates in the 2.4 GHz or 5 GHz band and with male SMA termination, can be used for the setup.                                                                                                        | `Pulse Larsen WA700/2700SMA Wideband Antenna <https://www.digikey.com/en/products/detail/pulse-electronics/WA700-2700SMA/5174623>`__                                                                                                                                                                                                          |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4   | **Coaxial Cable**                | Low loss RF coaxial cables to directly connect the two boards                                                                                                                                                            | RG-316 SMA-M to SMA-F patch cable, 30 cm                                                                                                                                                                                                                                                                                                      |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4   | **UFL to SMA Pigtail Connector** | Needed to connect ADRV9361-SOM antenna ports to standard SMA connectors                                                                                                                                                  | TE Connectivity CSI-SGFI-150-UFFR                                                                                                                                                                                                                                                                                                             |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **Attenuators**                  | Attenuators are used to adjust the receive power accordingly and not to oversaturate the internal RF circuitry.                                                                                                          | 10 dB attenuation; other sizes can be used for experimentation for signal strength and simulation of path loss                                                                                                                                                                                                                                |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1   | **Power Amplifier**              | To increase range, an external power amplifier module may be added                                                                                                                                                       | CN0417 Power Amplifier module (2.4 GHz)                                                                                                                                                                                                                                                                                                       |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1   | **Web Camera**                   | Used to capture video that will be transmitted over the wireless link. The camera is connected to the FPGA platform that will act as the drone.                                                                          | Any off-the-shelf USB camera                                                                                                                                                                                                                                                                                                                  |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **HDMI Monitor**                 | Used to display the UI and video received over the wireless link. The monitor is required on the board that will act as the controller. For convenience, you may also attach a monitor to the board acting as the drone. | Generic HDMI monitor                                                                                                                                                                                                                                                                                                                          |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **USB UART Cable**               | A USB UART cable is needed to interface with the SDR platform through serial.                                                                                                                                            | Comes with the ADRV1CRR-FMC SDR module carrier board                                                                                                                                                                                                                                                                                          |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **USB OTG**                      | For attaching other USB peripherals, such as web cam, keyboard and mouse, to the SDR platform.                                                                                                                           | Comes with the ADRV1CRR-FMC SDR module carrier board                                                                                                                                                                                                                                                                                          |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **SD Card**                      | Needed for flashing the FPGA image                                                                                                                                                                                       | Class 10 SD card, at least 16 GB in size                                                                                                                                                                                                                                                                                                      |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **USB Hub**                      | Ensure that the USB hub is rated to handle power from connected USB peripherals (keyboard, mouse, webcam)                                                                                                                | Generic USB Hub                                                                                                                                                                                                                                                                                                                               |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **USB Mouse and Keyboard**       | Needed to provide input and control to SDR platform’s software and operating system.                                                                                                                                     | Generic USB keyboard and mouse                                                                                                                                                                                                                                                                                                                |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2   | **Power Supply**                 | The SDR platform is powered via an AC-DC adaptor that is supplied with the FMC carrier board.                                                                                                                            | Comes with the ADRV1CRR-FMC SDR module carrier board                                                                                                                                                                                                                                                                                          |
+-----+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ==== Prerequisite ====

.. tip::

   To run the DroneTRX system, an SD card containing the software and FPGA image must be first prepared. An SD card size of at least 16 GB is required.

   
   

.. raw:: html

   <details><summary>**Click here for instructions on how to flash the FPGA image on SD Card**</summary>

| 
   | 1. First, download the base “vanilla” image from the `OpenWiFi Download Image QuickStart page <https://github.com/open-sdr/openwifi?tab=readme-ov-file#download-img-and-quick-start>`__. Flash this openwifi.img file using Balena Etcher or Raspberry Pi imager using the instructions indicated here:
   
   -  :doc:`Linux Hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`
   -  :doc:`Windows Hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`
   
   | 
   | 2. Once the SD card has been successfully flashed, you will need to update the FPGA bitstream and other system related files. Perform the following steps on a host machine.
   
   -  First, get the pre-built binaries from this repository: https://bitbucket.analog.com/scm/cos-apjc/drone_trx-images.git
   -  On the HDL folder, you will see two subfolders: SISO and MIMO. Each of these subfolders will contain the FPGA bitstream and other binaries to start a DroneTRX SISO or MIMO version. If you wish to setup a SISO system, copy the files from the HDL/SISO folder. Otherwise, copy the files from the HDL/MIMO folder to setup a MIMO system.
   
   | 
   | 3. Mount the prepared SD card from step 1. Copy the BOOT.bin, devicetree.dtb and uImage to the BOOT partition of the SD card.
   | 4.Eject the SD card and insert into the ADRV9361-SOM eval board’s SD card slot.
   | 5. Switch on the ADRV9361-SOM board. You will see the that the system will start to boot. Once booted, you should have access to the console or Kuiper desktop.
   | 6. Open a terminal and switch to the root user.
   
   -  Note that the default user is the “analog” user, the password for this user is “analog”. The password for the “root” account is “analog” as well.
   
   | 
   | 7. Copy the user space files (demo app and scripts) from https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git and copy into /home/analog directory.
   | 8. (ONLY FOR MIMO build) Get the pre-buillt SDR kernel modules from STEP1 under the SDR/MIMO subdirectory. Copy the sdr.ko and tx_intf.ko into the /root/openwifi folder.
   
   |

.. raw:: html

   </details>

   


| 
| ==== Wired Connection ==== |image2|

|

.. note::

   The DroneTRX system requires 2 sets of ADRV boards and peripherals (*please see* `#equipment_needed <https://wiki.analog.com/>`__ *list*), to be linked through coaxial cables. First set is designated as the Controller and the second set serves as the Drone.


| Follow below steps to get started.

1. Connect the :adi:`ADRV1CRR-FMC` carrier board into the `ADRV9361-Z7035 <https://www.xilinx.com/ADRV9361-Z7035>`__ board socket.


|image3|

| 
| 2. Set the jumpers to configure the Zynq boot mode. The ADRV9361 boot mode switches are labeled S3 and S4. Each switch has a white dot indicating “Logic 0” or “Off” position. Set both switches to “Logic 1” or “On” to enable Boot from SD Card Mode.

| |image4|
| 3. Insert the prepared SD card into the SD card slot of the :adi:`ADRV1CRR-FMC` carrier board.

| 
| 4. Connect the USB OTG Hub through the USB OTG port (P19) of the `ADRV9361-Z7035 <https://www.xilinx.com/ADRV9361-Z7035>`__ SOM. Then, connect the following peripherals:

-  Mouse
-  Keyboard
-  Camera **(Note: only the Drone side has a camera connected)**
-  Monitor

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/peripherals_configuration.png
   :alt: Peripherals Configuration
   :align: center
   :width: 600px

| 
| 5. Connect the UFL to SMA pigtail connectors to the on-board UFL RF ports (TX1A and RX1A). Note that the DroneTRX system is using the A_BALANCED port by default. Thus, we will use the ports suffixed by “A”.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ufl_connection_on_adrv9361-z70435_som.png
   :alt: UFL connection on ADRV9361-Z70435 SOM
   :align: center
   :width: 600px

| 6. Connect the attenuator to the SMA end of the UFL to SMA pigtail connector.
| |image5|

7. (Optional) Connect the Power Amplifier (the CN0417 for this demo setup). Instead of using an attenuator, replace the attenuator with power amplifier on the TX line to boost signal.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/tx_line_with_power_amplifier.png
   :alt: TX Line with power amplifier
   :align: center
   :width: 600px

8. Join the 2 `ADRV9361-Z7035 <https://www.xilinx.com/ADRV9361-Z7035>`__ boards and attenuators using the low loss coaxial cable. Each board requires 2 UFL to SMA pigtail connectors; one connector will be TX, the other will be RX.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/connecting_2_adrv_sdr_platforms_via_wired_connections.png
   :alt: Connecting 2 ADRV SDR platforms via wired connections
   :align: center
   :width: 600px

9. Connect the USB UART cable to the UART port (P10) of `ADRV9361-Z7035 <https://www.xilinx.com/ADRV9361-Z7035>`__ SOM. Connect the USB end to the host computer.

.. tip::

   Follow the steps in :doc:`DroneTRX Software Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/software>` to install the drivers and instructions on how to connect via serial.


| 
| 10. Connect the power adapter of the `ADRV9361-Z7035 <https://www.xilinx.com/ADRV9361-Z7035>`__ board.

| 
| 11. Turn on the power switch. If successful, the system will start to boot. Once booted, you should have access to the console or Kuiper Linux desktop.

| 
| 12. Open a terminal and switch to the root user.

-  Note that the default user is the “analog” user, the password for this user is “analog”. The password for the “root” account is “analog” as well.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/hardware_setup_using_2_adrv_boards.jpg
   :alt: Hardware Setup using 2 ADRV boards
   :align: center
   :width: 600px

>>>

Wireless Connection (Over-the-Air)
----------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/block_diagram_for_over-the-air_setup.png
   :align: center
   :width: 2000px

.. important::

   
   | The over-the-air setup follows the same connection as above, except that the 2 ADRV boards use antenna for communication instead of the coaxial cables.
   | When using the Over-the-Air or Wireless Setup, replace Hardware Assembly **Steps #6, #7, #8, and #9** with below procedure for connecting the antenna.
   


| 
| ==== Connecting the Antenna for Wireless Communication ====

.. container:: indent

   1. Connect the SMA port of the antenna to the SMA port of the UFL-SMA pigtail connector.


   |image6|

   | 
   | 2. Repeat step 1 for the rest of the RF ports. Below figure shows all antennas connected for both the drone and controller board.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/all_antennas_connected_for_both_the_drone_and_controller_board.jpg
      :align: center
      :width: 600px
   


--------------

| 
| ===== Troubleshooting ===== Refer to the :doc:`Troubleshooting section </wiki-migration/resources/eval/user-guides/dronetrx>` from the DroneTRX Overview page for commonly encountered issues and how to resolve them.

| 
| ===== Help and Support ===== For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 
| ===== Relevant Resources =====

-  :doc:`ADRV9361-Z7035 System on Module (SOM) SDR </wiki-migration/resources/eval/user-guides/adrv9361-z7035>`

| 
| |Overview #:[[:resources:eval:user-guides:dronetrx:software\| DroneTRX Software User Guide#none|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/dronetrx_hardware_setup_block_diagram_wired_connection_.png
   :width: 1000px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/block_diagram_for_wired_setup.png
   :width: 2000px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/mounting_the_adrv9361-z7035_som_to_adrv1crr-fmc_carrier_board.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/configuring_the_adrv9361_board_to_boot_from_sd_card_mode.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/connecting_an_attenuator.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/connecting_the_antenna.png
   :width: 600px
.. |Overview #:[[:resources:eval:user-guides:dronetrx:software\| DroneTRX Software User Guide#none| image:: /navigation #/resources/eval/user-guides/dronetrx
