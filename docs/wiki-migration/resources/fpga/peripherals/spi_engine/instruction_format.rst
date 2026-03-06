SPI Engine Instruction Set Specification
========================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/spi_engine/instruction-format.html\


The SPI Engine instruction set is a simple 16-bit instruction set of which 12-bit is currently allocated (bits 15,14,11,10 are always 0).

Instructions
------------

Transfer Instruction
~~~~~~~~~~~~~~~~~~~~

== == == == == == = = = = = = = = = =
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
== == == == == == = = = = = = = = = =
0  0  0  0  0  0  r w n n n n n n n n
== == == == == == = = = = = = = = = =

The transfer instructions perform a low-level SPI transfer. It will generate SCLK transitions for the specified amount of cycles according to the SPI configuration register. If the r bit is set the SDI pin will be sampled and stored in the shift register at the end of each word the data is output on the SDI_DATA stream. If the w bit is set the SDO pin will be updated with the data received from the SDO_DATA stream. If the w bit is set the sdo_t signal will also be set to 0 for the duration of the transfer. If the SDI_DATA stream is not able to accept data or the SDO_DATA stream is not able to provide data the execution is stalled at the end/start of the transfer until data is accepted/becomes available.

+------+--------+-----------------------------------------------------------------------------------------------------------------------+
| Bits | Name   | Description                                                                                                           |
+======+========+=======================================================================================================================+
| r    | Read   | If set to 1 data will be read from the SDI pin during and the read words will be available on the SDI_DATA interface. |
+------+--------+-----------------------------------------------------------------------------------------------------------------------+
| w    | Write  | If set to 1 data will be taken from the SDO_DATA interface and output on the SDO pin.                                 |
+------+--------+-----------------------------------------------------------------------------------------------------------------------+
| n    | Length | n + 1 number of words will be transferred.                                                                            |
+------+--------+-----------------------------------------------------------------------------------------------------------------------+

Chip-select Instruction
~~~~~~~~~~~~~~~~~~~~~~~

== == == == == == = = = = = = = = = =
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
== == == == == == = = = = = = = = = =
0  0  0  1  0  0  t t s s s s s s s s
== == == == == == = = = = = = = = = =

The chip-select instruction updates the value chip-select output signal of the SPI Engine execution module.

Before and after the update is performed the execution module is paused for the specified delay. The length of the delay depends on the module clock frequency, the setting of the prescaler register and the t parameter of the instruction. delay = t \* (div + 1) / f_clk. This delay is inserted before and after the update of the chip-select signal, so the total execution time of the chip-select instruction is twice the delay.

==== ===========
Name Description
==== ===========
t    Delay
s    Chip-select
==== ===========

Configuration Write Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

== == == == == == = = = = = = = = = =
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
== == == == == == = = = = = = = = = =
0  0  1  0  0  0  r r v v v v v v v v
== == == == == == = = = = = = = = = =

The configuration writes instruction updates a `configuration register <https://wiki.analog.com/>`__ of the SPI Engine execution module with a new value.

==== ===========
Name Description
==== ===========
r    Register
v    Value
==== ===========

Synchronize Instruction
~~~~~~~~~~~~~~~~~~~~~~~

== == == == == == = = = = = = = = = =
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
== == == == == == = = = = = = = = = =
0  0  1  1  0  0  0 0 n n n n n n n n
== == == == == == = = = = = = = = = =

The synchronize instruction generates a synchronization event on the SYNC output stream. This can be used to monitor the progress of the command stream. The synchronize instruction is also used by the :doc:`SPI Engine Interconnect </wiki-migration/resources/fpga/peripherals/spi_engine/interconnect>` module to identify the end of a transaction and re-start the arbitration process.

==== ===========
Name Description
==== ===========
n    id
==== ===========

Sleep Instruction
~~~~~~~~~~~~~~~~~

== == == == == == = = = = = = = = = =
15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
== == == == == == = = = = = = = = = =
0  0  1  1  0  0  0 1 t t t t t t t t
== == == == == == = = = = = = = = = =

The sleep instruction stops the execution of the command stream for the specified amount of time. The time is based on the external clock frequency the configuration value of the prescaler register and the time parameter of the instruction. sleep_time = (t + 1) \* ((div + 1) \* 2) / f_clk.

==== ===========
Name Description
==== ===========
t    Time
==== ===========

Configuration Registers
-----------------------

The SPI Engine execution module has a set of 8-bit configuration registers which can be used to dynamically modify the behavior of the module at runtime.

SPI Configuration Register
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SPI configuration register configures various aspects of the low-level SPI bus behavior.

+-------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bits  | Name       | Description                                                                                                                                                                                             |
+=======+============+=========================================================================================================================================================================================================+
| [7:3] | reserved   | Must always be 0.                                                                                                                                                                                       |
+-------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [2]   | three_wire | Configures the output of the three_wire pin.                                                                                                                                                            |
+-------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [1]   | CPOL       | Configures the polarity of the SCLK signal. When 0, the idle state of the SCLK signal is low. When 1, the idle state of the SCLK signal is high.                                                        |
+-------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [0]   | CPHA       | Configures the phase of the SCLK signal. When 0, data is updated on the leading edge and sampled on the trailing edge. When 1, data is is sampled on the leading edge and updated on the trailing edge. |
+-------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Prescaler Configuration Register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The prescaler configuration register configures the divider that is applied to the module clock when generating the SCLK signal and other internal control signals used by the sleep and chip-select commands.

===== ==== =======================
Bits  Name Description
===== ==== =======================
[7:0] div  Prescaler clock divider
===== ==== =======================

The frequency of the SCLK signal is derived from the module clock frequency using the following formula: f_sclk = f_clk / ((div + 1) \* 2). If no prescaler block is present div is 0.

Dynamic Transfer Length Register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The dynamic transfer length register sets the length (in bits) of a transfer. By default, the transfer length is equal to the DATA_WIDTH of the execution module. If required the user can reduce this length by setting this register. A general rule of thumb is to set the DATA_WIDTH parameter to the largest transfer length supported by the target device.

===== ==== =======================
Bits  Name Description
===== ==== =======================
[7:0] div  Dynamic transfer length
===== ==== =======================

More Information
----------------

-  `SPI Engine Framework <https://wiki.analog.com/.>`__
