.. _ad7405:

EVAL-AD7405FMCZ
===============================================================================

16-Bit, Isolated Sigma-Delta Modulator, LVDS Interface.

.. image:: images/eval-ad7405-fmcz.jpg
   :align: right
   :width: 400

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7405FMCZ` is a full featured evaluation board designed to allow the
user to easily evaluate all features of the AD7405 isolated analog-to-digital
converter (ADC). The evaluation board can be controlled by the 
:adi:`EVAL-SDP-CH1Z` via FMCZ connector (J9). The SDP-H1 board 
(:adi:`EVAL-SDP-CH1Z`) allows the evaluation board to be controlled through
a USB port of a PC using the evaluation board software available for 
download from the product page or from the included installer CD.

Features:

- 5 MHz to 20 MHz external clock input rate
- 6 bits, no missing codes
- Signal-to-noise ratio (SNR): 88 dB typical
- Effective number of bits (ENOB): 14.2 bits typical
- Typical offset drift vs. temperature: 1.6 µV/°C
- Low voltage differential signaling (LVDS) interface
- On-board digital isolator
- On-board reference
- Full-scale analog input voltage range: ±320 mV
- −40°C to +125°C operating temperature range
- High common-mode transient immunity: >25 kV/µs
- 16-lead, wide-body SOIC_IC, with increased creepage package
- Safety and regulatory approvals

Applications:

- Shunt current monitoring
- AC motor controls
- Power and solar inverters
- Wind turbine inverters
- Data acquisition systems
- Analog-to-digital and opto-isolator replacements

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

To better understand the :adi:`AD7405`, we recommend to
use the :adi:`EVAL-AD7405FMCZ` evaluation boards.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad7405 user-guide` - what you need to know about the evaluation
      board
   #. :ref:`Prerequisites <ad7405 prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <ad7405 quickstart>`:
     - Using the :ref:`ad7405 quickstart sdp_h1` (SDP)

#. Design with the AD7405

   - :ref:`ad7405 block-diagrams`

     - :adi:`AD7405 product page <AD7405>`

#. :ref:`Help and Support <help-and-support>`

.. _ad7405 block-diagrams:

Block diagrams
-------------------------------------------------------------------------------
EVAL-AD7405FMCZ

.. image:: images/functional-block-diagram.jpg
    :align: center
    :width: 800

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.