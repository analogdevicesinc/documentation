AXI CLKGEN IP core
==================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_clkgen/index.html\


The :git-hdl:`library/axi_clkgen` IP core is a software programmable clock generator.

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/axi_clkgen_1.svg
   :alt: AXI_CLKGEN Block diagram
   :align: center

| 
| The top module, axi_clkgen, instantiates a :git-hdl:`mcm wrapper <library/xilinx/common/ad_mmcm_drp.v>`, the :doc:`CLKGEN register map </wiki-migration/resources/fpga/docs/hdl/regmap>` and the :doc:`AXI handling </wiki-migration/resources/fpga/docs/up_if>` interface.

The ad_mmcm_drp is a wrapper over MMCM, which can instantiate a Virtex 6 MMCM or 7 Series MMCM. Detailed information regarding the 7 Series MMCM can be found in Xilinx `UG472 <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_ and `UG953 <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2015_2/ug953-vivado-7series-libraries.pdf>`_.

The register map allows resetting the MMCM, changing the clock source, checking the status of the MMCM lock and controlling the DRP interface.

Configuration Parameters
------------------------

+-------------------+----------------------------------------------------+---------------+
| Name              | Description                                        | Default Value |
+===================+====================================================+===============+
| ``ID``            | Core ID should be unique for each IP in the system | 0             |
+-------------------+----------------------------------------------------+---------------+
| ``DEVICE_TYPE``   | 7 Series (0) or Virtex 6 (1) device                | 0             |
+-------------------+----------------------------------------------------+---------------+
| ``CLKIN_PERIOD``  | Default clock period for CLKIN1                    | 5.0           |
+-------------------+----------------------------------------------------+---------------+
| ``CLKIN2_PERIOD`` | Default clock period for CLKIN2                    | 5.0           |
+-------------------+----------------------------------------------------+---------------+
| ``VCO_DIV``       | DIVCLK_DIVIDE MMCM parameter                       | 11            |
+-------------------+----------------------------------------------------+---------------+
| ``VCO_MUL``       | CLKFBOUT_MULT_F MMCM parameter                     |               |
+-------------------+----------------------------------------------------+---------------+
| ``CLK0_DIV``      | CLKOUT0_DIVIDE_F MMCM parameter                    |               |
+-------------------+----------------------------------------------------+---------------+
| ``CLK0_PHASE``    | CLKOUT0_PHASE MMCM parameter                       | 0.000         |
+-------------------+----------------------------------------------------+---------------+
| ``CLK1_DIV``      | CLKOUT1_DIVIDE MMCM parameter                      | 6             |
+-------------------+----------------------------------------------------+---------------+
| ``CLK1_PHASE``    | CLKOUT1_PHASE MMCM parameter                       | 0.000         |
+-------------------+----------------------------------------------------+---------------+

Signal and Interface Pins
-------------------------

+-------------+------------------------------------+------------+-------------------+
| Interface   | Pin                                | Type       | Description       |
+=============+====================================+============+===================+
| '' Clocks'' | **Input and output clocks**        |            |                   |
+-------------+------------------------------------+------------+-------------------+
|             | ``clk``                            | ``input``  | Reference clock 1 |
+-------------+------------------------------------+------------+-------------------+
|             | ``clk2``                           | ``input``  | Reference clock 2 |
+-------------+------------------------------------+------------+-------------------+
|             | ``clk_0``                          | ``output`` | Output clock 0    |
+-------------+------------------------------------+------------+-------------------+
|             | ``clk_1``                          | ``output`` | Output clock 1    |
+-------------+------------------------------------+------------+-------------------+
| ''s_axi ''  | **AXI Slave Memory Map interface** |            |                   |
+-------------+------------------------------------+------------+-------------------+

Register Map
------------

.. include:: hdl/regmap.rst .. include:: hdl/regmap.rst

References
----------

-  `7 Series FPGAs Clocking Resources User Guide <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`_
-  `MMCM and PLL Dynamic Reconfiguration <https://www.xilinx.com/support/documentation/application_notes/xapp888_7Series_DynamicRecon.pdf>`_

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
