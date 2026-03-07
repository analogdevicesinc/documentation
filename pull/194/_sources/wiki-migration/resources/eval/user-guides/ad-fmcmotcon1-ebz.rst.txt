AD-FMCMOTCON1-EBZ User Guide
============================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_
 The :adi:`AD-FMCMOTCON1-EBZ` is a complete motor drive system on an FMC board. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the **AD-FMCMOTCON1-EBZ** is to provide a complete motor drive system demonstrating efficient control of Brushed DC, BLDC, PMSM and Stepper motors. It consists of 2 boards: a controller board and a drive board. The system incorporates high quality power sources; reliable power, control, and feedback signals isolation; accurate measurement of motor current & voltage signals; high speed interfaces for control signals to allow fast controller response; industrial Ethernet high speed interfaces; flexible control with FPGA/SoC interface.

The **AD-DYNO1-EBZ** dynamometer is provided as an extension of the drive system. This is a dynamically adjustable load that can be used to test real-time motor control performance. It consists of two BLDC motors directly coupled through a rigid connection. One of the BLDC motors acts as a load and is controlled by the DYNO’s embedded control system while then second motor is driven by the **AD-FMCMOTCON1-EBZ**.

This platform is intended to be used as a prototyping system to verify the hardware and the control algorithms before moving to the production stage. It helps reduce the time needed to move a motor control system from concept to production. Example reference designs showing how to use the control solution with Xilinx FPGAs or SoCs and Simulink from Mathworks are provided together with the hardware.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/mc_system.jpg
   :align: right
   :width: 600px

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction>`

   -  :doc:`Electric Motor Drives </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/drives>`
   -  :doc:`Brushed DC Motor Control </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/dc_control>`
   -  :doc:`Brusless DC Motor Control </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/introduction/bldc_control>`

-  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart>`

   -  :doc:`Hardware Setup Guide </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/lv_setup_guide>`
   -  :doc:`Linux on Zynq </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/zynq>`
   -  :doc:`ISE Project with Chipscope </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/chipscope>`

-  :doc:`Hardware </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware>`

   -  :doc:`Controller Board </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_board>`
   -  :doc:`Low Voltage Drive Board </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>`
   -  :doc:`Signal Measurement Chain </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/signal_chain>`
   -  :doc:`Dynamometer Drive System </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/dyno>`

-  :doc:`HDL </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/reference_hdl>`

   -  :doc:`HDL Design for Linux </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/reference_hdl/linux>`
   -  :doc:`ISE HDL Design </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/reference_hdl/ise>`

-  :doc:`Software </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/software>`

   -  :doc:`Linux Drivers </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/linux_drivers>`
   -  :doc:`IIO Scope </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/iio_scope>`

-  :doc:`Simulink Models </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/matlab_models>`
-  :doc:`QDESYS Motor Control IP </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/qdesys_ip>`
-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/help_and_support>`

Videos
======

ADI/Avnet/MathWorks/Xilinx design seminar

.. image:: https://wiki.analog.com/_media/analogTV>3540825244001
   :alt: analogTV>3540825244001

From ADI's 2013 Design Conference


|youtube>-7CscB5sUIw|

.. |youtube>-7CscB5sUIw| image:: https://wiki.analog.com/_media/youtube>-7CscB5sUIw
