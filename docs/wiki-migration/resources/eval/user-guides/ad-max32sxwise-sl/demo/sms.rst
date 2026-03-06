Long Range Wireless Structural Health Monitoring​ Applications User Guide
=========================================================================

Overview
--------

To learn more about the reference designs, refer to :adi:`EV-STRUCTURAL-ARDZ` and :adi:`MAX32670-SX-ARDZ`.

The :adi:`EV-STRUCTURAL-ARDZ` is a vibration sensor that uses the :adi:`ADXL343` digital output MEMS accelerometer chip and the :adi:`ADIS16203` programmable 360° inclinometer. Aside from providing vibration data, this board also features the :adi:`MAX30210` digital temperature sensor which gives the option to shut down sensitive machines and equipment for smart motor sensing applications. This vibration sensor can also detect if the horizontal position of the sensor changes, which points towards a collapse of the structure where the sensor was deployed.

Demo Requirements
-----------------

Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~

-  Microcontroller/Sensors

   -  :adi:`EV-STRUCTURAL-ARDZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EV-STRUCTURAL-ARDZ.html>`
   -  :adi:`MAX32670-SX-ARDZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/MAX32670-SX-ARDZ.html>` (2x)
   -  Raspberry Pi 4
   -  Raspberry Pi 4 Power Supply Adapter
   -  RAK5146 PiHAT
   -  RAK5146 SPI Module
   -  Long Range Antenna
   -  LAN Cable
   -  Micro SD Card
   -  Spacer Bolt (4x)
   -  Screw (6x)

-  Microcontroller/Sensor Setup

   -  :adi:`MAX32625PICO` Rapid Development Platform with 10-pin ribbon cable
   -  CR123A Battery or any equivalent external DC power supply (+3 V to +4.7 V) (2x)
   -  Micro USB-to-USB Cable

-  Environment Setup

   -  3D Printed Building Model

Software Requirements
~~~~~~~~~~~~~~~~~~~~~

-  Host PC with administrator access

   -  Windows 10 OS or later
   -  Microsoft .Net Framework 4.6.2
   -  1920 by 1080 or greater screen resolution (recommended)

-  Downloaded and installed:

   -  :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`
   -  `AD-MAX32WISE-SLZ Firmware (Rel1.0.0) <https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/ad-max32wise-slz_firmware.zip>`__
   -  `ADI Wireless Sensor Hub Standalone Software <https://wiki.analog.com/_media/{{ {{ /resources/eval/user-guides/ad-max32sxwise-sl/demo/wireless_sensor_hub_rev_1.0.3.zip>`__
   -  `UART serial monitor <http://sourceforge.net/project/showfiles.php?group_id=67297>`__

      -  This demo uses Real Term serial monitor, but other UART serial terminals may also be used.

   -  `Balena Etcher <https://etcher.balena.io>`__ image writing tool
   -  `ChirpStack Gateway OS <https://www.chirpstack.io/docs/chirpstack-gateway-os/install/raspberry-pi.html>`__

Demo Setup
----------

Block Diagram
~~~~~~~~~~~~~

.. container:: indent

   The block diagram of the overall setup is shown below.


Hardware Setup
~~~~~~~~~~~~~~

.. container:: indent

   This section describes the :doc:`hardware setup </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` of the demo divided into three phases: **node board assembly**, **gateway assembly**, and **environment assembly**.

   
   **Sensor board assembly** involves connecting the :adi:`EV-STRUCTURAL-ARDZ` to the :adi:`MAX32670-SX-ARDZ`. This phase is to be repeated for each sensor board. **Gateway assembly** involves setting up the RAK5146 PiHAT and the Raspberry Pi 4 as the concentrator hardware, allowing data transmission from the sensor boards to the host PC. Lastly, **environment assembly** involves building the setup that will simulate the structural health monitoring system.


Sensor Board Assembly
^^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   For the needed components for this phase, see **Microcontroller/Sensors** and **Microcontroller/Sensor Setup** under :doc:`Hardware Requirements </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.


-  <WRAP> Insert one **CR123A battery (3 V to 4.7 V)** into the battery holder (BT1) of the :adi:`MAX32670-SX-ARDZ` Base Board.

|image1| To **check for the battery polarity** in the BT1 connector, refer to the figure above (right). The DS3 LED will light up indicating that you have inserted the battery correctly and that power is provided in the base board.</WRAP>

-  <WRAP> Connect the :adi:`EV-STRUCTURAL-ARDZ` Sensor Node to the :adi:`MAX32670-SX-ARDZ` Base Board by aligning the corresponding Arduino headers on each board.

|image2| </WRAP>

-  Connect the :adi:`MAX32625PICO` programming adapter to the :adi:`MAX32670-SX-ARDZ` Base Board through the 10-pin ribbon cable.

.. container:: center round box

   
   **Make sure that the** :adi:`MAX32625PICO` **programming adapter has been flashed with the correct image before connecting it to the** :adi:`MAX32670-SX-ARDZ` **Base Board.** If you do not know how to load the image, click on the instructions below:
   
   

.. raw:: html

   <details><summary>**How to flash the firmware image in the MAX32625PICO**</summary>

-  Download the firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin>`
   -  Do not connect the :adi:`MAX32625PICO` to the :adi:`MAX32670-SX-ARDZ` Base Board yet.
   -  Press the button on the :adi:`MAX32625PICO`. **Do not release the button until the MAINTENANCE drive is mounted**.

   |image3|

   -  While holding the button, connect the :adi:`MAX32625PICO` to the Host PC using the micro USB to USB cable.
   -  Release the button once the MAINTENANCE drive is mounted.
   -  Drag and drop (to the MAINTENANCE drive) the firmware image.
   -  After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the :adi:`MAX32625PICO` can now be used to flash the firmware of the :adi:`MAX32670-SX-ARDZ` Base Board.

.. raw:: html

   </details>

   


-  <WRAP> Connect the :adi:`MAX32625PICO` programming adapter to the Host PC using the micro USB to USB cable.

|image4| </WRAP>

.. container:: indent

   
   .. note::

         
         To **set up the firmware** of the sensor board, you may proceed to :doc:`Configuring the Sensor Board </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` under :doc:`Software Setup </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`. Since **this demo uses two sensor boards**, repeat all steps of :doc:`Sensor Board Assembly </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` for the second board.
         

   


Gateway Assembly
^^^^^^^^^^^^^^^^

.. container:: indent

   For the needed components for this phase, see **Gateway Essentials** under :doc:`Hardware Requirements </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.


-  Insert the RAK5146 SPI module into the mPCIe slot on the RAK2287 Pi HAT. Make sure the card fits snugly into the connector.
-  Gently press the SPI module down and fasten it using the screws provided.

|image5|

-  Connect the RAK5146 PiHAT to the Raspberry Pi using the 40-pin connector.

|image6|

-  Connect the Raspberry Pi to the Host PC using the LAN cable.
-  <WRAP> Power on the Raspberry Pi using the Raspberry Pi 4 Power Supply Adapter.

</WRAP>

.. container:: indent

   
   .. note::

         
         To **configure the gateway**, you may proceed to :doc:`Imaging the SD Card with ChirpStack OS </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` and :doc:`Configuring the Gateway </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` under :doc:`Software Setup </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.
         

   


Environment Assembly
^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   For the needed components for this phase, see **Environment Setup** under :doc:`Hardware Requirements </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.

   
   Once the sensor boards, gateway, and environment are all assembled, proceed to :doc:`Software Setup </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` to configure the sensor boards, gateway, and the application server.
   


</WRAP>

Software Setup
~~~~~~~~~~~~~~

.. container:: indent

   
   .. important::

      Before proceeding with the steps listed below. **Make sure that all requirements under** :doc:`Software Requirements </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` **are met, with all needed software downloaded and installed**.

   
   This section describes the software setup of the demo divided into five phases: **configuring the sensor board**, **imaging the SD card with ChirpStack OS**, **configuring the gateway**, **setting up a self-hosted application server**, and **connecting a sensor node to the gateway**.
   
   **Configuring the sensor board** involves uploading the appropriate firmware to the sensor board using the :adi:`MAX32625PICO` programming adapter and obtaining the board's DevEUI. To prepare the gateway, **imaging the SD card with ChirpStack OS** involves flashing the ChirpStack Gateway OS to the Raspberry Pi 4's micro SD card, while **configuring the gateway** involves creating the gateway through the ChirpStack Network Server.
   
   To configure the GUI, **setting up a self-hosted application server** involves configuring the Host PC, installing the GUI, and accessing the gateway. Lastly, **connecting a sensor node to the gateway** involves creating a device for each board and accessing the GUI.
   
   .. tip::

      Visit :doc:`ADI Long Range Wireless Radio Software User Guide </wiki-migration/resources/eval/user-guides/longrangewirelessradio/software>` for a more detailed software setup guide.

   


Configuring the Sensor Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   
   .. note::

      Make sure you have completed the steps described in :doc:`Sensor Board Assembly </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` before proceeding with the steps listed below.

         
      This phase will require `Real Term serial monitor <http://sourceforge.net/project/showfiles.php?group_id=67297>`__ and `AD-MAX32WISE-SLZ Firmware (Rel1.0.0) <https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/ad-max32wise-slz_firmware.zip>`__ installed.

   


-  <WRAP> If `AD-MAX32WISE-SLZ Firmware (Rel1.0.0) <https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/ad-max32wise-slz_firmware.zip>`__ is already downloaded, extracted, and installed, go to **C:\\Analog Devices\\AD-MAX32WISE-SLZ-Rel1.0.0\\Software\\ad_max32wise_src\\bin\\flow**.

The **flow folder** should contain the BIN, ELF, and HEX file.

|image7| </WRAP>

-  <WRAP> Go to My Computer and search for the **DAPLINK drive**. Drag and drop (or copy and paste) the **.bin firmware file** directly into the DAPLINK drive.

.. tip::

   To check if the flashing is successful, check the DAPLINK directory and make sure there is no **FAIL.TXT** file. In case there is, repeat the drag and drop step.


</WRAP>

-  <WRAP> Reset the :adi:`MAX32670-SX-ARDZ` Base Board by pressing the **S1 reset button**. </WRAP>

-  <WRAP> Open the `Real Term serial monitor <http://sourceforge.net/project/showfiles.php?group_id=67297>`__ to check if the firmware has been loaded correctly. Make sure to use the following settings:

.. container:: center round box

   
   -  **Ports**: Take note of the COM port used by checking the **Device Manager**
   -  **Baud Rates and Ports**: set to **921600**
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/2.png
      :align: center
      :width: 600px
   
   -  **Display formatting**: set to **ANSI**
   -  **Enable Scrollback**: set to **200**.

   |image8|

</WRAP>

-  Once configured, open the serial monitor by clicking **Open** on the **Port** tab.
-  <WRAP> Take note of the **DevEUI (64-bit end-device identifier)**. This will be used later during the gateway setup.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/deveui.png
   :align: center
   :width: 600px

.. tip::

   To **redisplay the DevEUI** on the screen, **reset the** :adi:`MAX32670-SX-ARDZ` **Base Board** by pressing the S1 button.


</WRAP>

Imaging the SD Card with ChirpStack OS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   
   .. note::

      This phase will require `Balena Etcher <https://etcher.balena.io>`__ **image writing tool** installed and `ChirpStack Gateway OS <https://www.chirpstack.io/docs/chirpstack-gateway-os/install/raspberry-pi.html>`__ downloaded. This phase will also use the **micro SD card** listed under :doc:`Gateway Essentials </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.

   


-  Run the `Balena Etcher <https://etcher.balena.io>`__ **image writing tool**.
-  Insert the micro SD card into the Host PC.
-  Click **Flash from file** from the options shown in the interface.

|image9|

-  Navigate to the location where the downloaded `ChirpStack Gateway OS <https://www.chirpstack.io/docs/chirpstack-gateway-os/install/raspberry-pi.html>`__ is saved.
-  Select target and choose the targeted micro SD card drive.
-  Click **Flash** to start the burning process of the image in the chosen SD card.
-  <WRAP> Wait until it is done.

|image10|

.. tip::

   In case the **flashing fails**, consult this guide to resolve the issue: `Balena Etcher FAQs <https://etcher.balena.io/#FAQs>`__.


</WRAP>

.. container:: indent

   
   .. important::

      After the first boot, the **gateway might reboot automatically** to apply some changes. The full image will set up the **PostgreSQL database** on its first boot. This could take a couple of minutes and during this time the gateway will be less responsive.

   


Configuring the Gateway
^^^^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   
   .. note::

      Make sure you have completed the steps described in :doc:`Gateway Assembly </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` before proceeding with the steps listed below. Make sure that the **Raspberry Pi (powered on) and Host PC are still connected** through the LAN cable.

   


.. container:: indent

   **Opening the SSH client**


-  Insert the imaged SD card on the designated slot on the Raspberry Pi.
-  <WRAP> Connect the Host PC to ChirpStack WiFi.

.. tip::

   When prompted to enter password, use **ChirpStackAP** (case-sensitive).


</WRAP>

-  Open command prompt or terminal on the Host PC.
-  <WRAP> On the terminal, enter: <code> ssh admin@192.168.0.1 </code> </WRAP>

-  <WRAP> SSH connection will ask for the password input. Use below credentials:
-  **Username:** admin
-  **Password:** admin
-  **StaticIP:** 192.168.0.1

</WRAP>

-  Once connected, check the assigned ChirpStack IP by typing **ifconfig**.


|image11|

-  <WRAP> This will show all configs, look for **eth0** and **save the IP address assigned to it**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/eth0_ip.png
   :align: center
   :width: 600px

.. tip::

   In this example, the IP assigned is **169.254.117.207**. This will be used in **Installing the GUI and Accessing the Gateway** under :doc:`Setting up a Self-Hosted Application Server </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.


</WRAP>

-  <WRAP> Open the Raspberry Pi terminal, then enter:

<code> sudo gateway-config </code> This will **open an SSH client** to configure the gateway.

</WRAP>

.. container:: indent

   **Navigating the SSH client**


-  In the main menu, choose **Setup concentrator shield**.
-  Choose **RAK5146 (with GNSS)**. Click **OK**.
-  Choose **AU915**. Click **OK**.
-  Choose **Channels 0 to 7 + 64**. Click **OK**.
-  The concentrator restarts and goes back to the main menu.
-  <WRAP> Quit the main menu.

</WRAP>

.. container:: indent

   
   .. tip::

      If you have properly configured the gateway and installed the required SD card image, then **you are ready to use the ChirpStack Network Server**.

   


Setting up a Self-Hosted Application Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   
   .. note::

      Make sure that the **Raspberry Pi (powered on) and Host PC are still connected** through the LAN cable.

         
      This phase will require `ADI Wireless Sensor Hub Standalone Software (Rev 1.0.3) <https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/wireless_sensor_hub.zip>`__ downloaded and extracted.

   
   **Configuring the Host PC for the Gateway**


-  <WRAP> Access **Advance Firewall settings** in your computer.

|\|| </WRAP>

-  <WRAP> Create a new **Inbound Rule**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/inbound_rule_1.png
   :align: center
   :width: 700px

</WRAP>

-  <WRAP> **Configure the Inbound Rule** as shown below.



.. raw:: html

   <details><summary>**Step-by-step configuration of a new ChirpStack Inbound Rule**</summary>

|image12| |image13| |image14| |image15| |image16| |image17| |image18|

.. raw:: html

   </details>


   | </WRAP>

|

.. container:: indent

   **Installing the GUI and Accessing the Gateway**


-  Run the `ADI Wireless Sensor Hub Standalone Software <https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/wireless_sensor_hub.zip>`__ with administrator privileges. This will start the initialization process and run the process on your PC.
-  <WRAP> Check and **save the IP address assigned to the Raspberry Pi gateway**. The server will show all connections available; select the IP of the connector you used.

.. tip::

   In this example, it is the Apple USB Ethernet Adapter.

   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/ip_address.png
      :align: center
   
   This information will be used in **Setting up a Local Host URL for the Application Server** under :doc:`Connecting a Sensor Node to the Gateway </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>` to integrate data from the gateway to the GUI.


</WRAP>

-  <WRAP> Use the assigned ChirpStack IP address saved earlier to access its configuration interface **by adding the ChirpStack Port (8080)** to the end of IP address. Open a page in the browser using **[saved IP address]:8080** as the URL.

.. tip::

   In this example, the saved IP address is 169.254.117.207. Hence, the URL would be **169.254.117.207:8080**.

   
   If you haven't saved the IP address, **revisit steps 3 to 7** in **Opening the SSH Client** under :doc:`Configuring the Gateway </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.


</WRAP>

-  This will open the login page. Enter the same credentials we used to establish an SSH connection with the ChirpStack Gateway.


|image19|

Connecting a Sensor Node to the Gateway
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: indent

   This phase describes how to connect the sensor nodes to ChirpStack and how to validate that it can send data. This process is divided into three sections: **creating a device profile**, **enrolling device applications**, and **setting up a local host URL for the application server**.

   
   .. note::

      At this point, it is assumed that you have a **working ChirpStack environment** with a connected gateway.

   
   **Creating a Device Profile**


-  Once you are in the ChirpStack landing page, navigate to the **Applications tab**.
-  Click **Device profiles** under the **Tenant** category.
-  Click on the **Add device profile** button.

|image20|

-  <WRAP> Answer all required information under the **General** tab, and then click **Submit** once done.

The following shows the configuration required to add a sensor node:

.. container:: center round box

   
   +-------------------------------------------+-----------------------------------+
   | **Attribute**                             | **Configuration**                 |
   +-------------------------------------------+-----------------------------------+
   | Name                                      | Enter desired sensor node name    |
   +-------------------------------------------+-----------------------------------+
   | Region                                    | AU915                             |
   +-------------------------------------------+-----------------------------------+
   | Region Configuration                      | AU915 (channels 0-7 +64)          |
   +-------------------------------------------+-----------------------------------+
   | MAC Version                               | LoRaWAN 1.0.4                     |
   +-------------------------------------------+-----------------------------------+
   | Regional parameters revision              | A                                 |
   +-------------------------------------------+-----------------------------------+
   | ADR algorithm                             | Default ADR algorithm (LoRa only) |
   +-------------------------------------------+-----------------------------------+
   | Expected uplink interval (sec)            | 10                                |
   +-------------------------------------------+-----------------------------------+
   | Device-status request frequency (req/day) | 8640                              |
   +-------------------------------------------+-----------------------------------+
   


</WRAP>

.. container:: indent

   **Enrolling Device Applications**


-  After adding a device, click the **Applications** option under **Tenant**.
-  Click on the **Add application** button.
-  Write the desired **Application Name** on the space provided. Hit **Submit** once done.

|image21|

-  <WRAP> Open the Application created and **add a device**.

The following details are also needed:

-  **Name:** previously defined application name set from the previous steps
-  **Device EUI (EUI64):** unique serial number of the device
-  **Device profile:** previously defined device profile set from the previous steps

.. important::

   In naming the devices, you must include a **specific keyword** (not case-sensitive) to distinguish the sensor nodes shown on the GUI. In this case, the two sensor nodes can be named **flow-1** and **flow-2** respectively.


|image22| </WRAP>

-  <WRAP> Once done, click **Submit**. Then, **repeat steps 5 and 6** for the other sensor board.

.. tip::

   For OTAA devices, confirm that when the device tries to OTAA activate, you see a **JoinRequest** message followed by a **JoinAccept** message.

   
   If you do not see a JoinRequest and JoinAccept, click on the **Flush OTAA devices** button.


</WRAP>

-  <WRAP> Enter the **Application key** and hit **Submit** once done.


|image23|

.. tip::

   For this demo, the **Application key** is **2b7e151628aed2a6abf7158809cf4f3c**.

   
   The App Key included in the LoraMAC was used as is for the purpose of evaluation. Users can generate the App Key and add it in the source code on their own.


</WRAP>

.. container:: indent

   **Setting up a Local Host URL for the Application Server**


-  In the Applications tab, select and open **WiSe_Sensors**.
-  <WRAP> Inside the **ADI_SENSOR_NODE** application, navigate to the **Integrations** tab.

|image24| </WRAP>

-  In the **Integrations** tab, select the **edit** button in the **HTTP Configuration** section.
-  <WRAP> Change the **Event Endpoint URL** to the IP of the adapter your gateway is connected.

|image25|

.. tip::

   In this example, it is the IP of the Apple Network Adapter, http://169.254.178.157:5050/api/data/post.

   
   If you haven't saved the IP address, **revisit steps 1 to 2** in **Installing the GUI and Accessing the Gateway** under :doc:`Setting up a Self-Hosted Application Server </wiki-migration/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter>`.


</WRAP>

-  After updating the HTTP Integration endpoint URL, submit the changes by pressing **Submit**.
-  A pop-up message will appear saying **HTTP Integration updated**.

|image26|

-  Open your browser and **enter the URL** http://localhost:5050. Now you’ll be able to see and monitor your active nodes.

Actual Demo
-----------

Working Setup
~~~~~~~~~~~~~

Custom GUI
~~~~~~~~~~

.. container:: indent

   The custom GUI for this demo highlights the :adi:`EV-STRUCTURAL-ARDZ` as a **structural health monitoring** with two main features: **acceleration detection** and **tiltation detection**.

   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_draft_gui.png
      :align: center
   


Resources
---------

-  :doc:`MAX32670-SX-ARDZ Base Board </wiki-migration/resources/eval/user-guides/max32670-sx-ardz>`

-  :doc:`EV-FLOWMETER-ARDZ Sensor for Flow Rate Metering </wiki-migration/resources/eval/user-guides/ev-flowmeter-ardz>`

| 
| ===== Design and Integration Files =====

.. admonition:: Download
   :class: download

   
   | `AD-MAX32SXWISE-SL Design Support Package <https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ad-max32sxwise-sl-designsupport.zip>`__
   | \* Schematic
   
   -  Bill of Materials
   -  Layout
   -  Fabrication Files
   


| 
| ===== Help and Support ===== For questions and more information about this product, connect with us through the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_battery_attachment.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/ev-structural-ardz_boardmount2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/max32625pico_maxdap.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_pico_attachment.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/gateway.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rpi_4_with_rak5146_hat.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/bin_files_2.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/1.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/flashing_sd_card.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/flashing_sd_card_2.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/chirpstack_ip.png
   :width: 600px
.. |\|| image:: /resources/eval/user-guides/longrangewirelessradio/advance_firewall_settings.png
   :width: 700px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/inbound_rule_2.png
   :width: 700px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config.png
   :width: 700px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_2.png
   :width: 700px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_3.png
   :width: 700px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_4.png
   :width: 700px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_5.png
   :width: 700px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_6.png
   :width: 700px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/log_in_page.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/software/gate_way_setup/add_device_profile.png
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/submit_application.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/device_details.png
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/app_key.png
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/integration.png
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/http_integration.png
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/http_integration_success.png
   :width: 600px
