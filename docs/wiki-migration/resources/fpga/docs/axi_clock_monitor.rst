AXI_CLOCK_MONITOR IP core
=========================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_clock_monitor/index.html\


The :git-hdl:`library/axi_clock_monitor` IP is used to measure clocks in the system.

Features
--------

-  Supports :git-hdl:`Intel <library/intel/axi_adxcvr>` and :git-hdl:`Xilinx <library/xilinx/axi_adxcvr>` devices.
-  Software can access the core's registers through an AXI4 Lite interface.
-  It can measure up to 16 clocks (set to 1 by default).

User Guidelines
---------------

HDL instantiation
~~~~~~~~~~~~~~~~~

-  Import the IP core to your block design
-  Select the desired number of clock inputs to be measured
-  Connect the IP to the AXI interface
-  Assign a base address to the IP Core, so it doesn't overlap with other components
-  Assign clock signals to the clock inputs
-  Build the HDL project

Software implementation
~~~~~~~~~~~~~~~~~~~~~~~

We use software to access the core's registers in order to get the data from the IP. So far, only no-OS software is supported.

The following example contains a simple functions that reads all the info from the IP and prints it on the serial terminal:

::

   void clock_monitor_info (uint32_t core_base_addr, uint32_t axi_clock_speed_mhz) {
       uint32_t clock_ratio = 0;
       uint32_t clk1_addr = 0x40;
       uint32_t n_clocks = 0;
       uint32_t info_var = 0;
       uint8_t n = 0;

       info_var = axi_io_read(core_base_addr);
       printf("PCORE_VERSION = %d\n", info_var);

       info_var = axi_io_read(core_base_addr, 4);
       printf("ID = %d\n", info_var);

       n_clocks = axi_io_read((core_base_addr, 12));
       printf("n clocks = %d\n", n_clocks);

       info_var = axi_io_read(core_base_addr, 16);
       printf("RESET OUT = %d\n", info_var);

       while (n < n_clocks & n < 16) {
           clock_ratio = axi_io_read((core_base_addr, clk1_addr + 4\*n));

           if (clock_ratio == 0) {
               printf("Measured clock_%d: off\n", n);
           } else {
               printf("Measured clock_%d: %d MHz\n", n,
                   (clock_ratio * axi_clock_speed_mhz + 0x7fff) >> 16);
           }
           n++;
       }
   }

To call the function, consider the following parameters:

-  "core_base_addr" will take the value of the base address set at step 4 of `HDL instantiation <https://wiki.analog.com/>`_
-  "axi_clock_speed_mhz" will be the reference frequency. In most cases we will assume this parameter to be 100 (MHz)

Register Map
------------

.. include:: hdl/regmap.rst
