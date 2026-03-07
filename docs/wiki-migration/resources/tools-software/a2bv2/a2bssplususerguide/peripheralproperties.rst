:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Peripheral Properties
=====================

Peripheral Programming
----------------------

This section describes the method to be followed for programming peripherals connected to an A2B node.

.. note::

   These peripherals can also be programmed using Thrift automation. For more information, you can refer to ":doc:`Peripheral Programming Using Thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/registeraccessapi>`".


The following general steps are involved in peripheral programming.

-  Create a valid A2B schematic (or open an existing A2B Schematic project) in SigmaStudio+. Make sure that the schematic has at least one peripheral connected to a sub-node.
-  Enter the relevant peripheral node properties (I2C address, Rx/Tx slots).
-  Download the schematic by clicking ‘LinkCompileDownload’ option of SigmaStudio+.
-  Open Peripheral device properties window ‘Open programmable Settings’ by right clicking on peripheral node.

The two options for programming the peripheral devices are explained in the following sub sections.

Generic Peripheral register programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the Generic option, user can read or write any individual register (one at a time) by setting required fields as shown in below Figure.

.. note::

   The Address and Data Widths are in Bytes.


   |image1|

.. container:: centeralign

   **Figure:** Generic peripheral programming window


Block Peripheral register programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Block programming option, user can read or write a set of registers as shown in below Figure. This can be accomplished by providing an xml file containing the instructions to be executed. By checking ‘Program during discovery’ option the peripheral will be programmed during the discovery process. Note that the order of peripheral programming depends on the order in which the peripherals were connected to the A2B node in the platform canvas. This can be updated by the arrow present in the Project window in the right.

.. note::

   The Address and Data Widths are in Bytes. Refer peripheral xml :doc:`specification </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/peripheralxml>` for more details


   |image2|

.. container:: centeralign

   **Figure:** Block peripheral register programming window


An example xml file contents are shown in below Figure. A new peripheral programming file with required :doc:`specification </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/peripheralxml>` can be created by using :doc:`Sequence Window </wiki-migration/resources/tools-software/sigmastudiov2/developmentenvironment/sequencewindow/sequence_window>` . This will open an editor in which the instructions can be added /edited.

Optionally, user can use Integrated DSP for ADI SigmaDSP peripheral corresponding to the XML file provided in the Block Register Read/Write section.


|image3|

.. container:: centeralign

   **Figure:** Sequencer window for creating block programming file.


Embed XML feature
^^^^^^^^^^^^^^^^^

With Embed XML feature, the Peripheral Programming file is appended to the shape file when exporting/saving the shape contents.

Generate XML feature
^^^^^^^^^^^^^^^^^^^^

With Generate XML feature, peripheral programming file embedded as part of shape can be regenerated manually.


|image4|

.. container:: centeralign

   **Figure:** Embed XML and Generate XML feature.


.. note::

   During load shape, if the peripheral configuration data is embedded in the shape file, the GenerateXML feature is auto invoked and XML file will be generated and saved in Project Settings folder


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/generic_peripheral_programming_window.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/block_peripheral_register_programming_window.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/sequencerwindow.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/embedgeneratexml.png
