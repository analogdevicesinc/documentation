EVAL-AD408x-FMCZ
================================================================================

.. image:: images/ad4080-chip-illustration.png
   :width: 250
   :align: right

The :adi:`EVAL-AD4080-FMC`, :adi:`EVAL-AD4083-FMC`, and :adi:`EVAL-AD4086-FMC`
are designed to demonstrate the performance of the :adi:`AD4080`, :adi:`AD4081`,
:adi:`AD4083`, :adi:`AD4084`, :adi:`AD4086`, and :adi:`AD4087` analog-to-digital
converters (ADCs) and provide access to a limited set of device configuration
features through the ACE Software environment. The :adi:`EVAL-AD4080-FMC`,
:adi:`EVAL-AD4083-FMC`, and :adi:`EVAL-AD4086-FMC` evaluation kits support the
following :adi:`AD4080`, :adi:`AD4083`, and :adi:`AD4086` features:

* Low voltage digital signaling (LVDS) data output interface.
* ADC configuration via serial peripheral interface (SPI).
* Internal or external generation of 1.1V regulated supply rails.
* Sampling rate capability between 1.25MSPS and up to 40MSPS, depending on the
  specific ADC.

The :adi:`AD4080`, :adi:`AD4083`, and :adi:`AD4086` that are physically mounted
on the boards can be evaluated with any sampling frequency range from 1.25 MHz
to 40 MHz. However, performance of the :adi:`AD4081`, :adi:`AD4084`, and
:adi:`AD4087` can also be estimated using this board by setting the sampling
frequency to 20MHz. Note that, the captured results for :adi:`AD4080`,
:adi:`AD4083`, and :adi:`AD4086` running at the reduced sample rate should only
be taken as indications of the signal-to-noise ratio (SNR) rather than the
actual measurement; nevertheless, measured SNR for the :adi:`AD4081`,
:adi:`AD4084`, and :adi:`AD4087` will not be worse.

Features:

.. flex::

   * :adi:`AD4080`

     - High performance

       - Throughput: 40 MSPS, 46.25 ns conversion latency
       - INL: ±4 ppm (typical), ±8 ppm (maximum)
       - SNR/THD

         - 93.6 dB (typical)/-110 dB (typical) at fIN = 1 kHz
         - 93.5 dB (typical)/-104 dB (typical) at fIN = 1 MHz

       - Noise spectral density: -167.6 dBFS/Hz
       - 20-bit resolution, no missing codes

     - Low power

       - 79.3 mW typical at 40 MSPS with -0.5 dBFS sine-wave input

     - Configurable data interface

       - Single lane, DDR, serial LVDS, 800 Mbps per lane
       - Dual lane, DDR, serial LVDS, 400 Mbps per lane
       - Single/quad lane SPI data interface

   * :adi:`AD4081`

     - High performance

       - Throughput: 20 MSPS, 77.50 ns conversion latency
       - INL: ±4 ppm (typical), ±8 ppm (maximum)
       - SNR/THD

         - 94 dB (typical)/-117.3 dB (typical) at fIN = 1 kHz
         - 93.7 dB (typical)/-103.7 dB (typical) at fIN = 1 MHz

       - Noise spectral density: -164.6 dBFS/Hz
       - 20-bit resolution, no missing codes

     - Low power

       - 68.6 mW typical at 20 MSPS with -0.5 dBFS sine-wave input

     - Configurable data interface

       - Single lane, DDR, serial LVDS, 400 Mbps per lane
       - Dual lane, DDR, serial LVDS, 200 Mbps per lane
       - Single/quad lane SPI data interface

   * :adi:`AD4083`

     - High performance

       - Throughput: 40 MSPS, 48.43 ns conversion latency
       - INL: ±8 ppm (typical), ±12 ppm (maximum)
       - SNR/THD

         - 92.2 dB (typical)/-111 dB (typical) at fIN = 1 kHz
         - 92 dB (typical)/-103.4 dB (typical) at fIN = 1 MHz

       - Noise spectral density: -165.9 dBFS/Hz
       - 16-bit resolution, no missing codes

     - Low power

       - 70.2 mW typical at 40 MSPS with -0.5 dBFS sine-wave input

     - Configurable data interface

       - Single lane, DDR, serial LVDS, 640 Mbps per lane
       - Dual lane, DDR, serial LVDS, 320 Mbps per lane
       - Single/quad lane SPI data interface

   * :adi:`AD4084`

     - High performance

       - Throughput: 20 MSPS, 78.13 ns conversion latency
       - INL: ±6 ppm (typical), ±10 ppm (maximum)
       - SNR/THD

         - 92.6 dB (typical)/-115.2 dB (typical) at fIN = 1 kHz
         - 92.4 dB (typical)/-103.5 dB (typical) at fIN = 1 MHz

       - Noise spectral density: -163 dBFS/Hz
       - 16-bit resolution, no missing codes

     - Low power

       - 66.8 mW typical at 20 MSPS with -0.5 dBFS sine-wave input

     - Configurable data interface

       - Single lane, DDR, serial LVDS, 320 Mbps per lane
       - Dual lane, DDR, serial LVDS, 160 Mbps per lane
       - Single/quad lane SPI data interface

   * :adi:`AD4086`

     - High performance

       - Throughput: 40 MSPS, 48.21 ns conversion latency
       - INL: ±12 ppm (typical), ±16 ppm (maximum)
       - SNR/THD

         - 85.34 dB (typical)/-110.4 dB (typical) at fIN = 1 kHz
         - 85.27 dB (typical)/-101.3 dB (typical) at fIN = 1 MHz

       - Noise spectral density: -158.9 dBFS/Hz
       - 14-bit resolution, no missing codes

     - Low power

       - 85 mW typical at 40 MSPS with -0.5 dBFS sine-wave input

     - Configurable data interface

       - Single lane, DDR, serial LVDS, 560 Mbps per lane
       - Dual lane, DDR, serial LVDS, 280 Mbps per lane
       - Single/quad lane SPI data interface

   * :adi:`AD4087`

     - High performance

       - Throughput: 20 MSPS, 82.14 ns conversion latency
       - INL: ±12 ppm (typical), ±16 ppm (maximum)
       - SNR/THD

         - 85.39 dB (typical)/-114.8 dB (typical) at fIN = 1 kHz
         - 85.27 dB (typical)/-101.35 dB (typical) at fIN = 1 MHz

       - Noise spectral density: -158.5 dBFS/Hz
       - 14-bit resolution, no missing codes

     - Low power

       - 68 mW typical at 20 MSPS with -0.5 dBFS sine-wave input

     - Configurable data interface

       - Single lane, DDR, serial LVDS, 280 Mbps per lane
       - Dual lane, DDR, serial LVDS, 140 Mbps per lane
       - Single/quad lane SPI data interface

Applications:

* Digital imaging
* Cell analysis
* Spectroscopy
* Automated test equipment
* High speed data acquisition
* Digital control loops, hardware in the loop
* Power quality analysis
* Source measurement units
* Electron and x-ray microscopy
* Radar level measurement
* Nondestructive test
* Predictive maintenance and structural health

.. figure:: images/ad408x-top-evaluation-board.png
   :width: 600

   EVAL-AD408x-FMCZ

Recommendations
--------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the **Help and Support** section at
the bottom of the page.

To better understand the :adi:`AD4080`, :adi:`AD4081`, :adi:`AD4083`,
:adi:`AD4084`, :adi:`AD4086`, and :adi:`AD4087`, we recommend using the
:adi:`EVAL-AD4080-FMC`, :adi:`EVAL-AD4083-FMC`, and :adi:`EVAL-AD4086-FMC`
evaluation boards.

Table of Contents
--------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 2

   prerequisites
   quickstart/index
   user_guide

Block Diagram
--------------------------------------------------------------------------------

.. figure:: images/ad4080-fbl.png
   :width: 800

   AD4080 Block Diagram

Additional Information
--------------------------------------------------------------------------------

Datasheets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD4080 <media/en/technical-documentation/data-sheets/ad4080.pdf>`
- :adi:`AD4081 <media/en/technical-documentation/data-sheets/ad4081.pdf>`
- :adi:`AD4083 <media/en/technical-documentation/data-sheets/ad4083.pdf>`
- :adi:`AD4084 <media/en/technical-documentation/data-sheets/ad4084.pdf>`
- :adi:`AD4086 <media/en/technical-documentation/data-sheets/ad4086.pdf>`
- :adi:`AD4087 <media/en/technical-documentation/data-sheets/ad4087.pdf>`

Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`iio-oscilloscope`
- :ref:`pyadi-iio`

Project Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+hdl:ref:`ad4080_fmc_evb`
- :git+hdl:`AD408x HDL repository <projects/ad4080_fmc_evb>`
- :git+pyadi-iio:`AD408x Pyadi-IIO example <examples/ad4080_example.py>`

Help and Support
--------------------------------------------------------------------------------

For additional questions or support, please visit the :ez:`/` forum.
