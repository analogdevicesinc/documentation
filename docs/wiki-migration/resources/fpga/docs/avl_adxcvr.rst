Avalon Transceiver Core
=======================

The Avalon ADI Transceiver (avl_adxcvr) core is implements a JESD link between an Altera (Intel) device and the converter device. It instantiates the Altera transceivers and the JESD core. This core is a 'direct-hdl-inference' core. That is, it does NOT have any HDL files. The core infers the Altera IP cores and generates a top level wrapper file on the fly. This method is necessary for some of the Altera IP cores that do not support direct HDL inference (some actually do, but you may end up with a lot of mess). The core also support 'transceiver sharing' by which you may instantiate multiple links (separate pairs) but merge them together (joined pairs). The core also allows transceiver sharing across asymmetrical and multiple links across the receive and transmit pairs.

Features
--------

-  Supports Altera (Arria 10 and above) devices
-  Supports transceiver sharing and dynamic reconfiguration
-  Supports up to 16 transceiver lanes per link

Components
----------

The core instantiates one or more of the following components.

-  clock_source
-  altera_clock_bridge
-  altera_iopll
-  altera_pll
-  altera_pll_reconfig
-  altera_xcvr_reset_control
-  altera_xcvr_atx_pll_a10
-  altera_jesd204
-  alt_xcvr_reconfig
-  avl_adxphy (ADI IP core)

Transceiver Sharing
-------------------

An Altera transceiver PHY is a transmit and receive pair. If you infer a PHY in a transmit only core for a DAC device link, you are also consuming a receive channel even if NOT used. The same applies to a receive only core for an ADC device link. This IP core is meant to provide the 'sharing' of these transmit and receive channels across multiple instantiations. As an example you may infer a transmit only core of 4 lanes (T1), a receive only core of 2 lanes (R1) and another receive only core of 2 lanes (R2). It is possible to merge these three instantiations to use only 4 PHY channels. However, the software may access them as if they are independent and separate. The core also supports a lane multiplexing so that the transmit and receive cores may occupy any channels within their range.

Parameters
----------

+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| Name                  | Description                                                                                            | Default Value |
+=======================+========================================================================================================+===============+
| ``DEVICE_FAMILY``     | System specific, inferred from project settings.                                                       | Arria 10      |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``TX_OR_RX_N``        | Indicates transmit (0x1) or receive (0x0) link type                                                    | 0             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``ID``                | An unique identifier for the core.                                                                     | 0             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``PCS_CONFIG``        | Altera specific, PCS soft or hard core options (see note 1).                                           | JESD_PCS_CFG2 |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``LANE_RATE``         | Altera specific, lane rate in Mbps (see note 1).                                                       | 10000         |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``SYSCLK_FREQUENCY``  | Altera specific, cpu clock frequency in MHz (see note 1).                                              | 100           |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``PLLCLK_FREQUENCY``  | Altera specific, transceiver pll clock frequency in MHz, usually 'LANE_RATE/2' (see note 1).           | 5000          |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``REFCLK_FREQUENCY``  | Altera specific, transceiver reference clock frequency in MHz (see note 1).                            | 500           |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``CORECLK_FREQUENCY`` | Altera specific, transceiver data path clock frequency in MHz, usually 'LANE_RATE/40' (see note 1).    | 250           |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``NUM_OF_LANES``      | Altera specific, number of lanes in the link (see note 1).                                             | 4             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``NUM_OF_CONVS``      | Altera specific, number of converters in the link (see note 1).                                        | 2             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``FRM_BCNT``          | Altera specific, number of bytes in a frame (see note 1).                                              | 1             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``FRM_SCNT``          | Altera specific, number of samples in a frame (see note 1).                                            | 1             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``MF_FCNT``           | Altera specific, number of frames in a multi-frame (see note 1).                                       | 32            |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+
| ``HD``                | Altera specific, high density (0x1) mode, samples are distributed across lanes in a link (see note 1). | 1             |
+-----------------------+--------------------------------------------------------------------------------------------------------+---------------+

Notes:

-  These parameters are passed to the Altera cores 'altera_jesd204' and 'altera_xcvr_atx_pll_a10'. Please refer to the documentation of these cores for a description of these parameters.

Interface
---------

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| Interface/Pin                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type            | Description                                                                    |
+===================================================================================================================================================================================================================================================================================================================================================================================================================================================+=================+================================================================================+
| ``sys_resetn``                                                                                                                                                                                                                                                                                                                                                                                                                                    | Input           | System reset (active low), must be the same as the processor reset.            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``sys_clk``                                                                                                                                                                                                                                                                                                                                                                                                                                       | Input           | System clock, must be the same as the processor clock.                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``ref_clk``                                                                                                                                                                                                                                                                                                                                                                                                                                       | Input           | Transceiver reference clock, primary IO must come from an external source.     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``core_clk``                                                                                                                                                                                                                                                                                                                                                                                                                                      | Output          | Transceiver core clock, data path is synchronous to this clock.                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``rst``                                                                                                                                                                                                                                                                                                                                                                                                                                           | Input           | Transceiver reset (active high), usually sourced by axi_adxcvr core.           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``ready``                                                                                                                                                                                                                                                                                                                                                                                                                                         | Output          | Transceiver ready (active high), indicates an active link.                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``core_pll_locked``                                                                                                                                                                                                                                                                                                                                                                                                                               | Output          | Transceiver core pll locked (active high), indicates pll lock status.          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``lane_pll_reconfig``                                                                                                                                                                                                                                                                                                                                                                                                                             | Input-Interface | Transceiver lane PLL reconfiguration avalon interface (transmit only).         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``core_pll_reconfig``                                                                                                                                                                                                                                                                                                                                                                                                                             | Input-Interface | Transceiver core PLL reconfiguration avalon interface.                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``phy_reconfig_{n}'' | Input-Interface | Transceiver PHY reconfiguration avalon interface (for each of the 'NUM_OF_LANES' in a link). | | ''ip_reconfig'' | Input-Interface | Transceiver IP programming avalon interface. | | ''tx_data_{n}``                                                                                                                                                                                                    | Output          | Transceiver transmit lane primary IO (transmit only).                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``rx_data_{n}'' | Input | Transceiver receive lane primary IO (receive only). | | ''sysref'' | Input | Transceiver SYSREF signal (subclass-1 only). | | ''sync'' | Mixed | Transceiver SYNC (input for transmit cores and output for receive cores). | | ''ip_sof'' | Output | Transceiver Start-Of-Frame (receive only). | | ''ip_data'' | Mixed | Transceiver data (input for transmit cores and output for receive cores). | | ''tx_ip_s_{n}`` | Input           | Transceiver transmit PHY swap port (if not really concerned, simply match up). |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``tx_ip_d_{n}'' | Output | Transceiver transmit PHY swap port (if not really concerned, simply match up). | | ''tx_phy_s_{n}``                                                                                                                                                                                                                                                                                                                    | Input           | Transceiver transmit PHY swap port (if not really concerned, simply match up). |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+
| ``tx_phy_d_${n}``                                                                                                                                                                                                                                                                                                                                                                                                                                 | Output          | Transceiver transmit PHY swap port (if not really concerned, simply match up). |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+--------------------------------------------------------------------------------+

Notes:

-  The ports 'sys_clk', 'ref_clk' and 'core_clk' corresponds to the 'SYSCLK_FREQUENCY', 'REFCLK_FREQUENCY' and 'CORECLK_FREQUENCY' parameters respectively.
-  All reconfiguration interfaces are 'AVALON' slave interfaces and must be connected to the CPU.
-  The 'tx_ip\_' and 'tx_phy\_' ports allow lane swapping within a link. If no swapping is desired, simply match them up with their indices. That is, tx_ip_s_0 == tx_phy_s_0 and tx_ip_d_0 == tx_phy_d_0. If swapping is desired the '\_s\_' and '\_p\_' pairs serve as a cross-bar switch for the IP and the PHY.

Register Map
------------

This core is a wrapper function for the above mentioned Altera IP cores. The register map of this core is one or more of its sub-cores.

Software Guidelines
-------------------

The core supports 'transceiver sharing' as described above, hence the same PHY is accessable from two different address regions. In other words, a transmit core can potentially access a receive core and corrupt the settings. There is no 'protection' of functionalities within the core.

More Information
----------------

-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
