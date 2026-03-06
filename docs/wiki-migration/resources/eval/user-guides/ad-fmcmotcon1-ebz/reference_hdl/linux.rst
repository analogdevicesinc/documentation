Xilinx HDL Reference Design
===========================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.

 This design is targeted for Zynq based FPGA systems. It has the complete infrastructure for Linux support.

Reference Design
----------------

The reference design contains HDL blocks for interfacing with the various components of the motor control hardware:

-  **ADC Interface** - Implements the communication with the AD7401 sigma delta modulators present on the AD-FMCMOTCON1-EBZ and also the SINC3 filters for demodulating the 1-bit digital stream provided by these parts. This HDL block exposes a set of registers that can be accessed through the AXI Lite interface. An AXI Streaming interface connected to a DMA controller allows the block to stream real time data to the application layer.
-  **Controller Interface** - Implements the interface to the IP control blocks in the system. An AXI Streaming interface connected to a DMA controller allows the block to stream real time data to the application layer.
-  **MathWorks FOC IP** - The FOC controller model is provided by MathWorks and it is integrated in the HDL design as a standalone IP core. The controller model is packaged into an IP core using the Simulink Workflow Advisor. It exposes a set of AXI-Lite registers that can be used to control the IP's operation as well as a set of interface signals for encoder input, current measurement data, inverter control and internal operations monitoring. All the monitoring signals connect to the Controller Interface IP which allows these signals to be monitored from the Linux IIO Scope application. The AXI-Lite registers exposed by the controller IP core can be directly accessed through an uio driver present in the ADI Linux distribution for Zynq.
-  **Position & Speed Processing** - Implements the algorithm for converting Hall, BEMF and Encoder signals into speed and position data. This HDL block exposes a set of registers that can be accessed through the AXI Lite interface. An AXI Streaming interface connected to a DMA controller allows the block to stream real time data to the application layer.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/reference_hdl/mc_design.png
   :alt: Reference Design
   :width: 600px

Vivado Design Generation
------------------------

Start Vivado in GUI mode, in a Windows environment. The project is generateed using the Vivado TCL console by issuing the following commands:

-  *cd [project_path]/projects/motor_control/zed*
-  *source ./system_project.tcl*

This will generate the entire system and create the bit file.

Downloads
---------

.. admonition:: Download
   :class: download

   
   -  :git-hdl:`Vivado ADI Libraries <library>`
   -  :git-hdl:`Vivado Motor Control Reference Design <projects/motor_control>`
   
   ::
   


Setting up Linux
----------------

|

.. note::

   For instructions on how to setup linux on the ZED board, please follow instructions at:


   | :doc:`Linux on Zynq Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/zynq>`
   |

Support
-------

.. hint::

   
   -  Questions? :ez:`Ask Help & Support <fpga>`.
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#none#../
   :alt: Overview#ise|Xilinx ISE HDL Reference Design
