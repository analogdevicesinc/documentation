Pioneer 1 - Wired CbM Evaluation Platform
=========================================

Overview
--------

The Pioneer 1 - Wired CbM Evaluation Platform provides a robust industrial wired link solution for the ADcmXL3021 Triaxial Vibration Sensor :adi:`adcmxl3021.html <en/products/adcmxl3021.html>`. The ADcmXL3021 features ultra low noise density (26 μg/√Hz) and wide bandwidth to 10 kHz, which supports excellent measurement resolution and tracking of key vibration signatures. The EV-CbM-Pioneer1-1Z and EV-CbM-Pioneer1-2Z kits provide a complete plug and play solution for operating the ADcmXL3021 on an RS-485 network over meters of cable in harsh industrial environments. This wired evaluation platform is enables monitoring of industrial assets to improve up-time, accelerating the path to :adi:`Industry 4.0. <en/applications/markets/industrial-automation-technology-pavilion-home/condition-based-monitoring.html>`

EV-CbM-Pioneer1-1Z / EV-CbM-Pioneer1-2Z Kit Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Provides 3 different Slave Board designs for ADcmXL3021 attach, which enable system design flexibility. Figure 1 and Table 1 provide details. Slaves 2 and 3 provide a direct SPI to RS-485 link, while Slave 1 includes an microcontroller which provides a UART to RS-485 interface.
-  Combines power and data over 1 standard cable, which reduces cable and connector costs at remote Sensor nodes.
-  Provides industry standard RJ45/RJ50 cables and connectors which are well shielded for noisy environments, are not bulky, and provide a path to IP67 enviornmental rating for integrated CbM module.
-  Includes a Master interface board with multiple connectors for system controller attach.
-  Provides open source schematics, layout, and bill of materials which can be used as a guideline for end product design.
-  Dedicated software GUI enables simple configuration of the ADcmXL3021 device, and vibration data and capture over long cables.

**Table 1. Solution Performance Trade Offs**

================= =========== ======== ========== ======
Solution          Flexibility PCB Area Complexity EMC
================= =========== ======== ========== ======
DEMO-CbM-Slave3-Z Low         Low      Low        Medium
DEMO-CbM-Slave2-Z Low         Low      Low        High
DEMO-CbM-Slave1-Z High        Medium   Medium     High
================= =========== ======== ========== ======

|image1| **Figure 1. Slave Solution Options**

SPI SCLK vs. Cable Length Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following guidelines apply for the direct SPI to RS-485 link designs (DEMO-CbM-Slave2-Z and DEMO-CbM-Slave3-Z). The SPI to RS-485/RS-422 link designs include a SPI clock transfer over RS-422 (SCLK) and a power over data lines implementation (phantom power), where data and power share the same twisted pair (SPI MISO).

**Cable Effects**

-  Over long cable runs the SPI SCLK signal will incur a propagation delay through the cable, of the order of 400-500 ns for a 100 m cable.
-  For a SPI MOSI data transfer from Master to Slave, the MOSI and SCLK are equally delayed by the cable.
-  However, data sent from the slave MISO to the master will be out of sync with SPI SCLK by twice the cable propagation delay.

**Maximum SPI SCLK**

-  Is set by the system propagation delay, which includes cable propagation delay, and Master + Slave Component propagation delays.

**Minimum SPI SCLK**

-  Is set by the Phantom Power filter components, which high-pass filter data on SPI MISO. This technique requires that the data signals being transmitted do not have content at DC or at very low frequencies. If operating at higher frequencies in the MHz range, it is important to note that a long string of logic '1' bits will mean a dynamic effective data rate in the kHz.

\*\* Typical Performance*\*

-  Typical SPI SCLK rate vs. cable length performance in a Phantom Power network is characterized in Figure 2. This shows DEMO-CbM-Slave3-Z (non-isolated slave) and DEMO-CbM-Slave2-Z (isolated slave)error free performance when porting the ADcmXL3021 SPI output over cabling.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pioneer_1_kit_sclk_vs_dr_wiki_rev1.png
   :align: center
   :width: 600px

**Figure 2. SPI SCLK vs. Cable Length Typical Performance**

Getting Started
---------------

Equipment
~~~~~~~~~

The following is supplied as part of the **EV-CbM-Pioneer1-1Z** demo kit:

-  Master Interface Controller board DEMO-CbM-Master-Z.
-  Low complexity non-isolated Slave Sensor interface board DEMO-CbM-Slave3-Z.
-  Low complexity isolated Slave Sensor interface board DEMO-CbM-Slave2-Z.
-  2m RJ50 cable (194612-02) and 10m RJ50 cable (194612-10)
-  AC/DC Power Supply - EU/UK/US/AU

The following is supplied as part of the **EV-CbM-Pioneer1-2Z** demo kit:

-  All of the **EV**-CbM-Pioneer1-1Z demo kit contents
-  :adi:`ADcmXL3021BMLZ 14-lead Module <en/products/adcmxl3021.html>`.
-   `Cypress SuperSpeed Explorer kit (CYUSB3KIT-003) <https://www.element14.com/community/docs/DOC-74653/l/ez-usb-fx3-superspeed-explorer-kit>`_ and USB 3.0 cable.

The following equipment is suggested as a vibration source, but not strictly required, as the system can also be tested manually:

-  `6cm 12VDC 0.15A cooling fan <https://www.amazon.co.uk/dp/B07BPXG5ZV/ref=pe_3187911_189395841_TE_dp_f1>`_
-  `Plastic Enclosure (for mounting the ADcmXL3021 and the cooling fan) <https://ie.farnell.com/camdenboss/cbard-clr/arduino-uno-enclosure-hips-clear/dp/2360475>`_
-  Power supply for the cooling fan

Typical Setup
~~~~~~~~~~~~~

The following steps describe a typical setup, as shown in Figure 3, to communicate over a SPI to RS-485 link using either DEMO-CbM-Slave2-Z or DEMO-CbM-Slave3-Z:

-  Ensure that the following jumper selections are made for the DEMO-CbM-Master-Z: LK8: position A or position B, and LK5 and LK6: Position A. The LK8 jumper needs to be set, but the position is at the user's discretion.
-  Connect the supplied 2-meter RJ50 cable to the J10 RJ50 connector on the DEMO-CbM-Master-Z as indicated in Figure 4. Do not confuse this with the RJ45 connector (J1). Inserting RJ50 cable plugs into RJ45 connectors will damage the plug/connector contacts.
-  Connect the Cypress Evaluation Board CYUSB3KIT-003 as shown in Figure 4 below. J6 and J7 on the DEMO-CbM-Master-Z align with the like-named J6 and J7 on the CYUSB3KIT-003.
-  Connect the supplied 2-meter RJ50 cable to the J10 RJ50 connector on the DEMO-CbM-Slave3-Z (or DEMO-CbM-Slave2-Z).
-  Connect the ADcmXL3021 XL module hi-rose connector (male) to the hi-rose connector (female) on the DEMO-CbM-Slave3-Z. Refer to Figure 5 for connector orientation. Ensure that Pin1 on both connectors is aligned as shown.
-  Connect the Power Supply to the barrel connector on the DEMO-CbM-Master-Z. The power supply should be set to a minimum of +6 V and a maximum of +12 V. This provides power to both master and slave boards.
-  **Note: the Master board barrel connector is configured for a positive centre tip power supply. For the demo kit power supply –-> connect the positive centre (+) to the positive centre (+) on the small tip adaptors.**
-  Connect the USB 3.0 cable supplied with the CYUSB3KIT-003 to a USB 3.0 port on your computer.

.. important::

   You can use the supplied 2 meter RJ50 cable with either the DEMO-CbM-Slave3-Z or DEMO-CbM-Slave2-Z. However, the 10 meter RJ50 cable can only be used with the DEMO-CbM-Slave3-Z.


|image2| **Figure 3. Typical Evaluation Setup**

|image3| **Figure 4. Master Board Setup**

|image4| **Figure 5. Hi-Rose Connector Orientation and S2 Pushbutton Switch**

Software Application (GUI)
--------------------------

Software Installation
~~~~~~~~~~~~~~~~~~~~~

Two downloads are required, with all software available on the :doc:`ADcmXL3021 wiki </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adcmxl-pc-eval>`.

-  Download and unzip the file called FX3Driver.zip. Then run the DriverSetup.exe file
-  Download, unzip, and Run the ADCMXL Evaluation Software, version 2.1.8.

.. tip::

   Tip: The ADcmXL3021 wiki also includes detailed software installation and troubleshooting instructions.


GUI measurements using Typical Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open the Vibration Evaluation software version 2.1.8 on your computer.
-  Open the ‘Comm’ menu and select ‘SPI’. Set the SPI SCLK to 2.5 MHz and hit ‘update’.
-  Select Manual Time Capture (MTC) from the Mode Selection drop down menu, and hit the start button.
-  For the Typical setup described in Figure 3 – the X, Y, and Z axis MTC measurements are shown in Figure 6.
-  The corresponding Manual Fast Fourier Transform (MFFT) measurements are shown in Figure 7.

.. tip::

   Tip: If the system is unresponsive, or data plots are erroneous, then press the S2 pushbutton switch on the DEMO-CbM-Slave2-Z / DEMO-CbM-Slave3-Z to reset the ADcmXL3021.


|image5| **Figure 6. Typical Manual Time Capture Plot - corresponding to Figure 3 Typical Setup**

|image6| **Figure 7. Typical Manual FFT Plot - corresponding to Figure 3 Typical Setup**

GUI measurements for a non-Repetitive Vibration Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To provide a more easily visible Manual Time Capture (MTC) of a 'finger tap' vibration on the top surface of the ADcmXL3021, access the AVG_CNT register as shown in Figure 8. Write HEX 0x3 to AVG_CNT and perform a read back to confirm the write. This will decimate the signal so that the MTC waveform can be viewed easily. Figure 9 shows an example MTC measurement where a 'finger tap' vibration is applied to the top surface of the ADcmXL3021 module.

|image7| **Figure 8. Write Hex 0x3 to the AVG_CNT Register to Decimate**

|image8| **Figure 9. Typical Manual Time Capture plot - Finger Tap Vibration Setup**

Schematics, Layout, BOM
-----------------------

Schematics, layout, BOM, and Gerber file for the DEMO-CbM-Slave2-Z: `click here to download <https://wiki.analog.com/_media/resources/eval/user-guides/demo-cbm-slave2-z_2_.zip>`_

Schematics, layout, BOM, and Gerber file for the DEMO-CbM-Slave3-Z: `click here to download <https://wiki.analog.com/_media/resources/eval/user-guides/demo-cbm-slave3-z_2_.zip>`_

Schematics, layout, BOM, and Gerber file for the DEMO-CbM-Master-Z: `click here to download <https://wiki.analog.com/_media/resources/eval/user-guides/demo-cbm-master-z.zip>`_

Schematics, layout, BOM, and Gerber file for the DEMO-CbM-Expandr-Z: `click here to download <https://wiki.analog.com/_media/resources/eval/user-guides/demo-cbm-expandr-z_zip.zip>`_

LTspice Simulation
------------------

A simplified power over data wires simulation circuit is provided in Figure 10. This circuit uses LTC2862 RS-485 transceiver LTspice macromodels and 1 mH inductors (Wurth 74477830). LTspice includes real inductor models, which include device parasitics, enabling closer correlation between simulation and real design performance. The DC blocking capacitor values are 10 µF. In general, using larger inductor and capacitor values enable a lower data rate performance on the communication network. The simulated test case is a 250 kHz data rate, which roughly corresponds to 100 meters of cabled communication when porting clock synchronised SPI over an RS-485 interface. The input voltage waveform used in the simulation corresponds to a worst-case dc content, with a 16-bit word and all logic high bits. Simulation results are presented in Figures 11 and 12. The input voltage waveform (VIN) matches the output at the remote powered device (no communication errors). Figure 12 presents a zoomed-in view of the bus voltage differential waveform (voltage A – voltage B) for droop analysis. The voltage at the remote sensor node, extracted from the L2 inductor (V(pout)) provides a power supply rail of 5V±1mV.

|image9| **Figure 10. Engineered Power LTspice simulation circuit using LTC2862 (RS-485) and 1mH Wurth Inductor 74477830**

|image10| **Figure 11. Simulation Result with RS-485 bus differential voltage V(A,B) , and droop points X and Y**

|image11| **Figure 12. Droop analysis for point X and Y**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/13.png
   :align: center

The VDROOP, VPEAK, and TDROOP are measured using the Figure 11 and 12 LTspice waveform. The L and C values are then calculated using equations 2 and 4. It depends where you measure on the waveform, however, the calculated L value is 1 to 3mH as shown in Table 1. Measuring at point X (Figure 12) is most accurate and yields the correct inductance value of approximately 1 mH. The high pass filter frequency (equation 6) is simply a function of the droop time and voltage, and for point X is approximately equates to 250 kHz/32 for 1 bit (half clock cycle), which matches the input waveform (V3) shown in the Figure 10 schematic.

**Table 1**


|image12|

When simulating Figure 10 it is also worth noting that the C8 capacitor is recommended to reduce voltage overshoot at the sensor (Vpout at power extraction node). With C8 added the overshoot is maximum 47mV and settles to within 1mV of the desired 5VDC within 1.6ms. Simulating without a C8 capacitor results in an underdamped system, with 600mV overshoot, and a permanent 100mV of voltage oscillation from the 5V dc target.

LTSpice models are available here: `click here to download <https://wiki.analog.com/_media/resources/eval/user-guides/podl_article.zip>`_

Change Log
----------

\*July 2019. Initial Release.

\*August 2019. Added additional information on demo power supply configuration.

\*February 2021. Added LTspice models for engineered power.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/slave_soln_options.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/figure_1.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/figure_2.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/figure_3.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/mtc.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/mfft.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/finger_tap2.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/finger_tap1.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/new.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/11.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/12.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/table.png
