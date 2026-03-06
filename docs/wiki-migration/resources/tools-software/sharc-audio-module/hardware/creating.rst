Creating your own Fin Board
===========================

Are you interested in creating your own Fin board to connect to the expansion interface of the SHARC Audio Module? This page contains a number some things to help you get started.

Fin - EAGLE Template
--------------------

The link below contains an Autodesk EAGLE schematic and PCB layout files for a blank SHARC Audio Module Fin with the two 64-pin headers.

`adi_sam_fin_template_v1.0.zip <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/adi_sam_fin_template_v1.0.zip>`__

The rendering below shows the front and back side of the PCB template.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sharc_fin_template_rendering.png
   :align: center
   :width: 600px

`Autodesk EAGLE <https://www.autodesk.com/products/eagle/overview>`__ is an affordable yet powerful schematic capture and layout tool and used extensively in the maker space. It's free for students and has a subscription fee of $15/month for the standard edition. It's also closely linked with `Autodesk Fusion 360 <https://www.autodesk.com/campaigns/fusion-360-for-hobbyists>`__ which is a powerful 3D CAD tool that is free for hobbyists and makers.

If you're looking for a low-cost PCB fab to fab for your Fin, check out https://oshpark.com/.

To access the components used in the PCB design, go to File->Export->Libraries when editing the PCB. This will create a new EAGLE library file with the components used in the template design.

Fin Design Considerations
-------------------------

The ADSP-SC589 has a rich peripheral set. Despite the fact that many of these are brought out to connectors on the SHARC Audio Module, there are still quite a few GPIO pins and other peripherals that are accessible on the two 64-pin expansion headers of the SHARC Audio Module.

The signals brought out the 64-pin headers are generally not used in other areas of the SHARC Audio Module with a few exceptions:

TWI / I2C (TWI0 / TWI1 / TWI2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  TWI0 and TWI1 are multiplexed together on the SHARC Audio Module. The multiplexed TWI signal is connected the ADAU1761 audio codec, the AD2425W A2B controller, the clock generation chip on the SHARC Audio Module, and the SigmaStudio tuning header (P2) for the USBi dongle (when using SigmaStudio). The mux is there to ease peripheral sharing between cores when the ARM is running Linux but otherwise is not really needed. The mux is controlled by PB08 and shown on sheet 4 of the SHARC Audio Module `schematics <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/a0939-2016.pdf>`__. The bare metal framework configures the mux to use TWI0 by default leaving TWI1 open.
-  **TWI2 is not connected to anything on the SHARC Audio Module and is the recommended TWI port to use on Fin boards.**

SPI (SPI0 / SPI1 / SPI2)
~~~~~~~~~~~~~~~~~~~~~~~~

-  SPI0 and SPI1 are available on the 64-pin header. SPI1 is also used on the SigmaStudio tuning header (P2). **SPI0 is the recommended SPI port to use on Fin boards.**
-  SPI2 connects to the boot flash on the SHARC Audio Module. The boot flash is only accessed at power up and when reprogramming the flash from the tools.

UART (UART0 / UART1 / UART2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  UART0 is brought out to the FTDI header on the SHARC Audio Module.

::

   *** UART1 and UART2 are unused so either or both may be used on a Fin board.**

Analog audio signals
~~~~~~~~~~~~~~~~~~~~

-  The ADAU1761 has an auxiliary set of analog inputs that are brought out to the expansion header. Additionally, the headphone output signals from the ADAU1761 are also brought out to the expansion header. These signals don't go through any sort of buffering so see the ADAu1761 datasheet to learn more about using them. You can also look at the schematics for the Audio Project Fin which uses these.
