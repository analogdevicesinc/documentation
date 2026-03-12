.. _ad77681 user-guide:

User guide
===============================================================================

The complete user guides of the evaluation boards can be found at:

- :adi:`EV-AD7768-1FMCZ User Guide (UG-1260) <media/en/technical-documentation/user-guides/ev-ad7768-1fmcz-ug-1260.pdf>`
- :adi:`EV-ADAQ7768-1FMC1Z User Guide (UG-1906) <media/en/technical-documentation/user-guides/eval-adaq7768-1-ug-1906.pdf>`

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD7768-1` and :adi:`EVAL-ADAQ7768-1` boards connect to the FPGA
carrier via the FMC LPC connector.

On the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__,
configure the BOOT switches (JP7–JP11) and the MIO0 jumper (JP6) for the desired
boot mode, and set VADJ to **2.5 V** as required by the HDL project.
Refer to the :ref:`ad77681 quickstart zed` guide for the specific jumper positions
for SD card and JTAG boot modes.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both evaluation boards receive power through the FMC LPC connector from the
FPGA carrier board. No separate power supply is required for the evaluation
board itself.

The required VADJ for the FMC interface is **2.5 V**, as specified in the
carrier README of the :external+hdl:ref:`ad77681evb` HDL project.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To the SMB connectors or terminal blocks at **AIN1+** and **AIN−** on the
:adi:`EVAL-AD7768-1`, connect a low-noise differential signal source. The
absolute input range is 0 V to 4.096 V on each input, with the common-mode
voltage (VCM) defaulting to 2.5 V.

To the SMB connectors or terminal blocks at **IN+** and **IN−** on the
:adi:`EVAL-ADAQ7768-1`, connect a low-noise differential signal source.
The differential input range is programmable from ±0.197 V to ±12.603 V via
the on-board PGIA gain setting.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files (schematics, PCB layout, and BOM) are available from the
respective product pages:

- :adi:`EVAL-AD7768-1`
- :adi:`EVAL-ADAQ7768-1`

Software guide
-------------------------------------------------------------------------------

The evaluation boards are supported through the :ref:`libiio` library, which
is cross-platform (Windows, Linux, Mac) with bindings for C, C#, Python,
MATLAB, and others. Applications that interface via libiio include:

- :ref:`iio-oscilloscope` — graphical waveform and spectrum analyzer
- :external+scopy:doc:`Scopy <index>` v2.0 or later (requires the IIO plugin)
- :external+pyadi-iio:doc:`index` — Python interface

For a step-by-step walkthrough of connecting and using these tools with the
:adi:`EVAL-AD7768-1` / :adi:`EVAL-ADAQ7768-1` on the ZedBoard, see the
:ref:`ad77681 quickstart zed` guide.
