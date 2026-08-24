.. _ad_freqcvt1_ebz eval:

AD-FREQCVT1-EBZ
===============================================================================
TX/RX channels, Frequency conversion from 1‑100 MHz up to 400 MHz

Overview
-------------------------------------------------------------------------------
The :adi:`AD-FREQCVT1-EBZ` is an add on board for the 
:adi:`FMCOMMS3/4/5 <AD-FMCOMMS3-EBZ>` boards which contain the :adi:`AD9361`.

The purpose of the :adi:`AD-FREQCVT1-EBZ` is frequency up and down conversion
to allow the :adi:`AD9361` to operate down to 1MHz.
The :adi:`AD-FREQCVT1-EBZ` module is comprised of the :adi:`AD8342` mixer, the
:adi:`ADL5530` LNA, the :adi:`ADF4351` synthesizer and power management 
components. It is controlled via Pmod port on the FPGA board.

Features:

-  Add on to the FMCOMMS3/4/5 family
-  Powered from FMCOMMSx board
-  Provides one channel down conversion transmit and one channel up conversion
   receive.

Applications:

-  Electronic test and measurement equipment
-  General-purpose software radios
-  Radar systems
-  Ultra wideband satellite receivers
-  Signals intelligence (SIGINT)
-  Point to point communication systems
-  Automated test equipment

.. image:: images/ad_freqcvt1_ebz.webp
   :align: center

.. toctree::
   :hidden:

   quickstart/index
   prerequisites
   user-guide

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of Contents
-------------------------------------------------------------------------------

Using the evaluation board/full stack reference design that we offer:

   #. :ref:`freqcvt1 user-guide`- what you need to know about the
      evaluation board
   #. :ref:`freqcvt1 prerequisites`- what you need to get started
   #. :ref:`Quick-Start Guide <freqcvt1 quickstart>`:

      #. Using the :ref:`ZC706 <freqcvt1 quickstart zc706>`


Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
