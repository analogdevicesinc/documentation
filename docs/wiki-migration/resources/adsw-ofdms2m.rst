ADSW-OFDMS2M HDL Reference Modem
================================

Overview
--------

The **ADSW-OFDMS2M** is an HDL reference modem showcasing ADI’s best-in-class RF transceivers in wireless communications applications. The design is implemented using the :doc:`ADRV9361-Z7035 System-on-Module (SoM) </wiki-migration/resources/eval/user-guides/adrv936x_rfsom>`, which is based on the :adi:`AD9361` RF Transceiver and the Xilinx Zynq®-7000 All Programmable (AP) System-on-Chip (SoC).

This reference design integrates an HDL PHY layer with a demo application for video streaming. The HDL PHY layer originally supports orthogonal frequency domain multiplexing 1T1R single-input single-output (OFDM-SISO) mode. This is further extended to support multiple input multiple output (OFDM-MIMO) spatial diversity mode. The wireless standard is based on a modified IEEE 802.11n protocol.

Despite the ubiquity of IEEE 802.11, there are few available reference projects that fully implement a customizable, full-stack communication system, from application layer down to the physical layer, on a system-on-chip. The purpose of this software reference design is to show customers how they may use the AD936x transceivers as a communication link for unmanned aerial vehicles (UAVs) and drones.

| 
| ===== System Architecture ===== Figure 1 illustrates the high-level ADSW-OFDM2M architecture. The communication stack is focused mainly on the FPGA where the signal processing for the PHY layer is implemented. The signal processing includes the TX and RX chains, as well as a lower MAC layer.

A demonstration GUI application runs on :doc:`ADI Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`. For the PHY layer to communicate with user space applications, it reuses existing upper-level protocols such as TCP/IP stack and loadable drivers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/high-level_architecture_block_diagram.png
   :align: center
   :width: 800px

.. container:: center

   *Figure 1. High-level Architecture Block Diagram*


| 
| ===== Features =====

.. container:: center

   
   +------------------------------+-----------------------------------------------------------+
   | **Transmitter/Receiver**     | 1T1R – Single Input Single Output                         |
   |                              | 2T2R - Multiple Input Multiple Output (Spatial Diversity) |
   +------------------------------+-----------------------------------------------------------+
   | **Frequency Bands**          | 2.4 GHz ISM band (2.412 GHz to 2.462 GHz)                 |
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
   | **Supported Platforms**      | Zynq 7020 (Zedboard) + AD-FMCOMMS3-EBZ                    |
   |                              | Zynq 7035 (ADRVSOM) + ADRV9361                            |
   +------------------------------+-----------------------------------------------------------+
   


.. container:: center

   Moreover, the following signal processing blocks are implemented in the reference HDL modem:

   
   -  Constellation mapper/demapper
   -  Scrambler/descrambler
   -  STBC combiner/decoder
   -  Cyclic delay shift
   -  Channel estimation, equalization & maximum ratio combining
   -  Preamble for HT-mixed format
   -  Measurement modules: latency, packet loss
   


| 
| ===== Applications ===== Possible applications of the ADSW-OFDMS2M reference modem include the following:

-  UAV communications
-  Wireless video transmission

| 
| ▶️Recorded demonstration of a wireless video transmission using the ADSW-OFDMS2M HDL reference modem

.. image:: https://wiki.analog.com/_media/youtube>QH53fXQbzeI
   :alt: youtube>QH53fXQbzeI

| 
| ===== Use Cases ===== The ADSW-OFDMS2M evaluation platform can be operated using the following use cases, depending on the loaded software in the SD card.

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **SISO** | The SISO build follows the use case of a typical IEEE 802.11 Basic Service Set where a wireless station/client connects to an access point.                                                          |
|          | On top of these standard IEEE 802.11 modes, the radio can be either configured to emulate drone or controller functionalities, depending on the connected peripherals and software scripts executed. |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **MIMO** | The MIMO build only supports the monitor mode and as such, only supports the following operation as packet injector and sniffer.                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== Demo Application ===== |image1|

The ADSW-OFDMS2M demo application has two operating modes which emulate functions for the drone and controller side. The drone mode is expected to start the video streaming and receive the telemetry commands. The controller mode will be sending the telemetry commands while receiving and performing video playback.

| 
| ===== Help and Support ===== For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 
| ===== Additional Resources =====

-  :doc:`Linux on RF SoM </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
-  :doc:`Analog Devices Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dronetrx/dronetrx_demo_application_as_run_in_kuiper_linux.png
   :width: 800px
