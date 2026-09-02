.. _ad7192_index:

AD7192 Evaluation Board User Guide
==================================

.. toctree::
   :hidden:

   hardware
   Using the System with ACE Software <software>

The EVAL-AD7192-ASDZ evaluation kit features the AD7192 which is 4.8 kHz
ultralow noise 24-bit sigma-delta (Σ-Δ) ADCs. The on-chip low noise gain stage
means that signals of small amplitude can interface directly to the ADC. The
internal clock option provides a compact solution for low BW requirements.

The AD7192 ACE Plugin fully configures the AD7192 device register functionality
and provides dc time domain analysis in the form of waveform graphs, histograms,
and associated noise analysis for ADC performance evaluation.

Full specifications on the AD7192 are available in the product data sheet, which
should be consulted in conjunction with this user guide when working with the
evaluation board.

.. image:: ../images/ad7192_blockdiag.png
   :align: center
   :width: 600

Features
--------

- Full featured evaluation board for the AD7192
- PC control in conjunction with the system demonstration platform
  (EVAL-SDP-CB1Z/EVAL-SDP-CK1Z)
- PC software for control and data analysis (time and frequency domain)

Related Documents
-----------------

- :adi:`AD7192 Data Sheet <ad7192>`

Required Software
-----------------

- :adi:`ACE Software <ACE>`
- :adi:`AD7192 ACE Plugin <EVAL-AD7192ASDZ>`

Quick Start Guide
~~~~~~~~~~~~~~~~~

The following steps highlight the process to begin using the evaluation board.

Equipment Required
------------------

- :adi:`EVAL-AD7192-ASDZ evaluation board <EVAL-AD7192ASDZ>`
- PC running Windows with a USB2.0 port and software installed.
- Controller Board

  - Option A: :adi:`EVAL-SDP-CK1Z <SDP-K1>`
    and a USB-C cable
  - Option B: :adi:`EVAL-SDP-CB1Z <SDP-B>`
    and a Micro-USB cable

Getting started
---------------

.. warning::

   Ensure the SDP board is not connected to the USB port of the PC

- Install the :adi:`ACE Software <ACE>`
- :ref:`Ace Plugin Install guide available here <ad7192_software>`
- If :adi:`ACE Software <ACE>`
  is already installed, update the Plugins to download AD719x Plugin.

- Connect the EVAL-AD7192-ASDZ to the controller board

  - **Option A:** Connect the EVAL-AD7192-ASDZ to the EVAL-SDP-CK1Z

    - Using the 120 pin connector

      - Screw the two boards together using the plastic screw-washer
        set included in the evaluation board kit to ensure that the
        boards are connected firmly together.
      - Using the Arduino Connectors

.. image:: ../images/sdp_connect.png
   :align: center
   :width: 400

- **Option B:** Connect the EVAL-AD7192-ASDZ to the EVAL-SDP-CB1Z

  - Using the 120 pin connector

    - Screw the two boards together using the plastic screw-washer
      set included in the evaluation board kit to ensure that the
      boards are connected firmly together.

- If using Windows® XP, it may be needed to search for the controller
  board drivers. Choose to automatically search for the drivers for the
  controller board if prompted by the operating system.
- Launch the ACE plugin from the Analog Devices subfolder in the
  Programs Menu.

.. image:: ../images/ace_plugin_open.png
   :align: center
   :width: 300

- The :ref:`Low Noise Test Demo <ad7192_software>` is a useful demo mode
  of the Ace Plugin software to ensure that the Evaluation board is
  communicating correctly with the Ace Plugin software.

