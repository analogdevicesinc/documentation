.. _dc2677a user-guide:

User guide
===============================================================================

The complete user guide for the evaluation board can be found at :adi:`DEMO
MANUAL DC2677A (UG-1387)
<media/en/technical-documentation/user-guides/DC2677A_UG-1387.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`DC2677A` connects to the FPGA carrier via the HSMC (High-Speed
Mezzanine Connector). It is compatible with the Altera Cyclone V SoCkit and
other Altera FPGA evaluation boards supporting 3.3V CMOS I/O.

On the Cyclone V SoCkit, configure the carrier jumpers and switches as described
in the :ref:`dc2677a quickstart c5soc` guide before connecting the board.

The interface mode (CMOS or LVDS) and the LTC235x device variant are selected at
HDL build time. Refer to :external+hdl:ref:`dc2677a` for supported build
parameters.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`DC2677A` receives power through the HSMC connector from the FPGA
carrier board. No separate external power supply is required for the evaluation
board itself.

The HSMC VCCIO voltage must be set to **3.3V** (JP2 on the Cyclone V SoCkit) to
match the board's CMOS I/O levels.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`LTC2358-18` on the :adi:`DC2677A` provides eight input channels with
SoftSpan programmable input ranges. Each channel can be independently configured
for unipolar or bipolar operation.

Connect a low-noise signal source to the screw terminal inputs. The input
circuitry incorporates up to 400V of continuous overvoltage protection,
supported by the on-board :adi:`ADA4522-2` zero-drift operational amplifier and
:adi:`LT6658` dual-output reference.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files (schematics, PCB layout, and BOM) are available from the product
page:

- :adi:`DC2677A`

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported through the :ref:`libiio` library, which is
cross-platform (Windows, Linux, Mac) with bindings for C, C#, Python, MATLAB,
and others.
