ADRV9029 DPD EVALUATION PRE-REQUISITES
======================================

EQUIPMENT NEEDED
----------------

-  1x :adi:`ADS9 Evaluation Platform <en/products/adrv9029.html#>`
-  1x :adi:`ADRV9029 Transceiver Evaluation Board <en/products/adrv9029.html#>`
-  1x Signal Generator for generating clock to the ADRV9029 Evaluation Board
-  1x Host Computer and an ethernet cable to connect the Host Computer to ADS9 Evaluation Platfrom
-  1x 5 Watt or lower RF Power Amplifier for evaluation
-  DC Power Supply and Cables for the RF power amplifier
-  1x 30dB fixed RF attenuator (Mini-Circuits BW-S30W20+ or equivalent)
-  1x 6dB fixed RF attenuator (Mini-Circuits VAT-6W2+ or equivalent)
-  1x Coupler (Mini-Circuits ZFBDC16-63HP-S+ or equivalent)
-  SMA connectors and RF cables to connect various components as shown in the figure below. Please note that the Observation Receiver (ORx) is on the bottom side of the ADRV9029 evaluation board.

| |image1|

SOFTWARE REQUIREMENTS
---------------------

-  Operating System: Windows-10 64-bit
-  :adi:`ADRV9029 Transceiver Evaluation System GUI <en/license/licensing-agreement/adrv9029-software-license-agreement.html>`

OTHER REQUIREMENTS
------------------

-  A wideband OFDM test signal such as LTE5/LTE10/LTE20 or NR100 signal sampled at a Tx IQ rate of 245.76 MSPS in <fc #ff0000>tab separated IQ format</fc> for evaluating DPD. Ensure that the Peak power level of the OFDM signal does not exceed -4dBFS to provide sufficient head-room for DPD gain expansion.

   -  Typically, an OFDM signal with -14dBFS rms and 8dB Peak-To-Average-Power Ratio is used for DPD evaluation.

      -  Third party vector signal generation tools such as `Keysight Signal Studio <https://www.keysight.com/us/en/lib/resources/miscellaneous/signal-studio-software-free-trial-1368357.html>`_, `Matlab Vector Generation <https://www.mathworks.com/help/5g/ug/downlink-carrier-waveform-generation.html>`_ can be used for generating wideband OFDM signals.

.. image:: https://wiki.analog.com/_media/navigation ADRV9029 DPD USER GUIDE#dpd_system_overview2
   :alt: DPD System Overview#resources:eval:user-guides:adrv9029|main page#evaluating_dpd_through_tes_gui|TES GUI

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_hw_setup.png
   :width: 800px
