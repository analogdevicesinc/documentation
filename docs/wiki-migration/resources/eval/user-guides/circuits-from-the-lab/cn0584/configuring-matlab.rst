MATLAB Configuration Guide for CN0584
=====================================

Configuring Custom HDL Models using Simulink
--------------------------------------------

Prerequisites:
~~~~~~~~~~~~~~

-  Recommended versions: Vivado 2021.1 – Matlab 2022B_U2

-  Recommended terminal for Windows: Cygwin (https://cygwin.com)

-  Make sure that the Vitis 2021.1 is installed.

-  The latest branch:

:git-HighSpeedConverterToolbox:`tree/cn0585_v1`

Make sure that the “SoC Blockset” and “SoC Blockset Support Package for Xilinx Devices” Add-ons are installed.


|image1|

*Figure 1. SoC Blockset Add-On*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/socblocksetsupportpackage.png

*Figure 2. SoC Blockset Support Package for Xilinx Devices Add-On*

Instructions to build the toolbox from terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1.1** Make a clone of the HDL repo and checkout the desired branch

::

   >git clone https://github.com/analogdevicesinc/HighSpeedConverterToolbox.git
   > cd HighSpeedConverterToolbox 
   ../HighSpeedConverterToolbox> git submodule update --init --recursive 
   ../HighSpeedConverterToolbox > git checkout cn0585_v1 

To avoid tool mismatches, before opening MATLAB set this variable in the terminal:

::

   ../HighSpeedConverterToolbox> export ADI_IGNORE_VERSION_CHECK=TRUE

Build according to the branch

::

   ../HighSpeedConverterToolbox > cd CI/scripts 
   ../HighSpeedConverterToolbox/CI/scripts > make build HDLBRANCH=cn0585_v1 

\*\* 1.2*\* In Matlab current folder list select navigate to the folder where the files had been copied from previous step. Launch MATLAB in the root of the HighSpeedConverterToolbox folder:

::

   ../HighSpeedConverterToolbox/CI/scripts > cd ../../ 
   ../HighSpeedConverterToolbox > matlab . 

Creating BOOT.BIN from Simulink Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/playground/figure3.png
   :width: 400px

*Figure 3. HighSpeedConverterToolbox Sources*

**2.1** Right click on test -> Add to Path -> Selected folders and subfolders. Right click on hdl -> Add to Path -> Selected folders and subfolders. **2.2** In the Matlab command window set the path to Vivado installation folder. The tool path should be replaced with the user’s Vivado path.

e.g. <code> hdlsetuptoolpath(‘ToolName’, ‘Xilinx Vivado’, ’ToolPath’, ‘</opt/Xilinx/Vivado/2021.1/bin/vivado>’) </code>

**2.3** Expand the test folder and double click on the desired Simulink test model, as shown in Figure 4.


|image2|

*Figure 4. Simulink Test Model*

**2.4** After opening the Simulink model, right click on the HDL_DUT and launch the HDL Workflow Advisor as shown in Figure 5, and Figure 6.

.. image:: https://wiki.analog.com/_media/playground/figure6.png
   :width: 600px

*Figure 5. Simulink Device Under Test*

.. image:: https://wiki.analog.com/_media/playground/figure5.png
   :width: 600px

*Figure 6. HDL Workflow Advisor Launching*

**2.5** Close this expected warning that will appear, as shown in Figure 7.

.. image:: https://wiki.analog.com/_media/playground/figure7.png
   :width: 600px

*Figure 7. Expected HDL Workflow Advisor Warning*

**2.6** Select IP Core Generation, choose the desired project and carrier from the dropdown list and check the Allow unsupported version box. Change the project folder name if desired. Finally press the Run this Task button.

.. image:: https://wiki.analog.com/_media/playground/figure8.png
   :width: 600px

//Figure 8. Set Target Device and Synthesis Tool //

**2.7** Choose the RX, RX-TX or TX configuration, then run the task.

.. image:: https://wiki.analog.com/_media/playground/figure9.png
   :width: 600px

*Figure 9. Set Target Reference Design*

**2.8** Assign the data ports as described in Figure 10 and Figure 11, add as many Input/Output registers as you need. Figure 9 and Figure 10 shows data ports for TX configuration. For RX and RX-TX port assignment is done similarly according to Table 2 and Table 3. Table 1 shows port descriptions for HDL DUT Tx Reference Design. AXI registers are defined in the Simulink model as input or output ports (AXI-lite option is selected in “Target Platform Interfaces” column. Register addresses are set in “Interface Mapping” column and written like x”<100, or another 9-bit hex address>”.) AXI registers that are input ports are write-only, and AXI registers that are output ports are read-only. If you connect those two together in the model, you now have a read-only register connected to the write-only register so it is readable, but at a different address.

.. image:: https://wiki.analog.com/_media/playground/figure10.png
   :width: 600px

*Figure 10. Set Input Target Interface*

.. image:: https://wiki.analog.com/_media/playground/figure11.png
   :width: 600px

*Figure 11. Set Output Target Interface*

.. image:: https://wiki.analog.com/_media/playground/table1.png
   :width: 600px

*Table 1: HDL DUT Ports for Transmit Reference Design (Tx)*

.. image:: https://wiki.analog.com/_media/playground/table2.png
   :width: 600px

*Table 2: HDL DUT Ports for Receive Reference Design (Rx)*

.. image:: https://wiki.analog.com/_media/playground/table3.png
   :width: 600px

*Table 3: HDL DUT Ports for Receive-Transmit Reference Design (Rx-Tx)*

-  The CN0585 ADC DATA <x> IN is the data in offset binary format captured by the ADC interface IP. IP sends the data at a variable sample rate (default is 15MHz but can be changed using the IIO Oscilloscope/ Python) along with the validIn<x> signal which has the logic value 1 for a clock period (8.33ns) when the data has changed.
-  IP DATA <x> OUT is the data in offset binary format sent to the DAC interface IP. Data must be sent at 15MSPS when both channels are enabled or at 30MSPS when only one channel is enabled. The validOut<x> signal should have the same behavior as validIn. If you make changes to the data captured by the adc (delay for 1 clock period) and want to send it to the dac output, make sure you delay the validOut signal at the same time. If the feedback resistors are placed in the default position, which is +/-10V, a 0000h code will represent -10.382V and a ffffh code will represent 10.380V as described in Table 4.

.. image:: https://wiki.analog.com/_media/playground/table4.png
   :width: 600px

*Table 4. AD3552R DAC Output Span Configuration*

**2.9** Run the task, as shown in Figure 12.

.. image:: https://wiki.analog.com/_media/playground/figure12.png
   :width: 600px

*Figure 12. Check Model Settings*

**2.10** Select Verilog for the HDL Code Generation Settings, then run task as shown in Figure 13.

.. image:: https://wiki.analog.com/_media/playground/figure13.png
   :width: 600px

*Figure 13. Set HDL Options*

**2.11** Check the Enable readback on AXI4 slave write registers as described in Figure 14. Then run task.

.. image:: https://wiki.analog.com/_media/playground/figure14.png
   :width: 600px

*Figure 14. Generate RTL code and IP Core*

**2.12** Run the task (this will create the Vivado block design in the hdl_prj/vivado_ip_prj folder, or the project folder name that was chosen in 1.6), as shown in Figure 15.

.. image:: https://wiki.analog.com/_media/playground/figure15.png
   :width: 600px

*Figure 15. Create Project*

**2.13** Run the task in Figure 16.

.. image:: https://wiki.analog.com/_media/playground/figure16.png
   :width: 600px

*Figure 16. Generate Software Interface*

**2.14** Choose the “Custom” option for the Tcl file synthesis build, then Browse for the adi_build.tcl file located under HighSpeedConverterToolbox/CI/scripts, as shown in Figure 17. A bash prompt will open, and you can see the entire build process log file, as shown in Figure 17 and Figure 18. This step usually takes about an hour or more.

.. image:: https://wiki.analog.com/_media/playground/figure17.png
   :width: 600px

*Figure 17. Build FPGA Bitstream*

.. image:: https://wiki.analog.com/_media/playground/figure18.png
   :width: 600px

*Figure 18. Build FPGA Bitstream Task Complete Message*

In the end you will get this message, and the generated BOOT.BIN file will be located in:

::

   /HighSpeedConverterToolbox/hdl_prj/vivado_ip_prj/boot

**2.15** Program target device

Tab 4.4 in the HDL Workflow Advisor is incompatible with The ADI SD card flow. Instead, choose one of the following methods to update the BOOT.BIN file on the SD card (BOOT.BIN with register access found in `sd_card_config_files_revb.zip <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/sd_card_config_files_revb.zip>`_). After the BOOT.BIN file is generated, you have 2 options:

-  1. Copy the BOOT.BIN file on the SD Card directly.

-  2. Send it via network using a terminal (CMD for Windows machine):

-  Go to the folder where the BOOT.BIN file is:

::

    HighSpeedConverterToolbox/hdl_prj/vivado_ip_prj/boot

-  Run this command:

::

    scp BOOT.BIN root@<your_board_ip>:/boot 

Finally, reboot the board.

Register Access Options
~~~~~~~~~~~~~~~~~~~~~~~

AXI-Lite registers in HDL_DUT can be accessed using one of the below three options:

PyADI-IIO
^^^^^^^^^

Get the PyADI-IIO repo, and switch to the compatible branch.

::

   git clone https://github.com/analogdevicesinc/pyadi-iio.git
   cd pyadi-iio  
   git checkout cn0585_v1     

Setup Python and run the example file. The path in the first line should be replaced with the location where you cloned the pyadi-iio repository.

::

   export PYTHONPATH=C:/work/python_LLDK/documentation_clone/pyadi-iio/  
   > ../pyadi-iio > pip install .  
   > ../pyadi-iio > pip install -r requirements.txt  
   > ../pyadi-iio > pip install -r requirements_dev.txt  
   > ../pyadi-iio> python examples/cn0585_fmcz_example.py ip:<your_board_ip> 

The console output will contain these 2 new lines:

::

   AXI4-Lite 0x108 register value: 0x2 
   AXI4-Lite 0x10c register value: 0xB 

These are the functions that were added to be able to access the HDL_DUT IP registers trough AXI4-Lite:

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

-  Open the CN0585StreamingTest.m file in Matlab

-  Update the board_ip variable with your board IP.

-  Run the CN0585StreamingTest.m example.

The output described by Figure 19 can be observed in the Command Window.

.. image:: https://wiki.analog.com/_media/playground/figure19.png
   :width: 600px

*Figure 19. MATLAB Command Window Output*

These are the functions that were added to be able to access the HDL DUT IP registers trough AXI4-Lite:

::

   write_reg = soc.libiio.aximm.WriteHost(devName='mwipcore0:mmwrchannel0',IPAddress=board_ip); 
   read_reg = soc.libiio.aximm.WriteHost(devName='mwipcore0:mmrdchannel1',IPAddress=board_ip); 
   write_reg.writeReg(hex2dec('100'),85) 
   write_reg.writeReg(hex2dec('104'),22)

Simulink
^^^^^^^^

-  From the HighSpeedConverterToolbox/test folder open the cn0585_host_axi4_lite_read_write_example.slx file.

-  Update the IP address for all the blocks existing in the host diagram.

-  Modify the value in the constant block to write to the register. Open the scope block to read the register.

.. image:: https://wiki.analog.com/_media/playground/figure20.png
   :width: 600px

*Figure 20. Host Simulink Block Diagram*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/socblocksetaddon.png
.. |image2| image:: https://wiki.analog.com/_media/playground/figure4.png
