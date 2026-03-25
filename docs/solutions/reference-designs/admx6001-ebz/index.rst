.. imported from: https://wiki.analog.com/resources/eval/user-guides/admx/admx6001resources/eval/user-guides/admx/admx6001_analog_devices_wiki

ADMX6001-EBZ
============

DC-Coupled Single-Channel 10 GSPS Digitizer Reference Design.

Overview
--------

The :adi:`EVAL-ADMX6001-EBZ` is a reference design of a DC-coupled
single-channel 10 GSPS digitizer that combines two ADC paths for comprehensive
signal capture across a broad frequency range from DC to 5 GHz.

The dual-path architecture integrates:

- A high-speed 12-bit ADC (:adi:`AD9213`) operating at 10 GSPS
- A precision 20-bit ADC (:adi:`AD4080`) for low-noise digitization

This design is ideal for applications such as time-of-flight mass spectrometry
and distributed fiber optic sensing.

Supported Devices
-----------------

- :adi:`AD9213` -- high-speed 12-bit, 10 GSPS ADC
- :adi:`AD4080` -- 20-bit precision ADC

Evaluation Board
----------------

- :adi:`EVAL-ADMX6001-EBZ`

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Evaluation Board
     - Carrier
     - FMC Slot
   * - :adi:`EVAL-ADMX6001-EBZ`
     - `VCU118 <https://www.xilinx.com/products/boards-and-kits/vcu118.html>`__
     - FMC+

HDL Reference Design
--------------------

The HDL reference design implements a processor-based embedded system
(MicroBlaze) with:

- High-speed JESD204B receive chain for ADC data transport
- Custom AXI AD408x interface for the precision data path
- FPGA block RAM buffering via ``util_adcfifo``
- DDR memory integration for sample storage
- AXI-Lite programmable cores for flexible system configuration

JESD204B Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::

   * - Parameter
     - Value
   * - L (lanes)
     - 16
   * - M (converters)
     - 1
   * - F (octets per frame)
     - 2
   * - S (samples per frame)
     - 16
   * - NP (bits per sample)
     - 16
   * - Lane Rate
     - 12.5 Gbps
   * - Sample Rate
     - 10 GSPS
   * - Reference Clock
     - 625 MHz

The source code is available at
:git-hdl:`projects/admx6001_ebz`
and documented at
:external+hdl:ref:`admx6001_ebz`.

Help and Support
----------------

For questions and more information, please visit the
:ez:`EngineerZone Support Community <reference-designs>`.

.. esd-warning::
