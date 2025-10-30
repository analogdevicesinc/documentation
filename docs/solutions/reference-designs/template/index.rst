.. _template:

EVALUATION BOARD
===============================================================================

.. Add a picture here of the chip

.. image:: ../images/ad9081.webp
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

.. Describe in max 10 rows the main features and applications of the evaluation board. Can be taken from analog.com

The :adi:`EVALUATION BOARD`, is a FMC radio card for the
:adi:`CHIP`, highly integrated, radio frequency (RF)
agile transceivers offering four independently controlled transmitters,
(...).

Features:

- feature 1
- feature 2

Applications:

- application 1
- application 2

.. Add a picture here of the evaluation board
.. image:: ../images/eval_ad9081.png
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`CHIP1` / :adi:`CHIP2`, we recommend to use
the :adi:`EVALUATION BOARD` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <template prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <template quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale MP SoC <template quickstart zynqmp>`
      #. Using the :ref:`VCK190/Versal <template quickstart versal>`

   #. Configure an SD Card with :external+adi-kuiper-gen:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the CHIP1/CHIP2

   - :ref:`template block-diagram`

     - :adi:`CHIP1 product page <CHIP1>`
     - :adi:`CHIP2 product page <CHIP2>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing a custom CHIP1/CHIP2-based platform software

     #. For Linux software:

        #. About the device driver:

           - :dokuwiki:`JESD204B Transmit Linux driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
           - :dokuwiki:`JESD204B Receive Linux driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
           - :dokuwiki:`JESD204B/C AXI_ADXCVR High-speed transceivers Linux driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
           - :dokuwiki:`AXI ADC HDL Linux driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
           - :dokuwiki:`AXI DAC HDL Linux driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
           - :dokuwiki:`AXI-DMAC DMA Controller Linux driver <resources/tools-software/linux-drivers/axi-dmac>`
           - :dokuwiki:`CHIP1/CHIP2 Linux device driver <resources/tools-software/linux-drivers/iio-transceiver/adrv9025>`

        #. About the device tree:

           - :dokuwiki:`Customizing the device tree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :dokuwiki:`JESD204 (FSM) interface Linux Kernel framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
           - :dokuwiki:`JESD204 status utility <resources/tools-software/linux-software/jesd_status>`
           - :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`
           - :external+hdl:ref:`jesd204`

     #. :external+hdl:ref:`HDL reference design <template_project>` which you must use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _template block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. Add here the block diagram of the chip
.. image:: ../images/ad9081_block_diagram.png
   :align: center
   :width: 800

.. If it applies, uncomment it and remove the indentation
  Videos
  -------------------------------------------------------------------------------

.. If it applies, uncomment it and remove the indentation
  Software Defined Radio using the Linux IIO Framework
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. If it applies, uncomment it and remove the indentation
  .. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI articles
-------------------------------------------------------------------------------

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

.. If it applies, uncomment it and remove the indentation
  MathWorks webinars
  -------------------------------------------------------------------------------

.. If it applies, uncomment it and remove the indentation
  #. :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
  #. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

..
  Here you should put other articles or pages that are related to the chips,
  and you think they're helpful to understand the overall system.
  Additional information
  -------------------------------------------------------------------------------

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
