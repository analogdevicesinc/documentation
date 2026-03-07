AD-GMSLCAMRPI-ADP# User Guide
=============================

|

.. note::

   We are in the process of migrating our documentation to GitHub Pages.

   | This user guide is now available at
   | https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-gmslcamrpi-adp/index.html


Seamlessly insert GMSL into the signal chain and create a full GMSL Camera System with off-the-shelf parts.

.. image:: https://wiki.analog.com/_media/playground/ signal_chain.png
   :width: 600px

| 
| ===== Overview ===== The :adi:`AD-GMSLCAMRPI-ADP# <design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-GMSLCAMRPI-ADP.html>` enables connecting GMSL serializer and deserializer Evaluation Kits (EVK) to a wide range of cameras and processing platforms supporting industry standard ribbon cable connectors. The adapter consists of three sections that can be broken apart from each other, with the following functionalities:

-  A **Ribbon Cable Adapter** having two pairs of 15-pin and 22-pin connectors routed to each other. The 15-pin connectors support 2 MIPI lanes, while the 22-pin connectors support 4 MIPI lanes.
-  A **GMSL Serializer EVK Adapter** with two 22-pin ribbon cable connectors, for connecting cameras to the GMSL serializers. A USB Type-A connector is available to supply 5V @ 4A to another system
-  A **GMSL Deserializer EVK Adapter** with two 22-pin ribbon cable connectors, for connecting to Raspberry Pi, Nividia or Xilinx development platforms, or any other processing platform supporting the 15-pin or 22-pin ribbon cable connectors

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-3dsmartcam1-prz/block_diagram.png
   :alt: Block diagram
   :width: 600px

.. image:: https://wiki.analog.com/_media/playground/wikigmsladptop.png
   :width: 600px

--------------

Specifications
--------------

.. warning::

   Do not use the 15-pin ribbon cable included with the Raspberry Pi camera since that is an opposite sided cable.


+-------------------------------+----------------------------------------------------------------------------------------------------------+
| Ribbon cable adapter          |                                                                                                          |
+===============================+==========================================================================================================+
| **Connectors**                | 2 x 15 Pin Type A (**

.. container:: hi

   same side


**) Flexible Ribbon Cable (2 x MIPI lanes, P/N: 1-84953-5) |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
|                               | 2 x 22 Pin Type B (**

.. container:: hi

   opposite side


**) Flexible Ribbon Cable (P/N: 687122149022)          |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| **Power**                     | Routing 3.3V external power between pairs of 15-pin and 22-pin connectors                                |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| GMSL Serializer EVK Adapter   |                                                                                                          |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| **Connectors**                | 1 x GMSL Serializer EV kit (P/N: QSH-030-01-L-D-A)                                                       |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
|                               | 2 x 22-pin (4 x MIPI lanes, P/N: 687122149022)                                                           |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| **Power**                     | Input: 12V from GMSL Serializer EV kit                                                                   |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
|                               | Output: 3.3V @ 0.5A on the 22-pin connectors                                                             |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| GMSL Deserializer EVK Adapter |                                                                                                          |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| **Connectors**                | 1 x GMSL Deserializer EV kit (P/N: QTH-030-01-L-D-A)                                                     |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
|                               | 2 x 22-pin (4 x MIPI lanes, P/N: 687122149022)                                                           |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
| **Power**                     | Input: 12V from GMSL Deserializer EV kit                                                                 |
+-------------------------------+----------------------------------------------------------------------------------------------------------+
|                               | Output: 5V @ 4A on the USB Type A connector to power external devices                                    |
+-------------------------------+----------------------------------------------------------------------------------------------------------+

.. admonition:: Download
   :class: download

   **Hardware design files**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/02_075922a_top.pdf>`_
      \* `Layout <https://wiki.analog.com/_media/resources/eval/user-guides/08_075922a.zip>`_
      \* `High level BOM <https://wiki.analog.com/_media/resources/eval/user-guides/05-075922-01-a.zip>`_
   


--------------

GMSL EV Kit Compatibility
-------------------------

The MIPI-CSI2 signals, I2C communication, and power pins align on the EV kits but the MFP connections can vary.

Refer to the `Serializer and Deserializer EV Kit Compatibility Guide <https://wiki.analog.com/resources/eval/user-guides/ad-gmslcamrpi-adp/comp_guide>`_ to see the connections across EV kits.

--------------

Camera Connections
------------------

Connect RPi 15-pin cameras to GMSL Serializer EVKIT's with the 15-22 pin adapter.

|image1| |image2|

Or use a 15-pin to 22-Pin Adapter Cable

--------------

SoC Connections
---------------

The same configuration is used for the SoC side where the 22-pin adapter can be directly connect to a Jetson Orin Development kit or use the 22-15 pin adapter to connect to an Raspberry Pi.

|image3| -OR - |image4|

--------------

Example Configurations
----------------------

The adapter can be used to connect the GMSL Deserializer EV kits to a number of processing platforms for GMSL evaluation and application development. The user guides below provide instructions on how to get the systems up and running by configuring the hardware and running the associated software.

.. note::

   
   -  :doc:`Nvidia Jetson Orin Nano User Guide </wiki-migration/resources/eval/user-guides/ad-gmslcamrpi-adp/ug_nvidia_jetson_orin_nano>`
   -  :doc:`Raspberry Pi User Guide </wiki-migration/resources/eval/user-guides/ad-gmslcamrpi-adp/ug_rpi>`
   -  :doc:`AMD Kria User Guide </wiki-migration/resources/eval/user-guides/ad-gmslcamrpi-adp/ug_amd_kria>`
   


--------------

Software development
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the supported processing platforms, and software user guides can be found on the `Analog Devices GMSL github repository <https://github.com/analogdevicesinc/gmsl>`_.

--------------

Support
-------

For questions and more information please contact us on the **Analog Devices Engineer Zone**.

-  :ez:`EngineerZone Linux Software Drivers <community/linux-software-drivers>`
-  :ez:`EngineerZone FPGA Reference Designs <community/fpga>`

.. |image1| image:: https://wiki.analog.com/_media/playground/wikigmslcamadpser.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/wikigmsl15adp22ser.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/playground/wikigmsladpdesjeto.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/playground/wikigmsladpdesrpi4.png
   :width: 400px
