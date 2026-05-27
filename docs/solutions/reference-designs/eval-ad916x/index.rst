.. _eval-ad916x:

EVAL-AD916X
===========

AD9161/AD9162/AD9163/AD9164 high speed RF DAC reference design.

.. image:: images/AD9161-TR-chip-illustration.png
   :align: left
   :width: 200

.. image:: images/AD9162-TR-chip-illustration.png
   :align: left
   :width: 200

Overview
---------

The :adi:`AD9161 <AD9161>`, :adi:`AD9162 <AD9162>`, :adi:`AD9163 <AD9163>`,
and :adi:`AD9164 <AD9164>` is a high performance, 16-bit (AD9164, AD9163, AD9162)/11-bit
(AD9161) resolution digital-to-analog converter (DAC) that supports data rates to
6 GSPS.

The DAC core is based on a quad-switch architecture coupled with a 2x interpolator
filter that enables an effective DAC update rate of up to 12 GSPS in some modes.
The high dynamic range and bandwidth makes this DAC ideally suited for the most
demanding high speed radio frequency (RF) DAC applications.

The AD916x-FMC HDL reference design provides a validated path to evaluate JESD204
link bring-up, DAC data transport, and clocking on supported FPGA carriers.

The HDL design supports configurable JESD operation modes, lane rates, and
device variants from a common build framework. For Linux bring-up, ADI Kuiper
images and ADI Linux device trees are available for supported ZynqMP platforms.

Features:

- Full featured evaluation board for the AD9161, AD9162, AD9163, and AD9164
- Direct clocking vs. on-board clocking
- Showing RF modes of the DAC, including mixed mode and 2× NRZ
- NCO only mode
- JESD204B/C transmit path with configurable modes and lane rates
- Reference HDL flow on :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
- Integrated DMA/data-offload based data path in HDL reference design
- Linux software enablement through ADI kernel drivers and device trees
- IIO-based remote evaluation from a host PC

Applications:

- Broadband communications systems
- Wireless communications infrastructure
- Instrumentation, automatic test equipment (ATE)
- Radars and jammers

.. figure:: images/AD9162-FMC-EBZTOP-evaluation-board.jpg
   :align: center
   :width: 500

   EVAL-AD9162-FMCB Top

.. figure:: images/AD9162-FMC-EBZBOTTOM-evaluation-board.jpg
   :align: center
   :width: 500

   EVAL-AD9162-FMCB Bottom

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9161 <AD9161>`, :adi:`AD9162 <AD9162>`,
:adi:`AD9163 <AD9163>`, and :adi:`AD9164 <AD9164>`, we recommend to use
the :adi:`EVAL-AD916X-FMCZ <EVAL-AD916X>` evaluation board.

Table of Contents
-----------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`eval-ad916x prerequisites` - what you need to get started with the setup

   #. :ref:`eval-ad916x quickstart`:

      #. Using the :ref:`Using the AMD Xilinx ZCU102 with the EVAL-AD9162-FMC <eval-ad916x quickstart zcu102>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9161/AD9162/AD9163/AD9164

   - :adi:`AD9161 product page <AD9161>`
   - :adi:`AD9162 product page <AD9162>`
   - :adi:`AD9163 product page <AD9163>`
   - :adi:`AD9164 product page <AD9164>`

   -  Resources for designing a custom AD916X-based platform software:

      #. For Linux software:

         - :external+linux:doc:`AD9161/AD9162/AD9163/AD9164 Linux support <drivers/iio-pll/ad9162>`
         - :git-linux:`AD9162 IIO driver <main:drivers/iio/frequency/ad9162.c>`
         - :git-linux:`AD916x IIO support <main:drivers/iio/frequency/ad916x>`

      #. HDL Software:

         - :external+hdl:doc:`AD916x-FMC HDL project documentation <projects/ad916x_fmc/index>`
         - :git-hdl:`AD916x-FMC HDL source code <projects/ad916x_fmc>`
         - :external+hdl:ref:`Build an HDL project <build_hdl>`

#. :adi:`Evaluating the AD9161, AD9162, AD9163, and AD9164 High Speed, RF DACs  <media/en/technical-documentation/user-guides/AD9161-9162-9163-9164-UG-1526.pdf>`

   .. note::
      This user guide uses the ADS7-V2EBZ platform (OBSOLETE).

#. :ref:`Help and Support <help-and-support>`


Block Diagram
-------------

.. figure:: images/ad9161-ad9162-block-diagram.png
   :align: center

   AD9161/AD9162 Block Diagram

Warning
-------------------------------------------------------------------------------

.. esd-warning::
