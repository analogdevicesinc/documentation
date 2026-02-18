.. _eval-cn0584-ebz matlab-configuration:

MATLAB Configuration
=====================

Configuring Custom HDL Models using Simulink
--------------------------------------------

Prerequisites
~~~~~~~~~~~~~~

- Recommended versions: Vivado 2021.1 – Matlab 2022B_U2
- Recommended terminal for Windows: Cygwin (https://cygwin.com)
- Make sure that the Vitis 2021.1 is installed.
- The latest branch: :git-HighSpeedConverterToolbox:`cn0585_v1:`

Make sure that the “SoC Blockset” and “SoC Blockset Support Package for Xilinx
Devices” Add-ons are installed.

.. figure:: socblocksetaddon.png

    SoC Blockset Add-On

.. figure:: socblocksetsupportpackage.png

    SoC Blockset Support Package for Xilinx Devices Add-On

Instructions to build the toolbox from terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1.1** Make a clone of the HDL repo and checkout the desired branch

.. shell::

   $git clone https://github.com/analogdevicesinc/HighSpeedConverterToolbox.git
   $cd HighSpeedConverterToolbox
   $git submodule update --init --recursive
   $git checkout cn0585_v1

To avoid tool mismatches, before opening MATLAB set this variable in the
terminal:

.. shell::

   ~/HighSpeedConverterToolbox
   $export ADI_IGNORE_VERSION_CHECK=TRUE

Build according to the branch

.. shell::

   ~/HighSpeedConverterToolbox
   $cd CI/scripts
   $make build HDLBRANCH=cn0585_v1

**1.2** In Matlab current folder list, navigate to the folder where
the files had been copied from previous step. Launch MATLAB in the root of the
HighSpeedConverterToolbox folder:

.. shell::

   ~/HighSpeedConverterToolbox/CI/scripts
   $cd ../../
   $matlab .

Creating BOOT.BIN from Simulink Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figure3.png

    HighSpeedConverterToolbox Sources

**2.1** Right click on test -> Add to Path -> Selected folders and subfolders.
Right click on hdl -> Add to Path -> Selected folders and subfolders.

**2.2** In the Matlab command window set the path to Vivado installation folder. The tool
path should be replaced with the user’s Vivado path.

For example:

.. code-block:: matlab

     hdlsetuptoolpath(‘ToolName’, ‘Xilinx Vivado’, ’ToolPath’,
     ‘</opt/Xilinx/Vivado/2021.1/bin/vivado>’)

**2.3** Expand the test folder and double click on the desired Simulink test
model, as shown in Figure 4.

.. figure:: figure4.png

    Simulink Test Model

**2.4** After opening the Simulink model, right click on the ``HDL_DUT`` and launch
the HDL Workflow Advisor as shown in Figure 5, and Figure 6.

.. figure:: figure6.png

    Simulink Device Under Test

.. figure:: figure5.png

    HDL Workflow Advisor Launching

**2.5** Close this expected warning that will appear, as shown in Figure 7.

.. figure:: figure7.png

    Expected HDL Workflow Advisor Warning

**2.6** Select IP Core Generation, choose the desired project and carrier from
the dropdown list and check the Allow unsupported version box. Change the
project folder name if desired. Finally press the ``Run this Task`` button.

.. figure:: figure8.png

    Set Target Device and Synthesis Tool

**2.7** Choose the RX, RX-TX or TX configuration, then run the task.

.. figure:: figure9.png

    Set Target Reference Design

**2.8** Assign the data ports as described in Figure 10 and Figure 11, add as
many Input/Output registers as you need. Figure 9 and Figure 10 shows data ports
for TX configuration address.

.. figure:: figure10.png

    Set Input Target Interface

.. figure:: figure11.png

    Set Output Target Interface

For RX and RX-TX port assignment is done similarly according to Table 2 and Table 3.
Table 1 shows port descriptions for HDL DUT Tx Reference Design.

AXI registers are defined in the Simulink model as input or
output ports (AXI-lite option is selected in “Target Platform Interfaces”
column. Register addresses are set in “Interface Mapping” column and written
like x”<100, or another 9-bit hex address>”.) AXI registers that are input ports
are write-only, and AXI registers that are output ports are read-only. If you
connect those two together in the model, you now have a read-only register
connected to the write-only register so it is readable, but at a different address.

.. figure:: table1.png

    HDL DUT Ports for Transmit Reference Design (Tx)

.. figure:: table2.png

    HDL DUT Ports for Receive Reference Design (Rx)

.. figure:: table3.png

    HDL DUT Ports for Receive-Transmit Reference Design (Rx-Tx)

-   The CN0585 ADC DATA <x> IN is the data in offset binary format captured by the
    ADC interface IP. IP sends the data at a variable sample rate (default is
    15MHz but can be changed using the IIO Oscilloscope/ Python) along with the
    validIn<x> signal which has the logic value 1 for a clock period (8.33ns) when
    the data has changed.

-   IP DATA <x> OUT is the data in offset binary format sent to the DAC interface IP.
    Data must be sent at 15MSPS when both channels are enabled or at 30MSPS
    when only one channel is enabled. The validOut<x> signal should have the same
    behavior as validIn. If you make changes to the data captured by the adc
    (delay for 1 clock period) and want to send it to the dac output, make sure
    you delay the validOut signal at the same time. If the feedback resistors are
    placed in the default position, which is +/-10V, a 0000h code will represent
    -10.382V and a ffffh code will represent 10.380V as described in Table 4.

.. figure:: table4.png

    AD3552R DAC Output Span Configuration

**2.9** Run the task, as shown in Figure 12.

.. figure:: figure12.png

    Check Model Settings

**2.10** Select Verilog for the HDL Code Generation Settings, then run task as
shown in Figure 13.

.. figure:: figure13.png

    Set HDL Options

**2.11** Check the Enable readback on AXI4 slave write registers as described in
Figure 14. Then run task.

.. figure:: figure14.png

    Generate RTL code and IP Core

**2.12** Run the task (this will create the Vivado block design in the
hdl_prj/vivado_ip_prj folder, or the project folder name that was chosen in
1.6), as shown in Figure 15.

.. figure:: figure15.png

    Create Project

**2.13** Run the task in Figure 16.

.. figure:: figure16.png

    Generate Software Interface

**2.14** Choose the “Custom” option for the Tcl file synthesis build, then
Browse for the adi_build.tcl file located under HighSpeedConverterToolbox/CI/scripts,
as shown in Figure 17. A bash prompt will open, and you can see the entire build process log file,
as shown in Figure 17 and Figure 18. This step usually takes about an hour or more.

.. figure:: figure17.png

    Build FPGA Bitstream

.. figure:: figure18.png

    Build FPGA Bitstream Task Complete Message

In the end you will get this message, and the generated BOOT.BIN file will be
located in:

    ::

        /HighSpeedConverterToolbox/hdl_prj/vivado_ip_prj/boot

**2.15** Program target device

Tab 4.4 in the HDL Workflow Advisor is incompatible with The ADI SD card flow.
Instead, choose one of the following methods to update the BOOT.BIN file on the
SD card (BOOT.BIN with register access found in :download:`SD Card Configuration Files<sd_card_config_files_revb.zip>`).
After the BOOT.BIN file is generated, you have 2 options:

    #. Copy the BOOT.BIN file on the SD Card directly.

    #.  Send it via network using a terminal (CMD for Windows machine).

    #.  Go to the folder where the BOOT.BIN file is:

        ::

            HighSpeedConverterToolbox/hdl_prj/vivado_ip_prj/boot

    #.  Run this command:

        ::

            scp BOOT.BIN root@<your_board_ip>:/boot

    #. Finally, reboot the board.

Register Access Options
~~~~~~~~~~~~~~~~~~~~~~~

AXI-Lite registers in HDL_DUT can be accessed using one of the below three
options:

PyADI-IIO
^^^^^^^^^

Get the PyADI-IIO repo, and switch to the compatible branch.

.. shell::

   $git clone https://github.com/analogdevicesinc/pyadi-iio.git
   $cd pyadi-iio 
   $git checkout cn0585_v1    

Setup Python and run the example file. The path in the first line should be
replaced with the location where you cloned the pyadi-iio repository.

.. shell:: ps1

   ~/pyadi-iio
   export PYTHONPATH=C:\work\python_LLDK\documentation_clone\pyadi-iio
   $pip install . 
   $pip install -r requirements.txt 
   $pip install -r requirements_dev.txt 
   $python examples/cn0585_fmcz_example.py ip:<your_board_ip>

The console output will contain these 2 new lines:

::

   AXI4-Lite 0x108 register value: 0x2
   AXI4-Lite 0x10c register value: 0xB

These are the functions that were added to be able to access the HDL_DUT IP
registers trough AXI4-Lite:

::

   if hdl_dut_write_channel.check_matlab_ip() :
       hdl_dut_write_channel.axi4_lite_register_write(0x100, 0x2)
       hdl_dut_write_channel.axi4_lite_register_write(0x104, 0xB)

   if hdl_dut_write_channel.check_matlab_ip() :
       reg_value = hdl_dut_read_channel.axi4_lite_register_read(0x108)
       reg_value1 = hdl_dut_read_channel.axi4_lite_register_read(0x10C)
       print("AXI4-Lite 0x108 register value:", reg_value)
       print("AXI4-Lite 0x10c register value:", reg_value1)

MATLAB
^^^^^^

- Open the CN0585StreamingTest.m file in Matlab
- Update the board_ip variable with your board IP.
- Run the CN0585StreamingTest.m example.
  The output shown in Figure 19 can be observed in the Command Window.

        .. figure:: figure19.png

            MATLAB Command Window Output

        These are the functions that were added to be able to access the HDL DUT IP
        registers trough AXI4-Lite:

        .. code-block:: matlab

            write_reg = soc.libiio.aximm.WriteHost(devName='mwipcore0:mmwrchannel0',IPAddress=board_ip);
            read_reg = soc.libiio.aximm.WriteHost(devName='mwipcore0:mmrdchannel1',IPAddress=board_ip);
            write_reg.writeReg(hex2dec('100'),85)
            write_reg.writeReg(hex2dec('104'),22)

Simulink
^^^^^^^^

- From the HighSpeedConverterToolbox/test folder open the
  cn0585_host_axi4_lite_read_write_example.slx file.
- Update the IP address for all the blocks existing in the host diagram.
- Modify the value in the constant block to write to the register. Open the
  scope block to read the register.

    .. figure:: figure20.png

        Host Simulink Block Diagram
