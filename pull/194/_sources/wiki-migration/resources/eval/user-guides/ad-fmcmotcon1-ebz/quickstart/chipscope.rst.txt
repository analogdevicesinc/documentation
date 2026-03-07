AD-FMCMOTCON1-EBZ ISE Project with Chipscope
============================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_
 This guide provides some quick instructions on how to setup the AD-FMCMOTCON1-EBZ on either:

-  `ZED Board <http://www.zedboard.org/>`_, Rev C or later

Software Tools
--------------

-  Xilinx ISE 14.6
-  Xilinx Chipscope Pro 14.6

Downloads
---------

.. admonition:: Download
   :class: download

   
   | :git-fpgahdl_xilinx:`ISE Project <motor_control/adi_zed_ise_rev2>`
   | :git-fpgahdl_xilinx:`Chipscope Project <motor_control/adi_zed_ise_rev2/Chipscope>`
   |


System Setup
------------

To setup the hardware follow the steps described in the :doc:`Hardware Setup Guide </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/lv_setup_guide>` section.

The FPGA must be programmed with the **top.bit** bitstream that results after compiling the ISE project. This has already been done, the bitstream was generated and it can be found in the ISE project's folder. To program the FPGA use the **iMPACT** tool from Xilinx.

The operation of the system can be controlled and monitored using the Chipscope project from the **Downloads** section.

Chipscope Interface
-------------------

The user interface uses Xilinx Chipscope 14.6. The project is available in the **Downloads** section. In order to be able to see the plots from section C and D, the triggers from UNIT:1 and UNIT:2 must be enabled.

| 
| |chipscope.png|
| The A section is used for control.

+---------------------------------------------+-------+----------------------------------------------------------------------------------------+
| Name                                        | Width | Description                                                                            |
+=============================================+=======+========================================================================================+
| PWM                                         | 32    | PWM value for controlling the motor. It must be larger than 0x480 and less than 0x800  |
+---------------------------------------------+-------+----------------------------------------------------------------------------------------+
| GAIN                                        | 2     | Amplification on the ADC signal chain. 0 - Gain 1, 1 - Gain 4, 2 - Gain 2, 3 - Gain 8  |
+---------------------------------------------+-------+----------------------------------------------------------------------------------------+
| RUN_MOTOR                                   | 1     | Start / Stop the motor                                                                 |
+---------------------------------------------+-------+----------------------------------------------------------------------------------------+
| STAR_MOTOR                                  | 1     | Set to 1 for star wired motors, set to 0 for delta wired motors                        |
+---------------------------------------------+-------+----------------------------------------------------------------------------------------+
| CW_DIR                                      | 1     | Set to 1 for clockwise direction of rotation, set to 0 for counter-clockwise direction |
+---------------------------------------------+-------+----------------------------------------------------------------------------------------+
| **Table 1 Section A parameter description** |       |                                                                                        |
+---------------------------------------------+-------+----------------------------------------------------------------------------------------+

The B section is used for checking the waveform for the currents in the design.

+---------------------------------------------+-------------------------------------------------------------------------+
| Name                                        | Description                                                             |
+=============================================+=========================================================================+
| IA_DRV                                      | IA current as read on the low voltage motor driver board                |
+---------------------------------------------+-------------------------------------------------------------------------+
| IB_DRV                                      | IB current as read on the low voltage motor driver board                |
+---------------------------------------------+-------------------------------------------------------------------------+
| IT_DRV                                      | IT current as read on the low voltage motor driver board                |
+---------------------------------------------+-------------------------------------------------------------------------+
| IA                                          | IA current as read on the controller board                              |
+---------------------------------------------+-------------------------------------------------------------------------+
| IB                                          | IB current as read on the controller board                              |
+---------------------------------------------+-------------------------------------------------------------------------+
| IT                                          | IT current as read on the controller board                              |
+---------------------------------------------+-------------------------------------------------------------------------+
| VBUS                                        | VBUS voltage as seen on the controller board                            |
+---------------------------------------------+-------------------------------------------------------------------------+
| SPEED                                       | Time between a change of the HALL sensors state measured in 100ns units |
+---------------------------------------------+-------------------------------------------------------------------------+
| POSITION                                    | HALL sensors reading                                                    |
+---------------------------------------------+-------------------------------------------------------------------------+
| **Table 2 Section B parameter description** |                                                                         |
+---------------------------------------------+-------------------------------------------------------------------------+

Section C is used to represent graphically the speed of the motor.

+---------------------------------------------+-------------------------------------------------------------------------+
| Name                                        | Description                                                             |
+=============================================+=========================================================================+
| SPEED                                       | Time between a change of the HALL sensors state measured in 100ns units |
+---------------------------------------------+-------------------------------------------------------------------------+
| **Table 3 Section C parameter description** |                                                                         |
+---------------------------------------------+-------------------------------------------------------------------------+

Section D is used to plot the currents and voltages described in section B.

.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#zynq
   :alt: Linux on Zynq#..:\|Overview#none

.. |chipscope.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/chipscope.png
   :width: 800px
