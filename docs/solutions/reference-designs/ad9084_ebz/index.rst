.. _ad9094:

AD9084-FMCA-EBZ (Apollo)
========================

16-bit, 28 GSPS, RF DAC core, and 12-bit, 20 GSPS RF ADC
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Overview
--------

.. image:: ad9084_ebz.png
   :align: right
   :width: 600px

The Apollo mixed signal front-end (MxFE®) is a highly integrated device with a
16-bit, 28 GSPS maximum sample rate, RF digital-to-analog converter (DAC) core,
and 12-bit, 20 GSPS maximum sample rate, RF analog-to-digital converter (ADC)
core. The AD9084 supports four transmit channels and four receive channels. The
AD9084 is well suited for applications requiring both wideband ADCs and DACs to
process signal(s) having wide instantaneous bandwidth. The device features a 48
lane, 32.5 Gbps JESD204C or 20 Gbps JESD204B data transceiver port, an on-chip
clock multiplier, and a digital signal processing (DSP) capability targeted at
either wideband or multiband, direct to RF applications. The AD9084 also
features a bypass mode that allows the full bandwidth capability of the ADC
and/or DAC cores to bypass the DSP data-paths. The device also features low
latency loopback and frequency hopping modes targeted at phased array radar
systems and electronic warfare applications.

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it should be.

#. Use the board to better understand the AD9084

   #. :ref:`What you need to get started <ad9084_ebz prerequisites>`
   #. :ref:`Quick Start Guides <ad9084_ebz quickstart>`

      #. :external+adi-kuiper-gen:doc:`Configure a SD Card <hardware-configuration>`
      #. :external+adi-kuiper-gen:doc:`Update the SD Card <repositories>`
      #. :ref:`AD9084 (Apollo) Profile Generator <ad9084 profile-generator>`
      #. :ref:`Running a new JESD mode on hardware <ad9084_ebz quickstart new_usecase>`

   #. Linux Applications

      #. :ref:`IIO Oscilloscope <ad9084 iio-oscilloscope>` with:

         - :ref:`AD9084 Plugin <ad9084 iio-oscilloscope-plugin>`

      #. :dokuwiki:`FRU EEPROM Utility <resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`

#. Design with the AD9084

   #. :ref:`ad9084 block-diagram`

      #. :adi:`AD9084 Product page <AD9084>`
      #. `Full Datasheet and chip design package <TODO>`__

   #. Design a custom AD9084 based platform

      #. Linux software

         .. #. `AD9084 Linux Device Driver <TODO>`__

            .. #. `AD9084 Device Driver Customization <TODO>`__

         #. :dokuwiki:`JESD204 (FSM) Interface Linux Kernel Framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         #. :dokuwiki:`AXI-DMAC DMA Controller Linux Driver <resources/tools-software/linux-drivers/axi-dmac>`
         #. :dokuwiki:`JESD204B Transmit Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B Receive Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            #. :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`

         #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      .. #. :dokuwiki:`HDL Reference Design <resources/eval/user-guides/ad9084/reference_hdl>` which you must use in your FPGA.

.. #. `Help and Support <TODO>`__

Pre-requisites and quickstart
-----------------------------

.. toctree::
   :caption: The prerequisites and quickstart guides are provided at:
   :titlesonly:
   :maxdepth: 1

   prerequisites
   quickstart/index

.. _ad9084 block-diagram:

Functional Block Diagram
------------------------

.. image:: apollo_block_diagram.png
   :width: 600px

Warning
-------

.. esd-warning::