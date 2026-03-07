AXI_LTC2387
===========

| The :git-hdl:`library/axi_ltc2387` IP core interfaces to the :adi:`LTC2387-16` and :adi:`LTC2387-18` devices. This documentation only covers the IP core and requires that one must be familiar with the device for a complete and better understanding.
| More about the generic framework interfacing ADCs can be read here: :doc:`axi_adc_ip </wiki-migration/resources/fpga/docs/axi_adc_ip>`, and about our architecture :doc:`here </wiki-migration/resources/fpga/docs/arch>`.

Features
--------

-  AXI Slave Memory Mapped control/status interface
-  Select between the 16-bit or 18-bit design
-  Supported only on Xilinx devices

Parameters
----------

+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Name                       | Description                                                                                                                                                                                                                     | Default Value        |
+============================+=================================================================================================================================================================================================================================+======================+
| ``ID``                     | Core ID should be unique for each LTC2387 IP in the system                                                                                                                                                                      | 0                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``FPGA_TECHNOLOGY``        | Encoded value describing the technology/generation of the FPGA device (arria 10/7series)                                                                                                                                        | set automatically    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``FPGA_FAMILY``            | Encoded value describing the family variant of the FPGA device(e.g., SX, GX, GT)                                                                                                                                                | set automatically    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``SPEED_GRADE``            | Encoded value describing the FPGA's speed-grade                                                                                                                                                                                 | set automatically    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DEV_PACKAGE``            | Encoded value describing the device package. The package might affect high-speed interfaces                                                                                                                                     | set automatically    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``IO_DELAY_GROUP``         | The delay group name which is set for the delay controller                                                                                                                                                                      | "adc_if_delay_group" |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``IO_DELAY_CTRL``          | Can have the values 0 or 1, conditioning the instantiation of the IODELAY_CTRL primitive. You can place only one IODELAY_CTRL per I/O bank, and need to set the same IO_DELAY_GROUP for the interfaces placed in that I/O bank. | 1                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DELAY_REFCLK_FREQUENCY`` | Reference clock frequency used for ad_data_in instances                                                                                                                                                                         | 200                  |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``USERPORTS_DISABLE``      | If set, indicates that the logic related to the User Data Format (e.g. decimation) was not implemented. (as a result of a configuration of the IP instance)                                                                     | 0                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``DATAFORMAT_DISABLE``     | Disable the Data Format control module                                                                                                                                                                                          | 0                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_INIT_DELAY``         | Initial delay                                                                                                                                                                                                                   | 22                   |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``ADC_RES``                | The ADC's resolution. Can be 16/18 bits.                                                                                                                                                                                        | 16                   |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``OUT_RES``                | The output data resolution. Can be 16/18 bits.                                                                                                                                                                                  | 16                   |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| ``TWOLANES``               | Specifies whether the two-lane output mode is activated or not. When activated, the ADC outputs two bits at the same time, on DA+/DA- and DB+/DB-. When it is low, then DB+/DB- is disabled.                                    | 1                    |
+----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

I/O Interface
-------------

+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
| Interface              | Pin           | Type                    | Description                                                     |
+========================+===============+=========================+=================================================================+
| **Delay Clock**        |               |                         |                                                                 |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``delay_clk`` | ``input``               | Delay clock input for IO_DELAY control, connect to 200MHz clock |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
| **LVDS ADC interface** |               |                         |                                                                 |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``ref_clk``   | ``input``               | LVDS input clock                                                |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``clk_gate``  | ``input``               | Signal enabling CLK+/CLK-                                       |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``dco_*``     | ``input``               | LVDS data clock input                                           |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``da_*``      | ``input``               | Serial LVDS data input                                          |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``db_*``      | ``input``               | Serial LVDS data input                                          |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
| **DMA ADC interface**  |               |                         |                                                                 |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``adc_valid`` | ``output``              | Indicates valid data at the current channel                     |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``adc_data``  | ``output[OUT_RES-1:0]`` | Received data output                                            |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``adc_dovf``  | ``input``               | Data overflow, must be connected to the DMA                     |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
| **AXI_S_MM interface** |               |                         |                                                                 |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+
|                        | ``s_axi_*``   |                         | Standard AXI Slave Memory Map interface                         |
+------------------------+---------------+-------------------------+-----------------------------------------------------------------+

Detailed description
--------------------

From the HDL perspective, the selection between :adi:`LTC2387-16` and :adi:`LTC2387-18` is done by the ``ADC_RES`` and ``OUT_RES`` parameters for the modules.

-  For :adi:`LTC2387-16` is ADC_RES = 16, and OUT_RES = 16
-  For :adi:`LTC2387-18` is ADC_RES = 18, and OUT_RES = 32 (because the addresses are on a number of bits that's power of 2)

Internal interface description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The :git-hdl:`LVDS interface module <library/axi_ltc2387/axi_ltc2387_if.v>` has as inputs the LVDS signals for clock and data:

DCO+/DCO-
^^^^^^^^^

| LVDS clock input; it is an echoed version of the CLK+/CLK- signal, and it's used to latch the data outputs from the chip.

DA+/DA- and DB+/DB-
^^^^^^^^^^^^^^^^^^^

| Serial LVDS data inputs; DB+/- is used only when ``TWOLANES`` parameter is active

CLK_GATE
^^^^^^^^

This signal ``clk_gate`` is enabling the CLK+/CLK- which is driven by the reference clock. It is generated by :doc:`AXI_PWM_GEN </wiki-migration/resources/fpga/docs/axi_pwm_gen>`.

ADC_VALID
^^^^^^^^^

| It is 1 for the current sample that is sent. This is generated depending on ``clk_gate``.

ADC_DATA
^^^^^^^^

| Depending on ``TWOLANES`` parameter, whether it is set or not, the output *adc_data* is either taken from the DA+/- port interleaved with bits from DB+/-, or it is taken only from DA+/- port.
|

.. note::

   Note that when using the **ONE LANE** configuration, the only resolution available is **18 bits**!


Channel module description
~~~~~~~~~~~~~~~~~~~~~~~~~~

| Here it's where the expected pattern is created and checked if the data received from the DMA is the correct one (this is used for quick validation of the design).
| In the case of the device with 16-bit resolution, a sign extension is done here also.

Register Map
------------

+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| Address |        | Name        |     |     | Description                                                                                   |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| DWORD   | BYTE   |             |     |     |                                                                                               |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | BASE        |     |     | See the `Base (common to all cores) <https://wiki.analog.com/>`_ table for more detail        |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | RX COMMON   |     |     | See the `ADC Common <https://wiki.analog.com/>`_ table for more detail                        |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+
| 0x0000  | 0x0000 | RX CHANNELS |     |     | See the `ADC Channel <https://wiki.analog.com/>`_ table for more detail                       |
+---------+--------+-------------+-----+-----+-----------------------------------------------------------------------------------------------+

.. include:: hdl/regmap.rst .. include:: hdl/regmap.rst .. include:: hdl/regmap.rst

Software Guidelines
-------------------

The software parts for this IP core can be found at:

-  :git-linux:`LTC2387 Linux Kernel driver <drivers/iio/adc/ltc2387.c>`
-  :git-linux:`LTC2387 Devicetree <arch/arm/boot/dts/zynq-zed-adv7511-ltc2387.dts>`

References
----------

-  :git-hdl:`AXI LTC2387 <library/axi_ltc2387>` IP source code
-  :adi:`LTC2387-16 chip information <LTC2387-16>`
-  :adi:`LTC2387-18 chip information <LTC2387-18>`
-  :doc:`HDL Architecture </wiki-migration/resources/fpga/docs/arch>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
