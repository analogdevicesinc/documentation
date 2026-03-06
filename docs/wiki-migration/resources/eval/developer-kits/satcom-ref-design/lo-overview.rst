Link to higher level page: :doc:`Satcom Reference Design </wiki-migration/resources/eval/developer-kits/satcom-ref-design>`

LO Generation
=============

While operation in the UHF, L band and C band can be achieved using direct sampling from the :adi:`AD9082` MxFE ADC and DACs, for operation in the X, Ku and Ka bands, an up down converter is required. As a result, wideband LO signal chains are required for Rx and Tx. The frequency plan for this system does not envisage continuous tuning across a wide frequency range since the LO does not need to jump through bands in real time. Rather the chain needs to be re-configurable between power downs. The goal is to provide a frequency plan that allows for coverage of popular satcom bands on the uplink and downlink from the space side. For example, you might switch from operating in the X band to operating in the Ka band with a long reconfiguration time during the switch. This means the signal chain needs to be tunable across these bands but not necessarily fast tunable.

Based on the frequency plan and the drive needs of the :adi:`ADMFM2000`/:adi:`ADMFM2001` Up/Down converters, a 0 dBm LO at 10,15 and 32 GHz is needed for Tx. For Rx, a 0 dBm LO at 9.5, 13.5 and 22.5 GHz is needed. The target spurious level is -50 dBc.

Transmit and receive signal chains are presented below. The Rx and Tx signal chains are very similar up to their outputs where the Tx and Rx LOs are split into two and four outputs to drive the :adi:`ADMFM2000` and :adi:`ADMFM2001` LO ports (:adi:`ADMFM2000` has a single LO port with an on-chip power splitter that connects to the two on-board down-converting mixers; :adi:`ADMFM2001` has two external LO ports which connect separately to the devices' two on-board up-converting.

The LO is developed from a 500 MHz reference clock by the :adi:`ADF4371` PLL with integrated VCO. The :adi:`ADF4371` has two outputs, one for high frequency (16-32 GHz) and one for lower frequencies (8-16 GHz). These outputs are filtered by the :adi:`ADMV8416` and :adi:`ADMV8432` tunable filters. Because the nominal output power of the higher frequency output is relatively low (-7 dBm), a buffer is placed in-line before the two paths are combined with an SPDT RF switch. The combined LO signal then passes through some amplifiers, an attenuator and a digital step attenuator before being split into two paths for Tx or four paths for Rx.

Receive LO Path
---------------

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/lo_rx_signal_path.png
   :align: center

Transmit LO Path
----------------

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/lo_tx_signal_path.png
   :align: center

Simulated Performance
---------------------

Simulation files have been created for operation of the PLL within ADISimPLL Version 5.60.05. The attached ZIP file contains ADIsimPLL design files for operation at 10 GHz, 15 GHz and 32 GHz (these frequencies can be adjusted). These design files can be used to simulate phase noise/jitter, lock times, and spurs.

`tunable_lo_adf4371_8-32_ghz.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/tunable_lo_adf4371_8-32_ghz.zip>`__

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/tunable_lo_adf4371_8-16_ghz_analysis_at_15_ghz.png

The level plan of the Rx and Tx signals chains can be simulated in :adi:`adisimrf`. The attached ZIP file contains Tx and Rx level plans for operation at 10, 15 and 32 GHz. Where device models for particular parts are not available, temporary devices are used.

`Tx and Rx LO Signal Chains Operation at 10 15 and 32 GHz.zip <https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/Tx and Rx LO Signal Chains Operation at 10 15 and 32 GHz.zip>`__

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/tx_lo_signal_chain_configured_for_operation_at_15_ghz.png

:doc:`Home </wiki-migration/resources/eval/developer-kits/satcom-ref-design>`
