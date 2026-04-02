.. _eval_ad5758 quickstart:

Quickstart
===============================================================================

The Quick Start Guide provides a simple step by step instruction on how to do
an initial system setup for the :adi:`EVAL-AD5758SDZ` board on the ZedBoard
FPGA development board. It will discuss how to program the bitstream and run a
no-OS program.

.. toctree::

   ZedBoard <zed>

.. _eval_ad5758 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD5758SDZ` is an SDP-format board; it connects to an FPGA
carrier's FMC LPC connector through the `EVAL-SDP-CK1Z
<https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-SDP-CK1Z.html>`__
(FMC-I-SDP) interposer.

The carrier we support is:

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  on the FMC LPC connector (via the EVAL-SDP-CK1Z interposer)

Supported Environments
-------------------------------------------------------------------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - No
     - Yes

Hardware Setup
-------------------------------------------------------------------------------

The :adi:`EVAL-AD5758SDZ` board connects to the ZedBoard FMC LPC connector
through the EVAL-SDP-CK1Z (FMC-I-SDP) interposer. The carrier setup requires
power, UART (115200 baud), and a USB connection for no-OS development.

A typical setup is shown below.

ZedBoard + EVAL-AD5758SDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-AD5758SDZ connects to the ZedBoard via the FMC LPC (Low Pin Count)
connector using the EVAL-SDP-CK1Z (FMC-I-SDP) interposer board. The interposer
provides the physical and electrical connection between the SDP-format AD5758
board and the ZedBoard's FMC connector.

.. image:: ../images/eval-ad5758+zedboard.jpeg
   :align: center
   :width: 600

Next Steps
-------------------------------------------------------------------------------

Proceed to the :ref:`ZedBoard quickstart guide <eval_ad5758 quickstart zed>`
for detailed build and programming instructions.
