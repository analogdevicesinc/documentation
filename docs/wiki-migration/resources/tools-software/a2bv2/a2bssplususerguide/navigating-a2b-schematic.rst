:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

SUPPORTED PLATFORMS
===================

Standard Platforms
------------------

The A2B Plugin for SigmaStudio+ gives the following default platforms for the user:

**A2B**

::

     *  **AD242x:**
     * LPS/ Main /Sub node
       * EVAL-AD2428WD1BZ
     * Sub node only
       * EVAL- AD2428WB1BZ
       * EVAL- AD2428WC1BZ
   * **AD243x:**
     * LPS/ Main /Sub node
       * EVAL- AD2433WA1BZ
       * EVAL- AD2435WA3LZ
       * EVAL- AD2430WD1BZ
       * EVAL- AD2437A1NZ
       * EVAL- AD2437A1MZ
     * LPS/Main node
       * EVAL- AD2438WD1BZ
     * Sub node only
       * EVAL- AD2433WB1BZ
       * EVAL- AD2435WJ3LZ
       * EVAL- AD2430WC1BZ
       * EVAL- AD2430WG1BZ
       * EVAL- AD2437B1NZ
       * EVAL- AD2437B1MZ
       

**A2BBusAnalyzer**

-  **AD242x:** This can be used for Main/Sub Node Emulation or Bus Monitoring of 242x transceiver variants in the A2B Bus Analyzer Hardware
-  **AD243x:** This can be used for Main/Sub Node Emulation or Bus Monitoring of 243x transceiver variants in the A2B Bus Analyzer Hardware

.. note::

   Refer :doc:`A2B Bus Analyzer Platform </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/a2banalyzerplatform>` for further information on Analyzer.


   |image1|

.. container:: centeralign

   **Figure:** A2B platforms in toolbox


Transceivers and Peripherals
----------------------------

In addition to these, the plugin also provides a range of transceivers and generic peripheral devices as follows:

-  AD242x, AD243x Main transceiver
-  AD242x, AD243x Subordinate transceiver
-  Generic device: A device that takes an xml file as input for programming via I2C and SPI.
-  Non-Programmable generic device: A device that is used for representing not programmable peripherals in A2B system (e.g. Microphone).

These devices are available as part of the toolbox once inside the platform view/canvas as shown in below, the platform canvas can be opened by double clicking on the platform in the system view or by clicking the “Canvas” option under the platform in the Project window.

Custom Platforms
----------------

A2B Platforms different from standard platforms can be created using custom platforms. This is also available as part of tool box.

.. note::

   \ :doc:`How to create loadable custom platforms </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/defineplatforms>`


.. note::

   \ `Refer <https://wiki.analog.com/resources/tools-software/sigmastudiov2/usingsigmastudio/_customvsstandard>`_ Standard vs Custom Platforms


Generic device
--------------

A generic device is not a fixed-function peripheral but rather a configurable node that can be programmed to behave in specific ways depending on the system requirements. These generic devices can be programmable or non-programmable. This is part of custom platform / standard platform. This can be programmed via I2C/SPI using xml files which is provided as an input as shown in the figure.\


|image2|

.. container:: centeralign

   **Figure:** XML update for Peripheral device


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tree_toolbox_.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/1961_peripheral.png
   :width: 400px
