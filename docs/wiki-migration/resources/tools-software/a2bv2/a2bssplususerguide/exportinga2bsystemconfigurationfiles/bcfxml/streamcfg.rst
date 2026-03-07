Go back to :doc:`Home Page </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>`

Stream_Configuration
====================

This xml element contains below sub elements with attributes.

|image1| Stream_Definition_Info consists of

-   Stream_ID
-   Stream_Name
-   Sample_Rate
-   Data_Width
-   Num_Channels
-   Channels_To_Skip

Stream_Assignment_Info consists of

::

     * Stream_ID 
     * Stream_Name 
   *  Source_Name 
   *  Source_ID 
   *  Dest_Count 
   * Destination_Name_x
   * Destination_ID_0
   *  Routing_style

Each attribute Is of “Byte” Data type except Stream Name which are of “String” Data type.

Tunnel Configuration has below fields

-  Tunnel_ID
-  Tunnel_Name
-  Num_of_Downslots
-  Num_of_Upslots
-  Members_Count
-  Member_Name_0

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image31.png
