.. _ad7405 user-guide:

User guide
===============================================================================

The complete user guides of the evaluation boards can be found at:

- `EVAL-AD7405 User Guide (UG-690) <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad7405fmcz_ug-690.pdf>`_

Hardware guide
-------------------------------------------------------------------------------
Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD7405` board connects to the :adi:`EVAL-SDP-CH1Z`
(SDP-H1) FPGA carrier board through the FMCZ connector (J9). The
EVAL-SDP-CH1Z provides the necessary power and control signals to
the evaluation board, allowing users to evaluate the performance of
the AD7405 isolated ADC.

Refer to the :ref:`ad7405 quickstart sdp_h1` quick start guide for the exact jumper
and switch settings corresponding to the selected boot mode.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This evaluation board is designed to be supplied via the EVAL-SDP-CH1Z.
The EVAL-SDP-CH1Z generates 12 V and 3.3 V supply rails. The 12 V supply
is connected to the on-board 5 V linear regulator that supplies the
:adi:`ADuM6000` with power. The ADuM6000 then generates an isolated 5 V supply
to power the VDD1 rail of the AD7405. The 3.3 V supply rail from the
EVAL-SDP-CH1Z is used to supply the VDD2 rail of the AD7405.

If VDD1 is supplied externally, connect an external power supply in the
range of 24 V ± 5% to the HIGH_V connector (J4). As an alternative, VDD1
may be supplied with an external 5 V ± 10% supply connected to the J3
connector.

The VDD2 supply may also be provided externally by connecting a power
supply in the range of 3 V to 5.5 V to the J5 connector.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-AD7405FMCZ evaluation board provides differential analog
input connections for the AD7405 through on-board input connectors.
The VIN+ and VIN– signals are routed directly to the ADC input pins.

Link options are provided to short either VIN+ or VIN– to ground for
setup and diagnostic purposes. These links must be removed when an
external input signal is applied to the corresponding input.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files (schematics, PCB layout, and BOM) are available from the
respective product pages:

- :adi:`EVAL-AD7405`

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported by the :adi:`EVAL-SDP-CH1Z` (SDP‑H1)
FPGA carrier board, which provides a USB interface for device control and
data acquisition. When used with the SDP‑H1 platform, the evaluation
board allows configuration, data capture, and analysis of the AD7405
isolated ADC through the associated PC-based evaluation software. The
EVAL‑SDP‑CH1Z software is available for download from the product page or
from the installer CD included with the evaluation kit. 

For a step-by-step walkthrough of connecting and using these tools with the
:adi:`EVAL-AD7405` on the SDP-H1, see the
:ref:`ad7405 quickstart sdp_h1` guide.