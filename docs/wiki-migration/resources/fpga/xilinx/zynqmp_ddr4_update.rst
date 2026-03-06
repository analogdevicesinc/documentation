ZynqMP DDR4 SODIMM update
=========================

This page provides a quick guide on how to update the initialization sequence for the new zcu102 boards shipped with the MTA8ATF51264HZ-2G6B1 DDR4 SODIMM part.

.. tip::

   More info on:

   
   - https://www.xilinx.com/support/answers/71961.html
   
   - https://www.xilinx.com/support/answers/72113.html\


Steps
-----

\* Open Xilinx Software Development Kit (XSDK) and provide the workspace location

\* Create a new Application Project: go to File → New → Application Project

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new-app.png
   :width: 400px

\* Specify the Hardware Description File: in the Target Hardware section -> New

\* Fill the Project name and browse for the desired hdf file

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new-hw.png
   :width: 400px

\* Hit Finish

\* Change the directory to the generated app

.. container:: box center

   cd /home/analog


\* Get the ddr patch script

.. container:: box center

   wget ':git-wiki-scripts:`no-OS/zynqmp_ddr_patch`.sh'


\* Apply the patch

.. container:: box center

   ./ddr_patch.sh hw/psu_init.tcl


\* Now the app should work normally
