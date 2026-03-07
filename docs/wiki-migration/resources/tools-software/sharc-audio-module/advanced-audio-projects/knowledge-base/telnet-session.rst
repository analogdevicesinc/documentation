Connecting to a Telnet Session
==============================

Overview
--------

A `telnet <https://en.wikipedia.org/wiki/Telnet#:~:text=Telnet%20(short%20for%20%22telecommunications%20network,area%20networks%20or%20the%20Internet.>`_ session on the Audio Starter allows users to connect to the SAM board via an Ethernet connection and provides access to the :doc:`shell commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands>` that are typically accessed via the USB OTG/USB-PHY connections on the Audio Starter hardware.

Details
-------

*This article assumes that the hardware is already up and running and proper connection to the USB port has been established. There are various instructions on setting this up. The* :doc:`Analog Audio </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-analog-audio>` *example is a great place to start.*

*This tutorial uses TeraTerm as the serial interface to your hardware.*

**Follow the instructions below to set up a connection to your hardware:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Establish a shell connection via :doc:`USB OTG/USB-PHY </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/usb-otg-session>`. This will be needed to get the IP address of the system.                                                         | |image8|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. In shell window, type one of the following commands:                                                                                                                                                                                                                                           | |image9|  |
| :doc:`eth </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/network-commands>`                                                                                                                                                                  |           |
| or                                                                                                                                                                                                                                                                                                |           |
| :doc:`syslog </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>`                                                                                                                                                           |           |
| Note down the IP address as <hw_ip_addr> as it will be used later.                                                                                                                                                                                                                                |           |
| //Note that not all projects support the *eth* command and not all projects support Ethernet. Refer to the Ethernet/Ethernet MDNS/DHCP tabs marked **YES** in :doc:`Appendix A </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`.//               |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Open a new TeraTerm Session and navigate to *File->New Connection*.                                                                                                                                                                                                                            | |image10| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Select *TCP/IP* and *Service->Telnet*.                                                                                                                                                                                                                                                         | |image11| |
| Under *Host:*, enter the IP Address: <hw_ip_addr> and select *OK* to start the telnet connection.                                                                                                                                                                                                 |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Users may also use the *Hostname* parameter from the *eth* command, where applicable.                                                                                                                                                                                                          | |image12| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. A successful connection will open a new TeraTerm window, displaying the IP Address or Hostname at the top. All shell commands available via USB OTG are also available in the telnet session.                                                                                                  | |image13| |
|                                                                                                                                                                                                                                                                                                   | |image14| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

`Knowledge Base#.|Knowledge Base#.|Knowledge Base <https://wiki.analog.com/_media/navigation Knowledge Base#.>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase0.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase1.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase2.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase3.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase4.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase6.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase5.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase0.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase1.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase2.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase3.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase4.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase6.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase5.jpg
   :width: 400px
