AXI_ADXCVR
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_adxcvr/index.html\


The AXI_ADXCVR is a utility core used to control and configure the highspeed transceivers instantiated in :doc:`UTIL_ADXCVR </wiki-migration/resources/fpga/docs/util_xcvr>`. There are separate AXI_ADXCVR cores for Intel and Xilinx designs, due to the small differences between the Xilinx's and Intel's transceivers architecture.

Features
--------

-  Supports :git-hdl:`Intel <library/intel/axi_adxcvr>` and :git-hdl:`Xilinx <library/xilinx/axi_adxcvr>` devices.
-  Software can access the core's registers through an AXI4 Lite Memory Mapped interface.
-  Link reset and monitor for Intel and Xilinx.
-  Reconfiguration interface control with broadcast capability for Xilinx.
-  Access to the Statistical eye scan interface of the PHY (Xilinx).
-  Supports up to 16 transceiver lanes per link. (Xilinx)

Intel Devices
-------------

For Intel devices, the adi_jesd204 IP is using the axi_adxcvr core, which can be accessed by the **link_management** interface. It provides a global reset signal for the JESD204B framework. Resets the XCVR reset controller IP, the link PLL reset controller, the PHY itself, and also the link layer of the stack. Besides the reset generation, monitors the PLLs and the PHY state.

Parameters
~~~~~~~~~~

+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| Name                | Description                                                                                                   | Default Value |
+=====================+===============================================================================================================+===============+
| ``ID``              | Instance identification number, if more than one instance is used.                                            | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``NUM_OF_LANES``    | The number of lanes (primitives) used in this link.                                                           | 8             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``XCVR_TYPE``       | Refers to the transciver speed grade 0-9.                                                                     | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_TECHNOLOGY`` | Encoded value describing the technology/generation of the FPGA device (e.g., Cyclone V, Arria 10, Stratix 10) | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_FAMILY``     | Encoded value describing the family variant of the FPGA device(e.g., SX, GX, GT)                              | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``SPEED_GRADE``     | Encoded value describing the FPGA's speed-grade                                                               | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``DEV_PACKAGE``     | Encoded value describing the device package. The package might affect high-speed interfaces                   | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_VOLTAGE``    | Contains the value(0-5000 mV) at wich the FPGA device supplied                                                | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+
| ``TX_OR_RX_N``      | If set (0x1), configures the link in transmit mode, otherwise receive.                                        | 0             |
+---------------------+---------------------------------------------------------------------------------------------------------------+---------------+

+-------------------+---------------------+-------+-------------------------------------------+
| Interface         | Pin                 | Type  | Description                               |
+===================+=====================+=======+===========================================+
| ``axi_aclk``      | ``axi_aclk``        | Input | System clock. (in general 100 MHz)        |
+-------------------+---------------------+-------+-------------------------------------------+
| ``axi_aresetn``   | ``axi_aresetn``     | Input | System reset.                             |
+-------------------+---------------------+-------+-------------------------------------------+
| ``s_axi``         | Slave-AXI           | IO    | Slave AXI4 Lite Memory Mapped interface   |
+-------------------+---------------------+-------+-------------------------------------------+
| ``up_pll_locked`` | ``core_pll_locked`` | Input | Connect to the fPLL's **pll_locked** pin. |
+-------------------+---------------------+-------+-------------------------------------------+
| ``up_ready``      | ``ready``           | Input | Connect to PHY reset controller.          |
+-------------------+---------------------+-------+-------------------------------------------+

Register Map
~~~~~~~~~~~~

+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Address |        | Bits               | Name            | Type | Description                                                                                                                                          |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |                    |                 |      |                                                                                                                                                      |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | REG_VERSION        |                 |      | Version Register                                                                                                                                     |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:0]             | VERSION[31:0]   | RO   | Version number.                                                                                                                                      |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0001  | 0x0004 | REG_ID             |                 |      | Instance Identification Register                                                                                                                     |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:0]             | ID[31:0]        | RO   | Instance identifier number.                                                                                                                          |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0002  | 0x0008 | REG_SCRATCH        |                 |      | Scratch (GP R/W) Register                                                                                                                            |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:0]             | SCRATCH[31:0]   | RW   | Scratch register.                                                                                                                                    |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0004  | 0x0010 | REG_RESETN         |                 |      | Reset Control Register                                                                                                                               |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [0]                | RESETN          | RW   | If clear, link is held in reset, set this bit to 0x1 to activate link. Note that the reference clock must be active before setting this bit.         |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0005  | 0x0014 | REG_STATUS         |                 |      | Status Reporting Register                                                                                                                            |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [0]                | STATUS          | RO   | After setting the RESETN bit above, wait for this bit to set. If set, indicates successful link activation.                                          |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0006  | 0x0018 | REG_STATUS_32      |                 |      | Status Reporting Register                                                                                                                            |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:NUM_OF_LANES]  | RESERVED        | RO   | 0                                                                                                                                                    |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [NUM_OF_LANES]     | UP_PLL_LOCKED   | RO   | After setting the RESETN bit above, wait for this bit be to set.                                                                                     |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [NUM_OF_LANES-1:0] | CHANNEL_N_READY | RO   | After setting the RESETN bit above, wait for this registers to be set.                                                                               |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0007  | 0x001c | REG_FPGA_INFO      |                 |      | FPGA device information :git-hdl:`Intel encoded values <library/scripts/adi_intel_device_info_enc.tcl>`                                              |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:24]            | FPGA_TECHNOLOGY | RO   | Encoded value describing the technology/generation of the FPGA device (e.g., cyclone V, arria 10, stratix 10)                                        |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [23:16]            | FPGA_FAMILY     | RO   | Encoded value describing the family variant of the FPGA device(e.g., SX, GX, GT or zynq, kintex, virtex)                                             |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [15:8]             | SPEED_GRADE     | RO   | Encoded value describing the FPGA's speed-grade                                                                                                      |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [7:0]              | DEV_PACKAGE     | RO   | Encoded value describing the device package. The package might affect high-speed interfaces                                                          |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0009  | 0x0024 | REG_GENERIC_INFO   |                 |      | Physical layer info                                                                                                                                  |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [31:28]            | RESERVED        | RO   | 0                                                                                                                                                    |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [27:24]            | XCVR_TYPE[3:0]  | RO   | Refers to the transceiver speed grade 0-9.                                                                                                           |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [23:12]            | RESERVED        | RO   | 0                                                                                                                                                    |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [11:9]             | RESERVED        | RO   | 0                                                                                                                                                    |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [8]                | TX_OR_RX_N      | RO   | Transceiver type (transmit or receive)                                                                                                               |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [7:0]              | NUM_OF_LANES    | RO   | Physical layer number of lanes.                                                                                                                      |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 0x0050  | 0x0140 | REG_FPGA_VOLTAGE   |                 |      | FPGA device voltage information                                                                                                                      |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|         |        | [15:0]             | FPGA_VOLTAGE    | RO   | The voltage of the FPGA device in mv                                                                                                                 |
+---------+--------+--------------------+-----------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Software Guidelines
~~~~~~~~~~~~~~~~~~~

When the board powers up, both ATX and fPLL's must have a stable reference clock in order to lock automatically. If this requirement can not be respected by the system (e.g. the reference clocks are generated by a device that requires software configuration, through an interface implemented in FPGA), the software needs to reconfigure both PLLs, and just after that resets the transceivers.

Xilinx Devices
--------------

In Xilinx Devices, the core configures itself to be interfaced with the GT variant supported by the UTIL_ADXCVR core. All the transceiver primitives are configured and programmed identically.

.. _parameters-1:

Parameters
~~~~~~~~~~

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Name                | Description                                                                                                                                                          | Default Value |
+=====================+======================================================================================================================================================================+===============+
| ``ID``              | Instance identification number, if more than one instance is used.                                                                                                   | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``NUM_OF_LANES``    | The number of lanes (primitives) used in this link.                                                                                                                  | 8             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``XCVR_TYPE``       | Define the current GT type, GTXE2(2), GTHE3(5), GTHE4(7).                                                                                                            | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_TECHNOLOGY`` | Encoded value describing the technology/generation of the FPGA device (7series/ultrascale)                                                                           | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_FAMILY``     | Encoded value describing the family variant of the FPGA device(e.g., zynq, kintex, virtex)                                                                           | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``SPEED_GRADE``     | Encoded value describing the FPGA's speed-grade                                                                                                                      | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``DEV_PACKAGE``     | Encoded value describing the device package. The package might affect high-speed interfaces                                                                          | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``FPGA_VOLTAGE``    | Contains the value(0-5000 mV) at wich the FPGA device supplied                                                                                                       | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``TX_OR_RX_N``      | If set (0x1), configures the link in transmit mode, otherwise receive.                                                                                               | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``QPLL_ENABLE``     | If set (0x1), configures the link to use QPLL on QUAD basis. If multiple links are sharing the same transceiver, only one of them may enable the QPLL.               | 1             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``LPM_OR_DFE_N``    | Chosing between LPM or DFE of modes for the RX Equalizer                                                                                                             | 1             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``RATE``            | Defines the initial values for Transceiver Control Register (REG_CONTROL 0x0008)                                                                                     | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``TX_DIFFCTRL``     | Driver Swing Control(TX Configurable Driver)                                                                                                                         | 8             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``TX_POSTCURSOR``   | Transmitter post-cursor TX pre-emphasis control.                                                                                                                     | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``TX_PRECURSOR``    | Transmitter pre-cursor TX pre-emphasis control.                                                                                                                      | 0             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``SYS_CLK_SEL``     | Selects the PLL reference clock source to drive the RXOUTCLK `#table_1 <https://wiki.analog.com/>`_                                                                  | 3             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``OUT_CLK_SEL``     | select the transceiver reference clock as the source of TXOUTCLK `#table_2 <https://wiki.analog.com/>`_                                                              | 4             |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+

Interface
~~~~~~~~~

+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Interface       | Pin             | Type   | Description                                                                                                                                                                                                                   |
+=================+=================+========+===============================================================================================================================================================================================================================+
| ``axi_clk``     | ``axi_clk``     | Input  | The CPU clock (assumed to be 100MHz), must be same as the DRP clock.                                                                                                                                                          |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``axi_aresetn`` | ``axi_aresetn`` | Input  | The CPU reset (internally used asynchronous to the axi_clk).                                                                                                                                                                  |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``up_status``   | ``up_status``   | Output | If set, indicates that the link is up and active. The same information is read on the register bit (see below). This signal may be connected to the JESD204B IP reset done input.                                             |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``s_axi``       | Slave-AXI       | IO     | The programmable interface, must be connected to a CPU master.                                                                                                                                                                |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``m_axi``       | Master-AXI      | IO     | The Eye-Scan DMA interface, must be connected to a memory slave. This interface is available only if parameter TX_OR_RX_N is set to 0x0.                                                                                      |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``up_cm_*``     | Common-DRP      | IO     | The common DRP interface, must be connected to the equivalent DRP ports of UTIL_ADXCVR. This is a QUAD interface, shared by four transceiver lanes. This interface is available only if parameter QPLL_ENABLE is set to 0x1.  |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``up_ch_*``     | Channel-DRP     | IO     | The channel DRP interface, must be connected to the equivalent DRP ports of UTIL_ADXCVR. This is a channel interface, one per each transceiver lane.                                                                          |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``up_es_*``     | Eye-Scan-DRP    | IO     | The Eye-Scan DRP interface, must be connected to the equivalent DRP ports of UTIL_ADXCVR. This is a channel interface, one per each transceiver lane. This interface is available only if parameter TX_OR_RX_N is set to 0x0. |
+-----------------+-----------------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _register-map-1:

Register Map
~~~~~~~~~~~~

.. include:: hdl/regmap.rst

.. _software-guidelines-1:

Software Guidelines
~~~~~~~~~~~~~~~~~~~

The system must have active DRP and reference clocks before any software access. The software is expected to write necessary control parameters to LPM_DFE_N, RATE, SYSCLK_SEL, OUTCLK_SEL register bits and then set RESETN bit to 0x1. After which monitor the STATUS bit to be set. There are no other requirements for initialization.

The DRP access is identical for common and channel interfaces. The SEL bits may be set to a specific transceiver lane or 0xff to broadcast. A write to the CONTROL register (bits WR, ADDR, WDATA) initiates DRP access in hardware. A read to this register has no effect. In order to write to the transceiver, set WR to 0x1 with the address. In order to read from the transceiver, set WR to 0x0 with the address. As soon as this register is written, the BUSY signal is set and is cleared only after the access is complete. The broadcast read is a logical OR of all the channels. After an access is started, do NOT interrupt the core for any reason (including setting RESETN to 0x0), allow the access to finish itself. Though the core itself is immune to a software abort, the transceiver may fail on further accesses and may require a system-wide reset.

The eye-scan feature also allows a SEL option and a broadcast has the effect of a combined mask. That is, the error counter will be zero ONLY if all the transceiver error counters are zero. To start eye-scan, set ES_REQ to 0x1 and wait for the same bit to self-clear. If eye-scan needs to be stopped, set the ES_REQ bit to 0x0.

Table 1
^^^^^^^

========== ==== ======== ======== =====
SYSCLK_SEL 00   01       10       11
========== ==== ======== ======== =====
GTXE2      CPLL RESERVED RESERVED QPLL
GTHE3      CPLL RESERVED QPLL1    QPLL0
GTHE4      CPLL RESERVED QPLL1    QPLL0
GTYE4      CPLL RESERVED QPLL1    QPLL0
========== ==== ======== ======== =====

Table 2
^^^^^^^

+------------+-----------+-----------+--------+----------+------------+------------------------+
| OUTCLK_SEL | 001       | 010       | 011    | 100      | 101        | All other combinations |
+============+===========+===========+========+==========+============+========================+
| GTXE2      | OUTCLKPCS | OUTCLKPMA | REFCLK | REFCLK/2 | RESERVED   | RESERVED               |
+------------+-----------+-----------+--------+----------+------------+------------------------+
| GTHE3      | OUTCLKPCS | OUTCLKPMA | REFCLK | REFCLK/2 | PROGDIVCLK | RESERVED               |
+------------+-----------+-----------+--------+----------+------------+------------------------+
| GTHE4      | OUTCLKPCS | OUTCLKPMA | REFCLK | REFCLK/2 | PROGDIVCLK | RESERVED               |
+------------+-----------+-----------+--------+----------+------------+------------------------+
| GTYE4      | OUTCLKPCS | OUTCLKPMA | REFCLK | REFCLK/2 | PROGDIVCLK | RESERVED               |
+------------+-----------+-----------+--------+----------+------------+------------------------+

The REFCLK selected by OUTCLK_SEL depends on the SYSCLK_SEL, it may be CPLL, QPLL0 or QPLL1 refclk.

Physical layer PRBS testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The REG_PRBS_CNTRL and REG_PRBS_STATUS registers expose controls of internal PRBS generators and checkers allowing the testing the multi-gigabit serial link at the physical layer without the need of the link layer bringup.

TX link procedure
^^^^^^^^^^^^^^^^^

-  Configure ref clock and device clocks for under test lane rate. Bring XCVR out from reset.
-  In the REG_PRBS_CNTRL registers set PRBSSEL to a non-zero value. See the transceiver guides for exact values, different transceiver families may have different encoding for the same pattern.
-  On the receiving side of the link set the checker for the same pattern and reset the error counters.
-  No error should be recorded on the receiver side.
-  Set the PRBSFORCEERR bit in the REG_PRBS_CNTRL register to force the error injection into the stream of bits.
-  The error should be detected and recorded on the receiver side.

RX link procedure
^^^^^^^^^^^^^^^^^

-  Configure ref clock and device clocks for under test lane rate. Bring XCVR out from reset.
-  On the transmit side of the link set a test pattern that is available in the receiving transceiver. Consult the transceiver documentation for details.
-  In the REG_PRBS_CNTRL registers set PRBSSEL to the corresponding pattern. Reset the error counters with PRBSCNTRESET.
-  Check REG_PRBS_STATUS fields for results. If the check is successful for non-GTX transceivers the PRBSLOCKED bit must appear as set and PRBSERR must stay low. For GTX transceivers the PRBSLOCKED bit can be ignored and checking the PRBSERR alone is sufficient. If PRBSERR is set, check with DRP accesses the internal error counter to get the number of errors received. See the transceiver guide for details.

More Information
----------------

-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

Reference
---------

-  `Intel® Arria® 10 Transceiver PHY User Guide <https://wiki.analog.com/https/www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/arria-10/ug_arria10_xcvr_phy.pdf>`_
-  `7 Series FPGAs GTX/GTH Transceivers User Guide - Xilinx <https://www.xilinx.com/support/documentation/user_guides/ug476_7Series_Transceivers.pdf>`_
-  `Ultrascale Architecture GTH Transceivers User Guide - Xilinx <https://www.xilinx.com/support/documentation/user_guides/ug576-ultrascale-gth-transceivers.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
