UTIL CLKDIV IP core
===================

The :git-hdl:`library/xilinx/util_clkdiv` IP core works as a clock frequency divider.

In Xilinx projects
------------------

| The frequency can be divided either by 2 or by 4, depending on the selection. Also, a family has to be selected: 7 series or UltraScale; depending on which was chosen, different types of buffers will be used.
| \* 7 series: BUFR (see `Regional Clock Buffer <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`__ section)

-  UltraScale: BUFGCE_DIV (see `General Clock Buffer with Divider Function <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2014_1/ug974-vivado-ultrascale-libraries.pdf>`__ section)

| For both families, the BUFGMUX_CTRL primitive is used to select which clock to be outputted. Divides the input clock to SEL_0_DIV (by 4) if clk_sel is 0 or to SEL_1_DIV (by 2) if clk_sel is 1.
| Provides a glitch free output clock.

In Intel projects
-----------------

Only the Cyclone5 family is supported so far. The IP can be found :git-hdl:`here <library/intel/util_clkdiv>`.

Signal and Interface Pins
~~~~~~~~~~~~~~~~~~~~~~~~~

=========== ========== ====================
Pin         Type       Description
=========== ========== ====================
``clk``     ``input``  Reference clock
``clk_sel`` ``input``  Clock selection
``clk_out`` ``output`` Divided output clock
=========== ========== ====================

References
~~~~~~~~~~

-  `7 Series FPGAs Clocking Resources User Guide <https://www.xilinx.com/support/documentation/user_guides/ug472_7Series_Clocking.pdf>`__

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
