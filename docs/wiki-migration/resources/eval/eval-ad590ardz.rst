Evaluation Board for the AD590 2-Terminal IC Temperature Transducer
===================================================================

Description
-----------

This user guide describes the :adi:`EVAL-AD590-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD590.html#eb-overview>` evaluation board hardware and software and includes detailed schematics and PCB layout artwork. This evaluation board is simple, easy-to-use platform which allows direct evaluation of the :adi:`AD590` analog temperature sensor.

The :adi:`AD590` is a 2-terminal integrated circuit temperature transducer that produces an output current proportional to absolute temperature. Requiring supply voltages between 4V and 30V, the device acts as a high impedance, constant current regulator passing 1μA/K. Laser trimming of the chip’s thin-film resistors is used to calibrate the device to 298.2μA output at 298.2K (25°C).

| When using the :adi:`AD590` evaluation board, in addition to this user guide, the user should also consult the :adi:`AD590` datasheet (available at the **Analog Devices, Inc.**, website, www.analog.com).
| === Figure 1. EVAL-AD590-ARDZ FUNCTIONAL BLOCK DIAGRAM === |Figure 1. EVAL-AD590-ARDZ FUNCTIONAL BLOCK DIAGRAM|

Hardware Setup
--------------

Setup Requirements
~~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-AD590-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD590.html#eb-overview>` Evaluation Board
-  SDP/Linduino Controller Board and User Guide
-  PC with a USB port and Windows 7 (32-bit) or higher
-  Serial Terminal Software (Putty/TeraTerm or similar)
-  USB Standard-A to Mini-B cable

Quick Start Procedure
~~~~~~~~~~~~~~~~~~~~~

-  Connect the EVAL-AD590-ARDZ evaluation board to the interface board using the SDP-120 or Arduino connector (switch the J8 jumper accordingly).
-  Connect the interface board thru USB cable to the host PC.
-  Compile the code in the MBED compiler.
-  Start the terminal emulator to access the evaluation board.

Location of Evaluation Board Schematics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The evaluation board schematic diagrams and bill of materials are included with all the supporting documentation on the :adi:`EVAL-AD590-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD590.html#eb-overview>` product page.

Power Supplies
~~~~~~~~~~~~~~

-  The :adi:`EVAL-AD590-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD590.html#eb-overview>` evaluation board is powered by 5V from either an **SDP board** or **Linduino board** via **JP1**. Alternatively, the :adi:`EVAL-AD590-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD590.html#eb-overview>` board can be powered externally via **P9**, which is selected by changing the **JP1** jumper to **position B**.


| 

Figure 2. EVAL-AD590-ARDZ EVALUATION BOARD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|

| |Figure 2. EVAL-AD590-ARDZ EVALUATION BOARD|
| === Figure 3. EVAL-AD590-ARDZ BOARD AND SDP BOARD CONNECTED DIAGRAM ===
| |Figure 3. EVAL-AD590-ARDZ BOARD AND SDP BOARD CONNECTED DIAGRAM|
| ===== Software Setup ===== The software is designed to be simple and straight forward to use. Select which sensor you would like to use, whether you want to use the internal sensor or a remote one and then simply enter a number corresponding to the required command and follow the on-screen prompts. Refer to software manual `EVAL-AD590-ARDZ Mbed Example [Analog Devices Wiki] <:doc:`/wiki-migration/resources/tools-software/product-support-software/eval-ad590ardz`>`__ for more detailed information.
| === FIGURE 4. EVAL-AD590-ARDZ DEMONSTRATION PROGRAM ===

.. image:: https://wiki.analog.com/_media/resources/eval/ad590_demo_program.png
   :alt: Figure 4. EVAL-AD590-ARDZ DEMONSTRATION PROGRAM
   :align: center

.. |Figure 1. EVAL-AD590-ARDZ FUNCTIONAL BLOCK DIAGRAM| image:: https://wiki.analog.com/_media/resources/eval/ad590_functional_diagram.jpg
.. |Figure 2. EVAL-AD590-ARDZ EVALUATION BOARD| image:: https://wiki.analog.com/_media/resources/eval/ad590_eval-ad590-ardz_top.jpg
   :width: 400px
.. |Figure 3. EVAL-AD590-ARDZ BOARD AND SDP BOARD CONNECTED DIAGRAM| image:: https://wiki.analog.com/_media/resources/eval/ad590_20220317_145849.jpg
   :width: 600px
