Microprocessor interface
========================

All the ADI IP cores contains multiple AXI register map modules, which control a well specified part of the IP. To avoid complicated interconnections inside the IP, using the :git-hdl:`library/common/up_axi.v` module, the AXI Memory Mapped interface is converted into a so called **Microprocessor interface** or **uP interface**. This interface has an independent write and read channel, and each channel contains an address bus, a data bus, a request (driven by master) and an acknowledge (driven by slave) control signals. All the uP interface signals names have a **up\_** prefix, this differentiate themselves clearly from other internal signals.

uP interface and signals
------------------------

+---------------------+--------------+------------------+-----------------------------------------------------------+
| Interface           | Pin          | Type             | Description                                               |
+=====================+==============+==================+===========================================================+
| **Clock and reset** |              |                  |                                                           |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_clk``   | ``input``        | Clock signal, should be connected to s_axi_aclk           |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_rstn``  | ``input``        | An active low reset, should be connected to s_axi_aresetn |
+---------------------+--------------+------------------+-----------------------------------------------------------+
| **Read interface**  |              |                  |                                                           |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_rreq``  | ``output``       | Read request from the processor                           |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_rack``  | ``input``        | Read acknowledge from the core                            |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_raddr`` | ``output[13:0]`` | Read address defined by the processor                     |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_rdata`` | ``input[31:0]``  | Read data, delivered by the core                          |
+---------------------+--------------+------------------+-----------------------------------------------------------+
| **Write interface** |              |                  |                                                           |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_wreq``  | ``output``       | Write request from the processor                          |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_wack``  | ``input``        | Write acknowledge from the core                           |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_waddr`` | ``output[13:0]`` | Write address defined by the processor                    |
+---------------------+--------------+------------------+-----------------------------------------------------------+
|                     | ``up_wdata`` | ``output[31:0]`` | Write data defined by the processor                       |
+---------------------+--------------+------------------+-----------------------------------------------------------+

**Note:** The directions of the signals are defined from the masters (microprocessor) perspective.

Timing diagram
--------------

The following timing diagram illustrates the signals and functionality of the interface. It show a register write access and two consecutive register read access.

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/up_if_2.svg
   :alt: UP interface timing diagram
   :align: center
