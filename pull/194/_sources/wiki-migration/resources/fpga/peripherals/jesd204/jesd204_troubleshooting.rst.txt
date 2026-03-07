Troubleshooting JESD204B Tx links
=================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/troubleshoot/troubleshoot_jesd204_tx.html\


Running one of the below commands on a Linux based system will return the status of the JESD link. This is one of the firsts steps to diagnose the link.

::

   #jesd_status
   or
   #grep "" /sys/bus/platform/devices/*.axi-jesd*/status*
      Link is enabled
      Measured Link Clock: 184.320 MHz
      Reported Link Clock: 184.320 MHz
      Lane rate: 7372.800 MHz
      Lane rate / 40: 184.320 MHz
      LMFC rate: 11.520 MHz
      SYNC~: deasserted
      Link status: DATA
      SYSREF captured: Yes
      SYSREF alignment error: No

Common symptoms
---------------

Below table describes the most commonly occurred problems during link bring-up and solutions to overcome these in a Linux environment.

Missing JESD link layer peripheral, \*.axi-jesd*/status\*: No such file or directory
------------------------------------------------------------------------------------

.. container:: center round box

   
   **Cause:** Base address mismatch between HDL and device tree, adi,axi-jesd204-tx-1.0 or adi,axi-adxcvr-1.0 driver does not probes.
   
   **Identify:** Check address allocation in the block design or system_bd.tcl against the corresponding device tree physical and link layer nodes.
   
   **Fix:** Adjust addresses. For ZCU102 add 0x20000000 offset to the address used in HDL.


--------------

Link is DISABLED, In Linux boot log following appears: axi-adxcvr-tx: TX Error: 0
---------------------------------------------------------------------------------

.. container:: center round box

   **Cause:** QPLL or CLL does not lock due missing reference clock.

   
   **Identify:** Check reference clock location constraints. Check if ref clock reaches the in use quads.
   
   **Fix:** Adjust location constraints.
   


.. container:: center round box

   **Cause:** QPLL or CLL does not lock due incorrect synthesis parameters.

   
   **Identify:** Check channel and common util_adxcvr parameters against ones created with the transceiver wizard.
   
   **Fix:** Adjust synthesis parameters of the util_adxcvr component.


.. container:: center round box

   **Cause:** QPLL or CLL does not lock due frequency mismatch of reference clock. Reference clock frequency is not the one the CPLL or QPLL was set to handle forcing the VCO go out of range.

   
   **Identify:** Check reference clock generation settings.
   
   **Fix:** Adjust setting of the clock chip to generate the correct frequency.


--------------

Link is DISABLED, In Linux boot log following appears: axi-jesd204-tx 44b90000.axi-jesd204-tx: axi_jesd204_tx_jesd204_link_setup: Link0 set lane rate 16500000 kHz failed (-22) ...
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. container:: center round box

   **Cause:** QPLL can't find a configuration for desired lane rate with the given reference clock.

   
   **Identify:** Check boot log. Check the required lane rate ref clock combination against the constraints defined in the transceiver manual.
   
   **Fix:** Configure the clock chip for different reference clock or switch to CPLL or QPLL0/1.


--------------

Link is DISABLED, In Linux boot log following appears: axi-adxcvr-tx: QPLL: failed to find setting for lane rate ...
--------------------------------------------------------------------------------------------------------------------

.. container:: center round box

   **Cause:** QPLL can't find a configuration for desired lane rate with the given reference clock.

   
   **Identify:** Check boot log. Check the required lane rate ref clock combination against the constraints defined in the transceiver manual.
   
   **Fix:** Configure the clock chip for different reference clock or switch to CPLL.


--------------

Link status stays in CGS and SYNC~ stays asserted
-------------------------------------------------

.. container:: center round box

   **Cause:** SYNC~ signal does not reach link layer hdl component

   
   **Identify:** Check location constraints against schematic
   
   **Fix:** Adjust location constraints to match the schematic


.. container:: center round box

   **Cause:** SYNC~ signal polarity reversed

   
   **Identify:** Check constraints and schematic, look for any polarity inversion
   
   **Fix:** Adjust location constraints to match the schematic


.. container:: center round box

   **Cause:** JESD Rx can’t detect the CGS characters due different lane rate settings

   
   **Identify:**
   
   -  Check if “Measured Link Clock” matches “Reported Link Clock” and “Lane Rate / 40”
   -  Check is lane rate is as expected
   -  If OUTDIV_CLK is used for link clock adjust out-clk-select to match Lane Rate/ 40
   -  If dedicated link clock is used adjust the external clock chip from device tree to output a clock of Lane Rate / 40
   
   **Fix:** Some general rules that always should hold:
   
   -   :math:`\displaystyle LaneRate = SampleRate \times (\frac{10}{8}) \times (M/L) \times NP`
   -   :math:`SampleRate = DACrate / TotalInterpolation`
   -   :math:`LinkClock = LaneRate/40`
   -  If OUTDIV_CLK is used: :math:`LinkClock = RefClock/(OutClkSel==4 ? 2 : OutClkSel==3 ? 1 : 1)`
   
   Where:
   
   -  M - *adi,converters-per-device*, device tree property from axi-jesd204-tx node
   -  L - number of lanes per link, parameter of JESD IP
   -  NP - *adi,bits-per-sample* device tree property from axi-jesd204-tx node
   -  RefClock – reference clock for the transceivers
   -  SampleRate - rate of sample that feeds the JESD link
   -  DACrate – DAC raw sample rate after interpolation,
   -  TotalInterpolation – product of selected interpolations on the datapath e.g dacInterpolation \*channelInterpolation
   -  OutClkSel - *adi,out-clk-select* device tree property from xcvr node
   


--------------

Link status stays in CGS and SYNC~ is deasserted
------------------------------------------------

.. container:: center round box

   **Cause:** SYNC~ signal not connected correctly, pulled high

   
   **Identify:** #jesd_status or #grep "" /sys/bus/platform/devices/\*.axi-jesd*/status\*
   
   ::
   
      Link status: CGS
      SYNC~: deasserted
   
   **Fix:** Make sure SYNC~ is connected to the Link Transmit peripheral and is properly driven.


.. container:: center round box

   **Cause:** Receive endpoint of the JESD link is not up

   
   **Identify:** #jesd_status or #grep "" /sys/bus/platform/devices/\*.axi-jesd*/status\*
   
   ::
   
      Link status: CGS
      SYNC~: deasserted
   
   **Fix:** Make sure software communicates correctly with the DAC, bring-up sequence was executed and JESD RX blocks configured and enabled.


.. container:: center round box

   **Cause:** Missing SYSREF at peripheral in subclass 1

   
   **Identify:** #jesd_status or #grep "" /sys/bus/platform/devices/\*.axi-jesd*/status\*
   
   ::
   
      Link status: CGS
      SYNC~: deasserted
      SYSREF captured         No
   
   **Fix:** Make sure SYSREF is connected to the Link Transmit peripheral and is properly driven.


--------------

Link status stays in DATA but output tone not as expected, raised noise floor
-----------------------------------------------------------------------------

.. container:: center round box

   **Cause:** Lane polarity inversion

   
   **Identify:** Read received ILAS registers from DAC, in such case they do not make any sense compared to the LANEn_ILAS0..3 registers of the axi_jesd204_tx. ILAS checksum mismatch.
   
   **Fix:** For each in use lane adjust the corresponding bit in the TX_LANE_INVERT parameter of the util_adxcvr component to match any polarity inversion from the schematic


--------------

Link status stays in DATA but output not as expected
----------------------------------------------------

E.g.: For a Link Clock: 184.320 MHz; Nothing is transmitted from the transport layer but spectrum looks like below:


|image1|

.. container:: center round box

   **Cause:** Mismatch in scrambling configuration.

   
   **Identify:** Check scrambling configuration registers from DAC against LINK_CONF1 config register SCRAMBLER_DISABLE bit of the link transmit peripheral.
   
   **Fix:** Adjust the above bits to match configuration.
   


--------------

Link status stays in DATA but output tone not as expected
---------------------------------------------------------

.. container:: center round box

   **Cause:** Swapped lanes, source ‘Lane n’ connects to other than sink ‘Lane n’;

   
   **Identify:** Read received LID in the ILAS registers of the DAC, in such case they are out of order, permuted
   
   **Fix:** Adjust link layer to physical layer connections in the FPGA block design through ad_xcvrcon procedure lane_map parameter; or \\\\Adjust crossbar from the DAC through the device tree nodes


--------------

Link status stays in DATA but output tone not as expected, signal and its spectrum presents randomness
------------------------------------------------------------------------------------------------------

.. container:: center round box

   **Cause:** Incorrect or missing constraint of the device clock (lane rate / 40)

   
   **Identify:** Report clocks of the transport layer, link layer component
   
   **Fix:** In the constraints file define/create clocks with period that match desired lane rate / 40


--------------

SYSREF alignment error: Yes
---------------------------

.. container:: center round box

   **Cause:** frequency of SYSREF signal is not as expected

   
   **Identify:** Check SYSREF generator parameters.
   
   **Fix:** Set the frequency of SYSREF to be integer multiple of the reported local multiframe clock (LMFC)


.. container:: center round box

   **Cause:** SYSREF signal sampling does not meet setup/hold requirements.

   
   **Identify:** Check if SYSREF path is constrained.
   
   **Fix:** Define timing constraints for SYSREF in edge aligned source synchronous interface mode and adjust device clock and SYSREF phase from the clock chip accordingly.


--------------

Template
--------

.. container:: center round box

   **Cause:** template

   
   **Identify:** template
   
   **Fix:** template


--------------

More Information
================

-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

Support
=======

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Video, Audio, etc) via the :ez:`EngineerZone <community/fpga>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/peripherals/jesd204/scrambling_mismatch_fft.jpg
