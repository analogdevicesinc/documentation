AD-FMCXMWBR1-EBZ HDL Reference Design
=====================================

Supported Devices
-----------------

-  :adi:`AD-FMCXMWBR1-EBZ`

Supported Carriers
------------------

-  :adi:`ADRV2CRR-FMC`

HDL Design Description
----------------------

The design is built upon ADI's generic HDL reference design framework. More information about the framework can be found in the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` wiki page.

The reference design uses SPI and I2C to interface with the AD-FMCXMWBR1 FMC bridge.

For more details regarding the digital interface, check the main :doc:`ADRV9009ZU11EG HDL Reference Design </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/hdl>` wiki page.

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see :git-hdl:`Release notes <releases>`)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI/I2C signals are controlled by a separate AXI based SPI/I2C core.

AD-FMCXMWBR1-EBZ Specific Boot Files
------------------------------------

.. admonition:: Download
   :class: download

   |FMCXMWBR1 HDL project|

.. include:: ../../../fpga/docs/hdl/downloads_insert.rst

.. image:: https://wiki.analog.com/_media/navigation AD-FMCXMWBR1-EBZ#./
   :alt: Hardware#.:\|Reference HDL Design#.:\|Software

.. |FMCXMWBR1 HDL project| image:: https://wiki.analog.com/_media/:git-hdl:`projects/adrv9009zu11eg/adrv2crr_fmcxmwbr1`
