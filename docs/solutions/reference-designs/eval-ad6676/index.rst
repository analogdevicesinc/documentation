.. _eval-ad6676 eval:

EVAL-AD6676
===============================================================================

Wideband IF Receiver Subsystem

.. TODO: No chip image currently available for the AD6676

Overview
-------------------------------------------------------------------------------

The :adi:`AD6676` is a highly integrated IF subsystem that can digitize radio
frequency (RF) bands up to 160 MHz in width centered on an intermediate
frequency (IF) of 70 MHz to 450 MHz. Unlike traditional Nyquist IF sampling
ADCs, the AD6676 relies on a tunable band-pass Σ-Δ ADC with a high
oversampling ratio to eliminate the need for band specific IF SAW filters and
gain stages, resulting in significant simplification of the wideband radio
receiver architecture. On-chip quadrature digital downconversion followed by
selectable decimation filters reduces the complex data rate to a manageable
rate between 62.5 MSPS to 266.7 MSPS. The 16-bit complex output data is
transferred to the host via a single or dual lane JESD204B interface
supporting line rates of up to 5.333 Gbps.

.. image:: Eval-AD6676.jpg
   :align: center
   :width: 500

Features:

- High instantaneous dynamic range

  - Noise figure (NF) as low as 13 dB
  - Noise spectral density (NSD) as low as −159 dBFS/Hz
  - IIP3 up to 36.9 dBm with spurious tones <−99 dBFS

- Tunable band-pass Σ-Δ analog-to-digital converter (ADC)

  - 20 MHz to 160 MHz signal bandwidth
  - 70 MHz to 450 MHz IF center frequency
  - Configurable input full-scale level of −2 dBm to −14 dBm
  - Gain flatness of 1 dB with under 0.5 dB out-of-band peaking
  - 2.0 GSPS to 3.2 GSPS ADC clock rate
  - 16-bit I/Q rate up to 266 MSPS

- On-chip digital signal processing

  - NCO and quadrature digital downconverter (QDDC)
  - Selectable decimation factor of 12, 16, 24, and 32

- Automatic gain control (AGC) support

  - On-chip attenuator with 27 dB span in 1 dB steps
  - Fast attenuator control via configurable AGC data port
  - Peak detection flags with programmable thresholds

- Single or dual lane, JESD204B capable
- Low power consumption: 1.20 W

  - 1.1 V and 2.5 V supply voltage
  - TDD power saving up to 60%

- 4.3 mm × 5.0 mm WLCSP

Applications:

- Wideband cellular infrastructure equipment and repeaters
- Point-to-point microwave equipment
- Instrumentation

  - Spectrum and communication analyzers

- Software defined radio

.. toctree::
   :hidden:

   prerequisites
   quickstart/index
   user-guide

Recommendation
-------------------------------------------------------------------------------

To better understand the :adi:`AD6676`, we recommend to use the
:adi:`EVAL-AD6676` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad6676 prerequisites`
   #. :ref:`eval-ad6676 user-guide`
   #. :ref:`eval-ad6676 quickstart`:

      #. Using the :ref:`ZC706 <ad6676-zc706>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Software Solutions

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`
      #. :ref:`libiio cli`
      #. :ref:`Python Interfaces <pyadi-iio>`
      #. :git-pyadi-iio:`AD6676 Python example <examples/ad6676.py>`

#. Design with the AD6676

   #. :ref:`ad6676 block-diagram`

      #. :adi:`AD6676 product page <AD6676>`
      #. :adi:`EVAL-AD6676 product page <EVAL-AD6676>`

   #. Resources for designing a custom AD6676-based platform software

     #. For Linux software:

        #. About the device driver:

           #. :external+linux:doc:`AXI ADC HDL Linux driver <drivers/iio-adc/axi-adc-hdl>`
           #. :external+linux:doc:`AXI-DMAC DMA Controller Linux driver <drivers/dma/axi-dmac>`
           #. :external+linux:doc:`AD6676 Linux device driver <drivers/iio-adc/ad6676>`

     #. For no-OS software:

        #. :external+no-OS:doc:`AD6676 no-OS Example Project <projects/adc/ad6676-ebz>`

     #. FPGA Resources:

        #. :external+hdl:ref:`HDL reference design <ad6676evb>` which you must use
           in your FPGA.
        #. :external+hdl:ref:`HDL User Guide <user_guide>`

.. _ad6676 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/AD6676_fbl.png
   :align: center
   :width: 800

Additional information
-------------------------------------------------------------------------------

Application notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and
   Evaluation*
#. :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs
   via SPI*

Design tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`VRMS / dBm / dBu / dBV Calculator <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/dbconvert.html>`
- :adi:`ADI RF Impedance Matching Tool <en/design-center/interactive-design-tools/rf-impedance-matching-calculator.html>`
- :adi:`ADIsimRF Software <en/design-center/adisimrf.html>`
- :adi:`ADI RF/IF Transceiver Products <en/rfif-components/rfif-transceivers/products/index.html>`

Help and support
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on the
:ez:`/` technical support community, but before that, please make
sure you read our documentation thoroughly.

Warning
-------------------------------------------------------------------------------

.. esd-warning::
