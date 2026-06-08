.. _ad7193_index:

AD7193 Evaluation Board User Guide
===================================

.. toctree::
   :hidden:

   hardware
   Using the System with ACE Software <software>
   Pmod Reference Design <pmod>

The EVAL-AD7193-ASDZ evaluation kit features the
:adi:`AD7193`, is a low noise, complete analog front
end for high precision measurement applications. It contains a low noise,
24-bit sigma-delta (Σ-Δ) analog-to-digital converter (ADC). The on-chip low
noise gain stage means that signals of small amplitude can interface directly
to the ADC. The internal clock option provides a compact solution for low BW
requirements.

The PC software fully configures the
:adi:`AD7193` device register functionality and
provides AC time domain analysis in the form of waveform graphs, histograms,
and associated noise analysis for ADC performance evaluation. The AC analysis
is also provided by the software, examples of which are; an FFT displaying
the first 5 harmonics SNR, SFDR S/N+D and THD.

The AD719x Family
-----------------

The AD719x family of ADCs are an ultralow noise ADC that incorporates a ∑-∆
modulator, a buffer, PGA, and on-chip digital filtering intended for the
measurement of wide dynamic range signals such as those in pressure
transducers, weigh scales, and strain gauge applications.

All devices in family offer excellent noise figures with very low offset and
gain drift. The ultra low noise integrated PGA supports gains from X1 to
X128, enabling an input span of +/- VREF/gain – See the PGA section for more
details. All devices comes with an option to work in differential or pseudo
differential mode. The devices have automatic channel sequencer, 4 GPOs and
can work with a single power supply. There is an on-chip 4.92MHz clock which
can be used as clock source to the ADC. AD719x also includes a zero latency
feature.

.. image:: ../images/ad7193_blockdiag.png
   :align: center
   :width: 400

Evaluation board Features
-------------------------

- Full featured evaluation board for the AD7193
- PC control in conjunction with the system demonstration platform
  (EVAL-SDP-CB1Z/EVAL-SDP-CK1Z)
- PC software for control and data analysis (time and frequency domain)

Related Documents
-----------------

- :adi:`AD7193 Data Sheet <ad7193>`

Required Software
-----------------

- :adi:`ACE Software <ACE>`
- :adi:`AD7193 ACE Plugin <EVAL-AD7193ASDZ>`

Quick Start Guide
~~~~~~~~~~~~~~~~~

The following steps highlight the process to begin using the evaluation
board.

Equipment Required
------------------

- :adi:`EVAL-AD7193-ASDZ evaluation board <EVAL-AD7193ASDZ>`
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
- :ref:`Ace Plugin Install guide available here <ad7193_software>`
- If :adi:`ACE Software <ACE>`
  is already installed, update the Plugins to download AD719x Plugin.

- Connect the EVAL-AD7193-ASDZ to the controller board

  - **Option A:** Connect the EVAL-AD7193-ASDZ to the EVAL-SDP-CK1Z

    - Using the 120 pin connector

      - Screw the two boards together using the plastic screw-washer
        set included in the evaluation board kit to ensure that the
        boards are connected firmly together.
      - Using the Arduino Connectors

.. image:: ../images/sdp_connect.png
   :align: center
   :width: 400

- **Option B:** Connect the EVAL-AD7193-ASDZ to the EVAL-SDP-CB1Z

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

- The :ref:`Low Noise Test Demo <ad7193_software>` is a useful demo
  mode of the Ace Plugin software to ensure that the Evaluation board is
  communicating correctly with the Ace Plugin software.

