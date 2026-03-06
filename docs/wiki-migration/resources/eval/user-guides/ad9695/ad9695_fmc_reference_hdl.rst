AD9695 FMC Card Reference Design
================================

Overview
--------

The AD9695 is a 14-bit, 1300/625MSPS analog-to-digital converter (ADC) featuring an on-chip buffer and a sample-and-hold circuit designed for low power, small size, and ease of use. The dual ADC cores feature a multistage, differential pipelined architecture with integrated output error correction logic. Each ADC features wide bandwidth inputs supporting a variety of user-selectable input ranges.

The AD9695-FMC reference design is a processor based (e.g. Microblaze) embedded system. The design consists of a receive chain.

The receive chain transports the captured samples from the ADC to the system memory (DDR). Before transferring the data to DDR the samples are stored in a 1MB buffer implemented on block rams from the FPGA fabric (util_adc_fifo) or 65k samples per channel.

All cores from the receive chain are programmable through an AXI-Lite interface.

Supported Devices
-----------------

-  :adi:`AD9695-1300EBZ <AD9695>`

Supported Carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`__ - HPC1 Slot

Clock Selection
~~~~~~~~~~~~~~~

-  External clock source :adi:`​HMC7044` :adi:`HMC7044-EVAL <en/​design-center/​evaluation-hardware-and-software/​evaluation-boards-kits/​eval-hmc7044.html>`

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/ad9695_fmc_clocking_0.svg
   :alt: ad9695_fmc_clocking_0.svg

Block Diagram
~~~~~~~~~~~~~

The data path and clock domains are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/ad9695_fmc_8.svg
   :width: 800px

The design has one JESD receive chain with 4 lanes at rate of 13Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module and transport layer represented by a RX JESD TPL module. The links operate in Subclass 0 since it is not using the SYSREF signal.

Both links are set for full bandwidth mode and operate with the following parameters:

Deframer paramaters: L=4, M=2, F=1, S=1, N’=16

| REFCLK – 325MHz (Lane Rate/40)
| DEVICECLK -325 MHz
| ADCCLK – 1300MHz
| JESD204B Lane Rate – 13Gbps

The transport layer component presents on its output 128 bits at once on every clock cycle, representing 4 samples per converter. The two receive chains are merged together and transferred to the DDR with a single DMA.

Building the HDL project
~~~~~~~~~~~~~~~~~~~~~~~~

ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository. Then go to the /projects/ad9695_fmc/zcu102 location and run the make command by typing in your command prompt:

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad9695_fmc/zcu102
   user@analog:~/hdl/projects/ad9695_fmc/zcu102$ make

A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

System setup
~~~~~~~~~~~~

Connections
^^^^^^^^^^^

AD9695 connected to ZCU102 on FMC HPC1

====== ============
ZCU102 HMC7044 EVAL
====== ============
J55-9  J1-12
J55-7  J1-14
J55-3  J1-16
J55-5  J1-18
J55-1  J1-20
J79    J38
J80    J39
====== ============

============ ============
ADC9695 EVAl HMC7044 EVAL
============ ============
P202         J28
============ ============

The HMC7044 EVAL requires a stable 5V power supply and at least 1A.

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/ad9695_eval_setup.jpg
   :width: 800px

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |AD9695 HDL Project.|

Software sources
----------------

.. admonition:: Download
   :class: download

   
   -


   
   |Linux Driver.|

More Information
~~~~~~~~~~~~~~~~

-  :doc:`EVALUATING THE AD9695/AD9697 ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/eval/ad9695-1300ebz>`
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

.. |AD9695 HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/ad9695_fmc`
.. |Linux Driver.| image:: https://github.com/analogdevicesinc/linux
