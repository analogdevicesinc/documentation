Playing with xsdb
=================

XSDB (`Xilinx System Debugger <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2014_3/SDK_Doc/concepts/sdk_c_xsd_over.htm>`_) is a user-friendly, interactive, and scriptable command line interface, Its main purpose is debugging.

Quick start guide
-----------------

Open xsdb console

You can open an xsdb(or xsct) terminal from SDK GUI(tools) or by running xsdb.bat(in Windows OS), xsdb(in a Linux OS)

Connect to the hw_server
~~~~~~~~~~~~~~~~~~~~~~~~

::

     connect

List available targets
~~~~~~~~~~~~~~~~~~~~~~

::

     target

Connect to one of the targets (e.g. 3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     target 3

Read data from a memory location (core register map)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     mrd -force 0x(adi axi core base address + (common register)*4)
     mrd -force 0x(adi axi core base address + (channel offset + channel register)*4)

Write data from a memory location (core register map)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

     mwr -force 0x(axi_ad9361 base address + (channel offset + channel register)*4)  0x(value)

Example
~~~~~~~

# For example, change the axi_ad9361 tx data select. Writing to REG_CHAN_CNTRL_7. For channel offset and register see the axi_ad9361 register map.

::

     mwr -force 0x79024418 0x2
     mwr -force 0x79024458 0x2
     mwr -force 0x79024498 0x2
     mwr -force 0x790244D8 0x2

More examples can be found in no-OS program and capture scripts

-  :git-no-OS:`scripts/xsdb`.tcl
-  :git-no-OS:`scripts/xilinx_capture`.tcl

References
~~~~~~~~~~

-  https://wiki.analog.com/resources/fpga/docs/axi_ip
-  https://www.xilinx.com/support/documentation/sw_manuals/xilinx2014_3/SDK_Doc/concepts/sdk_c_xsd_over.htm

.. image:: https://wiki.analog.com/_media/navigation #resources/fpga/quick_validation
   :alt: Quick system validation with no-Os#resources/fpga/docs/tips|Using and modifying the HDL design#resources/fpga/docs/hdl|Main page
