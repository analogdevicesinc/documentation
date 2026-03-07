EVAL-ADSD3100-NXZ Startup Guide
===============================

Kit Contents
------------

-  ADSD3100-NXZ Evaluation Module

   -  ADSD3100 Imager Module
   -  i.MX8 M Plus SOM (SolidRun)
   -  Camera Interface Board

-  16GB flashed microSD card (Inserted in module sd card slot)
-  Anker USB Hub
-  USB-C to USB-C cable. Supports PD 2.0, and USB 3.1

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100-nxz-kit.jpg
   :align: center
   :width: 400px

Software Download
-----------------

-  GUI Install Guide: :doc:`link </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`

Startup
-------

-  :doc:`Install Software Package </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`
-  Remove camera from packaging
-  Mount camera. Orientation shown in image below

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_w_enc.png
   :align: center
   :width: 400px

-  Connect USB-C cable to module

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_usbc_sdcard.jpg
   :align: center
   :width: 200px

-  Connect USB-C to laptop
-  Wait for green light under the USB-C connector on the module light up
-  Run :doc:`GUI </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui>`

.. important::

   If mp_pcm mode does not work (ie. GUI is stuck/crashes), disconnect USB-C Cable from laptop. Connect module to USB-C hub 5Gbps port (highlighted by white box), and connect hub to pc. Restart the GUI and try again.


|image1| |image2|

Troubleshooting
---------------

-  GUI Crash

   -  Ensure that that mode switching is done after module is stopped
   -  If the GUI is always crashing, particularly for mp_pcm, the module is likely not getting enough power. If adding the hub did not fix the issue, it is likely that the host port does not support the power requirements.

-  Green light under USB-C Connector not turning on

   -  SD-Card could be corrupted. 'Firmware Flashing Link'

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_hub.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_kit_w_hubandlaptop.jpg
   :width: 400px
