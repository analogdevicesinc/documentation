:doc:`Click here to return to the A2B Raspberry Pi User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi>`

SigmaStudioPlus Example Schematic for 243x
==========================================

A2B transceivers can be configured using the SigmaStudio+ tool, which offers a graphical interface for programming, development, and tuning of ADI DSP audio processors. With SigmaStudio+, the A2B Master node and Subnode can be configured, as illustrated in the attached image.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/243x_schematic.png
   :align: center

Stream Configuration
--------------------

A2B transceivers can be configured with multiple streams, as shown below. The figure illustrates the stream configuration for the 243x Transceiver.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/243x_stream_configuration.png
   :align: center

Further tuning can be performed for the Main Transceiver node property settings, as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/243x_main_settings.png
   :align: center

Bus Configuration Export
------------------------

To work with the transceiver nodes, a Bus Configuration File (BCF, .bcf) is required, which can be generated as shown below. This .bcf file is necessary for building the A2B Stack application for the Raspberry Pi board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2braspberrypi/export_busconfig.png
   :align: center

Running Example with 243x Transceiver
-------------------------------------

After migrating to the latest A2B stack, export the adi_a2b_busconfig.c file from the respective SigmaStudio+ version (compiled with the A2B stack) and paste it into the appropriate location in the Raspberry Pi application. Then, clean and build the application, and run it as explained in :doc:`Build kernel and Run application </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/buildingkernel>`.

.. note::

   The same .dts file can be used for both 242x and 243x transceivers without any issues.


**PREV :** :doc:`SigmaStudioPlus Example Schematic for 242x </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/schematic242x>`
