.. warning:: Conversion failed for ``resources/eval/user-guides/x-band-platform/software``

   Reason: pandoc error: Error at "/tmp/tmpsdwbk7ki.txt" (line 218, column 1):
expecting inline
not found
[[/resources/tools-software/linux-drivers/iio-mxfe/ad9081|AD9081 MxFE Linux Driver]]\\
^

.. code-block:: text

   ====== X-Band Platform Software ======
   
   ===== Software Needed =====
     * [[https://www.putty.org/|PuTTY]]
     * [[https://matlab.mathworks.com/|MATLAB]]
     * [[:resources:tools-software:linux-software:iio_oscilloscope|IIO Oscilloscope]] / LibIIO (Optional)]]
       * [[https://github.com/analogdevicesinc/iio-oscilloscope/releases/latest|Latest IIO Oscilloscope release]]
       * [[https://github.com/analogdevicesinc/libiio/releases|Latest Libiio release - Look for the '...-Windows-setup.exe']]
   
   ==== PuTTY ====
   PuTTY helps to provide a view into the Linux and give additional controls and debug abilities. Putty can be downloaded from here [[https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html|Putty Download Page]]. Ensure that the proper version for the computer is downloaded (64 bit for a 64 bit PC). 
   Once downloaded the COM port to the FPGA can be opened. This COM port can be identified through the device manager as the standard COM port:
   
   {{:resources:eval:user-guides:comport.png?400 |}}
   
   {{ :resources:eval:user-guides:x-band-platform:putty.png?400 |}}
   
   <note>In PuTTY, this should be opened with a baudrate of 115200.</note>
   
   
   -----
   ==== MATLAB 2021b or 2022a ====
   <note important>MATLAB 2021b is the primary version that all the code is tested with.</note>
   MATLAB is used to exercise the board through LibIIO objects and provide higher level application functionality. In order to work with the platform, a number of toolboxes and support packages are required:
   Required toolboxes:
     - MATLAB Communications Toolbox
     - DSP System Toolbox
     - Signal Processing Toolbox
     - Curve Fitting Toolbox
     - Instrument Control Toolbox
     - Communications Toolbox Support Package for Xilinx Zynq-Based Radio. Installed through MATLAB Add-On Explorer.
     - Analog Devices High Speed Converter Toolbox. Can be installed through MATLAB Add-On Explorer or latest version here: 
   <WRAP download>
     * [[https://github.com/analogdevicesinc/HighSpeedConverterToolbox|High Speed Converter Toolbox Download Page]]
   </WRAP> 
     - Analog Devices RF Microwave Toolbox. Can be installed through MATLAB Add-On Explorer or latest version here:
   <WRAP download>
     * [[https://github.com/analogdevicesinc/RFMicrowaveToolbox|RF Microwave Toolbox Download Page]]  
   </WRAP> 
   
   Customers can request a free trial via the [[https://urldefense.com/v3/__https://www.mathworks.com/products/communications.html__;!!A3Ni8CS0y2Y!u2iVBukmDblhk9-FINa9SNIcuL_Ap61oG1IvWi0qWnxrwju6qXrNws1jybUn_UlFhkQ$|Communications Toolbox product page]], or they can request a [[https://urldefense.com/v3/__https://www.mathworks.com/campaigns/products/trials/targeted/sdr.html__;!!A3Ni8CS0y2Y!u2iVBukmDblhk9-FINa9SNIcuL_Ap61oG1IvWi0qWnxrwju6qXrNws1jybUnqe87Ows$|Software-Defined Radio Design trial “package”]], which includes MATLAB, Simulink, DSP System Toolbox, Signal Processing Toolbox, and Communications Toolbox.
     
   ----
   
   ====== ZCU102 Set Up ======
   
   This guide will walk you through setting up the ZCU102 FPGA platform to work with the X-Band Developer's Kit. 
   
   
   ===== SD Card Setup =====
   <hidden>
     - Follow the instructions on one of the below pages to install the {{https://swdownloads.analog.com/cse/kuiper/image_2023-04-02-ADI-Kuiper-full.zip| 2021_r2 Linux kernel}} on the SD card.
       * [[resources/tools-software/linux-software/zynq_images/linux_hosts|Linux]]
       * [[resources/tools-software/linux-software/zynq_images/windows_hosts|Windows]]
     - Determine which version of the MxFE board you have. The version is printed in copper on the bottom right corner of the board with the RF connectors facing North. The writing is covered in soldermask and can be somewhat difficult to read. The board version should either be "B", "C", or "D".
     - There are three pertinent files to copy to the root of the SD card's /BOOT/ section:
       - Image, located in "zynqmp-common" folder
       - BOOT.BIN, located in "zynqmp-zcu102-rev10-stingray" folder
       - system.dtb, located in subfolders of "zynqmp-zcu102-rev10-stingray" folder
   <note>There are 3 folders in the "zynqmp-zcu102-rev10-stingray" folder. Be sure to take the "system.dtb" that corresponds with the clocking architecture of your setup.</note>
   
   <note>Be sure to rename the correct *.dtb file for your version of the AD9081 board to "system.dtb".</note>
   
   <note warning>**If your computer encrypts removable media for security purposes, it's easiest to use a personal computer to do this step. If encryption issues persist, use the file below which has AES disabled. This is version 2021_R1.**</note>
   
   {{ :resources:eval:user-guides:x-band-platform:zcu102_config_files_100mhz_vcxo_rev10_aes_disabled.zip | ZCU102 Configuration Files, 100MHz VCXO, AES Disabled}}
   
   \\ 
   
   
   </hidden>
   
   \\
   ===== ZCU102 Configurations =====
   ==== Boot from SD Card ====
   <hidden>
   To configure the ZCU102 to boot from the SD card, set SW6 as shown below. SW6 is halfway between the SD card input and the vertical SMA connectors on the ZCU102.
   {{ :resources:eval:developer-kits:x-band-dev-kit:zcu102_sw6_sdcard.jpg |SW6 Configuration for SD Card Boot}}
   
   </hidden>
   
   \\
   ==== USB Host Mode ====
   <hidden>
   Setting up the ZCU102 in USB Host Mode allows the use of USB peripherals such as a keyboard and mouse. This can be useful for operating the board directly rather than having to use the UART connection or some other form of indirect control. Configure the jumpers as indicated below:
     * Shunt J7
     * J109 -> Shunt pins 2-3
     * J110 -> Shunt pins 2-3
     * J112 -> Shunt pins 1-2
     * J113 -> Shunt pins 1-2\\
   {{ :resources:eval:developer-kits:x-band-dev-kit:zcu102_usb_host_mode.jpg |Jumper Configuration for USB Host Mode}}
   </hidden>
   
   \\
   ==== DisplayPort Not Working ====
   Once you have the board up and running (and control using the UART connection through PuTTy), [[resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp#displayport_-_no_picture|try this procedure at the bottom of the page]].
   
   
   \\
   ==== USB to UART Bridge ====
   The ZCU102 uses a mini-B USB cable to connect the USB UART port on the board to a host PC. If the USB to UART bridge is not installed or automatically recognized, then a drive must be installed. This will allow control using the UART connection through PuTTy or other SSH/Telnet Client, [[https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers|select Downloads tab for Driver download]].
   
   \\
   ==== Network Configuration ====
   The ZCU102 uses a RJ45 ethernet cable to connect the ethernet port on the board a host PC or network port to enable network access. Modifications to the network settings can be made following the guidance detailed on the [[resources/tools-software/linux-software/network-config|Network Configuration]] wiki.
   
   ===== ADAR1000EVAL1Z Power Sequence =====
   
   The proper power on sequencing for the ADAR1000EVAL1Z is embedded within the firmware of the ZCU102. The embedded script pulses the proper signal nets in the correct order (POWER_UP_DOWN and 5V_CTRL) automatically upon booting the FPGA. The power down sequence is not enabled in software. The ADAR1000EVAL1Z board can be powered down manually by pressing the RESET button on the primary side of the ADAR1000EVAL1Z board. The following steps need to be completed by the user to implement the ADAR1000EVAL1Z power up sequencing script.  
   
     - Open a UART terminal connecting to the FGPA [[:resources:eval:user-guides:ad9081_fmca_ebz:quickstart:zynqmp#setting_up_uart|Setting up ZCU102 UART]]
     - Download WinSCP 
   <WRAP download>
     * [[https://winscp.net/eng/download.php|WinSCP Download]]
   </WRAP>
     - Connect to the ZCU102 via WinSCP
         * Host: FPGA IP Address
         * Username: root
         * Password: analog
     - Navigate to the /etc/ folder
     - Copy the {{:resources:eval:user-guides:x-band-platform:adar1000eval1z_power_script.zip |power sequencing script}} to the /etc/ folder
     - Open the rc.local file in the /etc/ directory
         * Replace contents of rc.local file with the code below
     - Save files, exit WinSCP, and reboot FGPA
   
   
   <xterm>
   #!/bin/sh -e
   #
   # rc.local
   #
   # This script is executed at the end of each multiuser runlevel.
   # Make sure that the script will "exit 0" on success or any other
   # value on error.
   #
   # In order to enable or disable this script just change the execution
   # bits.
   #
   # By default this script does nothing.
   
   # Print the IP address
   _IP=$(hostname -I) || true
   if [ "$_IP" ]; then
     printf "My IP address is %s\n" "$_IP"
   fi
   
   python3 /etc/stingray_power.py up
   
   service iiod restart
   
   exit 0
   </xterm>
   
   
   <note>Due to the hardware design of the ADAR1000EVAL1Z, the user needs to keep in mind the power up and power down execution. If the power sequence is not followed in the correct order from, then the power sequence state will be indeterminate and a hard reset is required to revert to a known power state.
   
   
   For example the proper sequence is as follows: Power Up -> Power Down -> Power Up -> Power Down</note>
    
   
   ----
   
   ===== ADXUD1AEBZ Interposer FMC EEPROM Progamming=====
   The ADXUD1AEBZ Interposer Board FMC EEPROM is not factory programmed. The following commands in a UART Terminal (e.g. PuTTY) can be executed to program the FMC EEPROM. 
   
   <xterm>
   root@analog:~#
   root@analog:~# find /sys -name eeprom
   /sys/devices/platform/axi/ff030000.i2c/i2c-1/i2c-15/15-0050/eeprom
   /sys/devices/platform/axi/ff030000.i2c/i2c-1/i2c-6/6-0054/eeprom
   root@analog:~#
   root@analog:~# fru-dump -i /usr/local/src/fru_tools/masterfiles/AD-FMCOMMS2-EBZ-FRU.bin -o /sys/bus/i2c/devices/15-0050/eeprom
   read 251 bytes from /usr/local/src/fru_tools/masterfiles/AD-FMCOMMS2-EBZ-FRU.bin
   wrote 251 bytes to /sys/bus/i2c/devices/15-0050/eeprom
   root@analog:~#
   root@analog:~# fru-dump -i /sys/bus/i2c/devices/15-0050/eeprom -b
   read 256 bytes from /sys/bus/i2c/devices/15-0050/eeprom
   Date of Man     : Mon Jul 22 20:23:00 2013
   Manufacturer    : Analog Devices
   Product Name    : AD9361 RF Hardware Development Kit
   Serial Number   : 00045
   Part Number     : AD-FMCOMMS2-EBZ
   FRU File ID     : Empty Field
   PCB Rev         : C
   PCB ID          : 9361FMC01A
   BOM Rev         : 1
   Uses LVDS       : Y
   root@analog:~#
   root@analog:~# poweroff
   </xterm>
   
   
   ----
   
   ====== Software Architecture ======
   
   <note tip>All programmable devices on the X-Band platform are abstracted by IIO devices.</note>
   
   ^ IIO Device ^ Device Name ^ Driver Documentation ^
   | iio:device2 | adar1000_csb_1_1 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device3 | adar1000_csb_1_2 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device4 | adar1000_csb_1_3 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device5 | adar1000_csb_1_4 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device6 | adar1000_csb_2_1 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device7 | adar1000_csb_2_2 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device8 | adar1000_csb_2_3 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   | iio:device9 | adar1000_csb_2_4 | [[:resources:tools-software:linux-drivers:iio-transceiver:adar1000|ADAR1000 X/Ku Band Linux Driver]]|
   
   
   | iio:device18 | adf4371-0 | [[resources:tools-software:linux-drivers:iio-pll:adf4371|ADF4371 IIO Wideband Synthesizer Linux Driver]] |
   | iio:device19 | hmc7044 | [[resources:tools-software:linux-drivers:iio-pll:hmc7044|HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver]] |
   | iio:device20 | axi-ad9081-rx-hpc | <WRAP>
   [[resources:tools-software:linux-drivers:iio-mxfe:ad9081|AD9081 MxFE Linux Driver]]\\
   [[resources:tools-software:linux-drivers:iio-adc:axi-adc-hdl|AXI ADC HDL Linux Driver]]
   </WRAP> |
   | iio:device21 | TDD Core | [[:resources:fpga:docs:axi_tdd|Generic TDD Core]] |
   | iio:device22 | one-bit-adc-dac | TBD |
   | iio:device23 | one-bit-adc-dac | TBD |
   | iio:device24 | one-bit-adc-dac | TBD |
   | iio:device25 | axi-ad9081-tx-hpc | <WRAP>
   [[resources:tools-software:linux-drivers:iio-mxfe:ad9081|AD9081 MxFE Linux Driver]]\\
   [[:resources:tools-software:linux-drivers:iio-dds:axi-dac-dds-hdl|AXI DAC HDL Linux Driver]]
   </WRAP> |
   
   
   All these drivers feature a runtime API which can be controlled using [[resources:tools-software:linux-software:iio_oscilloscope|IIO Oscilloscope]], [[resources:tools-software:linux-software:libiio|libiio]], etc.
   However some configuration is static and done inside the device tree.
   Please see instructions on Building custom kernel and devicetree images here:
     * [[:resources:tools-software:linux-software:kuiper-linux |Linux on the Xilinx FPGA development Board]]
   
   
   ----
   
   ====== MATLAB Support ======
   
   MATLAB support is provided through the [[:resources:tools-software:hsx-toolbox|High Speed Converter Toolbox]] and [[:resources:tools-software:rf-microwave-toolbox|RFMicrowave Toolbox]], with unique classes for transmit and receive functionality. Currently you must grab a development build but installers are provided for convenience.
   
   
   ===== MATLAB Control Overview =====
   The X-Band Platform can be controlled via MATLAB using example scripts which are available as part of the [[repo>RFMicrowaveToolbox|Analog Devices, Inc. RF Microwave Toolbox]] add-on. This add-on can either be manually downloaded from the Releases section of the GitHub page or downloaded and installed via MATLAB Add-On Explorer. Please ensure you have installed both the Analog Devices, Inc. High Speed Converter Toolbox as well as the RF Microwave Toolbox.
   
   <note>It's recommended to install via the download from GitHub as this is generally more up to date than the MATLAB Add-On Explorer page</note>
   
   ^           MATLAB Toolboxes           ^^^
   ^   Toolbox   ^   Purpose   ^   Notes   ^
   |[[mw>hardware-support/adalm-pluto-radio.html?s_tid=AO_HS_info|Support Package for ADALM-Pluto]]| LibIIO Matlab Bindings |        |
   | [[repo>HighSpeedConverterToolbox|High Speed Converter]] | AD9081 Control |  |
   | [[repo>RFMicrowaveToolbox|RF Microwave ]] | ADAR1000EVAL1Z & ADXUD1A Control |  |
   | [[repo>genalyzer|Genalyzer]] | DSP of RF Signals |  |
   | [[mw>matlabcentral/fileexchange/52848-matlab-support-for-mingw-w64-c-c-compiler|MinGW-w64 C/C++ Compiler]] | Genalyzer Compiler |  |
   
   
   
   Example scripts are located within the add-on install directory, which is usually located in the directory: <code>C:\Users\<username>\AppData\Roaming\MathWorks\MATLAB Add-Ons\Toolboxes</code> 
   
   The example scripts are specifically located in the following folder: <code>Analog Devices, Inc. RFMicrowave Toolbox\rfm_examples</code>
   
   ==== Controlling X-Band Platform With MATLAB ====
   
   The control interface for the X-Band Platform is implemented using standard system objects in MATLAB. Basic information for instantiating the objects is provided in the toolbox documentation within MATLAB and on [[/resources/tools-software/hsx-toolbox#device_control_and_data_streaming|this page]] and [[/resources/tools-software/rf-microwave-toolbox#device_control_and_data_streaming|this page]]. Here is an example instantiation of the objects:
   
   <xterm>
   >> tx = adi.AD9081.Tx;
   
   tx = 
   
     adi.AD9081.Tx with properties:
   
       ChannelNCOFrequencies: [0 0 0 0]
          MainNCOFrequencies: [0 0 0 0]
            ChannelNCOPhases: [0 0 0 0]
               MainNCOPhases: [0 0 0 0]
        ChannelNCOGainScales: [0 0 0 0]
                  NCOEnables: [0 0 0 0]
             EnabledChannels: 1
                         uri: 'ip:analog'
                  DataSource: 'DMA'
         EnableCyclicBuffers: false
         
   >> rx = adi.AD9081.Rx;
   
   rx = 
   
     adi.AD9081.Rx with properties:
   
                SamplingRate: NaN
       ChannelNCOFrequencies: [0 0 0 0]
          MainNCOFrequencies: [0 0 0 0]
            ChannelNCOPhases: [0 0 0 0]
               MainNCOPhases: [0 0 0 0]
                    TestMode: 'off'
                 EnablePFIRs: false
               PFIRFilenames: ''
             SamplesPerFrame: 32768
             EnabledChannels: 1
                         uri: 'ip:analog'
   
   >> sray = adi.Stingray;
   
   sray = 
   
     Stingray with properties
   
                             ADF4371Frequency: 15000000000
                                  ADF4371Name: RF16x
                                 ADF4371Phase: 359999
                                BeamMemEnable: logical [2x4]
                                BiasDACEnable: logical [2x4]
                                  BiasDACMode: cell [2x4]
                                BiasMemEnable: logical [2x4]
                              CommonMemEnable: logical [2x4]
                            CommonRxBeamState: int32 [2x4]
                            CommonTxBeamState: int32 [2x4]
                                       Ctrl5V: 0
                               DetectorEnable: logical [4x8]
                                DetectorPower: double [4x8]
                               ElementSpacing: 0.015
                                       Enable: 0
                               EnableSyncSoft: 0
                                ExternalTRPin: cell [2x4]
                           ExternalTRPolarity: logical [2x4]
                      FPGARxOffloadSyncEnable: 0
        FPGARxOffloadSyncOffStartMilliseconds: 0
                 FPGARxOffloadSyncOffStartRaw: 0
         FPGARxOffloadSyncOnStartMilliseconds: 0
                  FPGARxOffloadSyncOnStartRaw: 0
                    FPGARxOffloadSyncPolarity: 0
                          FPGATDDEngineEnable: 0
            FPGATDDEngineOffStartMilliseconds: 0
                     FPGATDDEngineOffStartRaw: 0
             FPGATDDEngineOnStartMilliseconds: 0
                      FPGATDDEngineOnStartRaw: 0
                        FPGATDDEnginePolarity: 0
                      FPGATxOffloadSyncEnable: 0
        FPGATxOffloadSyncOffStartMilliseconds: 0
                 FPGATxOffloadSyncOffStartRaw: 0
         FPGATxOffloadSyncOnStartMilliseconds: 0
                  FPGATxOffloadSyncOnStartRaw: 0
                    FPGATxOffloadSyncPolarity: 0
                                  FrameLength: NaN
                      FrameLengthMilliseconds: 1
                                   LNABiasOff: double [2x4]
                                    LNABiasOn: double [2x4]
                             LNABiasOutEnable: logical [2x4]
                               LTC2314RFPower: 0
                                 MUXOutEnable: 1
                                         Mode: cell [2x4]
                                 NumADAR1000s: 2
                                    PABiasOff: double [4x8]
                                     PABiasOn: double [4x8]
                                         PAOn: 0
                                 PllOutputSel: 0
                                     PolState: logical [2x4]
                              PolSwitchEnable: logical [2x4]
                                  PowerUpDown: 0
                                       RxAttn: logical [4x8]
                                  RxBeamState: double [4x8]
                                       RxGain: double [4x8]
                             RxLNABiasCurrent: int32 [2x4]
                                  RxLNAEnable: logical [2x4]
                                 RxMxFEEnable: 0
                   RxMxFEOffStartMilliseconds: 0
                            RxMxFEOffStartRaw: 0
                    RxMxFEOnStartMilliseconds: 0
                             RxMxFEOnStartRaw: 0
                               RxMxFEPolarity: 0
                                      RxPhase: double [4x8]
                                  RxPowerDown: logical [4x8]
                             RxSequencerStart: logical [4x8]
                              RxSequencerStop: logical [4x8]
                                 RxToTxDelay1: int32 [2x4]
                                 RxToTxDelay2: int32 [2x4]
                           RxVGABiasCurrentVM: int32 [2x4]
                                  RxVGAEnable: logical [2x4]
                                   RxVMEnable: logical [2x4]
                         SelectChannelSetMode: A_RxLG
                              SequencerEnable: logical [2x4]
                     StartupDelayMilliseconds: 0
                               TRSwitchEnable: logical [2x4]
                              TargetFrequency: 10000000000
                                         Temp: double [2x4]
                                       TxAttn: logical [4x8]
                                  TxBeamState: double [4x8]
                                       TxGain: double [4x8]
                                 TxMxFEEnable: 0
                   TxMxFEOffStartMilliseconds: 0
                            TxMxFEOffStartRaw: 0
                    TxMxFEOnStartMilliseconds: 0
                             TxMxFEOnStartRaw: 0
                               TxMxFEPolarity: 0
                              TxPABiasCurrent: int32 [2x4]
                                   TxPAEnable: logical [2x4]
                                      TxPhase: double [4x8]
                                  TxPowerDown: logical [4x8]
                            TxRxSwitchControl: cell [2x4]
                             TxSequencerStart: logical [4x8]
                              TxSequencerStop: logical [4x8]
                             TxStingrayEnable: 0
               TxStingrayOffStartMilliseconds: 0
                        TxStingrayOffStartRaw: 0
                TxStingrayOnStartMilliseconds: 0
                         TxStingrayOnStartRaw: 0
                           TxStingrayPolarity: 0
                                 TxToRxDelay1: int32 [2x4]
                                 TxToRxDelay2: int32 [2x4]
                           TxVGABiasCurrentVM: int32 [2x4]
                                  TxVGAEnable: logical [2x4]
                                   TxVMEnable: logical [2x4]
                                          uri: 'ip:10.0.0.200'            
   </xterm>
   
   
   ----
                      
   
   ==== XBDP_SimpleRx.m ====
   This script is to be used with the Analog Devices X-Band Platform to demonstrate relatively simple MATLAB control of the system. It allows the user to configure the Rx aspects of the system by using the and rx = adi.AD9081.Rx and sray = adi.Stingray system objects.
   
   {{ :resources:eval:user-guides:x-band-platform:xbdp_simplerx_sampledomainplot.png |}}
   
   {{ :resources:eval:user-guides:x-band-platform:xbdp_simplerx_sampledomainplot_2.png |}}
   
   {{ :resources:eval:user-guides:x-band-platform:xbdp_simplerx_freqdomainplot_1.png |}}
   
   {{ :resources:eval:user-guides:x-band-platform:xbdp_simplerx_freqdomainplot_2.png |}}
   
   Using this script as a basis, the user can modify the script for their own use case such that they can:
     - View Analog Array Channel Mapping Using, For Example, **sray.ArrayMap**
     - Change Rx NCO Frequencies Using, For Example, **rx.MainNCOFrequencies** or **rx.ChannelNCOFrequencies**
     - Change Rx NCO Phases Using, For Example, **rx.MainNCOPhases** or **rx.ChannelNCOPhases**
     - Change Rx Analog per Channel Gain Using, For Example, **sray.RxGain**
     - Change Rx Analog per Channel Phases Using, For Example, **sray.RxPhase**
     - Change Rx Analog per Channel Attenuation Using, For Example, **sray.RxAttn**
     - Latch Rx Analog Settings Using, For Example, **sray.LatchRxSettings**
     - Capture Simultaneous Complex-Valued Rx Data for All Enabled Channels: **data=rx()**
     -   - Beam steer using **sray.SteerRx(azimuth,elevation,arrayPhaseOffsets)**
     - Beam taper using **sray.TaperRx(window,gain,arrayGainOffsets)**
     - Analyze and Post-Process Captured Waveforms
   
   ----
   
   ==== XBDP_SimpleTx.m ====
   This script is to be used with the Analog Devices X-Band Platform to demonstrate relatively simple MATLAB control of the system. It allows the user to configure the Tx aspects of the system by using the and tx = adi.AD9081.Tx and sray = adi.Stingray system objects.
   
   Using this script as a basis, the user can modify the script for their own use case such that they can:
     - View Analog Array Channel Mapping Using, For Example, **sray.ArrayMap**
     - Change Tx NCO Frequencies Using, For Example, **tx.MainNCOFrequencies** or **tx.ChannelNCOFrequencies**
     - Change Tx NCO Phases Using, For Example, **tx.MainNCOPhases** or **tx.ChannelNCOPhases**
     - Change Tx Analog per Channel Gain Using, For Example, **sray.TxGain**
     - Change Tx Analog per Channel Phases Using, For Example, **sray.TxPhase**
     - Change Tx Analog per Channel Attenuation Using, For Example, **sray.TxAttn**
     - Latch Tx Analog Settings Using, For Example, **sray.LatchTxSettings**
     - Transmit Complex-Valued Tx waveforms for All Enabled Channels: **release(tx)**
     - Beam steer using **sray.SteerTx(azimuth,elevation,arrayPhaseOffsets)**
     - Beam taper using **sray.TaperTx(window,gain,arrayGainOffsets)**
   
   ----
   
   ==== Matlab Channel Mapping ====
   The Matlab attribute mapping is linear indexed and matches that of the hardware channel mapping as shown in the figure below.
   
   {{ :resources:eval:user-guides:x-band-platform:channel_mapping.png?400 |ADAR1000EVAL1Z Cell and Channel Mapping}}
   
   <note tip>For example, sray.RxGain(1) will modify the gain for channel 1 and sray.RxGain(23) modifies the gain for channel 23. sray.RxGain = (127*ones(2,4) zeros(2,4);zeros(2,4) 127*ones(2,4)); will set the gain for subarray 1 and 3 to max gain and subarray 2 and 4 to 0 gain. </note>
   
   ----
   
   ====== Miscellaneous ======
   
   ===== Useful PuTTY Commands =====
   The use of the UART terminal to debug and understand device attribute and channel attribute settings can be insightful. There are a variety of [[:resources:tools-software:linux-software:libiio|libiio]] command sets that can be utilized such as [[:resources:tools-software:linux-software:libiio:iio_info|iio_info]] and [[:resources:tools-software:linux-software:libiio:iio_attr|iio_attr]]. Additional libiio tips and tricks can be found [[:resources:tools-software:linux-software:libiio_tips_tricks|here]].
   
   ==== Devices Attributes ====
   <xterm>
   root@analog:~# iio_attr -d
   IIO context has 19 devices:
           iio:device0, ltc2314-14: found 1 device attributes
           iio:device1, ams: found 1 device attributes
           iio:device18, adf4371-0: found 2 device attributes
           iio:device19, hmc7044: found 7 device attributes
           iio:device2, adar1000_csb_1_1: found 40 device attributes
           iio:device20, axi-ad9081-rx-hpc: found 13 device attributes
           iio:device21, axi-core-tdd: found 11 device attributes
           iio:device22, one-bit-adc-dac: found 1 device attributes
           iio:device23, one-bit-adc-dac: found 1 device attributes
           iio:device24, one-bit-adc-dac: found 1 device attributes
           iio:device25, axi-ad9081-tx-hpc: found 2 device attributes
           iio:device3, adar1000_csb_1_2: found 40 device attributes
           iio:device4, adar1000_csb_1_3: found 40 device attributes
           iio:device5, adar1000_csb_1_4: found 40 device attributes
           iio:device6, adar1000_csb_2_1: found 40 device attributes
           iio:device7, adar1000_csb_2_2: found 40 device attributes
           iio:device8, adar1000_csb_2_3: found 40 device attributes
           iio:device9, adar1000_csb_2_4: found 40 device attributes
           iio_sysfs_trigger: found 2 device attributes
   root@analog:~#
   </xterm>
   
   ----
   
   ==== Channel Attributes ====
   <xterm>
   root@analog:~# iio_attr -c
   IIO context has 19 devices:
           iio:device0, ltc2314-14: found 2 channels
           iio:device1, ams: found 30 channels
           iio:device18, adf4371-0: found 5 channels
           iio:device19, hmc7044: found 8 channels
           iio:device2, adar1000_csb_1_1: found 9 channels
           iio:device20, axi-ad9081-rx-hpc: found 17 channels
           iio:device21, axi-core-tdd: found 4 channels
           iio:device22, one-bit-adc-dac: found 6 channels
           iio:device23, one-bit-adc-dac: found 6 channels
           iio:device24, one-bit-adc-dac: found 5 channels
           iio:device25, axi-ad9081-tx-hpc: found 24 channels
           iio:device3, adar1000_csb_1_2: found 9 channels
           iio:device4, adar1000_csb_1_3: found 9 channels
           iio:device5, adar1000_csb_1_4: found 9 channels
           iio:device6, adar1000_csb_2_1: found 9 channels
           iio:device7, adar1000_csb_2_2: found 9 channels
           iio:device8, adar1000_csb_2_3: found 9 channels
           iio:device9, adar1000_csb_2_4: found 9 channels
           iio_sysfs_trigger: found 0 channels
   root@analog:~#
   </xterm>
   
   ----
   
   ==== HMC7044 PLL Lock ====
   <xterm>
   root@analog:~# cat /sys/kernel/debug/iio/iio:device19/status
   --- PLL1 ---
   Status: Locked
   Using:  CLKIN1 @ 100000000 Hz
   PFD:    10000 kHz
   --- PLL2 ---
   Status: Locked (Synchronized)
   Frequency:      3000000000 Hz (Autocal cap bank value: 12)
   SYSREF Status:  Valid & Locked
   SYNC Status:    Synchronized
   Lock Status:    PLL1 & PLL2 Locked
   root@analog:~#
   </xterm>
   
   <note>The HMC7044 reference clock priority is: [CLKIN1 → CLKIN0 → CLKIN2 → CLKIN3]. In this example, an external reference clock of 100MHz is applied and is selected as the reference clock source. If no external clock is detected, then the clock priority will be sequenced and the next available source will be chosen. See the [[:resources:eval:user-guides:x-band-platform:hardware#clocking_architecture|Hardware Clocking Architecture]] for additional information.</note>
   
   ----
   
   ==== JESD Status ====
   <xterm>
   root@analog:~# jesd_status
   lqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqk
   xl(DEVICES) Found 2 JESD204 Link Layer peripheralsqqqqqqqqqqqqqqqqqqqqqqqqqqqqkx
   xx                                                                            xx
   xx(0): axi-jesd204-rx/84a90000.axi-jesd204-rx  [*]                            xx
   xx(1): axi-jesd204-tx/84b90000.axi-jesd204-tx                                 xx
   xmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqjx
   xl(STATUS)qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqkx
   xxLink is                      enabled                                        xx
   xxLink Status                  DATA                                           xx
   xxMeasured Link Clock (MHz)    250.026                                        xx
   xxReported Link Clock (MHz)    250.000                                        xx
   xxMeasured Device Clock (MHz)  250.026                                        xx
   xxReported Device Clock (MHz)  250.000                                        xx
   xxDesired Device Clock (MHz)   250.000                                        xx
   xxLane rate (MHz)              10000.000                                      xx
   xxLane rate / 40 (MHz)         250.000                                        xx
   xxLMFC rate (MHz)              7.812                                          xx
   xxSYSREF captured              Yes                                            xx
   xxSYSREF alignment error       No                                             xx
   xxSYNC~                                                                       xx
   xmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqjx
   xl(LANE STATUS)qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqkx
   xxLane#                             0      1      2      3                    xt
   xxErrors                            0      0      0      0                    xj
   </xterm>
   
   ----
   
   ==== Firmware Identifiers ====
   A unique identifier will be returned for the Image, system.dtb, and BOOT.BIN files installed on the SD card using the md5 command. 
   
   <xterm>
   root@analog:~#
   root@analog:~# md5sum /boot/Image
   3c1ac2b114bbde82b38fc0463bf03dbd  /boot/Image
   root@analog:~#
   </xterm>
   
   <xterm>
   root@analog:~#
   root@analog:~# md5sum /boot/system.dtb
   bfc14855246807f4e62a2f71ce65deec  /boot/system.dtb
   root@analog:~#
   </xterm>
   
   <xterm>
   root@analog:~#
   root@analog:~# md5sum /boot/BOOT.BIN
   a77ca8194b457c2d020a44d83568cc52  /boot/BOOT.BIN
   root@analog:~#
   </xterm>
   
   <note>The returned identifiers in the example may not match the most recent firmware file versions. This is an example to show the use of the md5 command.</note>
   
   ----
   
   ====== Support ======
   For additional questions or support, please visit the Engineering Zone forum at [[ez>adef-system-platforms/|ADEF]]. 
   
   [[resources/eval/user-guides/x-band-platform|X Band Development Platform Main Page]]
