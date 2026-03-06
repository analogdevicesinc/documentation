IIO OSC ADRV9026/ADRV9029 Capture Window
========================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/eval/user-guide/transceiver/adrv9026/quickstart/index.html\


Introduction
------------

Main receivers RX1, RX2, RX3, and RX4 are handled by the axi-adrv9025-rx-hpc IIO device.

Channels:

+---------------------+-----------------------+-----------------------+-----------------------+-----------------------+
|                     | Receiver Inputs       |                       |                       |                       |
+=====================+=======================+=======================+=======================+=======================+
| IIO Device Channels | voltage0_i voltage0_q | voltage1_i voltage1_q | voltage2_i voltage2_q | voltage3_i voltage3_q |
+---------------------+-----------------------+-----------------------+-----------------------+-----------------------+
| axi-adrv9009-rx-hpc | RX1                   | RX2                   | RX3                   | RX4                   |
+---------------------+-----------------------+-----------------------+-----------------------+-----------------------+

Screenshots
-----------

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_TD_MAIN.png
   :align: center
   :width: 600px

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_FD_MAIN.png
   :align: center
   :width: 600px
