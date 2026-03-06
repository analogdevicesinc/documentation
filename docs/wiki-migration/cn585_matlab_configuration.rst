Steps for MATLAB Configuration of LLDK
======================================

-  Install “Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio” from Matlab Add-Ons, as shown in Figure 1:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/communications_toolbox_installation.png
   :width: 400px

Figure 1:Communications Toolbox Installation

-  On the remote machine terminal (Cygwin is recommended for Windows) write the following commands:

   -  git clone https://github.com/analogdevicesinc/HighSpeedConverterToolbox.git

      -  cd HighSpeedConverterToolbox
      -  ../HighSpeedConverterToolbox> git submodule update --init --recursive
      -  ../HighSpeedConverterToolbox > git checkout cn0585_v1
      -  ../HighSpeedConverterToolbox> matlab .

-  Loopback the DACs channels as shown in ` </resources/eval/user-guides/circuits-from-the-lab/cn0585/loopback_connection.jpg>`__
-  From Matlab expand the test folder, open the CN0585StreamingTest.m and press the Run button.
