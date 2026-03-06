:doc:`Click here to return to Stream Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`

Slot Configuration
==================

With sub-node-to-sub-node communication possible with AD242x/3x parts, the way upstream and downstream slots are computed in the A2B schematic varies depending on the A2B transceiver type used. This section describes the slot configuration for AD242x & AD243x types.

AD242x
------

In A242x, with the ability for a sub-node to directly receive/transmit data from/to other sub-nodes without having to move the data all the way up to the main, the Rx and Tx channels configured for the peripherals does not directly translate to the Upstream and Downstream slots.

One can configure slots for AD242x sub-nodes using

-  Stream based network design scheme where the slots are calculated **automatically** based on network wide stream configuration.
-  ‘Slot Config’ tab of window one can **manually** configure slots for AD242x sub-nodes. The fields are elaborated in the following section.

Upstream
~~~~~~~~

**Slots Received at Port B:** Number of slots received at Port B. Calculated as Maximum of ‘UPMaskmax ‘ and ‘Passed up slots from Port B’.

**Slots Passed Up from Port B:** Number of received slots to be passed up from Port B.

**Slots Contributed:** Number of slots being contributed to upstream.

**Receive Offset:** Number of slots which are skipped before transmission.

**Slots Transmitted at Port A:** Number of slots transmitted at Port A. This is the sum of ‘Slots Passed Up from Port B’ + ‘Slots Contributed’.

Downstream
~~~~~~~~~~

**Slots received at Port A:** Number of slots received at Port A. Calculated as Maximum of ‘DNMaskmax’ and ‘Passed down slots from Port A’.

**Slots Passed Down from Port A:** Number of received slots to be passed down from Port A

**Slots Contributed:** Number of slots being contributed to downstream.

**Slots Consumed:** Number of slots being consumed from downstream when the masks are not used.

**Receive Offset:** Number of slots which are skipped before transmission.

**Slots Transmitted at Port B:** This is the sum of ‘Passed down slots from Port A’’ + ‘Slots Contributed’.

**Broadcast Downstream Slots:** This is active only when the Select slots to consume is disabled.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure:** Slot Config – Sub-node Properties Window


AD243x
------

Like AD242x, AD243x can be either configured via ‘stream configuration’ or manual slot configuration in General/Register view. Additionally, stream-based auto-slot calculation is extended to SPI Data tunnels along with audio streams.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/slotconfig1_subnode.png
