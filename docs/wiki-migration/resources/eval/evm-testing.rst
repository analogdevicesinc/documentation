EVM Testing With MATLAB
=======================

This guide explains LTE EVM testing for IIO-based device with MATLAB. The following devices are supported:

-  ADALM-PLUTO
-  FMComms 2/3/4
-  ADRV936X

Set Up Process
--------------

To run these test you will need the following

-  MATLAB R2018b or later
-  `PlutoSDR Support Package <https://www.mathworks.com/hardware-support/adalm-pluto-radio.html>`__ or `Communications Toolbox Support Package for Xilinx Zynq-Based Radio <https://www.mathworks.com/matlabcentral/fileexchange/48491-communications-toolbox-support-package-for-xilinx-zynq-based-radio>`__
-  `ADI Board Support Package <https://gitlab.com/tfcollins/MathWorks_tools/-/jobs/artifacts/master/download?job=deploy>`__
-  A device listed above

Once everything is installed, clone the MathWorks_tools repo which contains the EVM testing code.

::

   git clone https://github.com/analogdevicesinc/MathWorks_tools.git

Checkout the testing branch

::

   cd MathWorks_tools
   git checkout evm-tests

Running Tests
-------------

Next, from within MATLAB navigate to the folder ``'MathWorks_tools/test/perf``' from the MathWorks_tools repo downloaded previously.

Before running tests, make sure the necessary URI(s) are updated to match your device(s) on :git-MathWorks_tools:`Line 7 <test/perf/HardwarePerformanceTests.m#L7>` and :git-MathWorks_tools:`Line 8 <test/perf/HardwarePerformanceTests.m#L8>`. If you are using one device the URIs should be the same.

Tests can be run in the following way:

-  To run all tests run the command: ``'hwTestRunner``'
-  To run an individual test use the following API: ``'runtests('HardwarePerformanceTests','ProcedureName','<testname>')``', where testname is one of the function names starting from :git-MathWorks_tools:`line 414 <test/perf/HardwarePerformanceTests.m#L414>`. Example testnames are LTE_R4_Pluto or LTE_R4_RFSOM.
