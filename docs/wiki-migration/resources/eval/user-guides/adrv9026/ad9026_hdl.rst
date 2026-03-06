ADRV9026 HDL reference design
=============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/adrv9026/index.html


.. admonition:: Download
   :class: download

   :git-hdl:`projects/adrv9026`


The reference design supports the following evaluation board:

Supported Carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`__ FMC1 Slot

Building the HDL project
------------------------

General build instructions can be found here: :doc:`Building HDL </wiki-migration/resources/fpga/docs/build>`

Block Diagram
-------------

The data path and clock domains are depicted on the below diagram:


|image1|

The Rx links (ADC Path) operate with the following parameters:

-  Rx Deframer parameters: L=4, M=4, F=4, S=1, N’=16, N = 16
-  Sample Rate : 250 MSPS
-  RX_DEVICE_CLK – 250 MHz (Lane Rate/40)
-  REF_CLK – 250MHz (Lane Rate/40)
-  JESD204B Lane Rate – 10Gbps
-  CPLL

The Tx links (DAC Path) operate with the following parameters:

-  Tx Framer parameters: L=4, M=4, F=4, S=1, N’=16, N = 16
-  Sample Rate : 250 MSPS
-  TX_DEVICE_CLK – 250 MHz (Lane Rate/40)
-  REF_CLK – 250MHz (Lane Rate/40)
-  JESD204B Lane Rate – 10Gbps
-  QPLL0

Clock sources
~~~~~~~~~~~~~

The clock sources are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9026/adrv9026_clocking.png
   :align: center
   :width: 400px

More Information
----------------

-  :doc:`ADRV9026 Prototyping Platform User Guide </wiki-migration/resources/eval/user-guides/adrv9025>`
-  :doc:`ADRV9026-ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9026/quickstart/zynqmp>`
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`
-  :doc:`ADRV9026 Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9025>`

Support
-------

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Video, Audio, etc) via the :ez:`EngineerZone <community/fpga>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9026/adrv9026_jesd_bd.png
