:doc:`Click here to return to the Transceiver properties </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/transceiver-properties>`

Crossbar View Dependencies Configuration
========================================

Number of Tx/Rx Pins Configuration
----------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/numberof_tx_rx_pins.png
   :align: center

.. container:: centeralign

   \ **Figure:** Number of Tx/Rx Pins Configuration


TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)
--------------------------------------------------

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure:** TX Crossbar registers (A2B_TXXBAR0 - A2B_TXXBAR31)


RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)
-------------------------------------------------

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ **Figure:** RX Crossbar registers (A2B_RXMASK0 - A2B_RXMASK7)


TDM Mode & Tx/Rx Interleave Configuration
-----------------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tdm_mode.png
   :align: center

.. container:: centeralign

   \ **Figure:** TDM Mode & Tx/Rx Interleave Configuration


Crossbar View with an example
=============================

For example, considering the 3-node schematic with this stream configuration example, crossbar view looks like as mentioned in the snapshots for all the nodes

Sample Stream Definition & Assignment for 3 node schematics
-----------------------------------------------------------

|image3|

.. container:: centeralign

   \ **Figure:** Sample Stream Definition & Assignment for Crossbar view visualization


Crossbar view at subnode0
-------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbar_view_subnode0.png
   :align: center

.. container:: centeralign

   \ **Figure:** Crossbar view at subnode0


Crossbar view at subnode1
-------------------------

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ **Figure:** Crossbar view at subnode1


Crossbar view at Main node with Tx Interleave enabled
-----------------------------------------------------

The similar way Rx Interleave also works.

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   \ **Figure:** Crossbar view at Main node with Tx & Rx Interleave enabled


Context Menu’s on Crossbar
==========================

Context Menu’s on Tx Crossbar at Main Node side
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crossbar supports the below options on Tx pin at the main node side as shown in the below snapshot:

-  Reset Channel Map (this option reset’s channel mapping if any mapping is done manually on crossbar)

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   \ **Figure:** Context Menu's on Tx Pin of Crossbar at Main Node


Context Menu’s on Rx Crossbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Crossbar supports the below options on Rx pin as shown in the below snapshot:

-  Enable Mapping (this option can be used to enable a particular slot on the Rx Pin)
-  Clear Mapping (this option clears the mapping of a particular slot on the Rx pin)

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   \ **Figure:** Context Menu's on Rx Crossbar


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tx_x-bar.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/ad243x_rx-x_bar.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/sample_stream.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbar_view_subnode1.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/crossbar_view_main_tx_rx.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/contextmenu_tx_settings.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/contextmenu_rx_settings.png
