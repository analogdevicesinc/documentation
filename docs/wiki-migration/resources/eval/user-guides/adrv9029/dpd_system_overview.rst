ADRV9029 DFE SYSTEM LEVEL OVERVIEW
==================================

The DPD feature on the ADRV9029 transceiver enables users to offload power amplifier linearization tasks from the baseband processor to the transceiver. With DPD implemented on the transceiver, the user does not need to allocate JESD serializer/de-serializer resources for observing power amplifier feedback data through the ORx channels, resulting in significant system power savings. Interpolators leading to the DPD actuator allow the baseband processor to transmit data at a lower rate on the JESD204B/C link than is needed for the full DPD correction bandwidth. The lower data rate at JESD translates directly into power savings and less number of lanes. Integration of the DPD into the transceiver chip results in significant system level cost, space, and power savings when compared to conventional FPGA/ASIC based implementations.

The ADRV9029 transceiver provides digital signal processing capabilities in the embedded ARM processor using closed-loop feedback signals from the observation receiver channels. These functions improve transmitter performance, measure system output, and reduce system power consumption. The list of functions includes the following: digital pre-distortion (DPD), closed-loop gain control (CLGC) and crest factor reduction (CFR). These functions are collectively grouped together as the transceiver digital front end (DFE).

The figure below is a simplified system level overview of the transceiver signal chain with DFE processing blocks highlighted. There are five main DFE processing blocks:

-  CFR and hard clipper are used to reduce peak to average power ratio (PAPR) of the baseband signal, especially for multi-carrier waveforms such as OFDM. With reduced PAPR, the PA can operate at a higher output power, increasing the PA efficiency. This function is explained in the Crest Factor Reduction (CFR) section.
-  There are two half band filters with a total interpolation factor of 4x before the DPD actuator. These blocks can provide a total of 1x, 2x or 4x interpolation.
-  There are three DPD capture buffers, which include pre-DPD actuator, post-DPD actuator, and observation buffers. Each buffer can capture a maximum of 4096 samples.
-  DPD actuator, which applies the inverse PA model to the baseband signal for power amplifier linearization.
-  Dual core embedded ARM processor in which the DPD and CLGC algorithms reside. One of the dual core ARM processors is a control processor(ARM-C) which is the master and the second core is a dedicated ARM core for DPD processing (ARM-D).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dfe_systemleveloverview.png
   :align: center
   :width: 800px

.. image:: https://wiki.analog.com/_media/navigation ADRV9029 DPD USER GUIDE#dpd_principle_of_operation
   :alt: Principle of operation#resources:eval:user-guides:adrv9029|main page#dpd_system_overview2|DPD System Overview
