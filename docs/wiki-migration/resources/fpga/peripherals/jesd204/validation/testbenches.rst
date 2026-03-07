JESD204 Testbenches
===================

Various levels of testbenches are available from component level to system level covering the whole stack including physical layer, link layer and transport layer components.

Component level testbenches
---------------------------

Location of testbenches
~~~~~~~~~~~~~~~~~~~~~~~

The component level testbnenches are located in the hdl repository, near to the JESD204 IPs itself in the tb folder.

:git-hdl:`Component level testbenches <library/jesd204/tb>`

Supported simulators
~~~~~~~~~~~~~~~~~~~~

The simulator can be selected through the SIMULATOR environment variable. Supported values are:

========== ==================================
$SIMULATOR Simulator name
========== ==================================
modelsim   Menthor/Siemens ModelSim/QuestaSim
xsim       Xilinx Vivado
xcelium    Cadence Xcelium
(default)  Icarus Verilog (iverilog)
========== ==================================

How to run the tb:
~~~~~~~~~~~~~~~~~~

-  open up a Cygwin or bash terminal
-  go to the library/jesd204/tb folder
-  set up the selected simulator by setting the $SIMULATOR environment variable with the corresponding value listed above.
-  launch the simulation by executing one of the below scripts

   -  axi_jesd204_rx_regmap_tb
   -  axi_jesd204_tx_regmap_tb
   -  crc12_tb
   -  frame_align_tb
   -  jesd204_frame_align_replace_tb
   -  jesd204_frame_mark_tb
   -  loopback_64b_tb
   -  loopback_tb
   -  rx_cgs_tb
   -  rx_ctrl_tb
   -  rx_lane_tb
   -  rx_tb
   -  scrambler_64b_tb
   -  scrambler_tb
   -  soft_pcs_8b10b_sequence_tb
   -  soft_pcs_8b10b_table_tb
   -  soft_pcs_loopback_tb
   -  soft_pcs_pattern_align_tb
   -  tx_64b_tb
   -  tx_ctrl_phase_tb
   -  tx_tb

System level testbenches
------------------------

The system level testbenches reside in a separate github repository: :git-testbenches:`testbenches <tree/main>` repo

.. _supported-simulators-1:

Supported simulators
~~~~~~~~~~~~~~~~~~~~

The test environment is built around Xilinx AXI VIPs so the only supported simulator is:

-  Xilinx Vivado matching the current hdl release version requirements

List of JESD system level testbenches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:git-testbenches:`jesd_loopback` - A generic testbench covering the ADI JESD framework physical layer, link layer and transport layer components, supporting 204B or 204C 64b66b operation modes.

:git-testbenches:`jesd_loopback_64b` - A JESD testbench with Xilinx PHY supporting only the 64b66b mode

Testbench architecture
~~~~~~~~~~~~~~~~~~~~~~

The devices under test (jesd204 components) are placed in a test harness which is made of several Xilinx verification IP's: clock and reset generators, AXI verification IPs to emulate the control side of the processor or to emulate a DDR storage module.

.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/jesd204/validation/examplesystemleveltestbench.jpg
   :align: center

SV API packages
^^^^^^^^^^^^^^^

-  `adi_jesd204_pkg.sv <https://www.github.com/analogdevicesinc/testbenches/blob/main/common/sv/adi_jesd204_pkg.sv>`_ - JESD204 link layer package, a collection of tasks and functions to high level control the link layer transmit and receive peripherals
-  `adi_xcvr_pkg.sv <https://www.github.com/analogdevicesinc/testbenches/blob/main/common/sv/adi_xcvr_pkg.sv>`_ - JESD204 physical layer package, a collection of tasks and functions to high level control and automatically configure the transceivers for a given lane rate and reference clock

.. _how-to-run-the-tb-1:

How to run the tb
~~~~~~~~~~~~~~~~~

Details on running the testbench you can find in the :git-testbenches:`jesd_loopback/README.md` of each testbench and in the general :git-testbenches:`README.md` of the repository.

Technical Support
-----------------

Analog Devices will provide limited online support for anyone using the core with Analog Devices components (ADC, DAC, Clock, etc) via the :ez:`EngineerZone <community/fpga>` under the GPL license. If you would like deterministic support when using this core with an ADI component, please investigate a commercial license. Using a non-ADI JESD204 device with this core is possible under the GPL, but Analog Devices will not help with issues you may encounter.

More Information
----------------

-  :doc:`JESD204 High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`
