Networking Commands
===================

This section describes each of the networking related shell commands in detail.

--------------

Ethernet Status - eth
---------------------

+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Description**   | This command reports the ethernet link status, information about the IP address, `MDNS Hostname <https://en.wikipedia.org/wiki/Multicast_DNS>`__, etc. Audio Starters which support this command use will use DHCP by default and each board will have a unique ethernet IP address which allows multiple ethernet connections to multiple Audio Starter boards. |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | *eth*                                                                                                                                                                                                                                                                                                                                                            |
|                   | |image5|                                                                                                                                                                                                                                                                                                                                                         |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | None                                                                                                                                                                                                                                                                                                                                                             |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | **Hostname** - This is the resolved MDNS Hostname that is unique the SAM board it is running on. This can be used on your local network instead of the IP address.                                                                                                                                                                                               |
|                   | |image6|                                                                                                                                                                                                                                                                                                                                                         |
|                   | |image7|                                                                                                                                                                                                                                                                                                                                                         |
|                   | **IP Address** - This is the local IP address of the Audio Starter which conforms to the IPv4 format. This can also be used in place of the Hostname for connection to the board for applications such as audio over ethernet.                                                                                                                                   |
|                   | **Gateway** - This is the default `gateway <https://en.wikipedia.org/wiki/Default_gateway#:~:text=A%20gateway%20is%20a%20network,networks%20with%20different%20network%20prefixes.>`__\ number of the system.                                                                                                                                                    |
|                   | **Netmask** - This is the default `netmask <https://en.wikipedia.org/wiki/Subnet>`__ of the system.                                                                                                                                                                                                                                                              |
|                   | **MAC Addr** - This is the default `MAC Address <https://en.wikipedia.org/wiki/MAC_address>`__ of the system.                                                                                                                                                                                                                                                    |
|                   | **Link** - This is the status of the ethernet connection. *Up* = Ethernet cable is connected and a link is established. *Down* = No connection detected/established.                                                                                                                                                                                             |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | *eth*                                                                                                                                                                                                                                                                                                                                                            |
|                   | |image8|                                                                                                                                                                                                                                                                                                                                                         |
|                   | //Note that the IP Address and similar parameters can also be retrieved by running the :doc:`syslog </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>` // command.                                                                                                                       |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------

.. image:: https://wiki.analog.com/_media/navigation Shell Commands
   :alt: Filesystem Commands#.filesystem-commands|Filesystem Commands#.|Shell Commands#.development-commands|Development and Debug Commands#.development-commands\|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/eth_help.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/eth.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/eth2.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/eth.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/eth_help.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/eth.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/eth2.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/eth.png
   :width: 400px
