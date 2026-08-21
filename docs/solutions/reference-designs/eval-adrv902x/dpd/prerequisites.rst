.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9029/prerequisites

.. _adrv902x dpd prerequisites:

ADRV9029 DPD evaluation prerequisites
===============================================================================

Equipment needed
-------------------------------------------------------------------------------

- 1x :adi:`ADS9 Evaluation Platform <en/products/adrv9029.html>`
- 1x :adi:`ADRV9029 Transceiver Evaluation Board <en/products/adrv9029.html>`
- 1x Signal generator for generating clock to the ADRV9029 evaluation board
- 1x Host computer and an ethernet cable to connect the host computer to the
  ADS9 evaluation platform
- 1x 5 Watt or lower RF power amplifier for evaluation
- DC power supply and cables for the RF power amplifier
- 1x 30 dB fixed RF attenuator (Mini-Circuits BW-S30W20+ or equivalent)
- 1x 6 dB fixed RF attenuator (Mini-Circuits VAT-6W2+ or equivalent)
- 1x Coupler (Mini-Circuits ZFBDC16-63HP-S+ or equivalent)
- SMA connectors and RF cables to connect various components as shown in the
  figure below. Please note that the Observation Receiver (ORx) is on the
  bottom side of the ADRV9029 evaluation board.

.. figure:: ../images/adrv9029_hw_setup.png
   :width: 800

Software requirements
-------------------------------------------------------------------------------

- Operating System: Windows-10 64-bit
- :adi:`ADRV9029 Transceiver Evaluation System GUI <en/license/licensing-agreement/adrv9029-software-license-agreement.html>`

Other requirements
-------------------------------------------------------------------------------

- A wideband OFDM test signal such as LTE5/LTE10/LTE20 or NR100 signal sampled
  at a Tx IQ rate of 245.76 MSPS in tab separated IQ format for evaluating DPD.
  Ensure that the peak power level of the OFDM signal does not exceed -4 dBFS
  to provide sufficient head-room for DPD gain expansion.

  - Typically, an OFDM signal with -14 dBFS rms and 8 dB Peak-To-Average-Power
    Ratio is used for DPD evaluation.

    - Third party vector signal generation tools such as
      `Keysight Signal Studio <https://www.keysight.com/us/en/lib/resources/miscellaneous/signal-studio-software-free-trial-1368357.html>`_,
      `Matlab Vector Generation <https://www.mathworks.com/help/5g/ug/downlink-carrier-waveform-generation.html>`_
      can be used for generating wideband OFDM signals.
