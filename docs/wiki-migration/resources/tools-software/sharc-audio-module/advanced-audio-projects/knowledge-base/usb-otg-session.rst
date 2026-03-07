Connecting to a USB OTG or USB-PHY Session
==========================================

Overview
--------

This article describes how to establish a shell connection via USB OTG/USB-PHY. This connection establishes an emulated serial port connection using the USB port connector on the physical hardware so that users can interact with the :doc:`shell commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands>` within the Audio Starter.

Details
-------

*This article assumes that the hardware is already up and running and proper connection to the USB port has been established. There are various instructions on setting this up. The* :doc:`Analog Audio </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/examples-analog-audio>` *example is a great place to start.*

*This tutorial uses TeraTerm as the serial interface to your hardware.*

**Follow the instructions below to set up a connection to your hardware:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
| 1. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port* or *FTDI COMxx Port*.                                                | |image8| |image9| OR |image10| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
| 2. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                                              | |image11| |image12|            |
| *Speed/Baud - 115200*                                                                                                                                                                 |                                |
| *Data Bits - 8-bit*                                                                                                                                                                   |                                |
| *Stop Bits - 1*                                                                                                                                                                       |                                |
| *Parity - None*                                                                                                                                                                       |                                |
| *Flow Control - None*                                                                                                                                                                 |                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
| 3. With a successful connection, after reset, the terminal will display the name of the Audio Starter application with the version. Type *help* to list the available shell commands. | |image13|                      |
|                                                                                                                                                                                       | |image14|                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+

--------------

`Knowledge Base#.|Knowledge Base#.|Knowledge Base <https://wiki.analog.com/_media/navigation Knowledge Base#.>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_serial.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_serial.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
