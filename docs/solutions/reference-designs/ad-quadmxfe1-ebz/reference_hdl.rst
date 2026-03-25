.. _ad-quadmxfe1-ebz-hdl:

AD-QUADMXFE1-EBZ HDL Reference Design
=======================================

.. note::

   The latest HDL documentation can be found at
   `projects/ad_quadmxfe1_ebz <https://analogdevicesinc.github.io/hdl/projects/ad_quadmxfe1_ebz/index.html>`__.

Functional Overview
-------------------

The AD-QUADMXFE1-EBZ reference design is a processor based (e.g. Microblaze)
embedded system. The design consists of a receive and a transmit chain.

The receive chain transports the captured samples from ADC to the system memory
(DDR). Before transferring the data to DDR the samples are stored in a buffer
implemented on block RAMs from the FPGA fabric (util_adc_fifo). The size of the
buffer is sized to store up to M x 16k samples per converter if a single channel
is selected or 16k samples per converter if all channels are selected.

The transmit chain transports samples from the system memory to the DAC devices.
Before streaming out the data to the DAC through the JESD link the samples first
are loaded into a buffer (util_dac_fifo) which will cyclically stream the
samples at the tx_device_clk data rate.

All cores from the receive and transmit chains are programmable through an
AXI-Lite interface.

The transmit and receive chains must operate at the same data rates having a
common device_clk.

HDL Source Code
---------------

- **Rev A/B:** :git-hdl:`hdl_2021_r1:projects/ad_quadmxfe1_ebz`
- **Rev C (latest):** :git-hdl:`projects/ad_quadmxfe1_ebz`

Supported Carriers
------------------

- :xilinx:`VCU118 <products/boards-and-kits/vcu118.html>` FMC+ Slot

Software Support
----------------

- :doc:`Quad-MxFE Software Quick Start Guide <quick_start>`

Building the HDL
----------------

To build the HDL, first clone the repo. Change the directory to the
``projects/ad_quadmxfe1_ebz`` folder and run the make command. For information
on how to change branches and more detailed steps of the build process, refer to
`ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.
This generates the .bit file used to load the platform.

Building the Corresponding Linux Image
---------------------------------------

To build the Linux image, the buildroot process is preferred. The instructions
are primarily based around a Linux environment. Once cloned there is a list of
device trees from :git-linux:`arch/microblaze/boot/dts`. A new device tree can
be specified during the build process if needed.

See the "Building for Microblaze - simpleImage.<board>" instructions as a
reference.

#. Change directory into the buildroot directory.
#. ``make microblaze_adi_defconfig``
#. ``make BR2_LINUX_KERNEL_INTREE_DTS_NAME=vcu118_quad_ad9081``

This will generate the .strip file that will be loaded onto the platform using
the .tcl script.

Build Image By Hand
~~~~~~~~~~~~~~~~~~~

Alternatively, the Linux image can be built by hand. This method is similar to
the buildroot path, but allows for a separate specification of root file system
and other environmental variables.

Block Design Parameters
-----------------------

.. code-block::

   JESD_MODE : used link layer encoder mode
      64B66B - 64b66b link layer defined in JESD 204C, uses Xilinx IP as Physical layer
      8B10B  - 8b10b link layer defined in JESD 204B, uses ADI IP as Physical layer

   RX_RATE :  line rate of the Rx link ( MxFE to FPGA ) used in 64B66B mode
   TX_RATE :  line rate of the Tx link ( FPGA to MxFE ) used in 64B66B mode
   REF_CLK_RATE : frequency of reference clock in MHz used in 64B66B mode
   [RX/TX]_PLL_SEL :  used in 64B66B mode,
                      0 - CPLL   for lane rates 4-12.5 Gbps and integer sub-multiples
                      1 - QPLL0  for lane rates 19.6-32.75 Gbps and integer sub-multiples (e.g. 9.8-16.375)
                      2 - QPLL1  for lane rates 16.0-26.0 Gbps and integer sub-multiple (e.g. 8.0-13.0)
   [RX/TX]_JESD_M : number of converters per link
   [RX/TX]_JESD_L : number of lanes per link
   [RX/TX]_JESD_NP : number of bits per sample, only 16 is supported
   [RX/TX]_NUM_LINKS : number of links, matches number of MxFE devices
   RX_KS_PER_CHANNEL : number of samples stored per channel in block RAM for contiguous capture
   TX_KS_PER_CHANNEL : number of samples loaded per channel in block RAM for contiguous cyclic streaming
   DAC_TPL_XBAR_ENABLE : enable NxN crossbar functionality at the transport layer

Supported Build Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Parameter
     - default
     - B_9_10
     - C_10_11
     - C_11_4
     - C_23_25
     - C_29_24
     - C_12_13
     - C_3_2
   * - JESD_MODE
     - 64B66B
     - 8B10B
     - 64B66B
     - 64B66B
     - 64B66B
     - 64B66B
     - 64B66B
     - 64B66B
   * - RX_RATE
     - 16.5
     - N/A
     - 16.5
     - 16.5
     - 24.75
     - 24.75
     - 24.75
     - 16.5
   * - TX_RATE
     - 16.5
     - N/A
     - 16.5
     - 16.5
     - 24.75
     - 24.75
     - 24.75
     - 16.5
   * - RX_PLL_SEL
     - 2
     - N/A
     -
     -
     - 1
     - 1
     - 1
     -
   * - TX_PLL_SEL
     - 2
     - N/A
     -
     -
     - 1
     - 1
     - 1
     -
   * - REF_CLK_RATE
     - 250
     - N/A
     - 250
     - 250
     - 250
     - 250
     - 250
     - 250
   * - RX_JESD_M
     - 8
     - 8
     - 4
     - 8
     - 4
     - 8
     - 2
     - 4
   * - RX_JESD_L
     - 2
     - 4
     - 4
     - 2
     - 4
     - 4
     - 4
     - 1
   * - RX_JESD_S
     - 1
     - 1
     - 1
     - 1
     - 2
     - 1
     - 1
     - 1
   * - RX_JESD_NP
     - 16
     -
     -
     -
     - 12
     - 12
     -
     -
   * - RX_NUM_LINKS
     - 4
     -
     -
     -
     -
     -
     -
     -
   * - TX_JESD_M
     - 16
     - 8
     - 4
     - 16
     - 4
     - 8
     - 2
     - 8
   * - TX_JESD_L
     - 4
     - 4
     - 4
     - 4
     - 4
     - 4
     - 4
     - 2
   * - TX_JESD_S
     - 1
     - 1
     - 1
     - 1
     - 2
     - 1
     - 1
     - 1
   * - TX_JESD_NP
     - 16
     -
     -
     -
     - 12
     - 12
     -
     -
   * - TX_NUM_LINKS
     - 4
     -
     -
     -
     -
     -
     -
     -
   * - RX_KS_PER_CHANNEL
     - 32
     -
     - 64
     - 32
     - 16
     - 16
     - 64
     - 16
   * - TX_KS_PER_CHANNEL
     - 16
     -
     - 16
     - 16
     - 16
     - 16
     - 64
     - 16
   * - DAC_TPL_XBAR_ENABLE
     - 0
     -
     -
     -
     -
     -
     -
     -

If parameter not specified the default value applies.

Software Considerations
~~~~~~~~~~~~~~~~~~~~~~~

- **ADC crossbar config**: Not required; this is handled in the HDL.
- **DAC crossbar config**: Not required; this is handled in the HDL.

Configuration names are encoded as ``<B_C>_<TX_MODE>_<RX_MODE>`` where ``B``
is for 8B/10B (JESD204B) and ``C`` for 64B66B (JESD204C).

.. list-table:: Configuration to Linux Device Tree Mapping
   :header-rows: 1

   * - Configuration name
     - Linux device tree
   * - B_9_10
     - :git-linux:`vcu118_quad_ad9081_204b_txmode_9_rxmode_10_revc.dts <arch/microblaze/boot/dts/vcu118_quad_ad9081_204b_txmode_9_rxmode_10_revc.dts>`
   * - C_10_11
     - :git-linux:`vcu118_quad_ad9081_204c_txmode_10_rxmode_11_revc.dts <arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_10_rxmode_11_revc.dts>`
   * - C_11_4
     - :git-linux:`vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.dts <arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.dts>`
   * - C_23_25
     - :git-linux:`vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc.dts <arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_23_rxmode_25_revc.dts>`
   * - C_29_24
     - :git-linux:`vcu118_quad_ad9081_204c_txmode_29_rxmode_24_revc.dts <arch/microblaze/boot/dts/vcu118_quad_ad9081_204c_txmode_29_rxmode_24_revc.dts>`
   * - C_12_13
     - :git-linux:`vcu118_quad_ad9082_204c_txmode_12_rxmode_13.dts <arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_12_rxmode_13.dts>`
   * - C_3_2
     - :git-linux:`vcu118_quad_ad9082_204c_txmode_3_rxmode_2.dts <arch/microblaze/boot/dts/vcu118_quad_ad9082_204c_txmode_3_rxmode_2.dts>`

Testcase M8, L4
~~~~~~~~~~~~~~~

The 4 MxFE Rx and Tx links are connected to a single transceiver block having
16 Rx and 16 Tx lanes in total. The 4 Rx links merge into a single receive link
layer and a single transport layer having a compatible configuration to
L=4;M=8;F=4;S=1. Similarly to Rx, the single transmit link layer and transport
layer handles the 4 Tx links.

.. figure:: ad9081_quad_block_diagram.png
   :align: center

   AD-QUADMXFE1-EBZ block diagram (8B10B mode, M8 L4)

**Build instructions:**

.. code-block:: bash

   make JESD_MODE=8B10B RX_JESD_M=8 RX_JESD_L=4 TX_JESD_M=8 TX_JESD_L=4

The Rx links (ADC Path) operate with the following parameters:

- Rx Deframer parameters: L=16, M=32, F=4, S=1, N'=16, N=16 (equivalent to Quick Config 0x0A)
- Dual link: No
- DEVICE_CLK --- 250 MHz (Lane Rate/40)
- REF_CLK --- 500 MHz (Lane Rate/20)
- JESD204B Lane Rate --- 10 Gbps
- QPLL0 or CPLL

The Tx links (DAC Path) operate with the following parameters:

- Tx Framer parameters: L=16, M=32, F=4, S=1, N'=16, N=16 (equivalent to Quick Config 0x09)
- Dual link: No
- DEVICE_CLK --- 250 MHz (Lane Rate/40)
- REF_CLK --- 500 MHz (Lane Rate/20)
- JESD204B Lane Rate --- 10 Gbps
- QPLL0 or CPLL

Testcase DAC M16,L4 ADC M8,L2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 4 MxFE Rx and Tx links are connected to a single transceiver block having
8 Rx and 16 Tx lanes in total. The 4 Rx links merge into a single receive link
layer and a single transport layer having a compatible configuration to
L=2;M=8;F=8;S=1. Similarly to Rx, the single transmit link layer and transport
layer handles the 4 Tx links of mode set to L=4;M=16;F=8;S=1.

The number of lanes on Rx is reduced to half in order to keep the same lane rate
as the Tx link (which has double the channel count of Rx).

.. figure:: ad9081_quad_204c.png
   :align: center

   AD-QUADMXFE1-EBZ block diagram (64B66B mode)

**Build instructions:**

.. code-block:: bash

   make JESD_MODE=64B66B RX_JESD_M=8 RX_JESD_L=2 TX_JESD_M=16 TX_JESD_L=4

The Rx links (ADC Path) operate with the following parameters:

- JESD 204C 64b66B mode
- Rx Deframer parameters: L=8, M=32, F=8, S=1, N'=16, N=16 (equivalent to Quick Config 0x04)
- Dual link: No
- DEVICE_CLK --- 250 MHz (Lane Rate/66)
- REF_CLK --- 250 MHz
- JESD204C Lane Rate --- 16.5 Gbps
- QPLL1

The Tx links (DAC Path) operate with the following parameters:

- JESD 204C 64b66B mode
- Tx Framer parameters: L=16, M=64, F=4, S=1, N'=16, N=16 (equivalent to Quick Config 0x0B)
- Dual link: No
- DEVICE_CLK --- 250 MHz (Lane Rate/66)
- REF_CLK --- 250 MHz
- JESD204C Lane Rate --- 16.5 Gbps
- QPLL1

Clock Sources
~~~~~~~~~~~~~

.. figure:: ad9081_quad_vcu118_clocking.png
   :align: center

   Clock sources diagram

Bandwidth Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~

1 MxFE has 8 lanes.
Max lane rate supported in 204C = 24.75 Gbps.

Max data rate for one MxFE per direction = 8 * 24.75 Gbps * 64/66 = 192 Gbps = 24 GB/s

The existing quad board has half the lanes, this gives us 12 GB/s per MxFE per
direction. The bandwidth requirement per direction is 4 x 12 GB/s = 48 GB/s.

The theoretical throughput of the DDR from the VCU118 is 19.2 GB/s, so far away
from the existing quad MxFE requirements, but an HBM FPGA would solve that.

GPIO Muxing
~~~~~~~~~~~

GPIO muxing enables multiple functions of gpio_0 pins, to have either the NCO
sync function or to be regular software controllable GPIOs.

e.g. function selection for gpio[0] line of MxFE0,1,2,3 done through GPIO[108]

**Gpio_0_mode (GPIO[108]) = 0 --- SW controlled GPIO**

.. list-table::
   :header-rows: 1

   * -
     - Pin Direction
     - Pin Data out
   * - MxFE0_gpio[0]
     - SW controlled
     - SW controlled
   * - MxFE1_gpio[0]
     - SW controlled
     - SW controlled
   * - MxFE2_gpio[0]
     - SW controlled
     - SW controlled
   * - MxFE3_gpio[0]
     - SW controlled
     - SW controlled

**Gpio_0_mode (GPIO[108]) = 1 --- NCO Sync**

.. list-table::
   :header-rows: 1

   * -
     - Pin Direction
     - Pin Data out
   * - MxFE0_gpio[0]
     - Out
     - MxFE3_gpio[0]
   * - MxFE1_gpio[0]
     - Out
     - MxFE3_gpio[0]
   * - MxFE2_gpio[0]
     - Out
     - MxFE3_gpio[0]
   * - MxFE3_gpio[0]
     - In
     - ---

Function selection for the first six gpio lines is done with the following
control GPIOs:

.. list-table::
   :header-rows: 1

   * - GPIO group
     - Function selection GPIO
   * - MxFE(0,1,2,3)_gpio[0]
     - 108

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B/C High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
