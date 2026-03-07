News
====

.. important::

   Support or Query: tof@analog.com


**2025-09-12**: Release 6.1.0 is available on GitHub; see :git-ToF:`releases`

.. important::

   \* Please reference the release note to see important changes.

   
   \* The documentation is now a part of the release and is also in the GitHub repo: :git-ToF:`External Link <doc/user-guide/ADTF3175D-EvalKit-610.md>`


EVAL-ADTF3175D-NXZ
------------------

Analog Devices 3D time of flight (ToF) camera products capture depth information, enabling advanced machine vision applications and allowing people and devices to sense, capture and interact with their spatial environments.

For more information see: :adi:`Time of Flight Camera – System Overview <en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`

Introduction
~~~~~~~~~~~~

The EVAL-ADTF3175D-NXZ time of flight (ToF) evaluation kit is showcasing the ADTF3175 module with ADI's depth ISP, the ADSD3500. The kit supports ethernet over USB connectivity to a PC for real-time visualization, capture and post processing of depth data. The kit includes host PC software (Windows) and an open source multi-platform SDK for custom application development.

Key Features
^^^^^^^^^^^^

.. container:: indent

   
   ================ ====================================
   Resolution:       1024x1024 TOF sensor
   Illumination:     FOI 81°x81° - 940nm Lumentum VCSEL
   Field of view:    FOV 75°x75°
   Operating range:  0.4 to 4m @ 15% reflectance (native)
   Depth Noise:      <15mm
   Accuracy:         +/- 3mm depth error
   ================ ====================================
   


Modes of Operation
^^^^^^^^^^^^^^^^^^

.. container:: indent

   See the :doc:`Modes Table </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz/mode_table>` page.


What is included in the kit?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  ADTF3175D Evaluation Module

   -  ADTF3175 Module
   -  i.MX8 M Plus SOM (SolidRun)
   -  Camera Interface Board
   -  ADSD3500 Interposer board

-  16GB flashed microSD card (Inserted in module sd card slot)
-  USB-C to USB-C cable. Supports PD 2.0, and USB 3.1
-  Tripod

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/crosby2.jpg
   :alt: crosby2.jpg
   :align: center
   :width: 300px

--------------

System Overview
~~~~~~~~~~~~~~~

Quarter-MegaPixel (512x512)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pulsatrix_qmp.png
   :align: center

MegaPixel (1024x1024)
^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pulsatrix_mp.png
   :align: center

:doc:`Click here for more information on each block </wiki-migration/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175d-bc>`

Quick Start
~~~~~~~~~~~

:doc:`Start Up Guide </wiki-migration/eval-adtf3175d-nxz-startup>`

--------------

System Information
~~~~~~~~~~~~~~~~~~

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

   ; Dimensions : 66mm x 58.6mm x 67.9mm
   ; Enclosure Drawing : [[https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz_drawing_v1.pdf|Link]]
   ; Laser Safety : Class 1
   ; Operating Environment : //TO BE COMPLETED//

--------------

Index of Pages
~~~~~~~~~~~~~~

.. container:: indent

   
   -  :doc:`ADSD3500 Guide </wiki-migration/resources/eval/user-guides/eval-adtf3175x-adsd3500>`
   -  :git-ToF:`User Guide for Release 6.1.0 <doc/user-guide/ADTF3175D-EvalKit-610.md>`
   
   ::
   
      Pre-release 6.1.0 documentation - these links have been deprecated:
      * [[/eval-adtf3175d-nxz-startup|Start Up Guide]]
      * [[/resources/eval/user-guides/eval-adtf3175d-nxz/workflow|Workflow]]
      * System Maintenance
        * [[/resources/eval/user-guides/eval-adsd3100-nxz-software-installation|Installation]]
        * [[/resources/eval/user-guides/eval-adtf3175d-nxz/system_update|System Update]]
        * [[/resources/eval/user-guides/eval-adtf3175x-access|Accessing the ADTF3175D]]
        * [[/resources/eval/user-guides/aditofgui_ts|Troubleshooting Guide]]
      * Tools
        * [[/resources/eval/user-guides/eval-adsd3100-nxz-gui|ADIToFGUI Tool]]
        * [[/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli|Data Collect CLI Tool]]
        * [[/resources/eval/user-guides/eval-adsd3100-nxz/tof_auxtools_cli|Python Tools]]
        * [[/resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli|Depth Compute CLI Tool (4.3.0 or older)]]
   


--------------

Support Links
~~~~~~~~~~~~~

-  Module and Eval kit questions : :ez:`EngineerZone <depth-perception-ranging-technologies/continuous-wave-cmos-time-of-flight-tof>`
-  Software/SDK questions : :git-ToF:`issues`
-  Lumentum VSCEL Information :

   -  https://www.lumentum.com/en/products/10-w-940-nm-triple-junction-vcsel-array
   -  https://www.lumentum.com/en/products/multi-junction-vcsel-arrays

Terms
~~~~~

::

   ; **FOI** : Field of Illumination
   ; **FOV** : Field of View
   ; **FPS** : Frames per Second
   ; **SOM** : System On Module
   ; **VCSEL** : Vertical-Cavity Surface-Emitting Laser
