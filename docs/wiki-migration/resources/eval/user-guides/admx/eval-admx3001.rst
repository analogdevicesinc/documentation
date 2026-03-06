<fc #ff0000>BE AWARE UNDER CONSTRUCTION</fc>

EVAL-ADMX3001 Power Supply & Load Evaluation Board
==================================================

<fc #ff0000>Just to Start</fc>

.. warning::

   WARNING: High Voltage!


Features
--------

-  Four Channels
-  Four Quadrant
-  Digital control to optimize source step response

   -  PID Coefficients adjustable for forcing and clamping

-  Multiple force/measure voltage ranges

   -  ±100V, ±10V, ±1V
   -  <50µV force & clamp resolution
   -  0.5µV measurement resolution (in 1V range)

-  Seven force/measure current ranges

   -  ±1A, ±100mA, ±10mA, ±1mA, ±100µA, ±10µA, ±1µA
   -  <100pA force & clamp resolution (in 1µA range)
   -  <10pA measurement resolution

-  Pulsed operation

   -  100µs to 100ms width pulses

-  0.02% FV accuracy (+/-100V range) after factory calibration
-  0.02% FI accuracy (+/- 10mA range) after factory calibration
-  Safety features

   -  Includes an acrylic enclosure to provide protection from high voltage
   -  Equipped with interlock circuits and connector integrated into the board

-  FMC (VITA-57) compliant daughter card
-  Safe Operating Range Plot

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/thereminsoa.png
   :width: 400px

Package Content
---------------

-   EVAL-ADMX3001-EBZ Board
-   Power cable – Mini-Fit Jr. Female to Pigtail
-   Phoenix Connector Terminal Blocks

Additional Equipment Needed
---------------------------

-  Xilinx KCU105 Evaluation Board
-  Benchtop Power supply or Power Supply from Protek PMP400
-  Power supply connector to be attached to the pigtail of the Mini-Fit Jr Female cable

Software, Application Tools, and Driver Needed
----------------------------------------------

-  Vivado Lab Edition, 2022.2

   -  Xilinx Downloads

-  Silicon Labs USB to UART Virtual COM Port Driver

   -  Silicon Labs VCP Windows Driver

-  Terminal Emulator - PuTTY
-  ACE Software

   -  ADMX3001 ACE plug-in
   -  Hardware.COMSupport plug-in

-  Admx3001Firmware-Rel1.7.0_EVAL.exe

   -  admx3001_app_kcu105.bin

General Description
-------------------

The ADMX3001 is a source measure unit that can provide up to +/- 100V and +/- 1A. It utilizes the AD3552R, a low drift, high precision, 16-bit DAC to set the programmable inputs to the next-generation high-voltage, high-current precision op amp, which serves as the output driver of this supply. The complete solution incorporates the AD4630-24 precision ADC, working in conjunction with a firmware-based PID control loop. The ADMX3001 is a complete four-channel solution with seven current ranges from 1 µA to 1 A and three voltage ranges: 1V, 10V, and 100V. Each channel uses programmable output driver supplies with the potential to minimize power loss, which helps simplify thermal design. This design can reduce space and cost in many instruments, while also simplifying and accelerating the time-to-market.

Block Diagram of One Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/blockdiagram.png
   :alt: blockdiagram.png

PID Firmware Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/the_smu_blk_dia.png
   :align: right

Evaluation Kit Contents
-----------------------

-  EVAL-ADMX3001-EBZ Board

| 
| ==== Additional Equipment Required ====

-  `Power Supply from Protek PMP400 <https://www.protek.com.tw/en/product/medicaladapter/PMP400.html>`__ or equivalent
-  `Xilinx KC705 Evaluation Board <https://www.xilinx.com/products/boards-and-kits/ek-k7-kc705-g.html>`__
-  `Cooling Fan for ADHV4711 <https://www.amazon.com/Kulannder-Absorber-Remover-Extrator-Prevention/dp/B0711LFYJ1/ref=pd_lutyp_d_rtpb_sccl_1_1/135-5349505-3900650?pd_rd_w=eQvad&content-id=amzn1.sym.356b6742-af77-4137-8d9e-8870729df5de&pf_rd_p=356b6742-af77-4137-8d9e-8870729df5de&pf_rd_r=BC67TNTXBXM7F0MQ6QDV&pd_rd_wg=CVCNH&pd_rd_r=5cbd0b90-4656-422a-ba69-7e647d12def9&pd_rd_i=B0711LFYJ1&th=1>`__ or equivalent

| 

Application Tools & Drivers
---------------------------

Application to install bin files into KC705
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| `Xilinx Downloads <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/2022-2.html>`__ |image1|

Silicon Labs USB to UART Virtual COM Port Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Silicon Labs VCP Windows Driver <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads>`__

Bit file to reprogram KC705 VAdjust
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`kc705_setup.bit <https://wiki.analog.com/_media/resources/eval/user-guides/admx/kc705_setup.zip>`__

--------------

Quick Start
^^^^^^^^^^^

There are five simple steps to start evaluating the ADMX3001:

-  First Time Setup of KC705
-  Basic Hardware Setup
-  Open a session through the terminal emulator (e.g. PuTTY)
-  Customer Evaluation Software (ACE)
-  Performing Basic Measurements

These steps are explained in detail in the following sections.

| 

--------------

1. First Time Set-up of KC705
-----------------------------

VADJ Configuration:
~~~~~~~~~~~~~~~~~~~

The KC705 sets the VADJ to 2.5V by default upon power up. To modify output of VADJ to 1.8V, please use the following instructions.

-  The following bit file can be used to modify VADJ: `kc705_setup.bit <https://wiki.analog.com/_media/resources/eval/user-guides/admx/kc705_setup.zip>`__
-  The bit file automatically sends the following PMBUS commands to the UCD9248

|image2|

-  Once the \*.bit file is downloaded and Vivado is installed, plug the KC705 into your PC and power it on.
-  Launch Vivado and open the Hardware Manager

|image3|

-  Click 'Open Target' and then 'Auto Connect'

|image4|

-  Select the path to the kc705_setup.bit file and click 'Program'

|image5|

-  Once the \*.bit file is programmed, the VADJ rail should be automatically set to 1.8V. After the programming is complete, the GPIO 0 LED should be lit up as shown

|image6|

-  Power cycle the KC705 and verify that the VADJ settings were set correctly with an external multimeter

|

.. note::

   The default communication interface to EVAL-ADMX3001EBZ is via its UART port. When using the UART to USB cable included with the KC705.


Program Flash:
~~~~~~~~~~~~~~

-  Once Vivado has been installed, open the application and click on Open Hardware Manager


|image7|

-  When Hardware Manager is opened a green bar will appear. Click on Open Target

|image8|

-  Open Target will have a dropdown menu, click on Open New Target and then click Next

|image9|

-  If you want to connect to the board in Remote PC select 'Remote Server' and refer to `Remote FPGA Programming or Debugging <https://confluence.analog.com/display/THE/Remote+FPGA+Programming+or+Debugging>`__ for further instructions. If you are connecting to local target select 'Local Server' and then click Next

|image10|

-  A pop-up window will appear with to indicate connection to the server, wait for connection to be complete

|image11|

-  List of FPGA targets will be shown. If xc7k325t_0 is shown then the FPGA is detected. If any errors occur or the list is empty, then please check the JTAG connection/ board powered on/ driver installed properly. Click Next and Finish in the summary page |image12|

|image13|

-  If the FPGA is detected, the Hardware manager will show a connection to the FPGA under the Hardware tab

|image14|

-  Right click on the FPGA device to get Program Device menu then click on Add Configuration Memory Device

|image15|

-  Search for 28f00ap30t device, select the corresponding part and then click OK

|image16|

-  Click OK when Add Configuration Memory Device Completed Prompt appears

|image17|

-  Browse and select the bin file. Make sure to check the Erase, Program, and Verify options, then click OK

|image18|

-  Wait for Programming to be successful
-  Once flashing is done, either power cycle the device or click on the FPGA part and choose Boot from Configuration Memory Device

|image19|

--------------

2. Basic Hardware Setup
-----------------------

The following figure shows the basic connections required for evaluating the AMDX3001.


|image20|

-  Connect the ADMX3001 board to the KC705 board using the FMC Connectors in the location shown above
-  Connect the power supply (12V - 48V) to the ADMX3001
-  Connect the wall mount transformer to power the KC705 board
-  Connect the Serial Port on the KC705 to a PC

| |image21|

--------------

3. Opening a Session via Terminal Emulator - PuTTY
--------------------------------------------------

Terminal Emulator Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To communicate with ADMX3001 via its command-line interface and UART of KC705, a terminal emulator such as PuTTY is recommended. Visit the URL below to download PuTTY

.. note::

   \ https://www.putty.org/\


| Download the MSI (Windows Installer) and execute it. Follow the on-screen instructions.
| In order to utilize the COM port for UART communication a USB to UART Driver must be installed. Follow the instructions to download the driver. https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads If installed correctly, the set-up should be detected under Device Manager.

Opening Session via Putty
~~~~~~~~~~~~~~~~~~~~~~~~~

| After installing PuTTY, select the Serial connection session, and configure the Serial category as shown below. Please note that the COM port can be seen in Device Manager on the local computer.
| |image22|
| |image23|

Make sure the hardware is properly installed and that power is available to the board via the 12V power adapter. Then, simply “Open” a serial connection to initiate the session. PuTTY will launch a blank window.

-  Press ENTER to display the ADMX3001> prompt
-  Type ``*idn?`` and press ENTER to display the firmware version
-  Type ``help`` and press ENTER to see a list of commands supported by ADMX3001.

For a complete list of ADMX3001 commands, please refer to the Command Reference section in this page.

| Please note that closing PuTTY's terminal window does not reset the ADMX3001 settings from the last session.

--------------

4. Customer Software (ACE)
--------------------------

Installing ACE
~~~~~~~~~~~~~~

Analysis, Control, Evaluation (ACE) is an extensible software platform that can be used by customers to evluate a wide array of products and boards in ADI's portfolio. The ACE installer can be downloaded from the following: :adi:`ace-software.html <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`

Once ACE is installed, double-click on the file and it should install the plugin and launch ACE. The ADMX3001 plugin can be installed with the ACEZIP file provided when the board is recieved.

User Functionality of the GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All widgets enclosed in the pink boxes are ONLY updates when the 'Configure Channel' button is pressed. All values can be edited in any order, but when 'Configure Channel' is pressed, every corresponding serial command will execute.

The PID controls enclosed in the blue boxes can be edited on the fly (regardless if the GO command has already been issues) and can be edited in any order.

Once you've set up all the necessary parameters for the current active selected channel and 'Configure Channel' has been pressed, the user can choose a different channel in the drop down and the GUI will update to read the current status for all the parameters for that newly selected channel. The user can then choose to change any parameters, click 'Configure Channel' to program each channel individually.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx3001configure_channel-and-pid.png
   :width: 400px

If the user wishes to read multiple data samples for a given channel, the "Enable FIFO Data Acq" toggle switch must be ON/enabled and a FIFO Sample Count value desired can be selected, as shown in the orange enclosed box. This must be done BEFORE issuing any Go command/clicking the "Go" button and the selected channel must be enabled to run and acquire data. Once a channel is running then the "Take Measurement" button can be clicked which will return the data for the active channel with all of the sample points acquired by the FIFO.

For debugging purposes, there is a direct access (like any serial port terminal application such as putty) for the user to type any command they want in the 'Raw Serial Command' textbox and then click 'Send Serial Command' and the response string from the serial command will be displayed in the 'Serial Response' text box, as shown all enclosed in the purple box.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx3001readfifo_and_clidebughook.png
   :width: 400px

Once all channels desired to be configured and enabled have been executed by the user and they want to run channels, the 'Go' button can be pressed. Any enabled channels will show that the channel output is running and all widgets that can not be configured on the fly will be grayed out. The only parameters that can be changed after a Go command is issued are the PID controls and the Voltage (if in Forced Voltage mode) or Current (if in Forced Current mode) IF the desired value is within the already configured voltage or current ranges, respectively. If any other configurations on any channels need to be changed, the user must first click the 'Abort Channel' button. This will also disable all channels (this is the only way to disable a channel, once a channel is enabled the only way to disable is to click 'Abort Channel'.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/admx3001go_abort_enable.png
   :width: 400px

--------------

5. Performing Basic Measurements
--------------------------------

.. note::

   The measurements reported by the module will not be accurate unless it has been calibrated. For detailed instructions on how to calibrate the module, please refer to the Calibration Procedure section in this user guide.


.. note::

   Please note that the following are basic examples of using both methods of Putty and Customer Evaluation Software(ACE) to force a Voltage and Current using the ADMX3001 and reading back the measured values.


Forcing and Measuring Voltage with Putty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Upon start-up the ADMX3001 is in 'force voltage' mode. To force a voltage, please make sure to enable the channel and then set the voltage. This is completed through the following commands:
| |image24|
| To measure voltage, utilize the 'measure v' command. As seen below, only the channel that was enabled and set has a proper reading.
| |image25|

Forcing and Measuring Current with Putty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| To force a current, the channel heeds to be changed to 'mode fi' which is force current mode. Once force current mode is enabled, a current can be set in the channel.

.. note::

   If the board is running (go is enabled), it should be stopped before trying to change the mode of the board. If a channel is running and is it force voltage mode, the abort command needs to be run before switching to force current mode.


| |image26|
| To measure current, utilize the 'measure i' command. As seen below, only the channel that was enabled and set has a proper reading.
| |image27|
| === Forcing and Measuring Voltage with ACE === Another method to interact with the ADMX3001 is to use the customer evaluation software (ACE) provided. This is a GUI that can be used to perform the same tasks as the CLI. To force and measure voltage using ACE, the channel is selected at the top drop down, then the mode (force voltage) can also be selected. Once the correct channel and mode are selected, type in the desired voltage into the text box, and click configure channel. In the right hand side, enable the desired channels and click 'enable channels'. Once the channel is configured click 'go'. Select the measurement type in the bottom left-hand corner and then click 'take measurement'. Now the measurements can be seen in the text boxes. |image28|

Forcing and Measuring Current with ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To force and measure current using ACE, the mode must be changed to 'force current', this can be done using the dropdown menu below the current box. Once force current mode is selected, input the desired current in the textbox. Once the desired current is inputted into the textbox click 'configure channel'. In the right hand side, enable the desired channels and click 'enable channels'. Once the channel is configured click 'go'. Select the measurement type in the bottom left-hand corner and then click 'take measurement'. Now the measurements can be seen in the text boxes.


|image29|

--------------

6. Performing Advanced Measurements
-----------------------------------

.. note::

   The measurements reported by the module will not be accurate unless it has been calibrated. For detailed instructions on how to calibrate the module, please refer to the Calibration Procedure section in this user guide.


.. note::

   The following are advanced examples of measurements that can be performed using Putty or another serial terminal emulator.


Making Measurements over a Pulse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the channel is in pulse mode, using the standard 'measure i', 'measure v' or 'measure all' commands might not capture a value from the desired point in time of a pulse. The 'measure rf' command can be used instead to capture a measurement at a specific point in the pulse, or over the length of the entire pulse.

| The following command sequence could be used to take a single 60 point average measurement 50us through a 100us on/100us off pulse:
| |image30|
| The following command sequence performs an aperture measurement every 0.5us to get an array of 399 voltages and currents over the length of a 100us on/100us off pulse:
| |image31|
| ----

7. Using the Online Help in the Command-Line Interface
------------------------------------------------------

| The ``help`` command will display all the commands available to the user from the command-line interface (CLI). |image32|
| To get help for any command, simply type

::

   ADMX3001> help <command>


   | 

--------------

Command Reference
^^^^^^^^^^^^^^^^^

Operation
---------

|

| ^ Command ^ Parameters ^

+--------+------------------------------------------------------------------------------------------------------------------------------+
| go     | -                                                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------+
| abort  | -                                                                                                                            |
+--------+------------------------------------------------------------------------------------------------------------------------------+
| enable | [ <channel> ] (selects the channel to be enabled. when the go command is executed it shall only operate in enabled channels) |
+--------+------------------------------------------------------------------------------------------------------------------------------+

| 

Source and Measurement Configuration
------------------------------------

|

| ^ Command ^ Parameters ^

+----------+------------------------------------------------------------------------------------------------------+
| channel  | [ <channel>] (selects the channel to be configured)                                                  |
+----------+------------------------------------------------------------------------------------------------------+
| measure  | [ voltage / current / all / rf ]                                                                     |
+----------+------------------------------------------------------------------------------------------------------+
| voltage  | [ <voltage> ]                                                                                        |
+----------+------------------------------------------------------------------------------------------------------+
| current  | [ <current> ]                                                                                        |
+----------+------------------------------------------------------------------------------------------------------+
| vclamp   | [ <voltage> / <positive_voltage> <negative_voltage>]                                                 |
+----------+------------------------------------------------------------------------------------------------------+
| iclamp   | [ <current> / <positive_current> <negative_current>]                                                 |
+----------+------------------------------------------------------------------------------------------------------+
| vrange   | [ <voltage> ]                                                                                        |
+----------+------------------------------------------------------------------------------------------------------+
| irange   | [ <current> ]                                                                                        |
+----------+------------------------------------------------------------------------------------------------------+
| mode     | [ fv / fi ]                                                                                          |
+----------+------------------------------------------------------------------------------------------------------+
| pulse    | [ [ <on_duration> / <off_duration> ] / off ]                                                         |
+----------+------------------------------------------------------------------------------------------------------+
| gang     | [on <leader_ch> <member_ch_a> ... <member_ch_b> / off]                                               |
+----------+------------------------------------------------------------------------------------------------------+
| gmode    | [fv / fi / fvleader]                                                                                 |
+----------+------------------------------------------------------------------------------------------------------+
| vsense   | [ local / remote ] 0: local, 1: remote                                                               |
+----------+------------------------------------------------------------------------------------------------------+
| average  | [ <n> ] Number of samples to be used for averaging the voltage and current ADC data. Range: 1 - 1024 |
+----------+------------------------------------------------------------------------------------------------------+
| measmode | [ <mode> ] Select the measurement mode. 0: Average, 1: Aperture                                      |
+----------+------------------------------------------------------------------------------------------------------+
| scount   | [ <n> ] Number of samples to be read from the fifo when using measure rf command. Range: 1 - 1024    |
+----------+------------------------------------------------------------------------------------------------------+
| enacq    | [ <enable> ] Enable or Disable the acquisition. 0: Disable, 1: Enable                                |
+----------+------------------------------------------------------------------------------------------------------+

| 

Measurement Timing
------------------

|

| ^ Command ^ Parameters ^

======== =====================================
aperture [ <time (us)> ] Range: 500ns to 512us
mdelay   [ <time (ms)> ] Range: 500ns to 500ms
count    [ <n> ] (pulse count)
======== =====================================

| 

Calibration
-----------

|

| ^ Command ^ Parameters ^

===== ================================================================
rdcal [<channel> <vrange> <irange>] Reads the calibration coefficients
===== ================================================================

| 
| ==== Utility ====
| ^ Command ^ Parameters ^

+--------------+--------------------------------------------------------------+
| \*idn?       | Displays board information, firmware revision, build details |
+--------------+--------------------------------------------------------------+
| help         | [ <command> ]                                                |
+--------------+--------------------------------------------------------------+
| get_attr     | Displays attributes of all channels                          |
+--------------+--------------------------------------------------------------+
| get_pid_attr | Displays PID attributes for the selected channel             |
+--------------+--------------------------------------------------------------+
| cls          | Clear the screen                                             |
+--------------+--------------------------------------------------------------+
| history      | Displays the previously entered commands                     |
+--------------+--------------------------------------------------------------+
| reset        | Reset FPGA and the module state                              |
+--------------+--------------------------------------------------------------+

| 
| ==== PID Configuration ====
| ^ Command ^ Parameters ^

+-----+-----------------------------------------------------------------------------+
| Kpf | [ <gain> ] Sets or Gets the PID controller's Kp force value                 |
+-----+-----------------------------------------------------------------------------+
| Fif | [ <gain> ] Sets or Gets the PID controller's Integral Frequency force value |
+-----+-----------------------------------------------------------------------------+
| Fdf | [ <gain> ] Sets or display the PID differential Frequency force             |
+-----+-----------------------------------------------------------------------------+
| Kpc | [ <gain> ] Sets or Gets the PID controller's Kp clamp value                 |
+-----+-----------------------------------------------------------------------------+
| Fic | [ <gain> ] Sets or Gets the PID controller's Integral Frequency clamp value |
+-----+-----------------------------------------------------------------------------+
| Fdc | [ <gain> ] Set or display PID differential Frequency clamp                  |
+-----+-----------------------------------------------------------------------------+

| 
| ==== Hidden Commands ====
| ^ Command ^ Parameters ^

+----------------+----------------------------------------------------------------------------------------------------------------+
| reg_write      | [ <devId> <addr> <data> ] Write to FPGA register with <devId> as a string                                      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| w              | [ <devId> <addr> <data> ] Write to FPGA register with <devId> as a numeric value                               |
+----------------+----------------------------------------------------------------------------------------------------------------+
| reg_read       | [<devId> <addr> ] Read data from FPGA register <devId> as a string                                             |
+----------------+----------------------------------------------------------------------------------------------------------------+
| r              | [<devId> <addr> ] Read data from FPGA register <devId> as a numeric value                                      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| regwait_bit_hi | [<dev_id> <address> <bit_mask> <attempts>] Checks if the <bit_mask> bits in the register readback are set to 1 |
+----------------+----------------------------------------------------------------------------------------------------------------+
| regwait_bit_lo | [<dev_id> <address> <bit_mask> <attempts>] Checks if the <bit_mask> bits in the register readback are set to 0 |
+----------------+----------------------------------------------------------------------------------------------------------------+
| i2cw           | [ <busid> <Slave addr> <Reg addr> <Data> <data length> ] Writes FMC EEPROM or AD5675 device                    |
+----------------+----------------------------------------------------------------------------------------------------------------+
| i2cr           | [ <busid> <Slave addr> <Reg addr> <data length> ] Reads FMC EEPROM or AD5675 device                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| echo_mode      | [ <on / off> ] Enable (on) or Disable (off) loopback printing characters while typing on CLI                   |
+----------------+----------------------------------------------------------------------------------------------------------------+
| ?              | Display command line help summary                                                                              |
+----------------+----------------------------------------------------------------------------------------------------------------+
| selftest       | Runs self test function                                                                                        |
+----------------+----------------------------------------------------------------------------------------------------------------+

| 
| ----

CLI Warnings Error Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Error Messages
--------------

| 
| ^ Error Message ^ Reason ^

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| SystemInit failed                                                       | Initialization system component(s) failed                                                            |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Self-test failed                                                        | Self-test failed for hardware component(s)                                                           |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Read Board info failed                                                  | Reading the board infomation stored in EEPROM failed                                                 |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Failed to set the output voltage to 0 Volt. Please Proceed with caution | Setting the output voltages of all channels to 0V on system power-up failed due to hardware issue(s) |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

| 
| ==== Warning Messages ====
| ^ Command ^ Warning Message ^ Reason ^

+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| -                             | Command not found                                                                                                     | Unsupported command provided by user                                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| All Commands                  | Invalid parameter(s)                                                                                                  | Wrong parameter given by user                                                                                                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| All Commands                  | Value outside range                                                                                                   | Value given by user is outside valid range                                                                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| All Commands                  | Wrong parameter(s)                                                                                                    | Wrong number of parameters given by user                                                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| All Commands                  | Extra parameter ignored                                                                                               | Extra parameter provided by user and ignored by CLI                                                                            |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| reg_write/reg_read            | Address/Data is outside range                                                                                         | Address or Data value provided by user is out of range                                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| reg_write/reg_read            | Invalid device ID                                                                                                     | Wrong device ID provided by user                                                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| w/r                           | Device ID out of range                                                                                                | Device ID provided by user is out of range                                                                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| regwait_bit_hi/regwait_bit_lo | Address/Mask is outside range                                                                                         | Address provided by user is outside range                                                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| regwait_bit_hi/regwait_bit_lo | Register invalid, register read failed                                                                                | Address provided by user is outside range                                                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| regwait_bit_hi/regwait_bit_lo | Register wait bit timed out                                                                                           | Register wait bit timed out due to hardware                                                                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| regwait_bit_hi/regwait_bit_lo | Invalid device ID                                                                                                     | Wrong device ID provided by user                                                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| count                         | Count value can't be zero or greater than 2,147,483,647 or less than -1                                               | Count value provided by user is out of range                                                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| enable                        | Invalid channel number                                                                                                | Channel number provided by user is out of range                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| iclamp/vclamp                 | Positive clamp cannot be negative                                                                                     | Negative value provided by user for positive clamp                                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| iclamp/vclamp                 | Negative clamp cannot be positive                                                                                     | Positive value provided by user for negative clamp                                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| vrange/irange/mode/vsense     | Command not supported when the channel is active                                                                      | This command cannot be executed on a channel when it is active. User needs to execute **abort** and then run the command again |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| vrange/irange                 | Value out of range                                                                                                    | Value provided is out of range                                                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| mode                          | Invalid argument                                                                                                      | Wrong mode parameter provided by user                                                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| scount                        | Sample count has to be between 1 and 1024                                                                             | Sample count value provided by user is out of range                                                                            |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| measmode                      | Invalid Argument                                                                                                      | Wrong measurement mode parameter provided by user                                                                              |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| measure                       | Acquisition not enabled                                                                                               | Acquisition mode needs to be enabled when trying to run this command with **rf** parameter                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| measure                       | Depth of the FIFO is 0. Data values are not sampled                                                                   | Acquisition failed as samples were not captured                                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| measure                       | Samples count is greater than the FIFO depth                                                                          | Acquisition failed as FIFO as not captured enough data                                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| vsense                        | Invalid sense selection                                                                                               | Wrong sense selection parameter provided by user                                                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| hvstat                        | AD7606 read failed                                                                                                    | Communication with AD7606 failed due to hardware issue                                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| rdcal                         | Channel/Vrange/Irange out of range                                                                                    | Input provided is out of range                                                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| pulse                         | The total duration of pulse must be greater than 100us and less than 100ms                                            | Total duration of pulse is out of range                                                                                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| pulse                         | Duration out of range. Valid range 100us to 100000 us                                                                 | Pulse ON or OFF parameter is out of range                                                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| average                       | Value out of range                                                                                                    | Average parameter is out of range                                                                                              |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| i2cw/i2cr                     | Device ID out of range                                                                                                | Device ID provided by user is out of range                                                                                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| i2cw/i2cr                     | Address/Data is outside range                                                                                         | Address/Data provided by user is outside range                                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| i2cw/i2cr                     | Length is outside range                                                                                               | Total number of bytes provided by user is out of range                                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| i2cw/i2cr                     | I2CW/I2CR Error                                                                                                       | I2C Write/Read failed                                                                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| kpf/fif/fdf/kpc/fic/fdc       | Can't set negative gain. Setting to 0                                                                                 | PID Gain parameter value provided by user is less than 0                                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| kpf/fif/fdf/kpc/fic/fdc       | Can't set gain. Setting to 8.0                                                                                        | Gain parameter value provided by user is larger than maximum allowed                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | DAC <n> AD3552R Device Id Read Failed                                                                                 | Reading the Device ID of AD3552R through SPI failed for DAC 0/1                                                                |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | DAC <n> AD3552R Scratch Pad Write Read Failed                                                                         | Scratch Pad Register Write Read of AD3552R through SPI failed for DAC 0/1                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | Channel <n> AD4630 Device Id Read Failed                                                                              | Reading the Device ID of AD4630 through SPI failed for Channel 0/1/2/3                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | Channel <n> AD4630 Scratch Pad Write Read Failed                                                                      | Scratch Pad Register Write Read of AD4630 through SPI failed for Channel 0/1/2/3                                               |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | Channel <n> ADHV4711 Device Id Read Failed                                                                            | Reading the Device ID of ADHV4711 through SPI failed for Channel 0/1/2/3                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | Channel <n> ADHV4711 Scratch Pad Write Read Failed                                                                    | Scratch Pad Register Write Read of ADHV4711 through SPI failed for Channel 0/1/2/3                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | AD7606 Device Id Read Failed                                                                                          | Reading the Device ID of AD7606 through SPI failed                                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | AD7606 Scratch Pad Write Read Failed                                                                                  | Scratch Pad Register Write Read of AD7606 through SPI failed                                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | EEPROM Device Id Read Failed                                                                                          | Reading the Device ID of EEPROM through I2C failed                                                                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | Analog Power Good status failed                                                                                       | Analog power supply good status from LTC2962 failed                                                                            |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| selftest                      | Digital Power Good status failed                                                                                      | Digital power supply good status from LTC2962 failed                                                                           |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The voltage set is less than the minimum voltage of the range. Setting the voltage as <x> V                    | Voltage provided by user is less than the minimum voltage supported by the voltage range                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The voltage set is greater than the maximum voltage of the range. Setting the voltage as <x> V                 | Voltage provided by user is greater than the maximum voltage supported by the voltage range                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The iclamp negative set is less than the minimum current of the range. Setting the iclamp negative as <x> A    | Current clamp negative provided by user is less than the minimum current supported by the current range                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The iclamp positive set is greater than the maximum current of the range. Setting the iclamp positive as <x> A | Current clamp positive provided by user is greater than the maximum current supported by the current range                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The current set is less than the minimum current of the range. Setting the current as <x> A                    | Current provided by user is less than the minimum current supported by the current range                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The current set is greater than the maximum current of the range. Setting the current as <x> A                 | Current provided by user is greater than the maximum current supported by the current range                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The vclamp negative set is less than the minimum voltage of the range. Setting the vclamp negative as <x> V    | Voltage clamp negative provided by user is less than the minimum voltage supported by the voltage range                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | CH:<n> The vclamp positive set is greater than the maximum voltage of the range. Setting the vclamp positive as <x> V | Voltage clamp positive provided by user is greater than the maximum voltage supported by the voltage range                     |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| go                            | Calibration coefficients CRC failed for channel : <n>. Restoring to defaults                                          | Calibration coefficients are not available in EEPROM for the selected channel, VRange, IRange settings                         |
+-------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

| 

Useful Hints
^^^^^^^^^^^^

Method for PID Tuning
---------------------

| For tuning, the integral and derivative gains can be expressed in terms of integral time and derivative time.
| Ki = (Kp*dt)/(2*Ti)
| Kd = (Kp*Td)/dt
| \* Set up ``Kp = 0``, ``td = 0`` and ``Ti = 10x`` larger than expected response from the plant. If plant is an RC circuit with 'τ = 1ms, then set ``Ti > 10ms``

-  Start with ``Kp = 1`` and increase by 10 until there is oscillation or ringing. If system oscillates, scale back by 10. If there is a lot of ringing, scale back by 2. Repeat this until the fastest response without visible oscillation or ringing is observed
-  Set ``Td = 100x`` shorter than sampling period dt and increase by a factor of 10 until output ringing is increased
-  Decrease Ti by factor of 10 until desired response is achieved. If output oscillates, scale back by 10 and then increase by factors of 2

Reducing ADC Noise
------------------

For more accurate ADC measurements the ADMX3001 has two editable parameters to reduce ADC noise.

Averaging
~~~~~~~~~

To reduce noise, there is the capacity to record N number of ADC measurements and return the average. The number of measurements must be a positive integer between 1 and 1024. Enabling averaging for channel 1 would can be completed using the following code:

::

   channel 1  
   enacq 1 //enabling read fifo mode
   scount 10 //number of fifo measurements
   average 1024 //number of samples for ADC averaging
   enable 1
   go
   measure rf //readback adc measurements

Aperture
~~~~~~~~

The ADC has an input sample rate of 500ns. This time between measurements can be scaled up at integer multiples of 500ns up to 100ms. Enabling aperture of 100ms for channel 1 would be completed using the following code:

::

   channel 1  
   enacq 1 //enabling read fifo mode
   scount 10 //number of fifo measurements
   aperture 100ms //increasing aperture of adc to 100ms
   enable 1
   go
   measure rf //readback adc measurements

<note >Average and Aperture can only be applied in 'Read FIFO' mode</WRAP>

Thermal Evaluation in ADHV4711
------------------------------

| The ADHV4711 may be configured to shut down if any programmable alarm limit is exceeded. There are five internal fault conditions that are monitored. One of the fault conditions is overtemperature.
| A thermal shutdown at absolute max temperature may be implemented without the need for threshold programming or SPI communication. Tie the TMP pin to SDN_IO, when the TMP pin’s analog output voltage reaches the SDN_IO’s logic high threshold at 150C, shutdown mode will be activated. The ADHV4711 will remain in shutdown mode until the die temperature has cooled below 150C.
| The ADHV4711 also has TMP pin which enables thermal monitoring. The pin’s analog output voltage is proportional to die temperature and can be converted to degrees C using the following:
| T(C) = (Vtmp - 1.6V)/6mV/C

ADHV4711 Shutdown Feature
-------------------------

| The ADHV4711 comes equipped with a shutdown mode to offer protection against overcurrent, overvoltage, and high temperatures. There are 5 programmable shutdown limits: overcurrent source, overcurrent sink, overvoltage positive, overvoltage negative, and temperature.
| For the ADMX3001 some initial values are set for each shutdown limit. The values are determined based on the range limits defined by the ADHV4711 and the current/voltage range of the ADMX3001. Overcurrent limits are restricted by the 100mA minimum value and 2A maximum. For this reason all current ranges 100mA or smaller are programmed to a shutdown limit of 109.375mA. There is some overhead room provided so users can easily force 100mA without going into shutdown. In the 1A current range, the limit is restricted to 1.06A to provide headroom for forcing 1A continuously.
| Overvoltage limit in the 1V and 10V range is set at +/- 11.7V to provide room for users to force 10V continuously. In the 100V range the limit is 105.46V for the same reason. The limits can be readjusted given the user’s desired output range, for example if user is in 100V range but will only be forcing 50V, the overvoltage limit can be set to 51V.
| The overtemperature limit is set to standard 104.43C to prevent damaging the ADHV4711. This limit can also be reprogrammed but it is advised against it. The shutdown limits can be reprogrammed by users through the CLI and ACE.

--------------

Compliance Headroom
-------------------

The ADHV4711 output requires the high voltage rails to be Vcc - 5V at Iout = 1A, and Vee + 11.1V at Iout = -1A. The ADHV4711 is required to source a level 1V higher than what is delivered to the load to account for 1V drop across output shunt. The compliance range allowed at output is limited by the overhead in the ADHV4711, 0.5V can be dropped from HF to HS and 0.5V between LS and GND while maintaining consistent and accurate readback.

Calibration Procedure
^^^^^^^^^^^^^^^^^^^^^

A few milliseconds after power up, the ADMX3001 is ready to perform measurements. Measurement accuracy can only be evaluated after performing calibration on the module with an external calibration source with certified traceability.

.. important::

   Please use a Keysight 3458A 8.5 digit DMM or equivalent to get the most accurate results with calibration


.. important::

   Please auto-calibrate the DMM prior to using it for calibrating the ADMX3001


To calibrate, follow the steps below:

-  Open the calibrate.py file in a simple text editor. On line 40 of the file, change the value of the COMPORT variable to equal the COM port that is being used by the FPGA connected to the computer.
-  Connect an HP/Agilent/Keysight 3458A (or equivalent) DMM to the computer via GPIB. Verify that the DMM is properly calibrated and warmed-up according to manufacturer specifications. Make note of the GPIB address that the device is currently set to.
-  Connect channel 0 to the 3458A. Short the HForce and HSense of the ADMX3001 output and connect them to the HI Input terminal of the DMM. Short the LSense and GND of the ADMX3001 and connect them to the LO input terminal of the DMM.

|image33|

-  Run the calibrate.py python file. The default GPIB address is set to 25. If the DMM is set to a different address, execute the calibration script with the --gpib argument: <code> >python calibrate.py --gpib <GPIB Address> </code>
-  The calibration procedure will prompt the user to adjust the probe connections as needed, either between the DMM Voltmeter and Ammeter input terminals, or between ADMX3001 output channels. After properly changing probe connections, pressing enter on the keyboard will advance the calibration procedure.
-  If there is an inconsistent measurement due to an improperly connected probe, the calibration script will prompt the user to verify their probe connections and will then repeat the measurement.
-  After calibration measurements have been completed for all four channels, the ADMX3001 EEPROM will be automatically flashed. After flashing is complete, the ADMX3001 and FPGA board will need to be rebooted for the new calibration coefficients to take effect.

--------------

ACE User Guide
^^^^^^^^^^^^^^

.. important::

   All Steps denoted by (\*) are optional


Forcing Voltage
~~~~~~~~~~~~~~~

-  Select VRange to match desired output level
-  Select IRange to match desired IClamp value \*
-  Ensure Force dropdown is 'Voltage'
-  Set desired output level
-  Set IClamps \*
-  Configure and Enable Channel - please note configuring channel takes a few seconds
-  Select 'Go' to see output on selected channel

.. important::

   Voltage output can be changed while output is running


Forcing Current
~~~~~~~~~~~~~~~

-  Select IRange to match desired output level
-  Select VRange to match desired VClamp value \*
-  Ensure Force dropdown is 'Current'
-  Set desired output level
-  Set VClamps \*
-  Configure and Enable Channel - please note configuring channel takes a few seconds
-  Select 'Go' to see output on selected channel

.. important::

   Current output can be changed while output is running


Configure vs Enable vs Go
~~~~~~~~~~~~~~~~~~~~~~~~~

Each channel has to be configured separately - this ensures all of the information set for each channel matches the currently selected channel. The channels can be enabled asynchronously - you can configure channels and then enable or vice versa as long as both are completed prior to 'Go'. The 'Go' happens synchronously - so every channel that has been enabled will output what has been configured.

Gang Mode
~~~~~~~~~

-  Click on gang mode button to open additional gang settings
-  Set the leader channel
-  Set gang mode
-  Checkbox the member channels
-  In the main board UI - ONLY enable the leader channel
-  Set the desired output settings for the leader channel
-  Click configure channel - you should see all the member channels auto-enabled
-  Click GO
-  View measurements for ganged channels

Pulse Mode
~~~~~~~~~~

-  Enable the pulse mode toggle switch
-  Define mdelay, pulse width and count - for continuous pulses the count should be set to -1
-  Configure the channel
-  Enable the channel
-  Click go
-  Please connect the output to an oscilloscope to view the pulses

Save Measurements
~~~~~~~~~~~~~~~~~

-  There is an option to save the most recent measurement taken and append to the initial file for more measurement data
-  You can choose to set a path and file name in the textbox - or if it is left blank a pop-up will appear to define file location
-  If you would like to append to an existing file - please put the correct file path in the textbox
-  Please note the files will be saved as .CSV

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_lab_solutions_-_2022.2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vadjcommands.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivadopen.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivadotarget.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/programbitfile.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/uploadled.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_hwmanager.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_open_target.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_open_new_target.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_hardware_settings.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_connect_to_local_server.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_select_target.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_target_summary.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_hw_manager_target.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_fpga_menu.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_select_device.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_memory_device_complete.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_program_memory_device.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/vivado_boot.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/pinout.png
   :width: 800px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/pinout_pwr.png
   :width: 800px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/devicemanager.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/puttysetup.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/forcev.png
   :width: 300px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/measurev.png
   :width: 300px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/forcei.png
   :width: 300px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/measurei.png
   :width: 300px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/forcevaceedit.png
   :width: 500px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/forceiaceedit.png
   :width: 500px
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/pulse_average_middle.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/pulse_samples_over_time.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/puttyhelp.png
   :width: 500px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/user-guides/admx/3458diag.png
