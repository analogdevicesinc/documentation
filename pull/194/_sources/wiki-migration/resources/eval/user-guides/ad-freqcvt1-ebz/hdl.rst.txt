HDL support for AD-FREQCVT1-EBZ board
=====================================

The :doc:`AD-FREQCVT1-EBZ </wiki-migration/resources/eval/user-guides/ad-freqcvt1-ebz>` board can be configured through an SPI interface, using the provided 12-pin ribbon cable. Care should be taken to connect the cable to the PMOD connector the same way on carrier and board side too.

The FMCOMMS2/3 HDL design fully supports the AD-FREQCVT1-EBZ board by enabling the second SPI interface of the Processing System 7 IP core, in this way providing full access for the software to configure and setup the frequency converter board.

Supported carriers
------------------

======================================== ==============
Carrier                                  PMOD connector
======================================== ==============
`ZC706 <https://www.xilinx.com/ZC706>`_ J58
`ZC702 <https://www.xilinx.com/ZC702>`_ J63
`Zed Board <http://www.zedboard.org>`_  JA1
======================================== ==============

IO layout
---------

========= ================== ============= =============
Carrier   PMOD connector pin SPI interface FPGA pin name
========= ================== ============= =============
**ZC706** PMOD1_0            CSN_TX        AJ21
:::       PMOD1_4            CSN_RX        Y20
:::       PMOD1_3            SCLK          AB16
:::       PMOD1_1            DATA          AK21
**ZC702** PMOD1_0            CSN_TX        E15
:::       PL_PJTAG_TDI       CSN_RX        V8
:::       PMOD1_3            SCLK          W5
:::       PMOD1_1            DATA          D15
**Zed**   JA1                CSN_TX        Y11
:::       JA7                CSN_RX        AB11
:::       JA4                SCLK          AA9
:::       JA2                DATA          AA11
========= ================== ============= =============
