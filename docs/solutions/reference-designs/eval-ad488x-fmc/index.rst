.. _ad488x:

EVAL-AD488X-FMC
===============================================================================

Evaluating the AD488x Family of Dual-Channel, Low Noise, High Speed SAR ADC

.. image:: images/ad4880_chip.png
   :align: left
   :width: 150

.. image:: images/ad4884_chip.png
   :align: left
   :width: 150

.. clear-content::

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD488X-FMC <eval-ad4884>` is an FMC evaluation board designed
to demonstrate the performance of the :adi:`AD4880` and :adi:`AD4884`
dual-channel, low noise, high speed successive approximation register (SAR)
analog-to-digital converters (ADC) with integrated fully differential drivers
(FDA) and gain setting resistors.

The evaluation board is designed for use with the Digilent ZedBoard via the FMC
connector. The ZedBoard uses a Xilinx Zynq7000 system on chip (SoC) that runs
Analog Devices Kuiper Linux and LIBIIO included on the SD card supplied in the
evaluation board kit, enabling ADC configuration and data capture.

Full specifications on the :adi:`AD4880` and :adi:`AD4884` are available in the
respective data sheets and must be consulted with this user guide when using
the :adi:`EVAL-AD488X-FMC <eval-ad4884>` evaluation board.

Features:

- Integrated fully differential ADC drivers
- Low-voltage digital signaling (LVDS) data output interface.
- Analog-to-digital converter (ADC) configuration via serial
  peripheral interface (SPI).
- Internal or external generation of 1.1V regulated supply rails.
- Sampling rate capability between 1.25MSPS and 20MSPS.
- FMC form factor for easy connection to FPGA carrier boards

Applications:

- Digital imaging
- Cell analysis
- Spectroscopy
- High speed data acquisition
- Digital control loops, hardware in the loop
- Power quality analysis
- Source measurement units
- Nondestructive test

.. figure:: images/eval_ad488x_board.png
   :width: 800

   EVAL-AD488X-FMC

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete as
it should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad488x prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <ad488x quickstart>`:

      #. Using the :ref:`ZedBoard <ad488x quickstart zed>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD488X

   - :ref:`ad488x block-diagram`

     - :adi:`EVAL-AD4884 product page <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4884.html>`
     - :adi:`AD4880 Datasheet <media/en/technical-documentation/data-sheets/ad4880.pdf>`
     - :adi:`AD4884 Datasheet <media/en/technical-documentation/data-sheets/ad4884.pdf>`

   - Resources for designing a custom AD488X-based platform

     #. For Linux software:

        #. :git-linux:`AD488X IIO ADC Linux Driver <drivers/iio/adc/ad4080.c>`

     #. :external+hdl:ref:`ad4880_fmc_evb`

#. :ref:`Help and Support <help-and-support>`

.. _ad488x block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: images/ad4884_block_diagram.png
   :align: center
   :width: 800

   EVAL-AD488X-FMC Block Diagram

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`AD4880 Product Page <AD4880>`
- :adi:`AD4884 Product Page <AD4884>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
