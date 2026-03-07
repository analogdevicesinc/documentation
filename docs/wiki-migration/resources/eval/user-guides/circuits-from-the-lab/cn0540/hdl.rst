CN0540 HDL Reference Design
===========================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/cn0540/index.html\


Overview
--------

The HDL reference design for the CN0540 provides all the interfaces that are necessary to interact with the devices on the 24-bit data acquisition system designed for IEPE sensors.

The design have a SPI Engine instance to control and acquire data from the AD7768-1 24-bit precisions ADC, providing support to capture continuous samples at maximum sampling rate. Currently the design support FPGA carriers from both Intel and Xilinx.

Used devices
~~~~~~~~~~~~

-  :adi:`AD7768-1`
-  :adi:`ADA4945-1`
-  :adi:`LT3092`
-  :adi:`LTC2606`

Evaluation board
~~~~~~~~~~~~~~~~

-  :adi:`CN0540 Circuit Note Page <CN0540>`
-  :doc:`CN0540 Wiki </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0540>`

Supported FPGA carrier
~~~~~~~~~~~~~~~~~~~~~~

-  `Cora Z7-07S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development>`_
-  `DE10-Nano <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`_

HDL Design Description
----------------------

The design is built upon ADI's generic HDL reference design framework. In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design framework in general.

The reference design uses the standard :doc:`SPI Engine Framework </wiki-migration/resources/fpga/peripherals/spi_engine>` to interface the AD7768-1 ADC. The SPI offload module, which can be used to capture continuous data stream at maximum data rate, is triggered by the DRDY (data ready) signal of the device.

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see :git-hdl:`Release notes <releases>`)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |CN0540 HDL Project.|

Software sources
----------------

.. admonition:: Download
   :class: download

   
   -


   
   |Cora Z7-07S No-OS Project.|

   -

   |Cora Z7-07S Linux Project.|

   -

   |DE10-Nano Linux Project.|

.. |CN0540 HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/cn0540`
.. |Cora Z7-07S No-OS Project.| image:: https://wiki.analog.com/_media/:git-no-OS:`tree/master`
.. |Cora Z7-07S Linux Project.| image:: https://wiki.analog.com/_media/:git-linux:`tree/master`
.. |DE10-Nano Linux Project.| image:: https://wiki.analog.com/_media/:git-linux:`tree/master`
