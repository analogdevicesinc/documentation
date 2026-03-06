Introduction
============

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated. Please check out our latest guide at https://analogdevicesinc.github.io/hdl/user_guide/introduction.html\


ADI provides FPGA reference designs for selected hardware featuring some of our products interfacing to publicly available FPGA evaluation boards. This wiki documentation details the HDL resources of these reference designs.

A list of supported hardware can be found here:

-   :doc:`Intel </wiki-migration/resources/alliances/altera>`
-   :doc:`Xilinx </wiki-migration/resources/alliances/xilinx>`

About this guide
----------------

The main purpose of this user guide is to help you understand and use (modify or otherwise) the HDL resources provided by Analog Devices and to provide advice and instructions for using these resources. After reading this guide, the user should be able to build a specific project from the HDL repository and be able to modify (if so desire) the digital data path implemented in the FPGA. Furthermore all ADI developed and supported IP is presented in detail.

At the same time, this user guide does not intend to be a guide for any third party tool. To understand and use the HDL framework efficiently the user needs to have a solid understanding how an FPGA works and needs to be familiar with all the design tools and flows. FPGA's and SoC's are highly complex systems, we do not have the time and place to cover every feature and aspect of it.

If somebody does not have this knowledge we highly recommend to make some general research and go through some basic tutorials with her targeted development platform. There can be found a lot of information and documentation at vendor's support pages :

-  `Xilinx support <https://www.xilinx.com/support.html>`__
-  `Intel support <https://www.intel.com/content/www/us/en/programmable/support/support-resources.html>`__

Location of the sources
-----------------------

All the HDL sources can be found at Analog Devices Inc. `Git <https://github.com/analogdevicesinc>`__ repository. Later in this guide, the structure of this repository will be presented.

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#none#hdl
   :alt: Main page#git|Git Repository
