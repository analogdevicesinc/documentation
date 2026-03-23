Quad-MxFE Prototyping Platform User Guide
=========================================

Product Details
---------------

The :adi:`Quad-MxFE System Development Platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>` contains four :adi:`MxFE™ <en/products/digital-to-analog-converters/high-speed-da-converters/mixed-signal-frontends.html>` software defined, direct RF sampling transceivers, as well as associated RF front-ends, clocking, and power circuitry. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a **16 transmit/16 receive channel** direct sampling phased array at L/S/C band (0.1 GHz to ~5GHz). The Rx & Tx RF front-end has drop-in configurations that allow for customized frequency ranges, depending on the user’s application.

The Quad-MxFE System Development Platform highlights a complete system solution. It is intended as a testbed for demonstrating multi-chip synchronization as well as the implementation of system level calibrations, beamforming algorithms, and other signal processing algorithms. The system is designed to mate with a `VCU118 <https://www.xilinx.com/VCU118>`_ Evaluation Board from Xilinx®, which features the Virtex® UltraScale+™ XCVU9P FPGA, with provided reference software, HDL code, and MATLAB system-level interfacing.

In addition to the Quad-MxFE Digitizing Card, the kit also contains a :doc:`16Tx/16Rx Calibration Board </solutions/reference-designs/quadmxfe/calboard>` that is used to develop system-level calibration algorithms, or otherwise more easily demonstrate power-up phase determinism in situations pertinent to their own use case. The Calibration Board also allows the user to demonstrate combined-channel dynamic range, spurious, and phase noise improvements and can also be controlled via a free MATLAB add-on when connected to the PMOD interface of the `VCU118 <https://www.xilinx.com/VCU118>`_.

The system can be used to enable quick time-to-market development programs for
applications like:

-  ADEF (Phased-Array, RADAR, EW, SATCOM)
-  Communications Infrastructure (Multiband 5G and mmWave 5G)
-  Electronic Test and Measurement

.. image:: images/adquadmxfe1ebztop-web.gif
   :alt: adquadmxfe1ebztop-web.gif

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/analogtv>6184061669001
   :alt: analogTV>6184061669001
   :align: center

--------------

User Resources
--------------

-  :doc:`High-Level Overview </solutions/reference-designs/quadmxfe/quadmxfe>`

   -  :doc:`System Features </solutions/reference-designs/quadmxfe/quadmxfe>`
   -  :doc:`General Description </solutions/reference-designs/quadmxfe/quadmxfe>`

-  :doc:`Getting Started </solutions/reference-designs/quadmxfe/quickbringup>` - **Install Fan/Heat Sinks Prior To First Use!**

   -  :doc:`Equipment Needed </solutions/reference-designs/quadmxfe/quickbringup>`
   -  :doc:`Required Software </solutions/reference-designs/quadmxfe/quickbringup>`

      -  :doc:`Download Supported Bitstreams & Use Cases </solutions/reference-designs/quadmxfe/quick-start>`
      -  :doc:`IIO Oscilloscope </solutions/reference-designs/quadmxfe/quick-start>`

   -  :doc:`MATLAB Control Overview </solutions/reference-designs/quadmxfe/quickbringup>`

      -  :doc:`Simple Tx & Rx Control </solutions/reference-designs/quadmxfe/quickbringup>`
      -  :doc:`System Phase/Amplitude Alignment/Equalization Using Programmable Finite Impulse Response Filters </solutions/reference-designs/quadmxfe/quickbringup>`
      -  :doc:`Demonstrate Multi-Chip Synchronization </solutions/reference-designs/quadmxfe/quickbringup>`
      -  :doc:`Low-Latency ADC-to-DAC Loopback Bypassing JESD204b/c Interface for Repeater or Translator Applications </solutions/reference-designs/quadmxfe/quickbringup>`

-  :doc:`Hardware Information </solutions/reference-designs/quadmxfe/boardhardwaredetails>`

   -  :doc:`Transmit Path </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Receive Path </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Clocking Architecture </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Digital Interface </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Control Interfaces </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Power Distribution </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Thermal Considerations </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
   -  :doc:`Schematic </solutions/reference-designs/quadmxfe/boardhardwaredetails>`

-  `HDL <https://wiki.analog.com/resources/eval/user-guides/ad_quadmxfe1_ebz/ad_quadmxfe1_ebz_hdl>`_

   -  `Rev A/B. Quad-MxFE HDL Reference Design <https://github.com/analogdevicesinc/hdl/tree/dev_quad_mxfe_revab/projects/ad_quadmxfe1_ebz>`_
   -  :git-hdl:`Rev C. Quad-MxFE HDL Reference Design <projects/ad_quadmxfe1_ebz>`

-  :doc:`Multi-Chip Synchronization Guide </solutions/reference-designs/quadmxfe/multichipsynchronization>`
-  :doc:`Related Documents </solutions/reference-designs/quadmxfe/quadmxfe>`

   -  :doc:`Publications </solutions/reference-designs/quadmxfe/quadmxfe>`
   -  :doc:`IC Part Pages </solutions/reference-designs/quadmxfe/quadmxfe>`

--------------

Features
--------

-  Multi-channel, wideband system development platform for the :adi:`AD9081` :adi:`MxFE™ <en/products/digital-to-analog-converters/high-speed-da-converters/mixed-signal-frontends.html>`
-  Mates with Xilinx `VCU118 <https://www.xilinx.com/VCU118>`_ Evaluation Board (Not Included)
-  16x RF Receive (Rx) Channels (32x Digital Rx Channels)

   -  Total 16x 1.5GSPS to 4GSPS ADC
   -  48x Digital Down Converters (DDCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
   -  16x Programmable Finite Impulse Response Filters (pFIRs)

-  16x RF Transmit (Tx) Channels (32x Digital Tx Channels)

   -  Total 16x 3GSPS to 12GSPS DAC
   -  48x Digital Up Converters (DUCs) , Each Including Complex
      Numerically-Controlled Oscillators (NCOs)

-  Flexible Rx & Tx RF Front-Ends

   -  Rx: Filtering, Amplification, Digital Step Attenuation for Gain Control
   -  Tx: Filtering, Amplification

-  Multiple System Control and Analysis Tools

   -  IIO Oscilloscope GUI
   -  MATLAB Add-Ons & Example Scripts
   -  HDL and Embedded Software Solutions for JESD204b/JESD204c Bring-Up

-  Provided Application-Specific Examples

   -  Multi-Chip Synchronization for Power-Up Phase Determinism
   -  System-Level Amplitude/Phase Alignment Using NCOs
   -  Low-Latency ADC-to-DAC Loopback Bypassing JESD Interface
   -  pFIR Control for Broadband Channel-to-Channel Amplitude/Phase Alignment
   -  Fast-Frequency Hopping

-  On-Board Power Regulation from Single 12V Power Adapter (Included)
-  Flexible Clock Distribution

   -  On-Board Clock Distribution from Single External 500MHz Reference
   -  Support for External Converter Clock

--------------

General Description
-------------------

This user guide serves as the main source of information for system engineers and software developers using the Quad-MxFE System Evaluation Board, which contains four :adi:`AD9081` software defined, direct RF sampling transceivers, as well as associated RF front-end, clocking, and power circuitry. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a 16 transmit/16 receive channel direct sampling phased array at L/S/C band (0.1 GHz to ~5GHz). The Rx & Tx RF front-end has drop-in configurations that allow for customized frequency ranges, depending on the user’s application.

The Quad-MxFE System Evaluation Board highlights a complete system solution. It is intended as a testbed for demonstrating multi-chip synchronization as well as implementation of system level calibrations, beam forming algorithms, and other signal processing algorithms. The board is designed to mate with a `VCU118 <https://www.xilinx.com/VCU118>`_ Evaluation Board from Xilinx®, which features the Virtex® UltraScale+™ XCVU9P FPGA, with provided reference software and HDL code.

High-Level Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quadmxfe_highlevelblockdiagram.png
   :width: 1000

System Integration
~~~~~~~~~~~~~~~~~~

Below is the full integrated system including the `VCU118 <https://www.xilinx.com/VCU118>`_, ADQUADMXFE1EBZ, and :doc:`ADQUADMXFE-CAL </solutions/reference-designs/quadmxfe/calboard>` in full operation.

|image1|

Key Component Locations
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quad_mxfe_labels_top.jpg

.. image:: images/quad_mxfe_labels_bottom.jpg

LED Status Indicators
~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quadfullleds.jpg
   :align: center

-  :doc:`Quad MxFE Power (Green) LED Information </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
-  :doc:`Quad MxFE Clock (Blue) LED Information </solutions/reference-designs/quadmxfe/boardhardwaredetails>`
-  :doc:`Calibration Broad LED Information </solutions/reference-designs/quadmxfe/calboard>`
-  `VCU118 LED Information (pg. 85) <https://www.xilinx.com/support/documentation/boards_and_kits/vcu118/ug1224-vcu118-eval-bd.pdf>`_

--------------

Related Documents
-----------------

Publications
~~~~~~~~~~~~

-  :adi:`Multichannel RF to Bits Development Platform <en/design-notes/multichannel-rf-to-bits-development-platform.html>`
-  :adi:`Power-Up Phase Determinism Using Multichip Synchronization Features in Integrated Wideband DACs and ADCs <en/technical-articles/power-up-phase-determinism-using-multichip-synchronization.html>`
-  :adi:`Integrated Hardened DSP on DAC/ADC ICs Improves Wideband Multichannel Systems <en/technical-articles/integrated-hardened-dsp-on-dac-adc-ics-improves-wideband-multichannel-systems.html>`
-  :adi:`Multi-Channel System Improvements Using Hardened DSP in Digitizer ICs <en/education/education-library/webcasts/multi-channel-system-improvements-using-hardened-dsp-digitizer-ics.html>`
-  :adi:`Empirically Based Multichannel Phase Noise Model Validated in a 16-Channel Demonstrator <en/technical-articles/empirical-based-multichannel-phase-noise-model.html>`

Related Part Pages
~~~~~~~~~~~~~~~~~~

MxFE
^^^^

-  :adi:`AD9081 <en/products/ad9081.html>`
-  :adi:`AD9082 <en/products/ad9082.html>`
-  `AD9081/AD9082 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide <https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`_
-  :adi:`UG-1578 User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`

ADF4371
^^^^^^^

-  :adi:`ADF4371 <en/products/adf4371.html>`
-  `ADF4371 IIO Wideband Synthesizer Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/adf4371>`_

HMC7043
^^^^^^^

-  :adi:`HMC7043 <en/products/hmc7043.html>`
-  `HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/hmc7044>`_

LTM4633
^^^^^^^

-  :adi:`LTM4633 <en/products/ltm4633.html>`

LTM8063
^^^^^^^

-  :adi:`LTM8063 <en/products/ltm8063.html>`

LTM8053
^^^^^^^

-  :adi:`LTM8053 <en/products/ltm8053.html>`

FPGA Evaluation Board Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Xilinx Virtex UltraScale+ FPGA VCU118 <https://www.xilinx.com/products/boards-and-kits/vcu118.html>`_

--------------

Questions
---------

For additional questions or support, please visit the Engineering Zone forum at :ez:`adef-system-platforms/ <adef-system-platforms>`.

--------------

.. |image1| image:: images/quadfull_edit.jpg
