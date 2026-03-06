Xilinx ISE HDL Reference Design
===============================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.

 This design is targeted for Zynq based FPGA systems.

Reference Design
----------------

The reference design contains HDL blocks for interfacing with the various components of the motor control hardware:

-  **ADC Interface** - Implements the communication with the AD7401 sigma delta modulators present on the AD-FMCMOTCON1-EBZ and also the SINC3 filters for demodulating the 1-bit digital stream provided by these parts.
-  **Controller** - Implements the motor control algorithm. The algorithm is designed and simulated in Simulink from Matworks and afterwards translated to HDL using the Mathworks HDL Coder.
-  **Speed Sensor Interface** - Implements the algorithm for converting Hall, BEMF and Encoder signals into speed and position data.

All the HDL blocks connect to Chipscope ILA and VIO modules which provide the means to monitor and control their operation.

Details about the Chipscope interface and how to run the ISE project can be found in the :doc:`ISE Project with Chipscope Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/chipscope>`.

Downloads
---------

|

.. admonition:: Download
   :class: download

   :git-fpgahdl_xilinx:`ISE HDL Reference Design <motor_control/adi_zed_ise_rev2>`


   | :git-fpgahdl_xilinx:`Chipscope Project <motor_control/adi_zed_ise_rev2/Chipscope>`
   |

Support
-------

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <fpga>`.
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#linux
   :alt: HDL Design for Linux#..:\|Overview#none
