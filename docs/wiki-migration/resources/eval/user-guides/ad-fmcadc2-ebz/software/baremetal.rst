AD-FMCADC2-EBZ Bare Metal Quick Start Guide
===========================================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD-FMCADC2-EBZ on either:

-  `ZC706 <https://www.xilinx.com/ZC706>`__
-  `VC707 <https://www.xilinx.com/VC707>`__

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

-  After :doc:`building the project on Vivado </wiki-migration/resources/fpga/docs/hdl>`, open the Xilinx SDK.

-  When the SDK starts it asks to provide a folder where to store the workspace. Any folder can be provided.

-  Type a project name and click **Next**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/software/baremetal/new_project.png
   :align: center
   :width: 500px

-  Select the **Empty Application** template and click **Finish**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/software/baremetal/new_empty_project.png
   :align: center
   :width: 500px

-  Download the required source files (check the :doc:`Downloads </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz/software/baremetal>` section).

-  Copy the downloaded source files into **src** folder of the just created empty application.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/software/baremetal/complete_project.png
   :align: center
   :width: 500px

-  The project can be easily debug using the Vivado Hardware Manager and the integrated logic analyzer (ILA) debug cores.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/software/baremetal/hardware_manager.png
   :align: center
   :width: 700px
