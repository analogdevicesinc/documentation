ADRV9029 DPD System Overview
============================

A simplified block diagram of the ADRV9029 transceiver DPD system is shown in the figure below

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpd_simplifiedblockdiagram.png
   :align: center
   :width: 800px

**Transmit Datapath** – The digital baseband signal from the JESD de-framer output goes through an optional Crest Factor Reduction (CFR) block for reduction of the overall peak to average power ratio(PAPR) of the signal followed by a digital interpolation filter which interpolates the baseband signal by a factor of 1x, 2x or 4x for analyzing the baseband signal over the DPD analysis bandwidth. The inverse PA model is applied by the DPD engine, followed by the rest of the transmit signal chain including digital to analog conversion, up conversion by a mixer before the signal is fed into the actual amplifier.

**Observation Datapath** – The DPD algorithm relies on observing the non-linearities via a feedback path. The feedback path is realized using an integrated observation receiver (ORx). The PA output data is sampled through the observation receiver, down converted and digitized for further analysis by the firmware.

**DPD Processing** - The DPD engine is based on an abbreviated implementation of generalized memory polynomial (GMP) that is a generalized subset of the well-known Volterra series. The simplified polynomial models a large number of PA characteristics such as weak nonlinearities, temperature variation, and memory effects. The inverse PA model is applied on the interpolated digital baseband samples through DPD actuator hardware. A dedicated embedded ARM processor (ARM-D) is used for computation of the GMP coefficients.

.. image:: https://wiki.analog.com/_media/navigation ADRV9029 DPD USER GUIDE#dpd_system_overview
   :alt: ADRV9029 DFE System Overview#resources:eval:user-guides:adrv9029|main page#adrv9029_dpd_capabilities|ADRV9029 DPD Specs
