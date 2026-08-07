.. _pulsar-lvds-adc quickstart:

Quickstart
==========

The Quick start guides provide simple step by step instructions on how to
do an initial system setup for the PulSAR LVDS ADC evaluation boards
(:adi:`EVAL-AD7625`, :adi:`EVAL-AD7626`, :adi:`EVAL-AD7960`,
:adi:`EVAL-AD7961`) on various FPGA development boards. In these guides, we
will discuss how to program the bitstream, run a no-OS program or boot a Linux
distribution.

.. toctree::

   Zedboard <zed>

.. _pulsar-lvds-adc carriers:

Supported carriers
------------------

The PulSAR LVDS ADC evaluation boards are, by definition, "FPGA
mezzanine cards" (FMC); that means they need a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD7625/AD7626/AD7960/AD7961
   - - `ZedBoard
       <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported Environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - `ZedBoard
       <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes

Hardware Setup
--------------

The evaluation board connects to the FMC LPC connector of the carrier board.
The carrier setup requires power, UART (115200), ethernet (Linux), HDMI
(if available) and/or JTAG (no-OS) connections.

A few typical setups are shown below.

ZedBoard + PulSAR LVDS ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~

..
   To be added: photo of the PulSAR LVDS ADC evaluation board connected to
   the ZedBoard via FMC LPC connector (hardware setup photo)
   .. figure:: ../images/pulsar_lvds_adc_zed_setup.jpg
      :align: center
      :width: 500

      ZedBoard + PulSAR LVDS ADC hardware setup
