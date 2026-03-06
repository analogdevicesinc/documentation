.. _eval-cn0506-fmcz:

EVAL-CN0506-FMCZ Hardware User Guide
===============================================================================

The :adi:`cn0506` shown in Figure 1 is a dual channel, low latency, low power 
Ethernet PHY card supporting speeds of 10/100/1000 Mbps for Industrial Ethernet 
applications.

The circuit consists of two individual, independent 10/100/1000 Mb PHYs, each 
with an energy efficient Ethernet (EEE) physical layer device (PHY) core with 
all associated common analog circuitry, input and output clock buffering, 
management interface, subsystem registers, MAC interface, and control logic.

Connectors and Jumper Configurations
-------------------------------------------------------------------------------

.. image:: images/image_1.png
   :align: center
   :width: 500

FMC Connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FMC connector connects to the LPC connector of the carrier board.

RJ45 Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The RJ45 connectors M1 for Channel A and M2 for Channel B have built-in 
magnetics that help reduce the size of the board. Each is dedicated to a PHY 
interface (ADIN1300), allowing each channel to operate independently.

Configuration Resistors
-------------------------------------------------------------------------------

MAC Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pins for selecting the MAC interface are shared with the 
RX_CTL/RX_DV/CRS_DV pin and RXC/RX_CLK pin, which have weak internal pull-down 
resistors and are configured to RGMII mode with 2ns delay by default. The 
ADIN1300 MAC interface selection can be done via software but can also be 
hardware configured upon device power-up using the table below.

.. list-table:: MAC Interface Selection
   :widths: 40 30 30
   :header-rows: 1

   * - MAC Interface Selection
     - MACIF_SEL1 (Phy A / Phy B)
     - MACIF_SEL0 (Phy A / Phy B)
   * - RGMII RXC/TXC 2 ns delay
     - R12 / R78
     - R9 / R75
   * - RGMII RXC/TXC 2 ns delay
     - R11 / R77
     - R9 / R75
   * - MII
     - R17 / R78
     - R8 / R74
   * - RMII
     - R11 / R77
     - R8 / R74

Configuration Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These configuration modes are used to set Auto-MDIX and PHY speed 
configurations for both PHY channels A and B.

.. list-table:: Configuration Modes
   :widths: 30 35 35
   :header-rows: 1

   * - Mode
     - R_LO
     - R_HI
   * - MODE_1
     - 10k
     - Open
   * - MODE_2
     - 10k
     - 56k
   * - MODE_3
     - 56k
     - 10k
   * - MODE_4
     - Open
     - 10k

PHY Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both channels are configured upon power-up for:
- 10 Mbps Half/Full Duplex
- 100 Mbps Half/Full Duplex
- 1000 Mbps Full Duplex (Slave mode)

Auto-MDIX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Auto-MDIX Configuration
   :widths: 70 30
   :header-rows: 1

   * - Configuration
     - MDIX_MODE
   * - Manual MDI
     - MODE_1
   * - Manual MDIX
     - MODE_2
   * - Auto MDIX – Prefer MDIX
     - MODE_3
   * - Auto MDIX – Prefer MDI
     - MODE_4

LED Indicators
-------------------------------------------------------------------------------

These LEDs indicate when a link is established and blink when there is activity.

- PHY Channel A LED: **DS4**
- PHY Channel B LED: **DS2**

.. image:: images/cn0506-silkscreen.jpg
   :align: center
   :width: 500

Schematic, PCB Layout, Bill of Materials
-------------------------------------------------------------------------------

Download Design & Integration Files:

:adi:`EVAL-CN0506-FMCZ Design & Integration Files <https://www.analog.com/cn0506-designsupport>`

- Schematics  
- Gerber Files  
- Bill of Materials  
- Allegro Layout Files  
- Assembly Files  

Additional Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`ADIN1300 Product Page <https://www.analog.com/ADIN1300>`

Quick Start Guides
-------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 1

   quickstart/index

HDL Reference Design
-------------------------------------------------------------------------------

- :external+hdl:ref:`cn0506`

Linux
-------------------------------------------------------------------------------

- :dokuwiki:`Linux driver </resources/tools-software/linux-drivers/net-phy/adin>`

Registration
-------------------------------------------------------------------------------

.. tip::

   Receive software update notifications, documentation updates, view the 
   latest videos, and more when you register your hardware. 
   `Register <https://my.analog.com/en/app/registration/hardware/EVAL-CN0506-FMCZ?&v=RevB>`__ 
   to receive all these great benefits and more!