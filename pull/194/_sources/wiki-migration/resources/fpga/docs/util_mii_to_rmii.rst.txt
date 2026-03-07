UTIL_MII_TO_RMII
================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/util_mii_to_rmii/index.html\


The :git-hdl:`library/util_mii_to_rmii` IP core is designed to interface the Zynq-7000/Zynq UltraScale+ MPSoC - PS Gigabit Ethernet MAC and Reduced Media Independent Interface (RMII) :adi:`ADIN1300` PHY from the :adi:`CN0506` Dual PHY Ethernet evaluation board.

Features
--------

-  configurable interface for the MAC block (Media Independent Interface - MII or Gigabit Media Independent Interface - GMII)
-  configurable data rate for the MAC block and PHY chip

Files
-----

+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Name                                                                                                                     | Description                                                                                    |
+==========================================================================================================================+================================================================================================+
| :git-hdl:`library/util_mii_to_rmii/mac_phy_link.v`                                                                       | Verilog source for the conversion between MII MAC block interface and RMII PHY chip interface. |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| :git-hdl:`library/util_mii_to_rmii/phy_mac_link.v`                                                                       | Verilog source for the conversion between RMII PHY chip interface and MII MAC block interface. |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| :git-hdl:`library/util_mii_to_rmii/util_mii_to_rmii.v`                                                                   | Verilog source for the main module made of the MII and RMII interfaces.                        |
+--------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/util_mii_to_rmii.drawio_3_.svg
   :alt: util_mii_to_rmii
   :align: center

Configuration Parameters
------------------------

+-----------------+----------------------------------------------------+---------+
| Name            | Description                                        | Default |
+=================+====================================================+=========+
| ``INTF_CFG``    | MAC Block Interface Selection (0 = GMII, 1 = MII). | 0       |
+-----------------+----------------------------------------------------+---------+
| ``RATE_10_100`` | Data Rate Selection (0 = 100 Mbps, 1 = 10 Mbps).   | 0       |
+-----------------+----------------------------------------------------+---------+

Interfaces
----------

+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
| Interface                                    | Pin                                      | Type               | Description                                            |
+==============================================+==========================================+====================+========================================================+
| ``MAC-PHY Link (MII MAC Block to RMII PHY)`` | \*\* MII to RMII conversion signals \*\* |                    |                                                        |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mac_txd ''                            | '' input [3:0] ''  | MII Transmit Data                                      |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mac_tx_en ''                          | '' input ''        | MII Transmit Enable                                    |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mac_tx_er ''                          | '' input ''        | MII Transmit Error                                     |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_tx_clk ''                         | '' output ''       | MII Transmit Clock                                     |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' rmii_txd ''                           | '' output [1:0] '' | RMII (PHY) Transmit Data                               |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' rmii_tx_en ''                         | '' output ''       | RMII (PHY) Transmit Enable                             |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
| ``PHY-MAC Link (RMII PHY to MII MAC Block)`` | \*\* RMII to MII conversion signals \*\* |                    |                                                        |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_col ''                            | '' output ''       | MII Collision Detect signal (only in half-duplex mode) |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_crs ''                            | '' output ''       | MII Carrier Sense signal (only in half-duplex mode)    |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_rxd ''                            | '' input [3:0] ''  | MII Receive Data                                       |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_rx_clk ''                         | '' input ''        | MII Receive Clock                                      |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_rx_dv ''                          | '' input ''        | MII Receive Data Valid                                 |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' mii_rx_er ''                          | '' input ''        | MII Receive Error                                      |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' phy_crs_dv ''                         | '' output ''       | PHY (RMII) Carrier Sense/Data Valid                    |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' phy_rxd ''                            | '' output[1:0] ''  | PHY (RMII) Receive Data                                |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' phy_rx_er ''                          | '' output ''       | PHY (RMII) Receive Error                               |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
| ``External``                                 | \*\* \*\*                                |                    |                                                        |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' ref_clk ''                            | '' input ''        | Reference Clock for MII to RMII IP core                |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+
|                                              | '' reset_n ''                            | '' input ''        | Active-Low reset for MII to RMII IP core               |
+----------------------------------------------+------------------------------------------+--------------------+--------------------------------------------------------+

Register Map
------------

There is no register map defined for this IP core.

Theory of operation
-------------------

The following timing diagrams illustrate different signal protocols for MII and RMII interfaces at data rates of 100 and 10 Mbps.

Receive Transactions
~~~~~~~~~~~~~~~~~~~~

-  RMII (PHY) receive transaction at 100 Mbps with no errors and phy_crs_dv asserted until the final packet dibit. According to the RMII Specification Rev. 1.2, after the assertion of phy_crs_dv, several 00's dibits can precede the preamble 01's dibits. The preamble is composed of 28 "01" dibits and the start of frame delimiter of 3 "01" dibits and one "11" dibit followed by the frame containing 64-1522 bytes:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/phy_rec_simple.svg
   :alt: PHY Receive Simple
   :align: center

-  RMII (PHY) receive transaction at 100 Mbps with no errors and phy_crs_dv toggling at 25 MHz starting on a nibble boundary and indicates the PHY has lost the carrier but has accumulated nibbles to transfer:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/d2_phy_rec_tog.svg
   :alt: PHY Receive Toggle
   :align: center

-  At a data rate of 10 Mbps (ref_clk frequency divided by 10), mii_rxd will be sampled every :math:`10^th` cycle.
-  MII receive transaction converted from RMII (PHY) receive transaction at 100 Mbps. In the MII mode mii_rx_dv and mii_rxd will be sampled on the falling edge of the 25 MHz mii_rx_clk and when mii_rx_dv is de-asserted, mii_rxd will present 0b0000 to the Ethernet MAC:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/mii_recv.svg
   :alt: ETH MAC Receive
   :align: center

Transmit Transactions
~~~~~~~~~~~~~~~~~~~~~

-  MII transmit transaction at 100 Mbps. In the MII mode mii_tx_en and mii_txd will be sampled on the rising edge of the 25 MHz mii_tx_clk:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/mii_transm.svg
   :alt: ETH MAC Transmit
   :align: center

-  In case of errors detection, mii_tx_er will be asserted and mii_txd dibits will be "01" for the rest of transmission to RMII interface.
-  At a data rate of 10 Mbps (ref_clk frequency divided by 10), mii_txd will be sampled every :math:`10^th` cycle.
-  RMII transmit transaction converted from MII transmit transaction at 100 Mbps. In the RMII mode rmii_tx_en and rmii_txd will be sampled on the rising edge of the 50 MHz ref_clk:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/rmii_transm.svg
   :alt: PHY Transmit
   :align: center

Software Support
----------------

Analog Devices recommends to use the provided software drivers.

-  :doc:`Analog Devices ADIN1300/ADIN1200 PHY Linux Driver </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin>`

References
----------

-  :git-hdl:`util_mii_to_rmii IP source code <library/util_mii_to_rmii>`
   \* :adi:`ADIN1300 PHY Information <adin1300>`
   \* :adi:`ADIN1300 PHY Documentation <media/en/technical-documentation/data-sheets/ADIN1300.pdf>`
   \* :doc:`ADIN1300 PHY Linux Driver </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin>`
-  :adi:`CN0506 Information <en/design-center/reference-designs/circuits-from-the-lab/cn0506.html>`
   \* :adi:`CN0506 Reference Note <media/en/reference-design-documentation/reference-designs/cn0506.pdf>`
   \* :doc:`CN0506 HDL Reference Design </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0506/hdl>`
   \* :doc:`CN0506 User Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0506>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
