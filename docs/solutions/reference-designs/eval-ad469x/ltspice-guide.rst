.. _eval-ad469x-ltspice-guide:

LTspice AD469x model user guide
===============================================================================

Overview
-------------------------------------------------------------------------------

Analog Devices provides LTspice models for the AD469x family of
16-bit SAR ADCs. These models enable hardware-free prototyping of
multichannel precision measurement signal chains.

Supported models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Generic
     - Channels (device)
     - Sample rate
     - Channels (model)
   * - :adi:`AD4695 <en/products/ad4695.html>`
     - 16
     - 500 kSPS
     - 8
   * - :adi:`AD4696 <en/products/ad4696.html>`
     - 16
     - 1 MSPS
     - 8
   * - :adi:`AD4697 <en/products/ad4697.html>`
     - 8
     - 500 kSPS
     - 8
   * - :adi:`AD4698 <en/products/ad4698.html>`
     - 8
     - 1 MSPS
     - 8

.. note::

   The 16-channel models (AD4695, AD4696) implement only 8 analog
   input channels in simulation.

Model revision history
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Original release: June 22, 2022.

Features and capabilities
-------------------------------------------------------------------------------

The LTspice models support transient simulations that evaluate
analog front-end settling and performance by modeling:

- Charge kickback transient glitch magnitude
- Timing relative to CNV rising edges
- ADC acquisition timing relative to sampling rate
- Input transient behaviors per channel sequencer configuration

For detailed transient simulation instructions, see
:ref:`eval-ad469x-ltspice-transient-sims`.

Symbol and pin functions
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Pin
     - Function
   * - IN0 -- IN7
     - Eight analog input channels for conversion
   * - SLCT0 -- SLCT2
     - Bit select for channel selection
       (valid when SEQ_EN = 0)
   * - CH_OUT0 -- CH_OUT2
     - 3-bit channel indicator;
       0 V = logic LOW, 1 V = logic HIGH
   * - COMM
     - Common channel input emulating COM pin
   * - REF
     - Reference voltage determining full-scale range;
       VREF = REF - REFGND
   * - AVDD / LDO_IN
     - Connect to 5 V
   * - CNV
     - Convert start signal initiating channel conversion
   * - RESET
     - Active-high reset signal
       (pulse required at simulation start)
   * - REFGND
     - Reference ground (REF referenced to REFGND)
   * - VSAMPLE
     - Sampled output voltage

Parameters
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 60 20

   * - Parameter
     - Description
     - Default
   * - OSR
     - Oversampling ratio; determines multi-sampling
       per channel (transient) or input-referred noise
       (noise analysis)
     - 1
   * - SEQ_EN
     - Sequencer enable; determines active channels
     - 0
   * - CNV_FREQ_NOISE
     - Conversion frequency for noise analysis
       (set to 0 except for noise analysis)
     - 0
   * - CNV_CH_NOISE
     - Channel selected for AC/noise analysis
     - 0
   * - COM_OPT
     - Common input enable; references conversion to
       COMM instead of REFGND for pseudo-differential
       conversion
     - 0

Limitations
-------------------------------------------------------------------------------

The model has not been validated for:

- DC sweeps
- AC analysis
- DC transfer function
- DC operating point analyses
