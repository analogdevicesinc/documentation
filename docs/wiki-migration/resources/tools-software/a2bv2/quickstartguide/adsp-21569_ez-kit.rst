:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

Using ADSP-21569 EZ-Kit
=======================

The ADSP-21569 EZ-Kit leverages the SigmaStudio+ framework to simplify the development and deployment of audio processing applications, particularly in A2B network environments. By flashing the SS+ target framework onto the board, developers can use graphical schematics to configure audio signal paths, manage A2B nodes, and deploy DSP algorithms without writing low-level code. The framework supports real-time interaction with the board through USBi and JTAG, enabling rapid prototyping and debugging of complex audio systems.

Flashing the target framework
-----------------------------

To enable communication between SigmaStudio+ and the EZ-Kit, a prebuilt target framework must be flashed onto the board. This process involves using the CrossCore Serial Flash Programmer to load the appropriate .ldr file, ensuring the board is ready for real-time schematic interaction. Here is the link to flash the programmer :doc:`Flashing ADSP-21569 SOM </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-h>`.

Building ADSP-21569 Project
---------------------------

Refer :doc:`building ADSP-21569 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-d>` to further information on building ADSP-21569 project.

Running sample demo
-------------------

Once the framework is flashed, developers can load a schematic in SigmaStudio+, connect to the board via USBi, and run the A2B demo. Here are the detailed steps :doc:`ADSP-21569 EZ-Kit as A2B Main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/adsp-21569_ez-kit_as_a2b_main>`.
