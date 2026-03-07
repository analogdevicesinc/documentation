UTIL_RFIFO
==========

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/util_rfifo/index.html\


UTIL_RFIFO is a core designed to downscale the clock rate of the TX data path. There are scenarios when the device clock (interface clock) is too high (above 200 MHz), making a challenge to integrate any processing cores between the device core and UPACK/DMA, because of the small timing margins. By reducing the clock rate of the data path, the user can easily integrate any custom processing core into the design.

In order to define the correct configuration, the following questions needs to be answered:

-  What is the clock rate of the device core's data interface? (dout_clk)
-  What is the data rate of the device core's data interface? (dout_valid@dout_clk)
-  What is the targeted clock rate of the data path (din_clk), and how we can achieve it, respecting the main rule of thumb: **input data rate must be equal to the output data rate**?

If the device clock rate is equal to the device data rate, the only solution to downscale the clock rate is to increase the data width of the output ports of the FIFO. Currently the util_rfifo supports four data width ratios: 1:1/1:2/1:4/1:8.

Features
--------

-  Supports Altera and Xilinx devices.
-  Downscale the DAC data path's clock rate.
-  Supports multiple channels (max eight channels)

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/rfifo_hdl_1.svg

Timing diagram
--------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/rfifo_timing_diagram.png
   :align: center
   :width: 900px

Parameters
----------

+-----------------------+----------------------------------------------------------------------------+---------------+
| Name                  | Description                                                                | Default Value |
+=======================+============================================================================+===============+
| ``NUM_OF_CHANNELS``   | The number of channels of the device.                                      | 4             |
+-----------------------+----------------------------------------------------------------------------+---------------+
| ``DIN_DATA_WIDTH``    | The bus width of the input data (DMA bus width).                           | 32            |
+-----------------------+----------------------------------------------------------------------------+---------------+
| ``DOUT_DATA_WIDTH``   | The bus width of the output data (device core's data interface bus width). | 64            |
+-----------------------+----------------------------------------------------------------------------+---------------+
| ``DIN_ADDRESS_WIDTH`` | The address width of the internal memory of the FIFO.                      | 4             |
+-----------------------+----------------------------------------------------------------------------+---------------+

Interface
---------

+--------------+---------------------------+---------------------------------+-----------------------+
| Interface    | Pin                       | Type                            | Description           |
+==============+===========================+=================================+=======================+
| ``din_0``    | **Input interface 0**     |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_enable_0``          | ``output``                      | Enable                |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_valid_0``           | ``output``                      | Valid                 |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_valid_in_0``        | ``input``                       | Looped back valid     |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_data_0``            | ``input[DIN_DATA_WIDTH-1:0]``   | Data                  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``din_1``    | **Input interface 1**     |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_enable_1``          | ``output``                      | Enable                |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_valid_1``           | ``output``                      | Valid                 |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_valid_in_1``        | ``input``                       | Looped back valid     |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_data_1``            | ``input[DIN_DATA_WIDTH-1:0]``   | Data                  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``...``      | **...**                   |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``din_7``    | **Input interface 7**     |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_enable_7``          | ``output``                      | Enable                |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_valid_7``           | ``output``                      | Valid                 |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_valid_in_7``        | ``input``                       | Looped back valid     |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_data_7``            | ``input[DIN_DATA_WIDTH-1:0]``   | Data                  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``din_unf``  | **Input data underflow**  |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``din_unf``               | ``input``                       | Input data underflow  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``dout_0``   | **Output interface 0**    |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_enable_0``         | ``input``                       | Enable                |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_valid_0``          | ``input``                       | Valid                 |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_valid_out_0``      | ``output``                      | Looped back valid     |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_data_0``           | ``output[DOUT_DATA_WIDTH-1:0]`` | Data                  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``dout_1``   | **Output interface 1**    |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_enable_1``         | ``input``                       | Enable                |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_valid_1``          | ``input``                       | Valid                 |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_valid_out_1``      | ``output``                      | Looped back valid     |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_data_1``           | ``input[DOUT_DATA_WIDTH-1:0]``  | Data                  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``...``      | **...**                   |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``dout_7``   | **Output interface 7**    |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_enable_7``         | ``input``                       | Enable                |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_valid_7``          | ``input``                       | Valid                 |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_valid_out_7``      | ``output``                      | Looped back valid     |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_data_7``           | ``input[DOUT_DATA_WIDTH-1:0]``  | Data                  |
+--------------+---------------------------+---------------------------------+-----------------------+
| ``dout_unf`` | **Output data underflow** |                                 |                       |
+--------------+---------------------------+---------------------------------+-----------------------+
|              | ``dout_unf``              | ``output``                      | Output data underflow |
+--------------+---------------------------+---------------------------------+-----------------------+

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
