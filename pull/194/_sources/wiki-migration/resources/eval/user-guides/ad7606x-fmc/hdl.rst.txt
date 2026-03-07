AD7606X HDL Reference Design
============================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/ad7606x_fmc/index.html\


Introduction
------------

The :adi:`EVAL-AD7606B-FMCZ` and :adi:`EVAL-AD7606C-18` evaluation boards are designed to help users to easily evaluate the features of :adi:`AD7606B`, :adi:`AD7606C-16` and :adi:`AD7606C-18` analog-to-digital converters (ADCs).

Used devices
~~~~~~~~~~~~

-  :adi:`AD7606B`
-  :adi:`AD7606C-16`
-  :adi:`AD7606C-18`
-  :adi:`ADP7118`
-  :adi:`ADR4525`

Evaluation board
~~~~~~~~~~~~~~~~

-  :adi:`EVAL AD7606B Product Page <EVAL-AD7606B-FMCZ>`
-  :adi:`EVAL AD7606C-16/18 Product Page <EVAL-AD7606C-18>`

Supported FPGA carrier
~~~~~~~~~~~~~~~~~~~~~~

-  `ZEDBOARD <https://digilent.com/reference/programmable-logic/zedboard/start>`_

Reference HDL Design
--------------------

The design is built upon ADI's generic HDL reference design framework. In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design framework in general.

Block diagram
~~~~~~~~~~~~~

-  AD7606X_FMC using the **PARALLEL** interface

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7606x-fmc/ad7606x_parallel_hdl.svg
   :alt: AD7606X_FMC with Parallel Interface
   :align: center

Required software
~~~~~~~~~~~~~~~~~

-  We're upgrading the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <releases>`.
-  An UART terminal (Tera Term/Hyperterminal), baud rate set to 115200.

Parameters
~~~~~~~~~~

+-------------------+---------------+------------------------------------------------------------------------+
| Parameter name    | Default value | Description                                                            |
+===================+===============+========================================================================+
| DEV_CONFIG        | 0             | Device that will be used: 0 - AD7606B, 1 - AD7606C-16, 2 - AD7606C-18  |
+-------------------+---------------+------------------------------------------------------------------------+
| SIMPLE_STATUS_CRC | 0             | ADC Read Mode options: 0 - Simple, 1 - STATUS, 2 - CRC, 3 - STATUS_CRC |
+-------------------+---------------+------------------------------------------------------------------------+
| EXT_CLK           | 0             | External clock option for the ADC clock: No(0), Yes(1)                 |
+-------------------+---------------+------------------------------------------------------------------------+

Using the HDL reference design
------------------------------

In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design in general.

In the :doc:`axi_ad7606x's </wiki-migration/resources/fpga/docs/axi_ad7606x>` wiki page, can be found a detailed description of the core.

The data path of the HDL design is simple as follows:

-  the parallel interface is controlled by the axi_ad7606x IP core
-  the serial interface is controlled by the SPI Engine Framework
-  data is written into memory by a DMA (axi_dmac core)
-  all the control pins of the device are driven by GPIO's

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see :git-hdl:`Release notes <releases>`)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Choose the required interface (see caption **Switching between interface types**)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

Switching between device types, operation modes and clocking option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the board power-up, the user has to choose the device type, operation mode and clocking option. Depending on the operation mode, some hardware modifications need to be done on the board and/or Tcl script:

In case of the **AD7606C-16** device:

.. code:: c

   $ make DEV_CONFIG=1

In case of the **STATUS** operation mode:

.. code:: c

   $ make SIMPLE_STATUS_CRC=1

PL Interrupts
^^^^^^^^^^^^^

=============== ============= ===================
Instance        HDL interrupt Linux PsU interrupt
=============== ============= ===================
---             0             89
---             1             90
---             2             91
---             3             92
---             4             93
---             5             94
---             6             95
---             7             96
---             8             104
---             9             105
---             10            106
---             11            107
---             12            108
axi_ad7606x_dma 13            109
---             14            110
---             15            111
=============== ============= ===================

GPIO signals
^^^^^^^^^^^^

Ps7 EMIO offset = 54

=========== ===== ==============
GPIO Signal GPIO  HDL GPIO EMIOn
=========== ===== ==============
adc_serpar  93    39
adc_refsel  92    38
adc_reset   91    37
adc_stby    90    36
adc_range   89-87 35
adc_os      86    34-32
=========== ===== ==============

Register Map
~~~~~~~~~~~~

The register map of the core contains instances of three generic register maps: Base, ADC common and ADC channel. The following table presents the base addresses of each instance, after that can be found the detailed description of each generic register map. The absolute address of a register should be calculated by adding the instance base address to the registers relative address.

.. include:: ../../../fpga/docs/hdl/regmap.rst .. include:: ../../../fpga/docs/hdl/regmap.rst .. include:: ../../../fpga/docs/hdl/regmap.rst

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |AD7606X-FMC HDL Project.|

Support
-------

.. hint::

   **Questions?** Feel free to ask your questions in EngineerZone support forums.

   
   -  :ez:`FPGA Reference Design <community/fpga>`
   -  :ez:`Microcontroller no-OS Drivers <community/linux-device-drivers/microcontroller-no-os-drivers>`.
   


.. |AD7606X-FMC HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/ad7606x_fmc`
