AD-FMCADC2-EBZ Bare Metal Quick Start Guide
===========================================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD-FMCADC2-EBZ
on either:

-  `ZC706 <https://www.xilinx.com/ZC706>`_
-  `VC707 <https://www.xilinx.com/VC707>`_

Downloads
~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  AD-FMCADC2-EBZ no-OS - :git-no-OS:`fmcadc2`
   

Required Software
~~~~~~~~~~~~~~~~~

-  We're upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.
-  A UART terminal (Tera Term/Hyperterminal), baud rate 115200.

Software Setup
~~~~~~~~~~~~~~

-  After `building the project on Vivado <https://wiki.analog.com/resources/fpga/docs/hdl>`_, open the Xilinx SDK.

-  When the SDK starts it asks to provide a folder where to store the workspace.
   Any folder can be provided.

-  Type a project name and click **Next**.

.. image:: ../images/new_project.png
   :align: center
   :width: 500

-  Select the **Empty Application** template and click **Finish**.

.. image:: ../images/new_empty_project.png
   :align: center
   :width: 500

-  Download the required source files (check the `Downloads <https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq2-ebz/software/baremetal>`_ section).

-  Copy the downloaded source files into **src** folder of the just created empty application.

.. image:: ../images/complete_project.png
   :align: center
   :width: 500

-  The project can be easily debug using the Vivado Hardware Manager and the
   integrated logic analyzer (ILA) debug cores.

.. image:: ../images/hardware_manager.png
   :align: center
   :width: 700
