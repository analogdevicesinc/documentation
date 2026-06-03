.. collection:: Pulsar ADC
   :subtitle: Evaluating 14-/16-/18-Bit ADCs from the 8/10 LEAD PulSAR Family
   :image: images/10_lead_pulsar_revc.jpg
   :label: eval user-guide

   documentation:
     - User guide <.>

   hdl:
     - HDL Project (pulsar_adc) <projects/pulsar_adc>

   no-OS:
     - no-OS driver (pulsar_adc) <drivers/adc/pulsar_adc>

.. _pulsar-adc:

Pulsar ADC
===============================================================================

Evaluating 14-/16-/18-Bit ADCs from the 8/10 LEAD PulSAR® Family

Overview
-------------------------------------------------------------------------------

Full-featured evaluation board for 8/10 lead PulSAR® ADCs. Versatile analog
signal conditioning circuitry. On-board reference, reference buffers and ADC
Drivers. PC software for control and data analysis of time and frequency domain.

These low power ADCs offer very high performance of up to 20 bits with
throughputs ranging from 100 kSPS to 2 MSPS. The evaluation boards are
designed to demonstrate the ADC's performance and to provide an easy to
understand interface for a variety of system applications. A full description
of these products is available in their respective data sheets and should be
consulted when utilizing the evaluation boards. On-board components include a
high precision buffered band gap 5.0V reference (:adi:`ADR435`), reference
buffers (:adi:`AD8032`), a signal conditioning circuit with two op-amps
(:adi:`ADA4841-1`) and regulators to derive necessary voltage levels on board
(:adi:`ADP3334`, :adi:`ADP3303`). SMB connectors are provided for the low
noise analog signal source.

Features:

- Full-featured evaluation board for 8/10 lead PulSAR® ADCs
- Versatile analog signal conditioning circuitry
- On-board reference, reference buffers and ADC Drivers
- PC software for control and data analysis of time and frequency domain
- Compatible with FPGA carriers via FMC and PMOD connectors

Evaluation Boards:

- :adi:`EVAL-AD400x-FMCZ` (FMC connector variant)
- :adi:`EVAL-ADAQ40xx` (PMOD connector variant)

Supported Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**FMC connector variant (EVAL-AD400x-FMCZ) — ZedBoard carrier:**

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Part Name
     - Resolution
     - Description
   * - :adi:`AD4000`
     - 16-bit
     - 2 MSPS/1 MSPS/500 kSPS, Precision, Pseudo Differential, SAR ADCs
   * - :adi:`AD4001`
     - 16-bit
     - 2 MSPS/1 MSPS, Precision, Differential SAR ADCs
   * - :adi:`AD4002`
     - 18-bit
     - 2 MSPS/1 MSPS/500 kSPS, Precision, Pseudo Differential, SAR ADCs
   * - :adi:`AD4003`
     - 18-bit
     - 2 MSPS/1 MSPS/500 kSPS, Easy Drive, Differential SAR ADCs
   * - :adi:`AD4004`
     - 16-bit
     - 2 MSPS/1 MSPS/500 kSPS, Precision, Pseudo Differential, SAR ADCs
   * - :adi:`AD4005`
     - 16-bit
     - 2 MSPS/1 MSPS, Precision, Differential SAR ADCs
   * - :adi:`AD4006`
     - 18-bit
     - 2 MSPS/1 MSPS/500 kSPS, Precision, Pseudo Differential, SAR ADCs
   * - :adi:`AD4007`
     - 18-bit
     - 2 MSPS/1 MSPS/500 kSPS, Easy Drive, Differential SAR ADCs
   * - :adi:`AD4008`
     - 16-bit
     - 2 MSPS/1 MSPS/500 kSPS, Precision, Pseudo Differential, SAR ADCs
   * - :adi:`AD4010`
     - 18-bit
     - 2 MSPS/1 MSPS/500 kSPS, Precision, Pseudo Differential, SAR ADCs
   * - :adi:`AD4011`
     - 18-bit
     - 2 MSPS/1 MSPS/500 kSPS, Easy Drive, Differential SAR ADCs
   * - :adi:`AD4020`
     - 20-bit
     - 1.8 MSPS/1 MSPS/500 kSPS, Easy Drive, Differential SAR ADCs
   * - :adi:`AD4021`
     - 20-bit
     - 1.8 MSPS/1 MSPS/500 kSPS, Easy Drive, Differential SAR ADCs
   * - :adi:`ADAQ4003`
     - 18-bit
     - 2 MSPS, Precision DAQ, Differential SAR ADCs

**PMOD connector variant (EVAL-AD7xxx) — CoraZ7S carrier:**

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Part Name
     - Resolution
     - Description
   * - :adi:`AD7685`
     - 16-bit
     - 250 kSPS PulSAR ADC in MSOP/QFN
   * - :adi:`AD7686`
     - 16-bit
     - 500 kSPS PulSAR A/D Converter in MSOP/QFN
   * - :adi:`AD7687`
     - 16-bit
     - 1.5 LSB INL, 250 kSPS PulSAR Differential ADC in MSOP/QFN
   * - :adi:`AD7688`
     - 16-bit
     - 500 kSPS Differential PulSAR A/D Converter in µSOIC/QFN
   * - :adi:`AD7689`
     - 16-bit
     - 8-Channel, 250 kSPS PulSAR ADC
   * - :adi:`AD7690`
     - 18-bit
     - 1.5 LSB INL, 400 kSPS PulSAR Differential ADC in MSOP/QFN
   * - :adi:`AD7691`
     - 18-bit
     - 1.5 LSB INL, 250 kSPS PulSAR Differential ADC in MSOP/QFN
   * - :adi:`AD7693`
     - 16-bit
     - ±0.5 LSB, 500 kSPS PulSAR Differential A/D Converter in MSOP/QFN
   * - :adi:`AD7915`
     - 16-bit
     - 250 kSPS PulSAR Differential ADC in MSOP/LFCSP
   * - :adi:`AD7916`
     - 16-bit
     - 500 kSPS PulSAR Differential ADC in MSOP/LFCSP
   * - :adi:`AD7942`
     - 14-bit
     - 250 kSPS PulSAR, Pseudo Differential ADC in MSOP/LFCSP
   * - :adi:`AD7946`
     - 14-bit
     - 500 kSPS PulSAR ADC in MSOP
   * - :adi:`AD7980`
     - 16-bit
     - 1 MSPS, PulSAR ADC in MSOP/LFCSP
   * - :adi:`AD7982`
     - 18-bit
     - 1 MSPS PulSAR Differential ADC in MSOP/LFCSP
   * - :adi:`AD7983`
     - 16-bit
     - 1.33 MSPS PulSAR ADC in MSOP/LFCSP
   * - :adi:`AD7984`
     - 18-bit
     - 1.33 MSPS PulSAR Differential ADC in MSOP/LFCSP
   * - :adi:`AD7988-1`
     - 16-bit
     - Lower Power PulSAR ADCs in MSOP/LFCSP
   * - :adi:`AD7988-5`
     - 16-bit
     - Lower Power PulSAR ADCs in MSOP/LFCSP

.. figure:: images/10_lead_pulsar_revc.jpg
   :align: center
   :width: 400

   10 Lead PulSAR ADC REV C evaluation board

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <pulsar-adc prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <pulsar-adc quickstart>`:

      #. Using the :ref:`ZedBoard / Zynq-7000 SoC
         <pulsar-adc quickstart zedboard>`
      #. Using the :ref:`CoraZ7-07S / Zynq-7000 SoC
         <pulsar-adc quickstart coraz7s>`

   #. Configure an SD Card with
      :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`IIO Oscilloscope <iio-oscilloscope>`

#. Design with the PulSAR ADC

   #. :ref:`pulsar-adc block-diagram`

      #. :adi:`EVAL-AD400x-FMCZ Product Page <EVAL-AD400x-FMCZ>`
      #. :adi:`EVAL-ADAQ40xx Product Page <EVAL-ADAQ40xx>`

   #. Design a custom PulSAR ADC based platform

      #. HDL software

         #. :external+hdl:ref:`PulSAR ADC HDL Reference Design <pulsar_adc>`
            which you must use in your FPGA.

      #. Linux software

         #. :git-linux:`PulSAR ADC Linux driver (ad_pulsar.c) <drivers/iio/adc/ad_pulsar.c>`
         #. :git-linux:`AD400x Linux driver (ad4000.c) <drivers/iio/adc/ad4000.c>`
         #. :git-linux:`PulSAR ADC / CoraZ7S Linux device tree <arch/arm/boot/dts/xilinx/zynq-coraz7s-pulsar.dtsi>`
         #. :git-linux:`AD400x / ZedBoard Linux device tree <arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad4020.dts>`

      #. No-OS software

         #. :git-no-os:`PulSAR ADC No-OS driver <drivers/adc/pulsar_adc>`
         #. :git-no-os:`PulSAR ADC No-OS project <projects/pulsar-adc>`

      #. More information

         #. :external+hdl:ref:`spi_engine`

#. :ref:`Help and Support <help-and-support>`

.. _pulsar-adc block-diagram:

Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/10_lead_pulsar_revc.jpg
   :align: center
   :width: 800

.. toctree::
   :hidden:
   :glob:

   user-guide
   eval-ad7944-ad7985-ad7986
   pulsar-adc-pmods
   prerequisites
   quickstart/index

Additional Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`ADR435 Product Page <ADR435>`
- :adi:`AD8032 Product Page <AD8032>`
- :adi:`ADA4841-1 Product Page <ADA4841-1>`
- :adi:`ADP3334 Product Page <ADP3334>`
- :adi:`ADP3303 Product Page <ADP3303>`
- :adi:`EVAL-AD400x-FMCZ Product Page <EVAL-AD400x-FMCZ>`
- :adi:`EVAL-ADAQ40xx Product Page <EVAL-ADAQ40xx>`
- :external+hdl:ref:`HDL Project Documentation <pulsar_adc>`

Software Projects and Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`PulSAR ADC + ZedBoard (FMC) <pulsar-adc quickstart zedboard>`
- :ref:`PulSAR ADC + CoraZ7S (PMOD) <pulsar-adc quickstart coraz7s>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
