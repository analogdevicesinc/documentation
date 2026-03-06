ADI AD-FMCJESDADC1-EBZ Boards & Xilinx Reference Design
=======================================================

|

.. warning::

   \ **NOTE:**

   | Support for the ad-fmcjesdadc1-ebz was discontinued on all carriers starting with 2022_R2 Kuiper Linux release and it won't be supported anymore in future releases. Latest MicroBlaze images with pre-build files can be downloaded from `here <:doc:`/wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading`>`__. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases. The project source code can still be found on :git-hdl:`hdl_2021_r2 <projects/fmcjesdadc1>` release branch.


.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/fmcjesdadc1/index.html\


Introduction
------------

The :doc:`AD-FMCJESDADC1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcjesdadc1-ebz>` is a high speed data acquisition (4 ADC channels at 250MSPS), in an FMC form factor, which has two high speed JESD204B Analog to Digital converters (:adi:`AD9250`) on it.

.. tip::

   This board is similar to the `4DSP FMC-176 <http://www.4DSP.com/fmc176>`__, which in addition to the AD9250, has two :adi:`AD9129` DACs. This reference design works for either of the boards, for details see `#fmc-176_information <https://wiki.analog.com/>`__ section.


The :adi:`AD9250` is a dual, 14-bit ADC with sampling speeds of up to 250 MSPS. It features a multistage, differential pipelined architecture with integrated output error correction logic. It supports wide bandwidth inputs for a variety of user-selectable input ranges. The AD9250 features JESD204B high speed serial interface.

The boards also feature the :adi:`AD9517-1` for multi-output clock distribution with sub-picosecond jitter performance, along with an on-chip PLL and VCO. The devices may be clocked by either an internal clock source (optionally locked to an external reference) or an externally supplied sample clock.

It also features an external trigger input for customized sampling control. The card is mechanically and electrically compliant to the FMC standard (ANSI/VITA 57.1).

The reference design includes the device data capture via the JESD204B serial interface and the SPI interface. The samples are written to the external DDR-DRAM. It allows programming the device and monitoring it's internal registers via SPI.

Supported Devices
-----------------

-  :adi:`AD-FMCJESDADC1-EBZ (ADI) <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-AD-FMCJESDADC1-EBZ.html>`

Supported Carriers
------------------

-  `KC705 <https://www.xilinx.com/KC705>`__ HPC Slot
-  `VC707 <https://www.xilinx.com/VC707>`__ HPC Slot
-  `ZC706 <https://www.xilinx.com/ZC706>`__ HPC Slot

Required Hardware
~~~~~~~~~~~~~~~~~

-  ZC706, KC705 or VC707 board
-  AD-FMCJESDADC1-EBZ
-  Signal generators (for ADC inputs)

Required Software
~~~~~~~~~~~~~~~~~

-  We upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.
-  A UART terminal (Tera Term/Hyperterminal), baud rate 115200.

Using the reference design
--------------------------

The reference design is built on a microblaze based system parameterized for linux. A functional block diagram of the design is given below.

Xilinx block diagram
^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/fmcjesdadc1_xilinx.svg
   :alt: block diagram
   :width: 800px

AD-FMCJESDADC1-EBZ block diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/ad-fmcjesdadc1-ebz.svg
   :alt: block diagram
   :width: 700px

The reference design consists of a single JESD204B core and two identical instances of AD9250 pcores.

The AD9250 core consists of three functional modules, the ADC interface, a PN9/PN23 monitor and a DMA interface. The ADC interface captures and buffers data from the JESD204B core. The DMA interface then transfers the samples to the external DDR-DRAM. The capture is initiated by the software. The status of capture (overflow, over the range) are reported back to the software.

All the pcores have an AXI lite interface that allows control and monitoring of data generation and/or capture.

The reference design also includes HDMI cores for GTX eye scan.

Changing ADC Sample Rates
~~~~~~~~~~~~~~~~~~~~~~~~~

The ADC sampling rate can vary from 40MHz to 250MHz. However, there are limitations imposed by the FPGA that may lower this range. In some cases, you may have to regenerate the cores for a different range. The reference design uses GTX (channel PLL) primitives and Xilinx's JESD204B core IP. The default design runs at 250MHz clock (5Gbps rate).

As of this writing, the GTX specification & switching characteristics may be found at:

| `ug476_7Series_Transceivers.pdf <https://www.xilinx.com/support/documentation/user_guides/ug476_7Series_Transceivers.pdf>`__
| `ds182_Kintex_7_Data_Sheet.pdf <https://www.xilinx.com/support/documentation/data_sheets/ds182_Kintex_7_Data_Sheet.pdf>`__
| The key switching characteristics are-

The reference clock has a range of 60MHz to 670MHz (700MHz). This limits the minimum sampling clock to 60MHz. Though it is NOT recommended, it is possible to use AD9517 to generate a 40MHz sampling clock to AD9250 and a 80MHz reference clock to the FPGA.

The line rate however, varies based on speed grade, package type and the use of CPLL vs QPLL. The CPLL supports rates between 0.5Gbps to 6.6Gbps (the core may have to be changed for rates less than 3.2Gbps (sampling rate 160MHz) - and the IP may not support all the combinations). Again, it is possible to run the device on a single lane at a higher rate (rather than 2 lanes each at a lower rate) to circumvent some of the troubles of line rate dependency on parametrization, package type and speed grade.

You must carefully evaluate these specifications against your requirements to run the design at a specific sampling frequency (or a range). As always, if you have any questions or run into any problems, :ez:`ask help & support <fpga>`.

FMC-176 Information
-------------------

The `4DSP FMC-176 <http://www.4DSP.com/fmc176>`__ is a high speed data acquisition (4 ADC channels at 250MSPS) and conversion (2 DAC channels at 5.6GSPS) card. This card features two :adi:`AD9250` and two :adi:`AD9129`.

The :adi:`AD9129` is a high performance 14-bit RF DAC supporting data rates up to 2.8GSPS. The DAC core is based on a quad-switch architecture that enables dual-edge clocking operation effectively increasing the DAC update rate to 5.6 GSPS when configured for mix-mode or 2x interpolation. Its high dynamic range and bandwidth enables multicarrier generation up to and beyond 4.2 GHz. The AD9129 features two 14bit LVDS parallel interface.

The following variations of this board are available.

+------------------------------------------------------------------------------------+----------------+----------------+
| Part Number                                                                        | ADC Channels   | DAC Channels   |
+====================================================================================+================+================+
| `FMC-176 <http://www.4dsp.com/FMC176.php>`__                                       | 4 (2 x AD9250) | 2 (2 x AD9129) |
+------------------------------------------------------------------------------------+----------------+----------------+
| `FMC-230 <http://www.4dsp.com/FMC230.php>`__                                       |                | 2 (2 x AD9129) |
+------------------------------------------------------------------------------------+----------------+----------------+
| :adi:`AD-FMCJESDADC1-EBZ <AD-FMCJESDADC1-EBZ#product-samples>`                     | 4 (2 x AD9250) |                |
+------------------------------------------------------------------------------------+----------------+----------------+

This reference design may be used as it is for FMC-176 and it's variations by selecting the appropriate number of DAC channels. It is also easy to port the design for other boards by removing one or more corresponding pcores. Also some devices may not be accessible depending on whether one choose to use LPC or HPC. To fully support both the DACs of the FMC-176, a carrier must have a fully populated HPC connector. The KC705 do not have a fully populated HPC.

The reference design includes (if enabled) RF generation via DDS and the SPI interface for the DACs. At the prompt just enter the number of DAC channels you have in your hardware setup. As an example, if you are using FMC-176 with KC705, simply enter '1' as the number of DAC channels. If you are using the ADC only boards, enter '0' as the number of DAC channels.

The quick start bit file also configures the AD9517 to generate a 2.5GHz clock to AD9129. It then generates a 333MHz tone for the DAC.

The DAC spectrum for a 333MHz tone is shown below.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/cf_fmc27x_spectrum.jpg
   :alt: DAC Spectrum
   :width: 200px

.. important::

   It is possible to use an adapter board such as FMC-700 with KC705 to access both the DACs on a FMC-176 board. However, the routing delays of FMC-LPC pins to the FMC-700 will cause timing errors on DAC1 and you may see parity errors on the UART terminal.


Downloads
---------

The HDL Reference Designs and the no-OS Software can be downloaded from the Analog Devices github.

**FPGA Reference Designs:**

.. admonition:: Download
   :class: download

   
   -  KC705 reference design: :git-hdl:`projects/fmcjesdadc1/kc705`
   -  VC707 reference design: :git-hdl:`projects/fmcjesdadc1/vc707`
   -  ZC706 reference design: :git-hdl:`projects/fmcjesdadc1/zc706`
   


**Software Files:**

.. admonition:: Download
   :class: download

   
   -  AD-FMCJESDADC1-EBZ Main, AD9250, AD9517 Drivers: :git-no-OS:`projects/fmcjesdadc1`
   -  Xilinx Platform Drivers: :git-no-OS:`drivers/platform/xilinx`
   -  ADC Core Driver: :git-no-OS:`common_drivers/adc_core`
   -  JESD204B Driver: :git-no-OS:`drivers/axi_core/jesd204`
   
   ::
   


.. hint::

   
   -  Questions? :ez:`Ask Help & Support <community/fpga>`.
   


More information
----------------

-  `VITA's FMC info <http://www.vita.com/fmc>`__
-  :ez:`Ask questions about the FPGA reference design <community/fpga>`
