Satcom Phased Array Reference Design
====================================

At Analog Devices, the Aerospace and Defense (ADEF) team provides a plethora of enablement solutions in different levels of development. *The Satcom Phased Array Reference Design* is a virtual reference design that contains a full signal chain solution for the desired specifications including a combination of RF front end design, digitizer integration, and power optimization. This design includes both Analog Devices and third-party hardware and is supported by multiple simulations and models for each design aspect. Customers can utilize this Wiki along with supporting technical articles to design this system and modify it to their specifications. The descriptions below show what type of solutions ADI provides, and where Satcom Phased Array Reference Design falls among them.

Types of ADEF Reference Designs
-------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02_077511a_adeftypesofplatforms.png
   :width: 600px

General Overview
----------------

For satellite communication systems that require in-mission frequency band reconfiguration, a multi-path design can be used to implement a single hardware design that can operate from L band to Ka band. This reference design shows an approach to developing a hybrid beamforming RX and TX system with up/down conversion that covers X, Ku and Ka band for satellite communication. However, the up/down converter can be bypassed to enable operation in the UHF, L, S, and C bands.

The reference design includes all aspects of the system including:

-  Analog Beamforming
-  RF Down/Up Conversion
-  LO and Clock Generation and Distribution
-  ADC and DAC Digitization
-  Digital Signal Processing
-  FPGA recommendation
-  Recommended Power Management

The highlighted performance for this reference design is the following:

-  16 Receive and 16 Transmit Elements (scalable)
-  Wide Frequency Coverage - Ka-band focused analog beamformer paired with wideband RF channel + Digitizer (L through Ka band)
-  Wide instantaneous BW
-  High NPR
-  Low noise figure
-  Quick reconfiguration
-  Synchronization across elements

--------------

Specifications and Array Level Beamforming
------------------------------------------

<fc #6495ed>\ **Click below to see the specifications for each subarray and full system level architecture along with beamforming** </fc>



.. raw:: html

   <details><summary>**1. Subarray Architecture and Specifications**</summary>

| <fc #6495ed>\ **Sub Array**\ </fc>
| The Satcom Phased Array Reference Design is a hybrid beamforming array that is modeled with 512 elements. The signal chain system is designed in a tiled fashion of 32 sub arrays. Shown below is a sub array. Each sub array has 16 channels for RX and 16 channels for TX, making up the entire 512 element hybrid array 16x32.

| 
| |image1|
| <fc #6495ed>\ **Ka Band Variant**\ </fc>

+--------------------------------+--------------------------------------------+------------------------------------------------------+
| *Parameter*                    | *Typ*                                      | *Comments*                                           |
+================================+============================================+======================================================+
| Number of Analog Beams         | 4T/4R                                      | Easily scalable up to 8 analog beams                 |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Number of Elements             | 16R Single Polarization                    | Scale up to higher element counts                    |
|                                | 16T Single Polarization                    | with large 1:N combiner between array                |
|                                |                                            | and digital channels                                 |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Scalability                    | Able to be scaled up to arbitrary          |                                                      |
|                                | number of elements and beams               |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Frequency Coverage             | Ka-band                                    | Using ADAR3000/ADAR3001 BFIC Front Ends              |
|                                | (27 to 30 GHz for Rx, 17 to 21 GHz for Tx) |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
|                                | Ku-band                                    | Using ADAR1000/ADAR3007 BFIC Front Ends              |
|                                | (13 to 14 GHz for Rx, 11 to 12 GHz for Tx) |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
|                                | X-band                                     | Using ADAR1000 BFIC Front End                        |
|                                | (8 to 9 GHz for Rx, 7 to 8 GHz for Tx)     |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
|                                | L, S, and C band                           | using mixer bypass and direct sampling               |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Instantaneous Bandwidth        | 1 GHz                                      | Max up to 2.4 GHz                                    |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Receive                        |                                            |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Rx Noise Figure                | < 2 dB typ.                                |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Rx Gain                        | 78 dB                                      | 16 Element Coherent Gain                             |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Rx Noise Power Ratio           | >40 dB typ.                                |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| IP1dB                          | -80 dBm                                    |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| IIP3                           | -60 dBm                                    |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Estimated DC Power per Element | 1 W typ.                                   | Can be reduced by increasing analog-to-digital ratio |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Transmit                       |                                            |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Tx Output Power                | 18 dBm typ.                                | With 6 dB backoff                                    |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Target OP1dB                   | 24 dBm                                     |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| OIP3                           | 35 dBm                                     |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| Tx Noise Power Ratio           | >30 dB typ.                                |                                                      |
+--------------------------------+--------------------------------------------+------------------------------------------------------+
| DC Power per Element           | 3.1 W typ.                                 | Can be reduced by increasing analog:digital ratio    |
+--------------------------------+--------------------------------------------+------------------------------------------------------+

| 
| ----

.. raw:: html

   </details>




.. raw:: html

   <details><summary>**2. Full 512-Element Hybrid Array Architecture and Specifications**</summary>

<fc #6495ed>\ **Full 512-Element Hybrid Array**\ </fc>

Shown below is the entire 512 element hybrid beamforming array. The system is capable of beamforming up to four independent analog beams. Each sub array steers four analog beams using 16 elements for a 16:1 analog combing ratio. The entire array combines 32 channels of each beam in the digital domain for a 32:1 digital combining ratio.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_entire_chain_array_v1.jpg
   :align: center

| 
| ---- <fc #6495ed>\ **System Level Specifications (Ka Band Variant)**\ </fc>

+----------------------------+--------------------------------+-----------------------------------------------+
| *Parameter*                | *Value*                        | *Comments/Conditions*                         |
+============================+================================+===============================================+
| Transmit                   |                                | *19.5 GHz - Taylor Taper: 30 dB SL rejection* |
+----------------------------+--------------------------------+-----------------------------------------------+
| Frequency Range            | Ka-band (Tx: 17 GHz to 21 GHz) | Using ADAR3001 BFIC Front End                 |
+----------------------------+--------------------------------+-----------------------------------------------+
| Instantaneous Bandwidth    | 1 GHz                          | Max up to 2.4 GHz                             |
+----------------------------+--------------------------------+-----------------------------------------------+
| Number of Elements         | 512 (32x16)                    | Single Polarization                           |
+----------------------------+--------------------------------+-----------------------------------------------+
| Number of Beams            | 4                              | Scalable up to 8 beams                        |
+----------------------------+--------------------------------+-----------------------------------------------+
| HPBW                       | Azimuth ±3.76 deg              | Assuming 1 Beam                               |
|                            | Elevation ±8 deg               |                                               |
+----------------------------+--------------------------------+-----------------------------------------------+
| FNBW                       | Azimuth ±10 deg                | Assuming 1 Beam                               |
|                            | Elevation ±20 deg              |                                               |
+----------------------------+--------------------------------+-----------------------------------------------+
| Beam Steering Range        | Azimuth ±60 deg                |                                               |
|                            | Elevation +/- 60deg            |                                               |
+----------------------------+--------------------------------+-----------------------------------------------+
| EIRP                       | 41 dBW                         | Per Beam at Boresight                         |
+----------------------------+--------------------------------+-----------------------------------------------+
| Antenna Directivity        | 31 dBi                         | At Boresight                                  |
+----------------------------+--------------------------------+-----------------------------------------------+
| Output Power Control Range | >30 dB                         | Using ADAR3000 DSA                            |
+----------------------------+--------------------------------+-----------------------------------------------+
| Beam Setting Accuracy      | <6 deg                         | Using ADAR3000 Phase Delay                    |
+----------------------------+--------------------------------+-----------------------------------------------+
| Sidelobes                  | 30 dB                          |                                               |
+----------------------------+--------------------------------+-----------------------------------------------+
| DC Power per Element       | 3.1 W typ.                     |                                               |
+----------------------------+--------------------------------+-----------------------------------------------+

+-------------------------+--------------------------------+---------------------------------------------+
| *Parameter*             | *Value*                        | *Comments/Conditions*                       |
+=========================+================================+=============================================+
| Receive                 |                                | *29 GHz - Taylor Taper: 30 dB SL rejection* |
+-------------------------+--------------------------------+---------------------------------------------+
| Frequency Range         | Ka-band (Rx: 27 GHz to 30 GHz) | Using ADAR3000 BFIC Front End               |
+-------------------------+--------------------------------+---------------------------------------------+
| Instantaneous Bandwidth | 1 GHz                          | Max up to 2.4 GHz                           |
+-------------------------+--------------------------------+---------------------------------------------+
| Number of Elements      | 512 (32x16)                    | Single Polarization                         |
+-------------------------+--------------------------------+---------------------------------------------+
| Number of Beams         | 4                              | Scalable up to 8 beams                      |
+-------------------------+--------------------------------+---------------------------------------------+
| Beam Steering Range     | Azimuth ±60 deg                |                                             |
|                         | Elevation ±60 deg              |                                             |
+-------------------------+--------------------------------+---------------------------------------------+
| HPBW                    | Azimuth ±3.76 deg              | Assuming 1 Beam                             |
|                         | Elevation ±8 deg               |                                             |
+-------------------------+--------------------------------+---------------------------------------------+
| FNBW                    | Azimuth ±10 deg                | Assuming 1 Beam                             |
|                         | Elevation ±20 deg              |                                             |
+-------------------------+--------------------------------+---------------------------------------------+
| G/T                     | 4.7 dB/K                       | Assuming Antenna Pointed at Earth           |
+-------------------------+--------------------------------+---------------------------------------------+
| Antenna Directivity     | 31.2 dBi                       | at Boresight                                |
+-------------------------+--------------------------------+---------------------------------------------+
| Beam Setting Accuracy   | <6 deg                         | Using ADAR3001 Phase Delay                  |
+-------------------------+--------------------------------+---------------------------------------------+
| Input Sensitivity       | >-120 dBm                      |                                             |
+-------------------------+--------------------------------+---------------------------------------------+
| Rx Noise Figure         | 2 dB                           |                                             |
+-------------------------+--------------------------------+---------------------------------------------+
| Sidelobes               | 30 dB                          |                                             |
+-------------------------+--------------------------------+---------------------------------------------+
| DC Power per Element    | 1.7 W typ.                     |                                             |
+-------------------------+--------------------------------+---------------------------------------------+

.. raw:: html

   </details>




.. raw:: html

   <details><summary>**3. Beamforming Patterns and Block Diagrams**</summary>

| 
| **Ka-band Beam Pattern Directivity**
| The following images were generated with the MATLAB Sensor Array Toolbox. Array geometry assumes 512 elements in 16x32 fashion with Taylor tapering in both row and column with 30dB sidelobe rejection.

| <fc #6495ed>\ **512 Element TX Beam Pattern Directivity at Ka Band (19.5GHz)**\ </fc> |image2|
| <fc #6495ed>\ **512 Element RX Beam Pattern Directivity at Ka Band (29GHz)**\ </fc> |image3|

| 
| **Ka-band RX Beamforming Implementation**
| Each of the four analog beams are steered using the variable amplitude and phase (VAP) blocks inside the ADAR3000 and ADAR3001 analog beamforming IC’s. Each subarray has 4 transmit and 4 receive channels for a total of 128 channels that are digitally combined 32:1 in a dedicated FPGA or digital ASIC. Shown below are 4 large analog beams for RX; Each with a digital beam inside, which is controlled by weights withing the FPGA or ASIC.

To increase the number of digital beams inside each analog beam, one can make copies of all phased array time domain data in the digital domain. Looking at the image below, there is a condensed diagram of the system to emphasize the delineation between analog and digital beamforming. Channels are color coded to show which beam they belong to. In the case of 4 digital beams, there are 32 instances of each analog beam that are combined in the digital domain. All of the channels from analog beam 1 are combined: Ch1, Ch5, Ch9, … , Ch125. All the channels from analog beam 2 are combined: Ch2, Ch6, Ch10, … , Ch126. So on and so fourth for beams 3 and 4.

| 
| <fc #6495ed>**512 Element RX Hybrid Beamforming (4Beams) \**</fc> |image4|

| 
| For 8 digital beams, ADC data is copied in the digital domain as shown in the picture below. Once the data is copied, it can be manipulated produce twice as many digital beams inside the analog beams. Theoretically, an infinite amount of digital beams inside each analog beam is realizable, but the caveat is FPGA processing power. After a certain number of beams, the task will be too computationally intensive to produce more. Further, each of the digital beams also have a finite beamwidth. At some point the beamwidths of digital beam inside each of the four analog beams will overlap and will be redundant.

| 
| <fc #6495ed>**512 Element RX Hybrid Beamforming (8Beams) \**</fc> |image5|

.. raw:: html

   </details>


Signal Chain Resources
----------------------

.. note::

   
   -  :doc:`Receiver Signal Chain Overview and Theory of Operation </wiki-migration/resources/eval/developer-kits/satcom-ref-design/rx-overview>`
   -  :doc:`Transmitter Signal Chain Overview and Theory of Operation </wiki-migration/resources/eval/developer-kits/satcom-ref-design/tx-overview>`
   -  :doc:`LO Generation Overview and Theory of Operation </wiki-migration/resources/eval/developer-kits/satcom-ref-design/lo-overview>`
   


--------------

Power Supply Design
-------------------

| 

.. raw:: html

   <details><summary>| The power solution for the Wideband Satcom Front End provides regulation for the four major functional blocks in the system:


   | \* Wideband Signal Conditioning TX/RX Chain

-  Band Specific Analog Beamforming TX/RX Chain
-  LO Generation and Conditioning Chain
-  AD9082 MxFE and Digitization Chain

**Click HERE to read more**</summary>

|

| <fc #6495ed>\ **TX/RX Beamforming Network Power Supply Design**\ </fc>

The power solution for both the transmit and receive analog beamforming front ends (shown below) feature two types of switching regulators. One is the :adi:`LTM8063`, which features Silent Switcher® technology and offers a wide selectable switching frequency from 200 kHz to 2.2 MHz. The other is the :adi:`ADP5600`, which again, integrates a low ripple interleaved inverting charge pump with a high performance LDO to easily produce clean negative voltages. The sensitive signal chain power domains are regulated by low noise, high performance linear regulators. LDOs such as the :adi:`LT3041` follow :adi:`LTM8063`. The :adi:`LT3041` features industry leading performance with 80 dB PSRR at 1 MHz.

| |image6|
| <fc #6495ed>\ **TX/RX LO Generation Power Supply Design**\ </fc>

The power solution for both the transmit and receive LO chains (shown below) feature two types of switching regulators. One is the ultra-small :adi:`MAXM17632`, which delivers 1 A at high efficiency from up to 36 Vin in a tiny 3x3 mm uSLICTM package. The other is the :adi:`ADP5600`, which integrates a low ripple interleaved inverting charge pump with a high performance LDO to easily produce clean negative voltages. The sensitive signal chain power domains are regulated by low noise, high performance linear regulators.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/lo_generation_4_18_2023.png
   :align: center

| 
| <fc #6495ed>\ **TX / RX Down-converter Power Supply Design**\ </fc>

The power solution for both the transmit chain and receive chain (shown below) follow a similar design philosophy as the LO. They feature two types of switching regulators. One is the :adi:`LTM8063`, which features Silent Switcher® technology and offers a wide selectable switching frequency from 200 kHz to 2.2 MHz. The other is the :adi:`ADP5600`, which again, integrates a low ripple interleaved inverting charge pump with a high performance LDO to easily produce clean negative voltages. The sensitive signal chain power domains are regulated by low noise, high performance linear regulators.

| |image7|
| <fc #6495ed>\ **Digitizer and Clock Power Supply Design**\ </fc>

The power solution for the MxFE and its clock (shown below) features Silent Switcher® technology. These high efficiency regulators, :adi:`LTM8051` and :adi:`LTM4702`, feature low EMI and output noise. Some power domains of the MxFE chip can be driven directly from a Silent Switcher® output, while the more sensitive ICs such as the :adi:`ADF4377` clock chip are further regulated by LDOs like the :adi:`LT3041`. The :adi:`LT3041` LDO features industry leading performance with 80 dB PSRR at 1 MHz.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/digitizer_power_supplies_4_18_2023.png
   :align: center

.. raw:: html

   </details>


--------------

Bill of Materials
-----------------

| 

.. raw:: html

   <details><summary>| The table below lists the part numbers for the components used in the design. Where space qualified parts are not available, the commercial part number is listed. Some of the part numbers listed below are space specials which do not appear on analog.com. Please contact ADI sales or an authorized distributor for more information and to receive orderable part numbers.
| **Click HERE to view the list.**</summary>

+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| *Circuit* |   | *Device*                                                                                                                                      |   | *Description*                                                     |   | *Package*           |   | *Process*                         |   | *Qualification Level* |   | *Production Status*         |
+===========+===+===============================================================================================================================================+===+===================================================================+===+=====================+===+===================================+===+=======================+===+=============================+
| Rx        |   | :adi:`ADRF5730`                                                                                                                               |   | 0.1 GHz to 40 GHz Digital Step Attenuator                         |   | 24-Terminal LGA     |   | Advanced Silicon                  |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADRF5022`                                                                                                                               |   | 0.1 GHz to 45 GHz Silicon SPDT Reflective Switch                  |   | 12-Lead LGA         |   | Advanced Silicon                  |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADRF5144`                                                                                                                               |   | 1 GHz to 20 GHz Silicon SPDT Reflective Switch                    |   | 20-Terminal LGA     |   | Silicon                           |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADRF5040`                                                                                                                               |   | 9 kHz to 12 GHz Silicon SP4T Nonreflective Switch                 |   | Surface-Mount LFCSP |   | Silicon                           |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`HMC8413`                                                                                                                                |   | Low Noise Amplifier, 0.01 GHz to 9 GHz                            |   | 6-Lead LFCSP        |   | GaAs pHEMPT                       |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADL8142S`-CSL                                                                                                                           |   | Low Noise Amplifier, 23 GHz to 31 GHz                             |   | 8-Lead LFCSP        |   | GaAs pHEMPT                       |   | CSL                   |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`AD9082`                                                                                                                                 |   | MxFE Quad, 16-Bit, 12 GSPS RF DAC and Dual, 12-Bit, 6 GSPS RF ADC |   | 324-Ball BGA        |   | -                                 |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADAR3001S`-CSL                                                                                                                          |   | 27.5 GHz to 31 GHz, 4-Beam and 4-Element, Ka-Band Beamformer      |   | 311-Pin BGA         |   | -                                 |   | CSL                   |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADAR5000`                                                                                                                               |   | 4-Way RF Splitter Combiner, 17 GHz to 32 GHz                      |   | WLCSP               |   | -                                 |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | :adi:`ADMFM2000`                                                                                                                              |   | 0.5 GHz to 32 GHz Microwave Down Converter SIP                    |   | 179-Pin BGA         |   | -                                 |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | `HFCN-3100+ <https://www.minicircuits.com/WebStore/dashboard.html?model=HFCN-3100%2B>`_                                                       |   | Mini Circuits LTCC High Pass Filter, 3400 to 9900 MHz             |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | `LFCW-5000+ <https://www.minicircuits.com/WebStore/dashboard.html?model=LFCW-5000%2B>`_                                                       |   | Mini Circuits LTCC Low Pass Filter, DC to 5000 MHz                |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | `LFCG-2600+ <https://www.minicircuits.com/WebStore/dashboard.html?model=LFCG-2600%2B>`_                                                       |   | Mini Circuits LTCC Low Pass Filter, DC to 2600 MHz                |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | `BFHK-6751+ <https://www.minicircuits.com/WebStore/dashboard.html?model=BFHK-6751%2B>`_                                                       |   | Mini Circuits LTCC Band Pass Filter, 5900 to 6900 MHz             |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | `BFCQ-2702+ <https://www.minicircuits.com/WebStore/dashboard.html?model=BFCQ-2702%2B>`_                                                       |   | Mini Circuits LTCC Band Pass Filter, 22000 to 31000 MHz           |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| Rx        |   | `B291MB0S <https://www.knowlescapacitors.com/getattachment/Products/Microwave-Products/BandpassFilters/B291MB0S_Datasheet.pdf?lang=en-US>`_   |   | Knowles DLI 29.1 GHz Surface Mount Band Pass Filter               |   | package             |   | GaAs Integrated Passive Component |   | Contact Knowles DLI   |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`ADRF5730`                                                                                                                               |   | 0.1 to 40 GHz Digital Step Attenuator                             |   | 24-Terminal LGA     |   | Advanced Silicon                  |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`ADRF5022`                                                                                                                               |   | 0.1 GHz to 45 GHz Silicon SPDT Reflective Switch                  |   | 12-Lead LGA         |   | Advanced Silicon                  |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`ADRF5144`                                                                                                                               |   | 1 GHz to 20 GHz Silicon SPDT Reflective Switch                    |   | 20-Terminal LGA     |   | Silicon                           |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`HMC8413`                                                                                                                                |   | Low Noise Amplifier, 0.01 GHz to 9 GHz                            |   | 6-Lead LFCSP        |   | GaAs pHEMPT                       |   | Commerical            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`HMC7950`                                                                                                                                |   | Low Noise Amplifier, 2 GHz to 28 GHz                              |   | 16-Lead LCC         |   | GaAs pHEMPT                       |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`ADAR3000S`-CSL                                                                                                                          |   | 17 GHz to 22 GHz, 4-Beam and 4-Element, Ka-Band Beamformer SIP    |   | 311-ball CSPBGA     |   | -                                 |   | CSL                   |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`ADAR5000`                                                                                                                               |   | 4-Way RF Splitter Combiner, 17 GHz to 32 GHz                      |   | WLCSP               |   | -                                 |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | :adi:`ADMFM2001`                                                                                                                              |   | 7 GHz to 31 GHz Microwave Up Converter SIP                        |   | 179-Pin BGA         |   | -                                 |   | Commercial            |   | Pre-Release                 |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | `LFCG-4400+ <https://www.minicircuits.com/WebStore/dashboard.html?model=LFCG-4400%2B>`_                                                       |   | Mini Circuits LTCC Low Pass Filter, DC to 4400 MHz                |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | `L204XF4S <https://www.knowlescapacitors.com/getattachment/Products/Microwave-Products/Lowpass-Filters/L204XF4S-Datasheet.pdf.aspx>`_         |   | Knowles DLI 20.4 GHz Surface Mount Low Pass Filter                |   | package             |   | GaAs Integrated Passive Component |   | Contact Knowles DLI   |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | `B192NB2S <https://www.knowlescapacitors.com/getattachment/Products/Microwave-Products/Bandpass-Filters/B192NB2S_Datasheet.pdf?lang=en-US>`_  |   | Knowles DLI 19.2 GHz Surface Mount Band Pass Filter               |   | package             |   | GaAs Integrated Passive Component |   | Contact Knowles DLI   |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| TX        |   | `BFHK-1982+ <https://www.minicircuits.com/WebStore/dashboard.html?model=BFHK-1982%2B>`_                                                       |   | Mini Circuits LTCC Band Pass Filter, 17500 to 22200 MHz           |   | package             |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | :adi:`ADF4371`                                                                                                                                |   | 62.5 MHz to 32 GHz Synthesizer with Integrated VCO                |   | 7x7 LGA             |   | Silicon                           |   | Commerical            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | :adi:`ADMV8416`                                                                                                                               |   | 6.3 GHz to 18 GHz, Tunable Band-Pass Filter                       |   | 6x6 LFCSP           |   | GaAs                              |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | :adi:`ADMV8432`                                                                                                                               |   | 15.1 GHz to 32 GHz, Tunable Band-Pass Filter                      |   | 6x6 LFCSP           |   | GaAs                              |   | Commerical            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | :adi:`HMC1126`                                                                                                                                |   | Low Noise Amplifier, 400 MHz to 52 GHz                            |   | 5x5 LGA             |   | GaAs pHEMPT                       |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | :adi:`ADRF5022`                                                                                                                               |   | Silicon Non-Reflective SPDT Switch, 100 MHz to 45 GHz             |   | 3x3 LGA             |   | Silicon                           |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | KAT-3+                                                                                                                                        |   | Mini Circuits DC to 43.5 GHz Absorptive 3 dB Fixed Attenuator     |   | 2x2 MCLP            |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | :adi:`ADRF5730`                                                                                                                               |   | 0.1 to 40 GHz Digital Step Attenuator                             |   | 4x4 LGA             |   | Silicon                           |   | Commercial            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| LO        |   | EP2KA+                                                                                                                                        |   | Mini Circuits 10 to 43.5 GHz 2 Way-0° Power Splitter              |   | 3.5x2.5 QFN         |   | GaAs Integrated Passive Component |   | Contact Mini Circuits |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| DIGI      |   | :adi:`AD9082`                                                                                                                                 |   | MxFE Quad, 16-Bit, 12 GSPS RF DAC and Dual, 12-Bit, 6 GSPS RF ADC |   | 324-Ball BGA        |   | -                                 |   | Commerical            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| DIGI      |   | :adi:`LTC6953`                                                                                                                                |   | Ultralow Jitter, 4.5 GHz, 11 Output Clock Distributor             |   | 52-Lead QFN         |   | -                                 |   | Commerical            |   | Last Time Buy               |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+
| DIGI      |   | :adi:`ADF4371`                                                                                                                                |   | 62.5 MHz to 32 GHz Synthesizer with Integrated VCO                |   | 7x7 LGA             |   | Silicon                           |   | Commerical            |   | Recommended for New Designs |
+-----------+---+-----------------------------------------------------------------------------------------------------------------------------------------------+---+-------------------------------------------------------------------+---+---------------------+---+-----------------------------------+---+-----------------------+---+-----------------------------+

.. raw:: html

   </details>


--------------

Software and Simulation Downloads
---------------------------------



.. raw:: html

   <details><summary>Download the simulation models and device drivers below:</summary>

| 
| <fc #6495ed>\ **Simulation Downloads**\ </fc>
| This section contains the simulation models generated using Keysight Genesys.
| <fc #6495ed>\ **TX Downloads**\ </fc>

.. admonition:: Download
   :class: download

   Keysight Genesys TX RF Signal Chain: `full_tx_signal_chain.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/full_tx_signal_chain.zip>`_


   | MATLAB TX 512-element phased array model: `sensorarray_19.5ghz_tx.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/sensorarray_19.5ghz_tx.zip>`_


<fc #6495ed>\ **RX Downloads**\ </fc>

|

.. admonition:: Download
   :class: download

   Keysight Genesys RX RF Signal Chain: Coming Soon


   | MATLAB RX 512-element phased array model: `sensorarray_29ghz_rx.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/sensorarray_29ghz_rx.zip>`_


|

| **<fc #6495ed>Supported Device Drivers</fc>**
| \* :doc:`ADRF5730: 0.5 dB LSB, 6-Bit, Silicon Digital Attenuator, 100 MHz to 40 GHz </wiki-migration/resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`

-  :doc:`ADMFM2000 0.5 GHz to 32 GHz Microwave Downconverter </wiki-migration/resources/tools-software/linux-drivers/iio-pll/admfm2000>`
-  `ADAR3000: 17 GHz to 22 GHz, 4-Beam and 4-Element, Ka-Band Beamformer <https://wiki.analog.com/resources/tools-software/linux-drivers/beamformer/adar300x>`_
-  `ADAR3001: 27.5 GHz to 31 GHz, 4-Beam and 4-Element, Ka-Band Beamformer <https://wiki.analog.com/resources/tools-software/linux-drivers/beamformer/adar300x>`_
-  :doc:`AD9082: MxFE® Quad, 16-Bit, 12 GSPS RF DAC and Dual, 12-Bit, 6 GSPS RF ADC </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
-  :doc:`ADF4371: Wideband Synthesizer with Integrated VCO </wiki-migration/resources/tools-software/linux-drivers/iio-pll/adf4371>`
-  :doc:`LTC6953: Ultralow Jitter, 4.5 GHz Clock Distributor with 11 Outputs, JESD204B/JESD204C </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ltc6952>`

| 
| **<fc #6495ed> Supported Evaluation Boards</fc>**
| \* :adi:`EVAL-ADRF5730`

-  :adi:`ADMFM2000` - Contact: SampleSupport@analog.com
-  :adi:`ADAR3000` - Contact: beamformer@analog.com
-  :adi:`ADAR3001` - Contact: beamformer@analog.com
-  :adi:`AD9082-FMCA-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad9082.html>`
-  :adi:`EVAL-ADF4371`
-  :adi:`DC2610A Demo Board for LTC6953 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/dc2610a.html>`

.. raw:: html

   </details>


--------------

Additional Information
----------------------

Publications and Media
~~~~~~~~~~~~~~~~~~~~~~

-  :ez:`Satcom Phased Array Webinar <webinar/c/e/538>`
-  :adi:`Satcom Phased Array Reference Design Highlights <en/education/education-library/videos/6311760314112.html>`
-  :adi:`ADEF Space Solutions Product Page <en/solutions/aerospace-and-defense/space/space-technology-complete-solution.html#>`

Reference Designs
~~~~~~~~~~~~~~~~~

-  :doc:`Developer Platforms and Reference Designs </wiki-migration/resources/eval/developer-kits>`

--------------

Help and Support
----------------

.. hint::

   For support on this reference design, please contact us through our technical support portal: :adi:`technical-support.html <en/support/technical-support.html>`


| 

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_entire_chain_updated_v3.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/3d_tx_directivity_.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/3d_rx_directivity_.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/array_level_beamforming_implementation_block_diagram_4_beams.jpg
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/array_level_beamforming_implementation_block_diagram_8_beams.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/bfic_power_supplies_11_22_2023.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/tx_rx_power_supplies_11_22_2023.png
