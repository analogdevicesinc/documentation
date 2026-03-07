AD9213-EVB HDL reference design
===============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/ad9213_evb/index.html\


.. admonition:: Download
   :class: download

   :git-hdl:`projects/ad9213_evb`


The reference design supports the following evaluation board:

========================================== ===================
Hardware                                   Evaluation Document
========================================== ===================
:adi:`AD9213` AD9213
========================================== ===================

Supported Carriers
------------------

-  `VCU118 <https://www.xilinx.com/VCU118>`_ FMC+ Slot

Building the HDL project
------------------------

General build instructions can be found here: :doc:`Building HDL </wiki-migration/resources/fpga/docs/build>`

Block Diagram
-------------

The data path and clock domains are depicted on the below diagram:


|image1|

The design has one JESD receive chain having 16 lanes at rate of 12.5Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module. The transport layer is common and is represented by a RX JESD TPL module. The link operates in Subclass 1 by using the SYSREF signal to edge align the internal local multiframe clock and to release the received data in the same moment from all lanes, therefore ensuring that data from all channels is synchronized at the application layer.

The link is set for full bandwidth mode and operates with the following parameters:

-  Deframer paramaters: L=16, M=1, F=2, S=16, N’=16, N=16
-  GLBLCLK – 312.5MHz (Lane Rate/40)
-  REFCLK – 625 MHz (Lane Rate/20)
-  SYSREF – 19.53MHz (DEVCLK/512)
-  DEVCLK – 10000MHz
-  JESD204B Lane Rate – 12.5Gbps

Clock sources
~~~~~~~~~~~~~

The clock sources are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_evb/ad9213_clocks.png
   :align: center

More Information
----------------

-  `AD9213-EVB VCU118 Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9213_evb/quickstart/vcu118>`_
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`
-  `AD9213 ADC Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/ad9213>`_

Support
-------

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Video, Audio, etc) via the :ez:`EngineerZone <community/fpga>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9213_evb/ad9213_jesd_diagram.png
