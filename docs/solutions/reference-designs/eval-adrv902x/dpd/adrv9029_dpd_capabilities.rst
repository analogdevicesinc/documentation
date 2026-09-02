.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9029/adrv9029_dpd_capabilities

.. _adrv902x dpd capabilities:

ADRV9029 DPD specifications
===============================================================================

This page captures the capabilities of the ADRV9029 compared with the previous
generation integrated DFE transceiver AD9375.

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   - -
     - **AD9375**
     - **ADRV9029**
   - - Approximate IBW
     - 50 MHz
     - 200 MHz
   - - Technology node
     - 65 nm
     - 28 nm
   - - Maximum DPD sample rate
     - 250 MHz
     - 1 GHz
   - - Actuator platform
     - GMP 4 LUTs
     - GMP 32 LUTs
   - - GMP features
     - 23
     - 95
   - - Adaptation rate per Tx channel
     - 250 ms
     - 1 s
   - - CFR support
     - No
     - Yes
   - - GaN PA support
     - No
     - Yes
   - - Typical applications
     - Small Cell
     - Small Cell, M-MIMO and Macro-cell 4G and 5G systems
   - - Other highlights
     -
     - - Dedicated ARM M4 processor for DPD
       - 96x96 HW correlator
       - HW Cholesky decomposition for acceleration
