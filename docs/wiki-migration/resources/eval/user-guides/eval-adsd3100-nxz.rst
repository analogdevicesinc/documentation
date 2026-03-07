EVAL-ADSD3100-NXZ
=================

.. admonition:: Download
   :class: download

   :git-ToF:`Download the latest software package from here <releases>`


Analog Devices 3D time of flight (ToF) camera products capture depth information, enabling advanced machine vision applications and allowing people and devices to sense, capture and interact with their spatial environments.

For more information see: :adi:`Time of Flight Camera – System Overview <en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`

Introduction
------------

The EVAL-ADSD3100-NXZ time of flight (ToF) evaluation kit is a complete high-resolution (1Mpixel) 3D depth camera system assembled with the NXP i.MX 8M Plus processor. The camera supports USB connectivity to a PC for real-time visualization, capture and post processing of depth data. The kit includes host PC software (Windows/Linux) and an open source multi-platform SDK for custom application development.

Key Features
~~~~~~~~~~~~

.. container:: indent

   
   ================ =====================================
   Resolution:       1024x1024 TOF sensor
   Illumination:     FOI 60°x60° - 940nm VCSEL
   Field of view:    FOV 51°x51°
   Operating range:  up to 5.2m @ 90% reflectance (native)
   Depth Noise:      1%
   Accuracy:         +/- 3mm depth error
   ================ =====================================
   


Modes of Operation
~~~~~~~~~~~~~~~~~~

.. container:: indent

   
   ========== ======================= ========== ===== ===
   Mode Index  Mode                     Resolution  Range  FPS
   5           Megapixel (mp)           1024x1024   5.2m   10
   7           Quarter-Megapixel (qmp)  512x512     5.2m   15
   ========== ======================= ========== ===== ===
   


What is included in the kit?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ADSD3100-NXZ Evaluation Module

   -  ADSD3100 Imager Module
   -  i.MX8 M Plus SOM (SolidRun)
   -  Camera Interface Board

-  16GB flashed microSD card (Inserted in module sd card slot)
-  USB-C to USB-C cable. Supports PD 2.0, and USB 3.1

.. container:: indent

   
   ======== ========
   |image1| |image2|
   ======== ========
   
   **Note:** the stand is *not* included.


--------------

Quick Start
-----------

:doc:`Start Up Guide </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-startup>`

--------------

System Information
------------------

::

   ; USB and Power : 

**Minimum Requirements**

-  USB 3.0 (5Gbps)
-  USB Type-C cable
-  2.0A

**Recommended Requirements**

-  USB 3.1 Gen2
-  USB Type-C cable
-  3.0A

Note: Do not use USB Type-C to USB Type-A adapters.

::

   ; Dimensions : 38mm x 72.5mm x 87mm
   ; Schematics : [[https://wiki.analog.com/_media/resources/eval/user-guides/eval-adsd3100-nxz_drawing_v1.pdf|eval-adsd3100-nxz_drawing_v1.pdf]]
   ; Laser Safety : Class 1
   ; Operating Environment : //TO BE COMPLETED//

--------------

Index of Pages
--------------

.. container:: indent

   \* :doc:`Start Up Guide </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-startup>`

   
   \* :doc:`Installation </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`
   
   \* :doc:`ADIToFGUI Tool </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui>`
   
   \* :doc:`Data Collect CLI Tool </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`
   
   \* :doc:`Depth Compute CLI Tool </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`
   
   \* :doc:`Auxillary Tools </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz/tof_auxtools_cli>`
   
   \* :doc:`EVAL-ADSD3100-NXZ Development </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-development>`


--------------

Terms
-----

::

   ; **FOI** : Field of Illumination
   ; **FOV** : Field of View
   ; **FPS** : Frames per Second
   ; **SOM** : System On Module
   ; **VCSEL** : Vertical-Cavity Surface-Emitting Laser

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_noenc.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_w_enc.png
   :width: 200px
