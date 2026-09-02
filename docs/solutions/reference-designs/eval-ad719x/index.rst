.. _ad719x_asdz:

EVAL-AD719x-ASDZ
================

Evaluation Boards for the AD719x Family of Ultralow Noise 24-Bit
Sigma-Delta ADCs.

Overview
--------

The :adi:`AD719x <ad7190>` family of ADCs are ultralow
noise, complete analog front ends for high precision measurement
applications. They incorporate a 24-bit sigma-delta (Σ-Δ) analog-to-digital
converter (ADC) with an on-chip low noise gain stage, enabling signals of
small amplitude to interface directly to the ADC.

The EVAL-AD719x-ASDZ evaluation boards provide a full-featured platform
for evaluating these devices. Each board includes PC control via the ACE
software in conjunction with the system demonstration platform
(EVAL-SDP-CB1Z/EVAL-SDP-CK1Z), as well as support for FPGA-based
carrier boards.

Features
--------

- Ultralow noise 24-bit sigma-delta ADC
- On-chip low noise programmable gain stage (gains from x1 to x128)
- 4.8 kHz output data rate
- On-chip digital filtering
- Internal clock option for compact solutions
- Automatic channel sequencer
- SPI-compatible serial interface
- PC software for control and data analysis (time and frequency domain)

Evaluation Boards
-----------------

.. list-table::
   :header-rows: 1

  - - Evaluation Board
    - Device
    - Data Sheet
  - - EVAL-AD7190ASDZ
    - :adi:`AD7190`
    - :adi:`Data Sheet <ad7190>`
  - - EVAL-AD7192ASDZ
    - :adi:`AD7192`
    - :adi:`Data Sheet <ad7192>`
  - - EVAL-AD7193ASDZ
    - :adi:`AD7193`
    - :adi:`Data Sheet <ad7193>`
  - - EVAL-AD7194ASDZ
    - :adi:`AD7194`
    - :adi:`Data Sheet <ad7194>`
  - - EVAL-AD7195ASDZ
    - :adi:`AD7195`
    - :adi:`Data Sheet <ad7195>`

User Guide
----------

.. toctree::
   :titlesonly:
   :glob:

   prerequisites
   */index
   AD719x IIO Application <ad719x_mbed_iio_application>

Help and Support
----------------

For questions and more information, please visit the :ez:`/`.
