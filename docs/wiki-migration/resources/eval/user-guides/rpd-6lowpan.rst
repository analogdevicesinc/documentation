Rapid-6LoWPAN Wireless Networking Protocol Solution
===================================================

Analog Devices offers Rapid RapidNet IP Protocol—a long range sub-GHz wireless networking solution that leverages the market proven ADF7023 radio transceiver and lowest power ULP processors (ADuCM3029 or ADuCM4050). RapidNet IP Protocol uses star-repeater network topology, targeting commercial and industrial applications such as Electronic Shelf Label (ESL), Smart Lock and Structural Health Monitoring (SHM).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/rpd-6lowpan/rapid-6lowpan-network-topology.jpg
   :align: center
   :width: 600px

Features and Specification
--------------------------

-  Efficient low power network

   -   Low power IEEE802.15.4g/e wireless network with time synchronized channel hopping (TSCH)—no collisions and no lengthy receive waits

      -  Lowest power consumption per node with star and extended star network topology configuration.

         -  Reliable end-to-end communications with acknowledgements

-  Long range

   -  Typical range of 500 m (2 hop and confguration setting dependent)

-  Data rate and frequency

   -   High throughput (4 pks/sec at 1 kB per packet)

      -   Fast network join time (for example, 256 motes in 47 sec)
      -   Low latency—minimum of 5 sec network loop cycle
      -   ISM frequency band support (433,868,915,920 MHz)
      -   Multiple data rate support (37.5 kbps to 300 kbps)
      -   On-demand bandwidth allocation (for example, up to 1 MB per node/1 hr)

-  Supported modes:

   -  Master mode (on-chip applications)

      -  Slave mode (application coprocessor)

-  Current consumption:

   -  Active: <10 µA ave. (3 updates of 1 kB packets/day case)

      -  Sleep: <1.5 µA

-  FCC and ARIB STD T108 regulation test feature support integrated
-  Supports OTA (over-the-air) update
-  Reliable scheduling of alert messages from any or all motes
-  Gateway software available for Linux® or ADuCM4050 with various backhaul connectivity options

Evaluation Kit
--------------

Below are the different kits available for evaluating Rapid-6LoWPAN.

-  EV-RAPDID-ESL-900Z - RapidNet IP Evaluation Kit for all the regions except Japan.
-  EV-RAPDID-ESL-900JZ -RapidNet IP Evaluation kit with TELEC Certification specific for Japan.
-  EV-RAPDID-NODE-900Z- Electronic Shelf Labelling node which should be ordered only if more nodes are required during the evaluation of EV-RAPID-ESL-900Z.

Below are the kit contents.

-  EV-RAPDID-ESL-900Z / EV-RAPDID-ESL-900jZ

   -  :doc:`EV-COG-AD3029LZ </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>` - development platform for Analog Devices Ultra Low Power Microcontroller :adi:`ADuCM3029`
   -  :doc:`EV-DNG-RFMOD-9001Z </wiki-migration/resources/eval/user-guides/ev-dng-rfmod-9001z>` - USB Dongle which acts as Border Router for RapidNet IP Network **(902-958MHz)**
   -  :doc:`EV-COG-ADF7023-9Z </wiki-migration/resources/eval/user-guides/ev-cog-adf7023-9z>` - :adi:`ADF7023-J` Connectivity Cog **(902-958MHz)**
   -  :doc:`EV-GEAR-EINK1Z </wiki-migration/resources/eval/user-guides/ev-gear-eink1z>` - Cog Ecosystem Gear with E-Paper Display from E-INK.

-  EV-RAPDID-NODE-900Z

   -  :doc:`EV-COG-AD3029LZ </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>` - development platform for Analog Devices Ultra Low Power Microcontroller :adi:`ADuCM3029`
   -  :doc:`EV-COG-ADF7023-9Z </wiki-migration/resources/eval/user-guides/ev-cog-adf7023-9z>` - :adi:`ADF7023-J` Connectivity Cog **(902-958MHz)**
   -  :doc:`EV-GEAR-EINK1Z </wiki-migration/resources/eval/user-guides/ev-gear-eink1z>` - Cog Ecosystem Gear with E-Paper Display from E-INK.
