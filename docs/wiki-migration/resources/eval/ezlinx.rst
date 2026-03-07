
.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_


ezLINX™ iCoupler® Isolated Interface Development Environment
============================================================

The *ez*\ LINX *i*\ Coupler Isolated Interface Development environment provides developers with a cost-effective, plug and play solution for evaluating eight physical Layer, digitally-isolated communication standards(USB, RS-422, RS-485, RS-232, CAN, SPI, I2C and LVDS). The Blackfin ADSP-BF548 processor is used to run the uCLinux operating system and allows for easy customization through the open source hardware and software platform. Development time is significantly reduced for embedded designers and system architects who are designing and evaluating isolated communication standards.The Interfaces on *ez*\ LINX use ADI's isolated transceivers with integrated *i*\ Coupler and *iso*\ Power® digital isolator technology.

Quick Start Installation Setup Guide
------------------------------------

The following guides give a complete step-by-step guide for the initial setup of the ezLINX board, including software installation for the ezLINX application, driver installation and setting the IP address. Before starting the setup guide, check that you have all of the necessary items from the following list to complete the setup process:

Evaluation Kit Contents
~~~~~~~~~~~~~~~~~~~~~~~

| EZLINX-IIIDE-EBZ Evaluation board
| USB A to mini USB B Cable
| Power supply
| ezLINX Software DVD

Installation Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

Select the operating system you are using from the list:

| :doc:`Windows XP Quick Start installation </wiki-migration/resources/eval/ezlinx/windows_xp_installation_and_setup_guide>`
| :doc:`Windows Vista 32-bit/64-bit Quick Start Installation </wiki-migration/resources/eval/ezlinx/windows_vista_installation_and_setup_guide>`
| :doc:`Windows 7 32-bit/64-bit Quick Start Installation </wiki-migration/resources/eval/ezlinx/windows_7_installation_and_setup_guide>`

Hardware
--------

.. container:: col1 left 600px

   The Hardware of the *ez*\ LINX *i*\ Coupler isolated interface development environment contains the ADSP-BF548 blackfin processor with 64MB of RAM and 32MB of Flash memory. The Isolated Physical layer communication standards are implemented using ADI's isolated transceivers with integrated *i*\ Coupler and *iso*\ Power technology. Routing between the various communication standards is implemented at the hardware level. Included are the following:

   
   ::
   
      *[[/resources/eval/ezlinx/isolated-usb|Isolated USB]] using the [[:adi:`en/interface/digital-isolators/adum3160/products/product`.html|ADuM3160]]
      *[[/resources/eval/ezlinx/isolated-can|Isolated CAN]] using the [[:adi:`en/interface/can/adm3053/products/product`.html|ADM3053]] Signal and Power Isolated CAN transceiver
      *[[/resources/eval/ezlinx/isolated-rs485-rs422|Isolated RS-485/RS-422]] using the [[:adi:`en/interface/digital-isolators/adm2587e/products/product`.html|ADM2587E]] Signal and Power Isolated RS-485/RS-422 transceiver
      *[[/resources/eval/ezlinx/isolated-rs232|Isolated RS-232]] using the [[:adi:`en/interface/digital-isolators/adm3252e/products/product`.html|ADM3252E]] Signal and Power Isolated RS-232 transceiver
      *[[/resources/eval/ezlinx/isolated-i2c|Isolated I2C]] using the [[:adi:`en/interface/digital-isolators/adum1250/products/product`.html|ADuM1250]] and [[:adi:`en/interface/digital-isolators/ADuM5000/products/product`.html|ADuM5000]]
      *[[/resources/eval/ezlinx/isolated-spi|Isolated SPI]] using the [[:adi:`en/interface/digital-isolators/ADuM3401/products/product`.html|ADuM3401]], [[:adi:`en/interface/digital-isolators/ADuM3402/products/product`.html|ADuM3402]] and [[:adi:`en/interface/digital-isolators/ADuM5000/products/product`.html|ADuM5000]]
      *[[/resources/eval/ezlinx/isolated-lvds|Isolated LVDS]] using the [[:adi:`en/interface/digital-isolators/ADuM3442/products/product`.html|ADuM3442]], [[:adi:`en/interface/digital-isolators/ADuM5000/products/product`.html|ADuM5000]], [[:adi:`en/interface/lvds/adn4663/products/product`.html|ADN4663]] and [[:adi:`en/interface/lvds/adn4664/products/product`.html|ADN4664]]

      |image1|

.. container:: col2 right 300px

   
   .. admonition:: Download
      :class: download

      :adi:`Download Schematics <static/imported-files/eval_boards/ezLINX_Schematic.pdf>`

   


.. container:: col2 right 300px

   


   ..

.. container:: col2 right 300px

   
   .. admonition:: Download
      :class: download

      :adi:`Download PCB Manufacturing Files <static/imported-files/eval_boards/ezLINXPCBManufacturing.zip>`

   


.. container:: col2 right 300px

   
   .. admonition:: Download
      :class: download

      :adi:`Download Bill of materials <static/imported-files/eval_boards/ezLINX-PCB-Bill_of_Materials.pdf>`

   


.. container:: col1 left 600px

   
   // // // //
   
   The ezLINX™ Development Platform also includes the following:
   
   -  :doc:`Hirose FX8 120P-SV(91) Extender Connector </wiki-migration/resources/eval/ezlinx/extender-connector>` for daughter board connections.
   -  :doc:`RS-232 DB-9 Console Connector </wiki-migration/resources/eval/ezlinx/rs232-console>`
   -  :doc:`1.2V, 2.5V, 3.3V, 5V Regulated Output Voltages </wiki-migration/resources/eval/ezlinx/power>`
   
   A full list of jumper configurations for the *ez*\ LINX hardware can be found :doc:`here </wiki-migration/resources/eval/ezlinx/config>`.


Software
--------

Sample PC Application Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: col1 left 600px

   The ADSP-BF548 Blackfin processor is running open source uCLinux kernel and sample application. The sample PC Application integrates with the *ez*\ LINX hardware platform via isolated USB, allowing for a complete plug and play evaluation and development experience with 8 isolated communication standards.

   
   .. image:: https://wiki.analog.com/_media/eval/ezlinx-pcapp.png
      :align: center
      :width: 600px
   


.. container:: col1 right 300px

   
   .. admonition:: Download
      :class: download

      :adi:`Download PC Application Install files <static/imported-files/eval_boards/ezLINXPCApp.zip>`

   


.. container:: col2 right 300px

   


   ..

.. container:: col1 right 300px

   
   .. admonition:: Download
      :class: download

      :adi:`Download PC Application Source Code <static/imported-files/eval_boards/ezLINXPCAppSourceCode.zip>`

   


Sample PC Application Software User guide
-----------------------------------------

The sample PC Application is available for

-  Windows XP
-  Windows Vista
-  Windows 7

| :doc:`Software User Guide for the Sample PC Application </wiki-migration/resources/eval/ezlinx/pcapp-software-user-guide>`.

Kernel Update Guide
-------------------

| The ezLINX board allows for the embedded kernel of the Blackfin® Processor to be updated with the latest version of the kernel image file. This will improve the functionality and reliability of the board.
| For the step-by-step kernel update guide and the latest image file, follow the link below:
| :doc:`Kernel Update Guide </wiki-migration/resources/eval/ezlinx/kernel_update>`

Kernel Restore Guide
--------------------

| If the kernel image file becomes corrupted then the ezLINX board cannot be connected to the PC application. In this case the factory reset feature can't be used and in order to re-establish the connection the kernel must be restored from the back-up location in the ezLINX board's flash memory. This process can also be used to revert the embedded software on the ezLINX board back to its original version.
| For the step-by-step kernel restore guide, follow the link below:
| :doc:`Kernel Restore Guide </wiki-migration/resources/eval/ezlinx/kernel_restore>`

Troubleshooting
---------------

:doc:`Troubleshooting Guide </wiki-migration/resources/eval/ezlinx/troubleshooting>`

Software License
----------------

:doc:`Software License </wiki-migration/resources/eval/ezlinx/software_license>`

.. |image1| image:: https://wiki.analog.com/_media/eval/ezlinxblockdiagram.png
   :width: 550px
