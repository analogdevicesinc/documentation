.. _eval-cn0579-ardz prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

DE10-Nano
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-CN0579-ARDZ`
- `DE10-Nano FPGA Board
  <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`__
- 5V/2A wall power supply with barrel jack
- Mini USB to USB Type A cable
- Class 10 16 GB microSD card
- Ethernet cable
- IEPE-compatible sensor

Cora Z7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-CN0579-ARDZ`
- `CoraZ7-07s FPGA Board
  <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development>`__
- Class 10 16 GB microSD card
- Ethernet cable
- Micro USB to USB Type A cable
- IEPE-compatible sensor

Software prerequisites
-------------------------------------------------------------------------------

Not all of the software listed below is strictly required - what you need
depends on how you intend to use the board. At a minimum, you need :ref:`kuiper`
running on the carrier board to bring up the IIO devices. For data capture,
:ref:`iio-oscilloscope` is the most common choice and covers most evaluation use
cases. :external+scopy:doc:`Scopy <index>` v2.0 or later and :ref:`pyadi-iio`
are useful alternatives depending on your workflow. A signal generator is
required to provide an input when evaluating the analog signal chain.

- :ref:`kuiper`
- :ref:`iio-oscilloscope`
- :external+scopy:doc:`Scopy <index>` v2.0 or later
- :ref:`pyadi-iio`
