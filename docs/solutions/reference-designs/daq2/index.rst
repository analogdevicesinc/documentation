AD-FMCDAQ2-EBZ User Guide
=========================

The :adi:`AD-FMCDAQ2-EBZ` is an FMC board for the high speed :adi:`AD9144` DAC and :adi:`AD9680` ADC. While the complete chip level design package can be found on the ADI product pages of these converters, information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the :adi:`AD-FMCDAQ2-EBZ` is a data acquisition platform that connects the analog world using FMC to the FPGA.

.. image:: images/dac2_top.jpg
   :align: right
   :width: 400

-  :doc:`Introduction </solutions/reference-designs/daq2/introduction>`
-  :doc:`Quick Start Guides </solutions/reference-designs/daq2/quickstart>`

   -  :doc:`Linux on ZC706 </solutions/reference-designs/daq2/quickstart/zynq>`
   -  :doc:`Linux on ZCU102 </solutions/reference-designs/daq2/quickstart/zcu102>`
   -  :doc:`Linux on KCU105, KC705, VC707 </solutions/reference-designs/daq2/quickstart/microblaze>`
   -  :doc:`Linux on Arria10 SoC Development Kit </solutions/reference-designs/daq2/quickstart/a10soc>`
   -  :doc:`Linux on Arria10 GX FPGA Development Kit </solutions/reference-designs/daq2/quickstart/a10gx>`

-  :doc:`Hardware </solutions/reference-designs/daq2/hardware>` (including :doc:`schematics </solutions/reference-designs/daq2/hardware>`)

   -  :doc:`Functional Overview & Specifications </solutions/reference-designs/daq2/hardware/functional_overview>`
   -  :doc:`Characteristics & Performance </solutions/reference-designs/daq2/hardware/card_specification>`

-  :doc:`Reference HDL Design </solutions/reference-designs/daq2/reference_hdl>`
-  :doc:`Software </solutions/reference-designs/daq2/software>`

   -  `High Speed Converter Toolbox for MATLAB and Simulink <https://wiki.analog.com/resources/tools-software/hsx-toolbox>`_
   -  :doc:`No-OS drivers </solutions/reference-designs/daq2/software/baremetal>`
   -  :doc:`Linux </solutions/reference-designs/daq2/software/linux>`

      -  :doc:`ZC706, ... </solutions/reference-designs/daq2/software/linux/zynq>`
      -  :doc:`KCU105, KC705, VC707 (Microblaze) </solutions/reference-designs/daq2/software/linux/microblaze>`
      -  `A10GX (Nios2) <https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/nios2>`_
      -  :doc:`Applications </solutions/reference-designs/daq2/software/linux/applications>`

         -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
         -  `FMCDAQ2 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcdaq2_plugin>`_

-  :doc:`Clocking Tree </solutions/reference-designs/daq2/clocking>` (including samplerate reconfiguration)
-  :doc:`Production Testing Process </solutions/reference-designs/daq2/testing>`
-  :doc:`Help and Support </solutions/reference-designs/daq2/help_and_support>`

Videos
======

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/analogtv>3726581576001
   :alt: analogTV>3726581576001

.. esd-warning::


.. toctree::
   :hidden:

   clocking
   hardware
   hardware/card_specification
   hardware/functional_overview
   help_and_support
   introduction
   quickstart
   quickstart/a10gx
   quickstart/a10soc
   quickstart/microblaze
   quickstart/zcu102
   quickstart/zynq
   reference_hdl
   software
   software/baremetal
   software/linux
   software/linux/applications
   software/linux/applications/fru_dump
   software/linux/applications/iio_scope
   software/linux/applications/libiio
   software/linux/microblaze
   software/linux/zynq
   testing
