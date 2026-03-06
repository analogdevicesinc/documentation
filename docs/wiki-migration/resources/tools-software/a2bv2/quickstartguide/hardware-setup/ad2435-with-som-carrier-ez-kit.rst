:doc:`Click here to return to the Hardware Setup page </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup>`

:doc:`Click here to return to the Running sample Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

AD2435 with SOM carrier ez-kit
==============================

Evaluation boards
-----------------

The AD243x high power evaluation boards used in the demos are explained in the following subsections.

ADZS2435-MINI
~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` shows a :doc:`ADZS2435-MINI </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` board which can be used as a high power A2B master. The board has following peripherals

-  AD2435 A2B transceiver
-  512K Self-Boot Memory (EEPROM)

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/adzs-2435mini.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure:** ADZS2435-MINI


Hardware modifications
^^^^^^^^^^^^^^^^^^^^^^

The following hardware modifications are required:-

-  For all ADZS2435-MINI boards, remove R70, R71, R85, R39.
-  For all ADZS2435-MINI boards, add R40.
-  For the board with I2C address 0x6A, remove R43 and add R42.

Jumper settings
^^^^^^^^^^^^^^^

The jumpers on the board must be in the following positions

-  P5 – connect 2 & 3
-  P6 – No connection
-  P10 – No connection

EVAL-AD2435WJ3LZ
~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` shows :doc:`EVAL-AD2435WJ3LZ </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` board which can be used as a high power bus powered A2B slave node. The board has following peripherals

-  AD2435 A2B transceiver
-  Stereo Audio Codec (ADAU1961) with Line I/O
-  Onboard Class D (FDA802S) Amplifier
-  4 Microphones
-  Onboard RGB LED

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/eval-ad2435j3lz_new.png
   :align: center
   :width: 1080px

.. container:: centeralign

   \ **Figure:** EVAL-AD2435WJ3LZ board Connections


.. _jumper-settings-1:

Jumper settings
^^^^^^^^^^^^^^^

The following jumper settings are required:-

=== ====================================
JP1 No connection
JP2 5-6, 7-8, 17-18, 19-20, 21-22, 23-24
JP3 1-2
JP5 2-3
=== ====================================

EV-21569-SOM Rev B
~~~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` shows :doc:`EV-21569-SOM </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` evaluation board which should be used with EV-SOMCRR-EZKIT. This pair will be used an audio host to the ADZS2435-MINI. It consists of the following peripherals.

-  8 Gb DDR3 (1.35V) Memory
-  512Mb SPI Flash Quad Memory
-  FTDI USB-to-UART

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/21569_som.png
   :align: center
   :width: 500px

.. container:: centeralign

   \ **Figure:** EV-21569-SOM Rev B (Top view)


EV-SC594-SOM Rev B
~~~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` shows :doc:`EV-SC594-SOM </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` evaluation board which should be used with EV-SOMCRR-EZKIT. This pair will be used an audio host to the ADZS2435-MINI. It consists of the following peripherals.

-  8 Gb DDR3 (800 MHz) Memory
-  512 Mb Quad SPI Flash Memory
-  256 Mb Octal SPI Flash Memory
-  FTDI USB-to-UART

|image1|

.. container:: centeralign

   \ **Figure:** EV-SC594-SOM Rev B (Top view)


EV-SOMCRR-EZKIT Rev A
~~~~~~~~~~~~~~~~~~~~~

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` shows the :doc:`EV-SOMCRR-EZKIT </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` which can be used with EV-21569-SOM or EV-SC594-SOM. This board along with a processor SOM board will be used as an audio host to the ADZS2435-MINI. It consists of the following peripherals.

-  ADAU1979 – Quad Analog-to-Digital Converter
-  ADAU1962A – 12 Channel, 192kHz, 24-bit DAC
-  CAN FD 2× ADM3056E
-  Macronix MX66LM1G45G 1 Gbit OSPI Flash Memory
-  Gigabit Ethernet TI DP83867
-  10/100 Ethernet TI DP83848
-  USB 2.0 PHY Microchip USB3340
-  USB 2.0 to QSPI FTDI
-  MicroSD Card Socket
-  2× A2B Interface Connectors

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ezcrr-board.png
   :align: center

.. container:: centeralign

   \ **Figure:** EV-SOMCRR-EZKIT Rev A (Top view)


.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/ev-somcrr-ezkit_ev-21569-som.png
   :align: center

.. container:: centeralign

   \ **Figure:** EV-SOMCRR-EZKIT + EV-21569-SOM


.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/ev-somcrr-ezkit_ev-sc594-som.png
   :align: center

.. container:: centeralign

   \ **Figure:** EV-SOMCRR-EZKIT + EV-SC594-SOM


Connections
-----------

To run the sample demo, the following setup connections are to be made.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_connections.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main connections using PC(Host) and EV-21569-SOM + EV-SOMCRR-EZKIT and ADZS-AD2435 MINI’s


.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_connections_for_audio_stream.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main connections for audio stream from SOM carrier to sub-node line-out using EV-SC594-SOM + EV-SOMCRR-EZKIT (Host) and ADZS-AD2435 MINI’s


.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_connections_for_audio_stream_from_subnode.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main connections for audio stream from subnode PDM mic to subnode line-out using SC594 SOM carrier kit (Host) and ADZS2435MINI’s


.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_connections_for_audio_stream_from_subnode_line-in.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main connections for audio stream from subnode line-in to subnode class-D amplifier-out using SC594 SOM carrier kit (Host) and ADZS2435MINI’s


The steps described in this section are recommended to run the following configurations

-  AD2435 multi-main sample demo using ADSP-21569 platform and PC as host.
-  AD2435 multi-main sample demo using ADSP-SC594 platform as a host

The Evaluation boards shall be connected in the following order.

-  For using both ADSP-21569 platform and PC as a host, connect the EV-21569-SOM to the EV-SOMCRR-EZKIT. For using just ADSP-SC594 platform as a host, connect the EV-SC594-SOM to the EV-SOMCRR-EZKIT
-  Connect one of the two ADZS2435-MINI boards to J10 A2B interface of the EV-SOMCRR-EZKIT. Let this be “main node 0” with I2C address configured to be 0x68.
-  Connect the other ADZS2435-MINI to J11 A2B interface of the EV-SOMCRR-EZKIT. Let this be “main node 1” with I2C address configured to be 0x6A.
-  For A2B chain 0:- ADZS2435-MINI (Main node 0) EVAL-AD2435WJ3LZ (Sub node 0) EVAL-AD2435WJ3LZ (Sub node 1), the connections are as follows

   -  Connect twisted-pair wire between the “B” connector on the main node 0 board and the “A” connector on the sub node 0 board.

      -  Ordered List ItemConnect twisted-pair wire between the “B” connector on the sub node 0 board and the “A” connector on the sub node 1 board.

-  For A2B chain 1:- ADZS2435-MINI (Main node 1) EVAL-AD2435WJ3LZ (Sub node 2) EVAL-AD2435WJ3LZ (Sub node 3), the connections are as follows

   -  Connect twisted-pair wire between the “B” connector on the main node 1 board and the “A” connector on the sub node 2 board.

      -  Connect twisted-pair wire between the “B” connector on the sub node 2 board and the “A” connector on the sub node 3 board.

-  Connect 12V power supplies to the power connectors of EV-SOMCRR-EZKIT and both the ADZS2435-MINI boards.

Audio In/out for ADSP-21569 and PC as a host – multi-main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect an audio source (e.g., output from an iPod) to ‘Audio Line- in’ ports, shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` (Audio Input).
-  Connect separate audio sinks (e.g., passive speakers) to output of Class-D amplifier ports as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`, on sub node boards.
-  Connect separate audio sinks such as headphones to line outs as shown in the :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`.

Audio In/out for ADSP-SC594 as a host – multi-main
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect audio sources (e.g., output from an iPod) to ‘Audio Line- in’ ports, shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` (Audio Input).
-  Connect separate audio sinks (e.g., passive speakers) to output of Class-D amplifier ports as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`, on subnode boards.
-  Connect separate audio sinks such as headphones to line outs as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/hardware-setup/sc594_som.png
   :width: 500px
