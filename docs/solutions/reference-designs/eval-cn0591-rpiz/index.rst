.. _eval-cn0591-rpiz:

EVAL-CN0591-RPIZ
================

2-port 10BASE-T1L Field Switch with SPoE PSE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

General Description
-------------------

.. figure:: eval-cn0591-rpiz-top-iso.png
   :width: 400 px
   :align: right

   EVAL-CN0591-RPIZ Board

The :adi:`EVAL-CN0591-RPIZ <CN0591>` is a 10BASE-T1L MAC/PHY interface with Single 
Pair Power over Ethernet (SPoE), designed for developing field devices and applications 
on the Raspberry Pi platform. It functions as Power Sourcing Equipment (PSE), 
capable of delivering power to other devices over a 10BASE-T1L network.

The board can be powered via USB-C (*M1*, up to 20V) or through a Pluggable Terminal 
Block (*P21*, up to 60V). A synchronous step-down DC-DC converter supplies a 
regulated 5V to the Raspberry Pi.

The system supports SPoE Class 10–12 (nominal 24V) and Class 13–14 (nominal 55V), 
enabling flexible power configurations for various industrial and embedded applications.

Designed for use on the Raspberry Pi platform, the CN0591 hardware features a 
40-pin GPIO header and uses an extended version of the standard HAT.

Evaluation Board Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: eval-cn0591-rpiz-top-with-labels.png

   EVAL-CN0591-RPIZ Primary Side

10BASE-T1L Ports (P1 and P2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: eval-cn0591-10base-t1l-port.png
   :width: 350 px

   10BASE-T1L Ports

The :adi:`EVAL-CN0591-RPIZ <CN0591>` evaluation board features two 10BASE-T1L ports, 
allowing connection to up to two PDs. Each port supports independent control of 
power sourcing and data transmission.

*P1* and  *P2* are 3-pin terminal blocks designed for twisted pair cables, with optional shielding. 
These ports deliver class-dependent DC voltage to connected PDs and transmit AC-coupled 
data signals for 10BASE-T1L communication. Both ports include protection against overvoltage 
and electrostatic discharge (ESD) events.

When the board is powered via USB-C, the default output voltage is 24V, generated 
by the :adi:`LT3757A` flyback boost converter, suitable for SPoE Classes 10–12. To enable 
SPoE Classes 13–14, which require 54V, switch *S3* to activate the higher voltage output.

.. figure:: eval-cn0591-s3-switch.png
   :width: 350 px

   SPoE Voltage Switch

The USB-C uses the :adi:`MAX77958 <MAX77958>` standalone USB Power Delivery 
(PD) controller, which can be programmed using the **P49** header. 
When power is supplied via the terminal block **P21**, the voltage can be set
to 24V or 55V using the customers power supply.
The supply port can be selected via the **S2** switch.

In either of the cases, to power the Raspberry Pi, 5V is generated using the 
:adi:`MAX17573`.

ADIN2111 
^^^^^^^^^

The onboard :adi:`ADIN2111` PHY provides the 10BASE-T1L connection to the host 
platform board. The :adi:`ADIN2111` is connected to the Raspberry Pi using the 
SPI0 port of the Raspberry Pi.

The :adi:`ADIN2111` features selectable peak-to-peak transmit voltage levels of either 1.1V or 2.4V. 
These levels can be configured by adjusting the P6 and P4 solder jumpers for PHY1 and PHY2, respectively:

- Disconnected: 2.4V
- Shorted: 1.1V

The generic SPI protocol is half duplex. Therefore, it is not possible
to write frame data into the MAC_TX register and read from the
MAC_RX register at the same time. To achieve full duplex transmission on 
Ethernet at 10 Mbps, OPEN Alliance SPI must be used.
To select which SPI protocol to use, the **JP1** (located on the bottom of the 
board) solder jumper should be configured as follows:

.. csv-table::
   :file: ADIN2111_SPI_Selection.csv

The :adi:`ADIN2111` supports software power-down functionality for each port 
independently after power-up or reset. To enable this feature:
- For PHY1, short the P8 jumper.
- For PHY2, configure the JP2 solder jumper as follows:

.. csv-table::
   :file: ADIN2111_Power_Down_Selection.csv

LTC4296
^^^^^^^

The :adi:`LTC4296<LTC4296-1>` is a five port, single-pair power over Ethernet 
(SPoE), power sourcing equipment (PSE) controller. The LTC4296-1 is designed 
for interoperability with powered devices (PDs) in 24 V or 54 V systems.
PD classification via the serial communication classification protocol (SCCP) 
and maintain full voltage signature (MFVS) ensure full operating voltage is 
only applied to the cable when a PD is present. PD initiated sleep and wake-up 
are supported.
Telemetry, status, and software control features are accessed via SPI bus 
interface with packet error code (PEC) protection.

The LTC4296 is directly powered from the :adi:`LT3757A <LT3757>` flyback boost 
converter or from the 24V or 55V power supply connected to the **P21** terminal 
block.

The device by default is configured to operate in SPoE Class 12 (24V nominal) or
SPoE Class 14 (54V nominal) mode. In order to use classes 11 and 13, the 
following solder jumper configurations are required:

.. figure:: eval-cn0591-spoe-classes.png
   :width: 475 px

   SPoE PD Power Class Jumpers

.. csv-table:: SPoE PSE High Side Circuit Breaker Resistor Selection Table
   :file: SPoE_PSE_Power_Class_Selection_High_Side.csv
   
.. csv-table:: SPoE PSE Low Side Sensing Resistor Selection Table
   :file: SPoE_PSE_Power_Class_Selection_Low_Side.csv

The :adi:`LTC4296` also supports SPoE Class 10. To enable this functionality, 
specific resistor changes are required:

High-side circuit breaker resistors:

- For PORT1, replace R15 or R16 with 1.6Ω, 1/10W resistors.
- For PORT2, replace R49 or R50 with 1.6Ω, 1/10W resistors.

Low-side sensing resistors:

- For PORT1, replace R19 or R20 with 0.4Ω, 1/10W resistors.
- For PORT2, replace R53 or R54 with 0.4Ω, 1/10W resistors.

The complete power requirements for the SPoE classes are shown in the table below:

.. csv-table:: SPoE PSE Power Class Requirements
   :file: SPoE_PSE_Power_Class_Requirements.csv
   
Secondary Side
~~~~~~~~~~~~~~

.. figure:: eval-cn0591-rpiz-bottom-with-labels.png

   EVAL-CN0591-RPIZ Secondary Side

The secondary side of the :adi:`EVAL-CN0591-RPIZ <CN0591>` evaluation board
features a Raspberry Pi compatible 40-pin GPIO header, which is used to
connect the board to the Raspberry Pi and the serial communication and 
classification protocol (SCCP) drivers. 
The USB-C uses a standalone USB Power Delivery (PD) controller, can be 
configured using the following jumper configurations:

.. csv-table:: USB-C Power Delivery Controller Configuration
   :file: USB_PD_Controller_Configuration.csv

.. warning:: 

   Although the PD supports 5V input, we do not recommend using it because the :adi:`MAX17573` 
   requires a voltage higher than 5V to reliably generate a stable 5V output for the Raspberry Pi.

.. attention::

   Using a 9V power source is not recommended for Class 14 operation without external active cooling. 
   The boost converter generates significant heat at this voltage, which could potentially damage the 
   Raspberry Pi or the :adi:`EVAL-CN0591-RPIZ <CN0591>` evaluation board.

.. important::

   A power supply of at least 15V is recommended to help mitigate excess heat and prevent potential damage to the system.

System Setup
------------

**Required Equipment**

**Hardware**

- :adi:`EVAL-CN0591-RPIZ <CN0591>` Circuit Evaluation Board
- Raspberry Pi Model 3B (or higher)
- Micro-SD Card for Raspberry Pi
- 10BASE-T1L media converter, either:

  - :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` Product Evaluation Board
  - :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` USB2.0 to 10BASE-T1L Interface Board 
  - Other 10BASE-T to 10BASE-T1L media converter


- Power Source Options:
   - USB-C Input: Powered via a DC power supply using a USB-C connector.
   - External DC Supply: Any external DC power source with an output of either 24V or 55V.

- Host Windows, Linux, or Mac computer

**Software**

- :ref:`kuiper`

**Documentation**

- :adi:`CN0591` Circuit Note

Block Diagram
~~~~~~~~~~~~~

Setup with DC Power Supply with USB-C or other DC Power Supply
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure::
   eval-cn0591-rpiz-block-diagram.png

   EVAL-CN0591-RPIZ Block Diagram

Software Setup
~~~~~~~~~~~~~~

Downloading and Flashing the Micro-SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the :adi:`EVAL-CN0591-RPIZ <CN0591>` with the Raspberry Pi, the
micro-SD card should be preloaded with :ref:`kuiper`, a distribution based on 
Raspbian from the Raspberry Pi Foundation that incorporates Linux drivers for 
ADI products as well as tools and other software products.

Complete instructions, including where to download the SD card image, how to
write it to the micro-SD card, and how to configure the system are provided at
:ref:`kuiper`.

Configuring the Micro-SD Card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Linux kernel requires a matching device tree overlay to identify the
devices on the CN0591. The overlay table is included with the :ref:`kuiper`
and simply needs to be enabled.

To do this, follow the Hardware Configuration procedure under **Configuring
the SD Card for Raspberry Pi Projects** in the :ref:`kuiper` page.
Enable the CN0591 overlay by adding the following line to *config.txt*
for class 12:

::

   dtoverlay=rpi-cn0591-class12

or for class 14:

::

   dtoverlay=rpi-cn0591-class14

Save the changes and reboot the system by entering the following command in the console:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   $sudo reboot

Setting up a static IP
^^^^^^^^^^^^^^^^^^^^^^

To set up a static IP address for the CN0591, the user has to modify the IPv4
address of the chosen network interface.
This can be done by right-clicking in the top right corner the network icon
and selecting Wireless & Wired Network Settings.

.. figure:: eval-cn-0591-rpiz-static-ip-location.png
   :width: 400 px

   Network Settings Location

Next to the **interface** field select the wanted interface (e.g. **eth1 / 
eth2**) and type in the chosen IP address as shown below:

.. figure:: eval-cn-0591-rpiz-static-ip-set-ip.png
   :width: 400 px

   Static IP Address Configuration

The next set is to reset the ip link, which can be done by entering the
following command in a terminal:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   $sudo ip link set eth0 down

.. figure:: eval-cn-0591-rpiz-static-ip-set-eth0-down.png
   :width: 400 px

   Setting eth0 down

Next, set the interface up again by entering the following command:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   $sudo ip link set eth0 up

.. figure:: eval-cn-0591-rpiz-static-ip-set-eth0-up.png
   :width: 400 px

   Setting eth0 up

If everything was done correctly the interface should be up and running with the
static IP address set. To verify this, enter the following command in the
console, the next to the **inet** field the static IP address should be shown:

.. shell::
   :user: analog
   :group: analog
   :show-user:

   $ip a

.. figure:: eval-cn-0591-rpiz-static-ip-result.png
   :width: 400 px

   Static IP Address Result

Basic Operation
~~~~~~~~~~~~~~~

.. figure:: eval-cn0591-setup.png

   Complete Evaluation Setup

To establish a 10BASE-T1L connection to a Raspberry Pi using the
:adi:`EVAL-CN0591-RPIZ <CN0591>` evaluation board and ping the Raspberry Pi 
follow the below procedure:

#. Ensure that the jumpers and switches of the :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` are configured to the default settings.

#. Insert the micro-SD card into its slot on the Raspberry Pi.

#. Connect the :adi:`EVAL-CN0591-RPIZ <CN0591>` circuit evaluation board to the Raspberry Pi GPIO header.

#. Using a twisted-pair cable, connect **P2** on the
   :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` USB2.0 to 10BASE-T1L Interface
   to the **P2** terminal block on the :adi:`EVAL-CN0591-RPIZ <CN0591>`

#. Using a USB-C cable, connect **P1** on the
   :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` evaluation board to a USB port on
   the computer.

#. *Operation with USB-C DC Power Supply: (Skip to step 7 if using a the P21 terminal block)*

   * Set the **S3** switch to supply to either 24V (Class 12) or
     55V (Class 14), depending on the overlay added to the *config.txt*.
   * Set the **S2** switch towards the **USB-C**.

#. *Operation with external DC Power Supply (Using the P21 terminal block):*

   * Using wires, connect the **P21** terminal block on the :adi:`EVAL-CN0591-RPIZ <CN0591>`
   * Set the **S2** switch towards the **Terminal Block**. 

#. Wait for the **DS1** LED on the :adi:`EVAL-CN0591-RPIZ <CN0591>` circuit
   evaluation board and the **DS1**, **DS2** LEDs on the 
   :adi:`EVAL-ADIN1100EBZ <EVAL-ADIN1100>` evaluation board to turn on and
   start blinking at the same time. This indicates that a 10BASE-T1L link has 
   been established.

#. On the host PC, change the IP address of the AD-T1LUSB2.0-EBZ:

   * From the start menu open the **Control Panel** and click on **Network and Internet**
  
   * Click on **View network status and tasks**
      You should see two networks.

      .. figure:: ad-t1lusb2-network.png
         :width: 400 px

         Network Connections
   * Click on the **Connections: Ethernet** and click on **Properties**
   * Select **Internet Protocol Version 4 (TCP/IPv4)** and click on 
     **Properties**
   * Select **Use the following IP address:** and type in the following **IP 
     address** and **Subnet mask**:
     ::

         IP address: 192.168.90.zzz
         Subnet mask: 255.255.0.0

     where **zzz** is a number between 1 and 254, currently unused in the network (for example, 10 cannot be used, since it is used by the CN0591).
   * Click on **OK** to save the changes and close the dialog boxes.

#. Open up a terminal and ping the CN0591:
   ::

      ping 192.168.90.10 

   .. figure:: ping-result.png
      :width: 400 px

      Result

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

  :download:`EVAL-CN0591-RPIZ Design & Integration Files <CN0591-DesignSupport.zip>`

  - Schematics
  - PCB Layout
  - Bill of Materials
  - Allegro Project

Additional Information and Useful Links
---------------------------------------

- :adi:`CN0591 Design Support Package <CN0591-DesignSupport>`
- :adi:`CN0591 Circuit Note Page <CN0591>`
- :adi:`ADIN2111 Product Page <ADIN2111>`
- :adi:`MAX17573 Product Page <MAX17573>`
- :adi:`MAX77958 Product Page <MAX77958>`
- :adi:`LTC4296 Product Page <LTC4296-1>`
- :adi:`LT3757A Product Page <LT3757>`
- :dokuwiki:`ADIN2111 Linux Driver <resources/tools-software/linux-drivers/net-mac-phy/adin2111>`

Hardware Registration
---------------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you :adi:`register <EVAL-CN0591-RPIZ?&v=RevC>` your hardware.

Help and Support
-------------------

For questions and more information about this product, connect with us through the Analog Devices :ez:`/` .
