.. _ad-apardpfwd-sl:

AD-APARDPFWD-SL
================

2-port 10BASE-T1L Arduino Shield with SPoE Power Forwarding
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

General Description
-------------------

.. figure:: apard-pfwd-top-iso.png
   :width: 475 px
   :align: right

   AD-APARDPFWD-SL

The :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` is a 10BASE-T1L power forwarder 
with Single Pair Power over Ethernet (SPoE) for development of field devices and
applications on a :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform board. 
The SPoE powered device (PD) and isolated flyback regulator provide 12 V 
power to the platform board. SPoE Class 10-12 (24 V nominal) and 
Class 13-14 (55 V nominal) are supported.

Designed for use on the :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform, 
the :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` hardware features Arduino Mega
Form-factor headers, and two 10BASE-T1L ports for connecting to a
10BASE-T1L Power Sourcing Equipment (PSE) such as the 
:adi:`EVAL-CN0591-RPIZ <CN0591>` 2-port 10BASE-T1L w/SPoE PSE Development
Platform.

To allow board stacking and development of field device applications using
Arduino shields, the :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` has extra tall 
headers that allows other Arduino shields to be stacked on top of it. 

The design also features a complete power and data isolation to the host 
:adi:`AD-APARD32690-SL <AD-APARD32690-SL>`.

Evaluation Board Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: apard-pfwd-top-with-labels.png

   AD-APARDPFWD-SL Primary Side

The :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` uses 2 10BASE-T1L ports. One port 
is the input port (**P7**), which supplies power to the 
:adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform board, and the other port 
is the output port (**P8**), which can be used to connect to another 10BASE-T1L 
device or to daisy chain multiple devices. The input port is connected to the 
:adi:`LTC9111` SPoE PD controller, which extracts the SPoE power from the 
10BASE-T1L cable and provides it to the :adi:`LT8304` isolated flyback 
regulator. The :adi:`LT8304` provides a regulated 12V.

Power is supplied to the :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform 
board via **PIN8** of the **P1** header.

The onboard :adi:`ADIN2111` PHY provides the 10BASE-T1L connection to the host 
platform board. The :adi:`ADIN2111` is connected to the :adi:`AD-APARD32690-SL 
<AD-APARD32690-SL>` platform board via the **P5** and uses the SPI4 port of the 
:adi:`AD-APARD32690-SL <AD-APARD32690-SL>`.

The :adi:`ADIN2111` supports selectable peak-to-peak transmit levels of 1.1V or 2.4V for each PHY. To select the desired level, configure the P9 and P10 solder jumpers for PHY1 and PHY2, respectively:

- Disconnected: Sets the transmit level to 2.4V
- Shorted: Sets the transmit level to 1.1V

The generic SPI protocol is half duplex. Therefore, it is not possible
to write frame data into the MAC_TX register and read from the
MAC_RX register at the same time. To achieve full duplex transmission on 
Ethernet at 10 Mbps, OPEN Alliance SPI must be used.
To select which SPI protocol to use, the **JP3** solder jumper should be
configured as follows:

.. csv-table::
   :file: ADIN2111_SPI_Selection.csv

The :adi:`ADIN2111` supports software power-down after power-up / reset for each
port independently. To utilize this feature:

- Short jumper P11 to enable the software power-down for PHY1.
- In order to enable the software power-down for PHY2, configure JP4 solder jumper with the following settings
  
.. csv-table::
   :file: ADIN2111_Power_Down_Selection.csv

Secondary Side
~~~~~~~~~~~~~~

.. figure:: apard-pfwd-bottom-with-labels.png

   AD-APARDPFWD-SL Secondary Side

SPoE PD Power Class Selection (JP1 and JP2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the :adi:`LTC9111` SPoE PD
controller included in the :adi:`AD-APARDPFWD-SL` circuit is configured for
PD Class 12. If a different PD class is required for the application, the
**JP1** and **JP2** solder jumpers should be reconfigured to match the desired
class.

.. figure:: apard-pfwd-classes.png
   :width: 475 px

   SPoE PD Power Class Jumpers

.. csv-table::
    :file: SPoE_PD_Power_Class_Selection.csv

.. warning::

   Do not use PD Classes 15!

   The :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` evaluation board is not 
   designed to handle the class 15's power specifications.

System Setup
------------

**Required Equipment**

**Hardware**

- :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` Circuit Evaluation Board
- :adi:`AD-APARD32690-SL <AD-APARD32690-SL>`
- 10BASE-T1L media converter, either:

  - :adi:`EVAL-ADIN1100EBZ <eval-adin1100>` Product Evaluation Board
  - :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` USB2.0 to 10BASE-T1L Interface Board 
  - Other 10BASE-T to 10BASE-T1L media converterBoard 
  
- Other 10BASE-T to 10BASE-T1L media converter

- Power Source, either:
  
  - :adi:`EVAL-CN0591-RPIZ <CN0591>` 2-port 10BASE-T1L w/SPoE PSE Development Platform
  
    - Raspberry Pi Model 3B (or higher)
    - Micro-SD Card for Raspberry Pi
  
  - Other 10BASE-T1L Power Coupling Network Board w/ SPoE PSE 

- :adi:`MAX32625PICO <MAX32625PICO>` or any other similar programmer supporting 
  the SWD interface

Block Diagram
~~~~~~~~~~~~~

Setup with SPoE via PSE 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-CN0591-RPIZ <CN0591>` 2-port 10BASE-T1L w/SPoE PSE Development 
Platform provides a complete solution for powering the 
:adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` evaluation board and the 
:adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform board via SPoE.

.. figure:: apard-pfwd-block-diagram.png

   Test Setup with SPoE via PSE

Basic Operation
~~~~~~~~~~~~~~~

.. figure:: apard-pfwd-setup.png

   Complete Evaluation Setup

To establish a 10BASE-T1L connection to an 
:adi:`AD-APARD32690-SL <AD-APARD32690-SL>` using the
:adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` evaluation board 
and ping the :adi:`AD-APARD32690-SL <AD-APARD32690-SL>`:

#. Ensure that the jumpers and switches of the :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` are configured to the default settings.

#. Connect the :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` circuit evaluation board to the 
   :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` Arduino headers.

#. Using a USB-C cable, connect **P1** on the
   :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` evaluation board to a USB port on
   the computer.

#. Operation with SPoE PSE:

   * Set the output of the PSE or DC power supply to either 24V (Class 12) or
     55V (Class 14), depending on the settings of **JP1** and **JP2** on the AD-APARDPFWD-SL board.
   * Using a PROFIBUS cable, connect **P1** on the CN0591 evaluation board to **P7** on the :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` evaluation board.
   * Using a PROFIBUS cable, connect **P2** on the CN0591 evaluation board to **P2** on the :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` evaluation board.

#. Upload the :git-no-OS:`AD-APARD32690-SL ADIN2111 Example <projects/ASWPF/src/examples/adin2111_example/>`
   to the :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform board using the :adi:`MAX32625PICO <MAX32625PICO>` programmer.
   
#. By default the :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` has 192.168.97.40 as its IP address.
   If you are using a different IP address, make sure to update the
   :git-no-OS:`AD-APARD32690-SL ADIN2111 Example <projects/ASWPF/src/examples/adin2111_example/>`
   with the new IP address.

#. Update the IP address of the Raspberry Pi's Ethernet Interface depending on which port of the
   :adi:`EVAL-CN0591-RPIZ <CN0591>` you are using (**ETH1** / **ETH2**).

   .. warning::
        
        ADD STATIC IP FOR BOTH PORTS
        ETH1 192.168.97.10
        ETH2 192.168.90.10
   
   Save the table and reboot the system by entering the following command in the console:
   
   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $sudo reboot

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

#. Wait for the **DS1** LED on the :adi:`AD-APARDPFWD-SL <AD-APARDPFWD-SL>` evaluation board
   and the **DS1** LED on the :adi:`EVAL-CN0591-RPIZ <CN0591>`
   evaluation board to turn on and start blinking at the same time.
   This indicates that a 10BASE-T1L link has been established.

#. Now you can ping the device to see if the connection is working properly.
   Open a terminal on your host PC connect to the CN0591 through SSH:
 
   ::

      ssh analog@192.168.90.10
   
   Enter the password **analog** when prompted.

   You can now ping the :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` platform board using the following command:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ping 192.168.97.50

   .. figure:: 
      apard-pfwd-result.png

      Result

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

  :download:`AD-APARDPFWD-SL Design & Integration Files<AD-APARDPFWD-SL-DesignSupport.zip>`

  - Schematics
  - PCB Layout
  - Bill of Materials
  - Allegro Project

Additional Information and Useful Links
---------------------------------------
- :adi:`ADIN2111 Product Page <ADIN2111>`
- :adi:`LTC9111 Product Page <LTC9111>`
- :adi:`LT8304 Product Page <LT8304>`

Hardware Registration
---------------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you :adi:`register <AD-APARDPFWD-SL?&v=RevB>` your hardware.

Help and Support
-------------------

For questions and more information about this product, connect with us through the Analog Devices :ez:`/` .
