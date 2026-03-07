:doc:`Click here to return to Stream Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`

Stream based Network Design
===========================

Alternative to the approach of configuring slots in an A2B network using General View/Register view tabs, one could use the Stream based network design approach wherein SigmaStudioPlus does all required A2B slots register settings.

.. note::

   General / Register View and Stream Configuration View are mutually exclusive. On "Auto Slot Calculate" enabled, Stream Configuration gets preference over other views


This feature enables auto configuration of A2B slots based on the network wide stream specification. It also facilitates mechanism to store, communicate and import of network wide stream information.

Network wide Stream Configuration
---------------------------------

Open Stream configuration window by right clicking Target processor.

Stream Definition
~~~~~~~~~~~~~~~~~

This window allows the user to define streams along with properties like sampling rate, number of channels per stream etc. Separate option is provided to edit a selected stream properties. User may remove as well as re-order a selected stream using the respective options.

.. note::

   We can also create, add, or delete streams using Thrift. For more information, you can refer to the :doc:`stream configuration using Thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`.


.. note::

   User shall provide a unique name and ID for each stream.


.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ **Figure:** Stream Definition Window


Stream Assignment
~~~~~~~~~~~~~~~~~

All the defined streams are available for assignment. For each stream, user needs to select the source and destination. Each stream can have a single source and one or more destination. The option "*Auto Slot Calculate*" ensures that slot configuration registers are programmed according to the assignment during schematic Link/download. Optionally, user may trigger slot calculation based on the current assignment by using the button “Calculate Now”.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ **Figure:** Stream Assignment


.. note::

   The *‘Auto Slot Calculate’* option uses sub-node to sub-node communication. Hence, it is enabled only when all the nodes support sub-node to sub-node communication


.. note::

   Download button dynamically writes the current stream assignment to the network without the need of rediscovery


Data Tunnel Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Like audio, Data tunnels can be defined with the properties like name, tunnel down slots & tunnel up slots. Further, data tunnel can be configured by selecting the participating nodes. Configuration window ensures that user cannot create overlapping data tunnels. ‘Auto Slot Calculate’ option ensures that the data tunnel offsets are calculated implicitly while adhering to the constraints.

.. note::

   We can also create and modify tunnel configurations using Thrift. For more information, you can refer to the :doc:`Tunnel configuration using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/streamconfiguration>`.


.. note::

   ‘Strict Bound’ option ensures that data tunnel slots are not passed beyond the first & last node of the tunnel. However, disabling the ‘Strict Bound’ allows data tunnel offset constraints to be relaxed and can potentially accommodate wider set of use cases.


.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ **Figure:** Data Tunnel Configuration


Node specific Stream Information
--------------------------------

The *‘Stream View’* tab of *‘Device Properties’* window as shown in the below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`, captures the node level information based on the stream assignment. User can view all the streams associated with the current node. Usage of the streams, direction and corresponding bus slots are captured in the in this view. Note that *‘Stream View’* will be populated only when *“Auto Slot Calculate”* option is enabled during Stream Assignment. *‘Stream View’* also captures the bandwidth used by the current node.

.. note::

   Stream configuration window and ‘Stream View’ can be viewed concurrently. One can use the “Apply” button of stream configuration window to trigger slot calculation. The latest changes with respect to the current node shall be viewed by clicking the “Refresh” button of device properties (as shown in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`).


.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   \ **Figure:** Stream View


.. note::

   The *‘Auto Slot Calculate’* option uses sub-node to sub-node communication. Hence, it is enabled only when all the nodes support sub-node to sub-node communication


.. note::

   Download button dynamically writes the current stream assignment to the network without the need of rediscovery


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/stream_definition.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/stream_properties1.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/stream_assignment.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/data_tunnel_2stream.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/stream_view.png
