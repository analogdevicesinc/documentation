ADRV904x DPD EVALUATION PRE-REQUISITES
======================================

EQUIPMENT NEEDED
----------------

-  1x :adi:`ADS10 Evaluation Platform <en/products/adrv9040.html#evaluation-kit>`
-  1x :adi:`ADRV904x Transceiver Evaluation Board <en/products/adrv9040.html#evaluation-kit>`
-  1x Signal Generator for generating clock to the ADRV904x Evaluation Board
-  1x Host Computer and an ethernet cable to connect the Host Computer to ADS10 Evaluation Platfrom
-  1x 5 Watt or lower RF Power Amplifier for evaluation
-  DC Power Supply and Cables for the RF power amplifier
-  1x 30dB fixed RF attenuator (Mini-Circuits VAT-3A+ or equivalent)
-  1x 3dB fixed RF attenuator (Mini-Circuits VAT-6W2+ or equivalent)
-  1x Coupler (Mini-Circuits ZFBDC16-63HP-S+ or equivalent)
-  SMA connectors and RF cables to connect various components as shown in the
   figure below.

.. image:: ../images/adrv904x_dpd_evalsystem.jpg
   :align: center
   :width: 800

SOFTWARE REQUIREMENTS
---------------------

-  Operating System: Windows-10 64-bit
-  :adi:`ADRV904x Evaluation GUI <en/products/adrv9040.html#part-ecosystem>`

OTHER REQUIREMENTS
------------------

-  A wideband OFDM test signal such as LTE5/LTE10/LTE20 or NR100 signal sampled
   at a Tx IQ rate of 491.52 MSPS in tab separated IQ format for evaluating DPD.
   Ensure that the Peak power level of the OFDM signal does not exceed -3dBFS to
   provide sufficient head-room for DPD gain expansion.

   -  Typically, an OFDM signal with -14dBFS rms and 8dB Peak-To-Average-Power
      Ratio is used for DPD evaluation.

      -  Third party vector signal generation tools such as `Keysight Signal Studio <https://www.keysight.com/us/en/lib/resources/miscellaneous/signal-studio-software-free-trial-1368357.html>`_, `Matlab Vector Generation <https://www.mathworks.com/help/5g/ug/downlink-carrier-waveform-generation.html>`_ can be used for generating wideband OFDM signals.
