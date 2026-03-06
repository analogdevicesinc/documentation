DroneTRX HDL Reference Design
=============================

Overview
--------

**DroneTRX** is an HDL reference modem showcasing ADI’s best-in-class RF transceivers in wireless communications applications. The design is implemented using the ADRV9361-Z7035 System-on-Module (SoM), which is based on the AD9361 RF Transceiver and the Xilinx Zynq®-7000 All Programmable (AP) System-on-Chip (SoC).

DroneTRX integrates an HDL PHY layer with a demo application for video streaming. The DroneTRX HDL PHY layer originally supports Orthogonal Frequency Domain Multiplexing 1T1R Single-Input Single-Output (OFDM-SISO) mode. This is further extended to support multiple input multiple output (OFDM-MIMO) spatial diversity mode. The wireless standard is based on a modified IEEE 802.11n protocol.

Despite the ubiquity of IEEE 802.11, there are few available reference projects that fully implement a customizable, full-stack communication system, from application layer down to the physical layer, on a system-on-chip. The purpose of this software reference design is to show customers how they may use the AD936x transceivers as a communication link for UAVs and drones.

Supported Platforms
-------------------

-  Zynq 7020 (Zedboard) + AD-FMCOMMS3-EBZ
-  Zynq 7035 (ADRVSOM) + ADRV9361

Features
--------

+------------------------------+-----------------------------------------------------------+
| **Transmitter/Receiver**     | 1T1R – Single Input Single Output                         |
|                              | 2T2R - Multiple Input Multiple Output (Spatial Diversity) |
+------------------------------+-----------------------------------------------------------+
| **Frequency Bands**          | 2.5 GHz ISM band (2.412 GHz to 2.462 GHz)                 |
|                              | 5.2 GHz ISM band (5.180 GHz to 5.240 GHz)                 |
+------------------------------+-----------------------------------------------------------+
| **Supported Bandwidth**      | 5 MHz, 10 MHz, 20 MHz                                     |
+------------------------------+-----------------------------------------------------------+
| **Bit Rate (PHY)**           | 54 Mbps (SISO) / 65 Mbps (MIMO)                           |
+------------------------------+-----------------------------------------------------------+
| **Standard**                 | Non-standard IEEE 802.11                                  |
+------------------------------+-----------------------------------------------------------+
| **Symbol modulation**        | BPSK, QPSK, 16-QAM, 64-QAM                                |
+------------------------------+-----------------------------------------------------------+
| **Forward Error Correction** | Convolutional Coding, Viterbi Decoder                     |
|                              | 1/2, 3/4, 5/6 coding rate                                 |
+------------------------------+-----------------------------------------------------------+
| **Video Resolution**         | QVGA, SD                                                  |
+------------------------------+-----------------------------------------------------------+

Moreover, the following signal processing blocks are implemented in the reference HDL modem:

-  Constellation mapper/demapper
-  Scrambler/descrambler
-  STBC combiner/decoder
-  Cyclic delay shift
-  Channel estimation, equalization & maximum ratio combining
-  Preamble for HT-mixed format
-  Measurement modules: latency, packet loss

| 

System Architecture
-------------------

Below figure illustrates the high-level DroneTRX architecture. The communication stack is focused mainly on the FPGA where the signal processing for the PHY layer is implemented. The signal processing includes the TX and RX chains, as well as a lower MAC layer. A demonstration GUI application runs on ADI Kuiper Linux. For the PHY layer to communicate with user space applications, it reuses existing upper-level protocols such as TCP/IP stack and loadable drivers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/high-level_architecture_block_diagram.png
   :align: center
   :width: 800px

|

| ===== Applications ===== Possible applications of the DroneTRX reference modem include the following:

-  Unmanned aerial vehicles (UAV) communications
-  Wireless video transmission

A recorded demonstration of a wireless video transmission can be viewed from this link: <fc #ff0000>\ **Recorded Demo**\ </fc>

| 
| ----

Evaluation Platform
-------------------

The software for the DroneTRX is provided by Analog Devices as an open-source reference design under the AGPL-v3 license. The system source code consists of several components:

-  **FPGA HDL Code**: https://bitbucket.analog.com/scm/cos-apjc/drone_trx-hdl.git
-  **SDR Device Driver**: https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git
-  **Graphical User Interface & other set-up scripts**: https://bitbucket.analog.com/scm/cos-apjc/drone_trx-sdr-app.git

In case you do not want to build binaries from scratch, you may use the pre-built binaries from this repository: https://bitbucket.analog.com/scm/cos-apjc/drone_trx-images.git

The reference modem can be evaluated using the ADRV9361-Z7035 system on module (SOM) mounted on the ADRV9361-FMC carrier board. To evaluate the DroneTRX reference modem, you will need two sets of ADRV9361-Z7036 SDR boards.

| 
| ===== Getting Started =====

.. tip::

   Please refer to the following pages for detailed instructions on how to set up the DroneTRX system for evaluation.

   
   -  :doc:`DroneTRX Hardware Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/hardware>`
   -  :doc:`DroneTRX Software Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/software>`
   


| 
| ===== Use Cases ===== The DroneTRX reference design can be used in following configurations:

-  Single Input Single Output (SISO)
-  Multiple Input Multiple Output (MIMO)

Each configuration presents different use cases as detailed below.

| 
| ==== SISO Use cases ==== The SISO build follows the use case of a typical Wi-Fi Basic Service Set, where a wireless station/client connects to an access point.

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Access Point (AP)**    | An access point is a device that allows wireless devices to connect to a wired network by transmitting and receiving Wi-Fi signals                                     |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Station/Client (STA)** | A station or client refers to a device, software, or system that accesses services, resources, or information from another computer or server, typically via a network |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

On top of these standard IEEE 802.11 modes, the radio can be also configured to emulate drone or controller functionalities, depending on the connected peripherals and software scripts executed.

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Drone**      | A web camera is connected to the AD9361-SOM evaluation board. Functionality includes streaming the video feed over the wireless link. The drone functionality also includes receipt of dummy telemetry commands |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Controller** | The AD9361-SOM evaluation board displays video streaming from the wireless feed. Functionality also includes transmission of dummy telemetry commands to the drone board.                                       |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ==== MIMO Use Cases ==== The MIMO build only supports the monitor mode and as such, only supports the following use cases.

.. container:: center box

   
   +---------------------+-----------------------------------------------------------------------------------------------+
   | **Packet injector** | This board runs the inject_80211 application, which sends our 802.11 management over-the-air. |
   +---------------------+-----------------------------------------------------------------------------------------------+
   | **Packet sniffer**  | This board sniffs the packets from the packet injector via tcpdump.                           |
   +---------------------+-----------------------------------------------------------------------------------------------+
   


.. note::

   As of writing, it is

   
   .. container:: hi

      \ **NOT possible to demonstrate video transmission**\

   
   for the MIMO build due to gaps with the Medium Access Control (MAC) interface. The version only supports high throughput mode (HT-mode). Based on testing, it is unable to detect or process legacy 802.11 management beacons needed to setup AP-client initial handshake as needed in the 802.11 MAC. Moreover, since we are unable utilize MAC, incoming frames to PHY layer does not have rate flow control and channel access control. These are items that is expected to be handled by the upper layers.


| 
| ----

Demo Application
----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/dronetrx_demo_application_as_run_in_kuiper_linux.png
   :align: center
   :width: 800px

The DroneTRX demo application has two operating modes which emulate functions for the drone and controller side. The drone mode is expected to start the video streaming and receive the telemetry commands. The controller mode will be sending the telemetry commands while receiving and performing video playback. Below figure shows the GUI components, while the table details their respective functionality.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/parts_of_the_dronetrx_demo_app.png
   :align: center
   :width: 800px

+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Number** | **Label**                | **Description**                                                                                                                                                                                                                                                                                                                                                             |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1          | IP address               | **Controller IP Addr:** IP address of the video transmitter (default: 192.168.13.1)                                                                                                                                                                                                                                                                                         |
|            |                          | **Drone IP Addr:** IP address of the video player (default: 192.168.13.5)                                                                                                                                                                                                                                                                                                   |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2          | Port                     | **Port:** Port number of choice (Default: 8085)                                                                                                                                                                                                                                                                                                                             |
|            |                          | **Note:** From the base port number, the next 2 succeeding ports will be opened. This is to prevent the following functions from running on the same ports                                                                                                                                                                                                                  |
|            |                          | Base port number + 1: port for video streaming                                                                                                                                                                                                                                                                                                                              |
|            |                          | Base port number + 2: port for telemetry demo                                                                                                                                                                                                                                                                                                                               |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3          | Stop/Start Stream        | **Start Stream button:** Starts the video streaming. This opens the MPlayer window (RX). Starts ffmpeg video transmission (TX).                                                                                                                                                                                                                                             |
|            |                          | **Stop Stream button:** Stops the video streaming. This closes the MPlayer window (RX). Stops ffmpeg video transmission (TX).                                                                                                                                                                                                                                               |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4          | Reset Register           | Resets the RX/TX Latency & Throughput HDL registers                                                                                                                                                                                                                                                                                                                         |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5          | Stop Reading             | Stop reading the RX/TX Latency and Throughput HDL registers                                                                                                                                                                                                                                                                                                                 |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6          | Dummy Telemetry Commands | (Present on controller side) These buttons emulate the sending of dummy telemetry commands from controller to drone. Click **“Send A”** or **“Send B”** or **“Send C”** or **“Send D”** to test the telemetry commands. Clicking any of these buttons will send the corresponding letter (dummy command) write command to the drone side, only works while streaming video. |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7          | BW Setting               | **Bandwidth dropdown list:** Sets the bandwidth by selecting between 5 MHz, 10 MHz, and 20 MHz. The bandwidth is adjusted by changed the bandwidth of the AD9361 analog RF filter.                                                                                                                                                                                          |
|            |                          | **Set BW button:** Locks in the value of channel bandwidth will be used.                                                                                                                                                                                                                                                                                                    |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8          | MCS setting              | **MCS dropdown list:** Sets the MCS by selecting the number on the MCS dropdown box then click “Save MCS”.                                                                                                                                                                                                                                                                  |
|            |                          | **Save MCS button:** Writes the value of the selected MCS into the hardware registers.                                                                                                                                                                                                                                                                                      |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9          | Frequency setting        | **Frequency dropdown list:** Sets the bandwidth to 5 GHz and 2.4 GHz                                                                                                                                                                                                                                                                                                        |
|            |                          | **Channel dropdown list:** Selects between the available channels.                                                                                                                                                                                                                                                                                                          |
|            |                          | **Set Band button:** Writes the chosen values to configuration files.                                                                                                                                                                                                                                                                                                       |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10         | Set video quality        | Sets video quality resolution for video streaming. Options include QVGA, SD                                                                                                                                                                                                                                                                                                 |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11         | Status Message           | Displays measurement readings from HDL registers                                                                                                                                                                                                                                                                                                                            |
|            |                          | **PHY CRC errors:** Number of OFDM symbols detected to have parity/CRC errors, since start of transmission.                                                                                                                                                                                                                                                                 |
|            |                          | **Rx Latency:** One-way latency of the HDL PHY Rx path                                                                                                                                                                                                                                                                                                                      |
|            |                          | **Tx Latency:** One-way latency of the HDL PHY Tx path                                                                                                                                                                                                                                                                                                                      |
|            |                          | **Throughput:**                                                                                                                                                                                                                                                                                                                                                             |
|            |                          | **RX1 RSSI:** RSSI reading for antenna 1 receive                                                                                                                                                                                                                                                                                                                            |
|            |                          | **RX2 RSSI:** RSSI reading for antenna 2 receive                                                                                                                                                                                                                                                                                                                            |
+------------+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

>>

--------------

Running the System as SISO
--------------------------

.. note::

   Proceeding to this section assumes that the user has already prepared the evaluation platform as indicated in the :doc:`DroneTRX Hardware Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/hardware>` and :doc:`DroneTRX Software Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/software>`.


Since the DroneTRX POC is based on OpenWiFi, we leverage the 802.11 infrastructure mode basic service set. This means that an access point (AP) is required to setup the wireless network for the other wireless stations or devices (STA) to join in.

With this said, it is possible to have the following combinations:

.. container:: center box

   
   ============== =========================== ============================
   \              **AP**                      **STA**
   **Drone AP**   with drone function         STA with drone function
   **Controller** AP with controller function STA with controller function
   ============== =========================== ============================
   


In terms of end-to-end link, there are two possible options as listed in the table below.

.. container:: center box

   
   ============ =========================== ============================
   \            **Board 1**                 **Board 2**
   **Option A** AP with drone function      STA with controller function
                Runs camera                 Plays back video
   **Option B** AP with controller function STA with drone function
                Plays back video            Run camera
   ============ =========================== ============================
   


The block diagrams below show the typical setup for SISO demonstration.

   


|image1|

.. container:: center

   **Block Diagram for Over-the-Air Setup**


| 
| |image2|

.. container:: center

   **Block Diagram for Wired Setup**


The default setup for operation is the wireless setup. However, the user may also evaluate the system using the wired setup due to the following reasons:

-  DroneTRX operates at 2.4 GHz or 5 GHz ISM band, which is a shared spectrum used by other radios such as Wi-Fi, Bluetooth, Zigbee, and other mobile communications. Depending on the operating environment, this spectrum may be noisy due to co-existence with other radios. Switching to a wired setup would allow the user to avoid RF noise that may be detrimental to the link quality.
-  Some countries require regulatory approval for transmitting over-the-air. In the absence of regulatory approval, the user must test the system using a wired connection, inside an RF box or an anechoic chamber.

The procedures below assume that you have already prepared the SD card image, and you have confirmed that the device has booted and loaded the OS. Terminal commands to be typed are emphasized blue text, such as <fc #6495ed>\ *command*\ </fc>.

| 
| ==== How to Setup the Access Point with Transmit (Tx) GUI ====
| 1. On the ADRV board chosen to be the access point, open a terminal.

2. Set current user to superuser by running <fc #6495ed>\ *sudo su*\ </fc>.


|image3|

3. Next, run <fc #6495ed>\ *cd /home/analog/Desktop/DroneTRX*/</fc> to access the DroneTRX folder in the home directory.


|image4|

4. Run the <fc #6495ed>\ *“./drn_ap.sh”*\ </fc> script to load kernel modules, enable the wireless interface and setup the AP network along with the Transmit GUI.


|image5|

5. Wait to finish the setup. The GUI window should appear.


|image6|

6. On a separate terminal Run <fc #6495ed>\ *ifconfig*\ </fc> to check the AP IP address. The expected address is 192.168.13.1.


|image7|

7. Configure the IP and Port settings.

-  a. IP: IP address of the client (Default: 192.168.13.5)
-  b. Port: Port number of choice (Default: 8085)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ap_tx_ip_address.png
   :align: center
   :width: 600px

8. Click start stream to launch the mplayer video window. Refer to Section 7 Demo Application for further information on the GUI app functionality.


|image8|

\*Alternatively, you may execute the equivalent commands for step 4.

::

   1.  cd /root/openwifi 
   2.  ./wgd.sh 
   3.  ./fosdem.sh 
   4.  cd /home/analog/Desktop/DroneTRX/src 
   5.  python3 transmit_gui.py

.. note::

   Always set up the AP before the client, this will make sure that the static IP will be set properly. This applies when changing bandwidth, band, and channel.


| 

How to Setup the Station/Wireless Client with Receive (Rx) GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. On the ADRV board chosen to be the wireless station, open a terminal.

2. Set current user to superuser by running <fc #6495ed>\ *sudo su*\ </fc>.


|image9|

3. Next, run <fc #6495ed>\ *cd /home/analog/Desktop/DroneTRX*/</fc> to access the DroneTRX folder in the home directory.


|image10|

4. Run <fc #6495ed>./drn_client.sh</fc> script to load kernel modules, enable the wireless interface and setup the client network along with the **Receiver GUI.**


|image11|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_setup_rx_gui_4.png
   :align: center
   :width: 400px

5. Check the IP address of the client board by running <fc #6495ed>\ *ifconfig sdr0*\ </fc> on a separate terminal. This command should display the IP address assigned by the IP. The expected IP address should be **192.168.13.5.**


|image12|

6. Verify the connection from Station to AP. Check the connection by pinging the AP by running <fc #6495ed>\ *ping 192.168.13.1*\ </fc>


|image13|

7. The GUI window should appear. Configure the IP and Port settings

-  a. IP: IP address of the AP (Default: 192.168.13.1)
-  b. Port: Port number of choice (Default: 8085)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_setup_rx_gui_window.png
   :align: center
   :width: 600px

8. Click start stream to launch the ffmpeg video capture.


|image14|

\*\ *Alternatively*, execute the following commands to have finer control when testing or debugging. These are equivalent to what the drn_client script does.

::

   a.  service network-manager stop 
   b.  cd /root/openwifi 
   c.  ./wgd.sh 
   d.  ifconfig sdr0 up 
   e.  iwlist sdr0 scan

   | grep -A 10 -B 10 openwifi (check if ‘openwifi’ network is detected, re-run the command if not) 
   f.  wpa_supplicant -i sdr0 -c wpa-openwifi.conf  & (to connect to openwifi AP) 
   g.  enable_static_ip.sh 192.168.13.5 sdr0 (to set static IP to ‘192.168.13.5’) 
   h.  cd /home/analog/Desktop/DroneTRX/src 
   i.  python3 receive_gui.py

.. note::

   Always set up the AP before the client, this will ensure that the static IP is set properly. This applies when changing bandwidth, band, and channel.


|

| ==== Verification ==== The general flow involved in setting up and testing the functionality of the DroneTRX POC is summarized by the following outline.

1. Establish first the wireless connection between the AP and STA.

-  a. Set up the AP. Follow steps in `Configuration Procedure Section A <https://wiki.analog.com/>`__.
-  b. Set up the STA. Follow steps in `Configuration Procedure Section B <https://wiki.analog.com/>`__.

2. Check AP-Client connection. AP and client boards should be able to ping each other.

3. Run the GUI. Follow steps and details in the Configuration Procedure above.

-  a. Select MCS
-  b. Start Stream
-  c. Check video
-  d. Reset RX-TX Latency
-  e. Reset Throughput Measurements
-  f. Send dummy telemetry commands
-  g. Stop Stream
-  h. Check log files

--------------

Running the System as MIMO
--------------------------

.. note::

   Proceeding to this section assumes that the user has already prepared the evaluation platform as indicated in the :doc:`DroneTRX Hardware Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/hardware>` and :doc:`DroneTRX Software Setup Guide </wiki-migration/resources/eval/user-guides/dronetrx/software>`.


The setup consists of two ADRV boards, one for packet injector and one for packet sniffing.

End-to-end link setup:

.. container:: center box

   
   ========= =============== ===============
   \         **Board 1**     **Board 2**
   **Setup** Packet injector Packet receiver
   ========= =============== ===============
   


Below diagram illustrates the setup when used in MIMO configuration. The evaluation is done over-the-air to allow the mixing of the RF signals from the two transmitter antennas and to allow multiple signals to arrive at each receiving antenna.

   


|image15|

.. container:: center

   **Block Diagram for Over-the-Air Setup**


The procedures below assume that the user has already prepared the SD card image, and confirmed that the device has booted and loaded the OS. Terminal commands to be typed are emphasized blue text, such as *<fc #6495ed>command</fc>*.

| 
| ==== How to Use the Packet Sniffer ==== 1. On the ADRV board chosen to be the Packet Sniffer, open a terminal.

2. Set current user to superuser by running <fc #6495ed>\ *sudo su*\ </fc>.


|image16|

3. Next, run <fc #6495ed>// cd /home/analog/Desktop/testing_scripts/mimo_packet_inject_test *</fc> to access the packet injection test folder in the home directory. 4. Run the <fc #6495ed>*\ “./packet_capture_rx.sh”\ *</fc> script to load kernel modules, enable the wireless interface and run the PCAP application. The parameters of packet sniffed can be set to name the* **pcap file** *accordingly for ease of file tracking, for example, <fc #6495ed>*\ “./packet_capture_rx.sh n 0 d 1000 1”//</fc>

-  <fc #6495ed>\ *a. “n” for the hardware operation modes. (Available modes: a, g, n)*\ </fc>
-  <fc #6495ed>\ *b. “0” is for the MCS values. (Available values: 0 – 7)*\ </fc>
-  <fc #6495ed>\ *c. “d” data type of the packet. (Available types: m, c, d, r)*\ </fc>
-  <fc #6495ed>\ *d. “1000” is the number of transmit packets. (Recommended number of packets 10000)*\ </fc>
-  <fc #6495ed>\ *e. “1” is the size of packets send in bytes. (Recommended sizes: 1, 32, 64)*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_sniffer_3.png
   :align: center
   :width: 600px

5. Wait to finish the setup. It will automatically start capturing packets.


|image17|

6. Stop the script by pressing combination keys “ctrl + c”.


|image18|

7. Check the log files and pcap file on a separate folder called “pcap_files” on the Desktop.


|image19|

.. note::

   Always start the packet sniffer before the packet transmitter, this ensures that the sniffer will capture the transmitted packets.


.. note::

   Use Wireshark application to extract and view the raw data of the pcap file.


| 
| ==== How to Use the Packet Injector ==== 1. On the ADRV board chosen to be the Packet Sniffer, open a terminal.

2. Set current user to superuser by running <fc #6495ed>\ *sudo su*\ </fc>.


|image20|

3. Next, run <fc #6495ed>\ *cd /home/analog/Desktop/testing_scripts/mimo_packet_inject_test*\ </fc> to access the packet injection test folder in the home directory.


|image21|

4. Run the <fc #6495ed>\ *“./packet_inject_rx.sh”*\ </fc> script to load kernel modules, enable the wireless interface and run the injector script. The parameters of the transmitted packets can be adjusted on different setup, the delay of when command will send and how many times the command will run can be also set, for example: <fc #6495ed>\ *“./packet_capture_rx.sh n 0 d 1000 1 2 3”*\ </fc>

-  <fc #6495ed>\ *a. “n” for the hardware operation modes. (Available modes: a, g, n)*\ </fc>
-  <fc #6495ed>\ *b. “0” is for the MCS values. (Available values: 0 – 7)*\ </fc>
-  <fc #6495ed>\ *c. “d” data type of the packet. (Available types: m, c, d, r)*\ </fc>
-  <fc #6495ed>\ *d. “1000” is the number of transmit packets. (Recommended number of packets 10000)*\ </fc>
-  <fc #6495ed>\ *e. “1” is the size of packets send in bytes. (Recommended sizes: 1, 32, 64)*\ </fc>
-  <fc #6495ed>\ *f. “2” is the time delay between the commands.*\ </fc>
-  <fc #6495ed>\ *g. “3” is how many times the command will run.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_injector_3.png
   :align: center
   :width: 600px

4. Wait to finish the setup. It will automatically starts injecting packets.


|image22|

5. The script will automatically stop once done but it can be stopped by pressing combination keys “ctrl + c”.


|image23|

6. Check the TX read log files on a separate folder called “tx_out” on the Desktop.


|image24|

.. note::

   Always set up the packet sniffer before the packet injector, this will make sure that the sniffer will capture the transmitted packets.


.. note::

   Use Wireshark application to extract and view the raw data of the pcap file.


| 
| ----

Troubleshooting
---------------

This section compiles frequently encountered issues and how to resolve them.

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Issue**                                                               | **Resolution**                                                                                                                                                                     |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| My system does not boot                                                 | Check that the board is powered on.                                                                                                                                                |
|                                                                         | Check that the ADRV9361-Z7035 SOM is firmly connected to the FMC carrier board.                                                                                                    |
|                                                                         | Check that you have correctly copied files to the SD card. If your company has encryption policies when transferring files to external media, please reach out to your IT support. |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The drone board and the controller board cannot establish a connection. | Please check your testing environment. 2.4 GHz or 5 GHz ISM band is usually noisy due to the presence of other Wi-Fi radios. Consider switching to a different channel.            |
|                                                                         | Consider using the wired setup instead of a wireless setup.                                                                                                                        |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| I accidentally closed the GUI and would like to relaunch the GUI.       | In current terminal run the following command to launch the GUI:                                                                                                                   |
|                                                                         | <fc #6495ed>\ *cd /home/analog/Desktop/DroneTRX/src python3 transmit_gui.py*\ </fc>                                                                                                |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== Help and Support ===== For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 
| ===== Additional Resources =====

-  :doc:`Linux on RF SoM </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
-  :doc:`Analog Devices Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

| 
| |Overview #:resources:eval:user-guides:dronetrx:hardware|DroneTRX Hardware User Guide #:resources:eval:user-guides:dronetrx:software|DroneTRX Software User Guide#none|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/block_diagram_for_over-the-air_setup.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/block_diagram_for_wired_setup.png
   :width: 1000px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ap_setup1.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ap_setup2.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ap_setup3.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ap_gui_window.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ap_ip_address.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ap_ip_and_ip_port_settings.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_setup_rx_gui.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_setup_rx_gui_2.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_setup_rx_gui_3.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_ifconfig_sdr0.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/ping_192.168.13.1.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/sta_setup_rx_start_stream.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/mimo_setup.png
   :width: 1000px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_sniffer_1.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_sniffer_4.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_sniffer_5.png
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/pcap_files.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_injector_1.png
   :width: 600px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_injector_2.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_injector_4.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/packet_injector_5.png
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/tx_out.png
   :width: 600px
.. |Overview #:resources:eval:user-guides:dronetrx:hardware|DroneTRX Hardware User Guide #:resources:eval:user-guides:dronetrx:software|DroneTRX Software User Guide#none| image:: /navigation #/resources/eval/user-guides/dronetrx
