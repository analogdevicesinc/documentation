ADXBAND16EBZ Quick Start Guide
==============================

Equipment Included with Quad ADXBAND16EBZ Kits
----------------------------------------------

-  1x ADXBAND16EBZ instructions card
-  1x 12V, 25A+ Wall Supply and power cable
-  2x SMPN-to-SMPN cables. Used to test to with equipment
-  3x Board Standoffs
-  2x Installed Fans
-  1x Installed Heat Sinks

Equipment Included with Calibration Board Kits (ADXBAND16EBZ-CAL)
-----------------------------------------------------------------

-  1x Instructions card
-  1x 12V, Wall Supply and power cable
-  1x 6" SMA-SMPM cable. Used to connect between ADXBAND16EBZ Board & Calibration Board
-  4x Board Standoffs
-  1x PMOD ribbon cable

Required Additional Equipment
-----------------------------

-  1x 100MHz Reference Oscillator or Waveform Generator
-  1x Ethernet Cable
-  1x USB to Ethernet Dongle

   -  https://www.digikey.com/products/en?keywords=TL824-ND

-  2x USB Micro Cables
-  50Ω SMPN Cables - As Needed
-  32x MMCX-MMCX cables (2 are provided with the CAL kit). Used to connect between Main Board & Calibration Board

   -  https://www.samtec.com/products/rf316-03sp1-03sp1-0100

-  1x `VCU118 FPGA Board <https://www.xilinx.com/products/boards-and-kits/vcu118.html>`__

*NOTE: do not use the Ethernet cable that comes with the VCU118 board. It is a crossover cable and will not work with the platform*

Test Setup
----------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_setup.png

--------------

Software Needed
===============

-  :doc:`Supported Use Cases / Bitstreams Available For Download </wiki-migration/resources/eval/user-guides/quadmxfe/quick-start>`
-  :doc:`IIO Oscilloscope / LibIIO </wiki-migration/resources/eval/user-guides/quadmxfe/quickbringup>`

   -  :git-iio-oscilloscope:`Latest IIO Oscilloscope release <releases/latest>`
   -  :git-libiio:`Latest Libiio release - Look for the '...-Windows-setup.exe' <releases>`

-  :doc:`PuTTY </wiki-migration/resources/eval/user-guides/quadmxfe/quickbringup>`
-  :doc:`Xilinx Vivado Toolchain </wiki-migration/resources/eval/user-guides/quadmxfe/quickbringup>`
-  :doc:`MATLAB (Optional) </wiki-migration/resources/eval/user-guides/quadmxfe/quickbringup>`

• Xilinx Vivado Lab Link: https://www.xilinx.com/member/forms/download/xef.html?filename=Xilinx_Vivado_Lab_Win_2023.1_0507_1903.tar.gz

Notes: You will need to create an account with AMD.  • Extract files using 7-zip to known folder. Run the xsetup application (you will need admin role for this). • Version: Most versions are fine. 2023.1 is latest at the time of writing. It is known to be working.

Pre-Release High Speed Converters Toolbox • Link to file: hsx-ad9081-Aug15.zip • Link to instructions for installing custom toolbox: Toolboxes in Development in Wiki https://www.mathworks.com/hardware-support/adalm-pluto-radio.html • ADI RF and Microwave Toolbox Analog Devices, Inc. RF and Microwave Toolbox - File Exchange - MATLAB Central (mathworks.com)

Genalyzer

1. Install Toolboxes

::

     Launch Matlab Add-On Explorer 

2. Download MinGW-w64 C/C++ compiler for Windows

::

     Download --> File Sent
         Extract to desired folder 
     Add to Matlab's Set Path 

3. Download latest Genalyzer EXE Installer from Github

::

     [[:git-genalyzer:`actions/runs/5677400027/job/15385644518]]` 

4. Run fft_analysis.m example

::

     It generates a .json file that can be used to configure settings for custom FFT analysis 

5. In matlab command window, type help genalyzer for more info on properties

PUTTY

Link: https://www.putty.org/ Version: Any version is fine

IIO Oscilloscope

Link: :git-iio-oscilloscope:`actions/runs/5334364156` Note: Need a Github account with your ADI email to download Version: Above link is the latest version from the software team

LibIIO Installer

Install the latest libIIO package from github https://swdownloads.analog.com/cse/azure_builds/libiio-setup.exe `libiio <https://github.com/analogdevicesinc/libiio>`__

--------------

Booting ADXBAND16EBZ
====================

1. You will already have needed to follow the Software Installation instructions above and have a Triton image on your PC. The images come as Zip files so be sure to extract the zip before beginning. 

2. Latest Build Files: vcu118_quad_ad9084_2023-09-28.zip

Power on the board. The recommended power on order is to first provide your 400MHz Reference Clock (4 dBm), Then power on Triton's 12V in, then power on the FPGA.

3. Open up "Xilinx Vivado Lab TCL Shell"

4. Use cd to change directory to where you extracted the Triton Image. You need to use forward slash (/) and put the directory in Quotes. See below

Example: cd "C:/MyTritonStuff/vcu118_quad_ad9084_2023-09-28"

5. Run dir to confirm you are in the right directory. If you are you should see a file named run.tcl and others

6. Run xsdb

7. Run source run.tcl you may also have run_26p4.tcl or others. The procedure is the same just use source <Whichever file you want to run .tcl> instead.

8. The file transfer will begin and take a couple minutes. After the file transfer you will start seeing the boot happen in Putty. 

9. After the board is fully booted and you are asked for your login

::

     Username: root 
     Password: analog 

NIC setup
=========

You will need an extra 1G ethernet NIC available. We typically use a USB NIC

The IP Address for that interface will need to be changed to Static. see below.

1. Locate which NIC is the one you intend to use for Triton. I think the easiest way is to open up command prompt and run ipconfig /all

2. Most of the USB ethernet adapters we have in the lab are Realtek based and will show up with a Description similar to "Realtex USB GbE Family Controller"

3. If you have more than one the easiest way to identify the one you want is unfortunately to just unplug it and see which disappears. 

4. The following steps will require elevated user permissions. \*If you don't have admin see below for a work around

5. Open up Network Connections. Easiest way is Win+R then type ncpa.cpl and hit enter Double click the adapter you want to use for Triton

6. Click "Properties"

7. Double Click "Internet Protocol Version 4 (TCP/IPv4)" Check "Use the following IP address" And select the following settings

IP Address: 192.168.2.10

Subnet Mask: 255.255.255.0

You can leave the rest blank

Click Okay and close out

Alternative if you don't have PC admin.

Boot up Triton, connect the serial console with Putty (See below)

Open up command line and run ipconfig /all find your PC's IP address for the interface you connected Apollo to make a note of it

You will need to make an IP address on the same subnet as your PC for triton to use. For example: if the address you got for your PC is 169.254.177.23 you can use an address like 169.254.177.22. The address for triton should only have the 4th number changed and make sure you don't choose .1 or the same as your PC

In the Triton console run ifconfig eth0 <your PC Ip that you came up with on the same subnet for Triton>

You will need to use this IP for IIO Oscilloscope and matlab instead of the normal so this method is not ideal but works in a pinch

Putty
=====

The Xilinx VCU118 Exposes a UART console which we use to interact with the Microblaze OS directly. The instructions below outline setting it up. Note the instructions below require you to have connected both Micro USB connections to the FPGA and powered it on.

1. Open up Device Manager. You will be asked to log in as Admin but it is not required to view devices only to make changes which you wont need to do.

2. Expand Ports. You will see 2 or more available ports. The VCU118 will show up as 2 ports one labelled "Silicon Labs Dual CP2105 USB to UART Bridge: Enhanced COM Port (COM<some number>)" and "Silicon Labs Dual CP2105 USB to UART Bridge: Standard COM Port (COM<some number>)". Make a note of the COM port number labelled Standard.

Open up PUTTY

3. Change connection type to Serial. 

4. Type in the "COM<the number for the standard port>" in Serial line

5. Change the Speed to 115200 for Triton

6. Click Open

7. Note: If the board is already booted hit enter after the port opens to start seeing stuff. If the board is not booted you won't see anything in the console until it is booted.

IIO Oscilloscope
================

IIO Oscilloscope is a handy way to test with Triton. Note: The instructions below you have Triton already fully booted up and connected to your PC with Ethernet. You will also have needed to follow the instructions above in NIC setup already.

1. Open up IIO Oscilloscope

2. In the connection window that opens first change select or discover contexts to Manual

3. Type in "ip:192.168.2.1"

4. Note: If you used the option in NIC setup that works without Admin use the IP address you configured Triton to use instead

5. Click Refresh

6. You should see a context description populate

7. Click Connect

8. You're good to go :D 

Putty After the board is booted
===============================

Once the board is fully booted you will be asked for a login in Putty

The username is: root

The password is: analog

After logging in run resize

You can run jesd_status to check JESD

There should be no errors with the 13.1 use case

Support
=======

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone FPGA reference designs <community/fpga>` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.
